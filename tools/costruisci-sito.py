#!/usr/bin/env python3
"""Genera la navigazione del sito a partire da manifest.json.

Una sola fonte di verità: aggiungere un artefatto significa aggiungere una voce
al manifest. Questo script riscrive, dentro ogni pagina, i blocchi delimitati da

    <!-- sito:menu -->      ... <!-- /sito:menu -->      il menù fra le pagine
    <!-- sito:catalogo -->  ... <!-- /sito:catalogo -->  l'elenco (solo index)
    <!-- sito:pie -->       ... <!-- /sito:pie -->       firma, data, licenza

I blocchi assenti vengono inseriti al primo passaggio: il menù subito dopo
<body>, il piè di pagina prima di </body>. Nient'altro della pagina viene
toccato, e rieseguire lo script due volte non produce differenze.

    python3 tools/costruisci-sito.py            genera
    python3 tools/costruisci-sito.py --verifica non scrive: dice cosa cambierebbe
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
MANIFEST = RADICE / "manifest.json"

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
        "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def data_estesa(iso):
    a, m, g = iso.split("-")
    return f"{int(g)} {MESI[int(m) - 1]} {a}"


def blocco(nome, contenuto):
    return f"<!-- sito:{nome} -->{contenuto}<!-- /sito:{nome} -->"


def sostituisci(testo, nome, contenuto, dove):
    """Rimpiazza il blocco se c'è, altrimenti lo inserisce nel punto indicato."""
    nuovo = blocco(nome, contenuto)
    marcatore = re.compile(rf"<!--\s*sito:{nome}\s*-->.*?<!--\s*/sito:{nome}\s*-->", re.S)
    if marcatore.search(testo):
        return marcatore.sub(lambda _: nuovo, testo, count=1)

    if dove == "dopo-body":
        m = re.search(r"<body[^>]*>", testo)
        if not m:
            raise ValueError("nessun <body>")
        return testo[:m.end()] + "\n" + nuovo + testo[m.end():]
    if dove == "prima-body":
        i = testo.rfind("</body>")
        if i < 0:
            raise ValueError("nessun </body>")
        return testo[:i] + nuovo + "\n" + testo[i:]
    raise ValueError(dove)


# ------------------------------------------------------------------ contenuti

STILE = """<style>
.sito-bar{position:sticky;top:0;z-index:900;display:flex;align-items:center;gap:2px;flex-wrap:wrap;
  padding:0 14px;background:#0b0d12;border-bottom:1px solid #262d3d;font:600 13px/1 -apple-system,
  BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.sito-bar a{text-decoration:none}
.sito-marchio{color:#e6e9f0;padding:11px 12px 11px 0;letter-spacing:.4px;white-space:nowrap}
.sito-marchio b{color:var(--ac,#7dd3fc)}
.sito-tema{position:relative}
.sito-tema>button{background:none;border:0;color:#a2acc2;font:inherit;padding:11px 12px;cursor:pointer;
  border-bottom:2px solid transparent}
.sito-tema>button:hover,.sito-tema.aperto>button{color:#e6e9f0}
.sito-tema.qui>button{color:var(--ac,#7dd3fc);border-bottom-color:var(--ac,#7dd3fc)}
.sito-menu{display:none;position:absolute;left:0;top:100%;min-width:290px;background:#12151d;
  border:1px solid #333c52;border-radius:0 0 10px 10px;border-top:0;padding:6px;
  box-shadow:0 14px 34px rgba(0,0,0,.5)}
.sito-tema.aperto .sito-menu{display:block}
.sito-menu a,.sito-menu span.chiuso{display:block;padding:8px 10px;border-radius:7px;color:#c9d1de;font-weight:600}
.sito-menu a:hover{background:#1b2030;color:#fff}
.sito-menu a.qui{color:var(--ac,#7dd3fc)}
.sito-menu small{display:block;color:#6d7891;font-weight:500;margin-top:2px;font-size:11.5px;line-height:1.4}
.sito-menu span.chiuso{color:#6d7891;cursor:default}
.sito-menu span.chiuso:before{content:'\\1F512';margin-right:7px;opacity:.7}
.sito-bar .sito-sp{flex:1}
.sito-bar .sito-casa{color:#6d7891;padding:11px 0 11px 12px;white-space:nowrap}
.sito-bar .sito-casa:hover{color:var(--ac,#7dd3fc)}
@media(max-width:760px){.sito-marchio{padding-right:6px}.sito-tema>button{padding:11px 8px}
  .sito-menu{position:static;min-width:0;border:0;box-shadow:none;background:#0f121a}}
.sito-pie{border-top:1px solid #262d3d;margin-top:56px;padding:26px 20px 34px;color:#6d7891;
  font:400 12.5px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;text-align:center}
.sito-pie b{color:#a2acc2;font-weight:700}
.sito-pie a{color:#6d7891;text-decoration:underline}
.sito-pie .sito-lic{margin-top:6px;font-size:12px}
@media print{.sito-bar{display:none}.sito-pie{border-color:#bbb;color:#333}}
</style>"""

SCRIPT = """<script>
(function(){
  var bar=document.querySelector('.sito-bar'); if(!bar) return;
  bar.querySelectorAll('.sito-tema>button').forEach(function(b){
    b.onclick=function(e){
      e.stopPropagation();
      var t=b.parentNode, era=t.classList.contains('aperto');
      bar.querySelectorAll('.sito-tema').forEach(function(x){x.classList.remove('aperto')});
      t.classList.toggle('aperto', !era);
    };
  });
  document.addEventListener('click',function(){
    bar.querySelectorAll('.sito-tema').forEach(function(x){x.classList.remove('aperto')});
  });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape') bar.querySelectorAll('.sito-tema').forEach(function(x){x.classList.remove('aperto')});
  });
})();
</script>"""


def verso(corrente, meta):
    """Indirizzo di `meta` visto da `corrente`: le pagine non stanno tutte
    nella stessa cartella, e i collegamenti devono restare relativi."""
    su = "../" * len(Path(corrente).parent.parts)
    return (su + meta).replace(" ", "%20")


def menu(m, corrente):
    """Il menù fra le pagine: un tema per voce, gli artefatti nella tendina."""
    e = html.escape
    fuori = [STILE, '<nav class="sito-bar" aria-label="Navigazione del sito">',
             f'<a class="sito-marchio" href="{verso(corrente, "index.html")}">{e(m["sito"]["nome"])} '
             f'<b>{e(m["sito"]["titolo"])}</b></a>']

    for t in m["temi"]:
        figli = sorted([a for a in m["artefatti"] if a["tema"] == t["id"]],
                       key=lambda a: (a.get("ordine", 99), a["titolo"]))
        if not figli:
            continue
        qui = any(a.get("indirizzo") == corrente for a in figli)
        fuori.append(f'<div class="sito-tema{" qui" if qui else ""}">'
                     f'<button type="button">{e(t["titolo"])}</button><div class="sito-menu">')
        for a in figli:
            desc = f'<small>{e(a["descrizione"])}</small>' if a.get("descrizione") else ""
            if a["accesso"] == "riservato" or not a.get("indirizzo"):
                fuori.append(f'<span class="chiuso">{e(a["titolo"])}{desc}</span>')
            else:
                attuale = " qui" if a["indirizzo"] == corrente else ""
                fuori.append(f'<a class="{attuale.strip()}" href="{e(verso(corrente, a["indirizzo"]))}">'
                             f'{e(a["titolo"])}{desc}</a>')
        fuori.append("</div></div>")

    fuori += ['<span class="sito-sp"></span>',
              f'<a class="sito-casa" href="{verso(corrente, "index.html")}">Tutti i contenuti &#8594;</a>',
              "</nav>", SCRIPT]
    return "\n".join(fuori)


def pie(m, art):
    e = html.escape
    s = m["sito"]
    riga = f'<b>{e(s["nome"])}</b> &middot; aggiornato al {data_estesa(art["aggiornato"])}'
    vivo = ""
    if art.get("indirizzo"):
        vivo = (f' &middot; <a href="{e(s["base"] + art["indirizzo"].replace(" ", "%20"))}">'
                "versione online sempre aggiornata</a>")
    return (f'\n<footer class="sito-pie">{riga}{vivo}'
            f'<div class="sito-lic">{e(s["licenza"])}</div></footer>\n')


def catalogo(m):
    """L'elenco per la pagina d'ingresso: un gruppo per tema."""
    e = html.escape
    fuori = []
    for t in m["temi"]:
        figli = sorted([a for a in m["artefatti"] if a["tema"] == t["id"]],
                       key=lambda a: (a.get("ordine", 99), a["titolo"]))
        if not figli:
            continue
        fuori.append(f'\n<section class="cat-tema">\n  <h2>{e(t["titolo"])}</h2>'
                     f'\n  <p class="cat-sub">{e(t["descrizione"])}</p>\n  <div class="grid">')
        for a in figli:
            chiuso = a["accesso"] == "riservato" or not a.get("indirizzo")
            meta = []
            if a.get("durata"):
                meta.append(e(a["durata"]))
            if a.get("lezioni"):
                meta.append(f'{a["lezioni"]} lezioni')
            if a.get("percorsi"):
                meta.append(f'{len(a["percorsi"])} percorsi')
            riga = f'<div class="cat-meta">{" &middot; ".join(meta)}</div>' if meta else ""
            azione = ('<span class="go chiuso">Riservato ai partecipanti</span>' if chiuso
                      else f'<a class="go" href="{e(verso("index.html", a["indirizzo"]))}">Apri &#8594;</a>')
            fuori.append(
                f'\n    <div class="card{" chiuso" if chiuso else ""}">'
                f'\n      <div class="tag">{e(a.get("etichetta", a["tipo"]))}</div>'
                f'\n      <h3>{e(a["titolo"])}</h3>'
                f'\n      <p>{e(a.get("descrizione", ""))}</p>{riga}'
                f'\n      {azione}\n    </div>')
        fuori.append("\n  </div>\n</section>\n")
    return "".join(fuori)


# ------------------------------------------------------------------ esecuzione

def main():
    ap = argparse.ArgumentParser(description="Genera la navigazione dal manifest")
    ap.add_argument("--verifica", action="store_true", help="non scrive: dice cosa cambierebbe")
    a = ap.parse_args()

    if not MANIFEST.exists():
        sys.exit("manifest.json assente")
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))

    temi = {t["id"] for t in m["temi"]}
    for art in m["artefatti"]:
        if art["tema"] not in temi:
            sys.exit(f"{art['id']}: tema sconosciuto '{art['tema']}'")
        if art.get("indirizzo") and not (RADICE / art["indirizzo"]).exists():
            sys.exit(f"{art['id']}: indirizzo inesistente '{art['indirizzo']}'")

    pagine = [(a["indirizzo"], a) for a in m["artefatti"]
              if a.get("indirizzo") and a["accesso"] == "aperto"]
    pagine.append(("index.html", None))

    cambiate, invariate = [], 0
    for nome, art in pagine:
        f = RADICE / nome
        originale = f.read_text(encoding="utf-8")
        testo = sostituisci(originale, "menu", menu(m, nome), "dopo-body")
        if art:
            testo = sostituisci(testo, "pie", pie(m, art), "prima-body")
        else:
            testo = sostituisci(testo, "catalogo", catalogo(m), "prima-body")
        if testo != originale:
            cambiate.append(nome)
            if not a.verifica:
                f.write_text(testo, encoding="utf-8")
        else:
            invariate += 1

    verbo = "cambierebbero" if a.verifica else "aggiornate"
    print(f"{len(cambiate)} pagine {verbo}, {invariate} già allineate")
    for n in cambiate:
        print(f"  {n}")
    if a.verifica and cambiate:
        sys.exit(1)


if __name__ == "__main__":
    main()
