#!/usr/bin/env python3
"""Genera la navigazione del sito a partire da manifest.json.

Una sola fonte di verità: aggiungere un artefatto significa aggiungere una voce
al manifest. Questo script riscrive, dentro ogni pagina, i blocchi delimitati da

    <!-- sito:menu -->      ... <!-- /sito:menu -->      il menù fra le pagine
    <!-- sito:mappa -->     ... <!-- /sito:mappa -->     la mappa (solo index)
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



CAMPI_OBBLIGATORI = {"id", "titolo", "tipo", "tema", "accesso", "aggiornato"}
CAMPI_NOTI = CAMPI_OBBLIGATORI | {
    "indirizzo", "etichetta", "descrizione", "ordine", "durata", "lezioni", "livello",
    "prerequisiti", "percorsi", "provenienza", "estrazione", "manipolabile", "bok",
}
TIPI = {"deep-dive", "tool", "corso"}
ACCESSI = {"aperto", "riservato"}


def valida(m):
    """Controlla il manifest contro le proprie regole, prima di generare.

    Serve a intercettare gli errori che non darebbero errore: un identificativo
    duplicato, un prerequisito che non esiste, due artefatti con lo stesso posto
    in fila, un campo scritto male. Producono una navigazione leggermente
    sbagliata, e ce ne si accorge mesi dopo."""
    temi = {t["id"] for t in m["temi"]}
    identificativi, rilievi = set(), []

    for t in m["temi"]:
        for c in ("id", "titolo"):
            if not t.get(c):
                rilievi.append(f"tema senza {c}: {t}")

    for a in m["artefatti"]:
        chi = a.get("id", "(senza id)")

        mancanti = CAMPI_OBBLIGATORI - set(a)
        if mancanti:
            rilievi.append(f"{chi}: campi obbligatori mancanti: {', '.join(sorted(mancanti))}")
        sconosciuti = set(a) - CAMPI_NOTI
        if sconosciuti:
            rilievi.append(f"{chi}: campi sconosciuti (refuso?): {', '.join(sorted(sconosciuti))}")

        if a.get("id") in identificativi:
            rilievi.append(f"{chi}: identificativo duplicato")
        identificativi.add(a.get("id"))

        if a.get("tema") not in temi:
            rilievi.append(f"{chi}: tema sconosciuto '{a.get('tema')}'")
        if a.get("tipo") not in TIPI:
            rilievi.append(f"{chi}: tipo '{a.get('tipo')}' fuori da {sorted(TIPI)}")
        if a.get("accesso") not in ACCESSI:
            rilievi.append(f"{chi}: accesso '{a.get('accesso')}' fuori da {sorted(ACCESSI)}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(a.get("aggiornato", ""))):
            rilievi.append(f"{chi}: data '{a.get('aggiornato')}' non in forma AAAA-MM-GG")

        if a.get("accesso") == "aperto" and not a.get("indirizzo"):
            rilievi.append(f"{chi}: aperto ma senza indirizzo")
        if a.get("indirizzo") and not (RADICE / a["indirizzo"]).exists():
            rilievi.append(f"{chi}: indirizzo inesistente '{a['indirizzo']}'")

    for a in m["artefatti"]:
        for q in a.get("prerequisiti", []):
            if q not in identificativi:
                rilievi.append(f"{a.get('id')}: prerequisito inesistente '{q}'")

    for t in temi:
        posti = {}
        for a in m["artefatti"]:
            if a["tema"] == t and a.get("ordine"):
                posti.setdefault(a["ordine"], []).append(a["id"])
        for posto, chi in posti.items():
            if len(chi) > 1:
                rilievi.append(f"tema '{t}': stesso posto {posto} per {', '.join(chi)}")

    return rilievi


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



MAPPA_STILE = """<style>
.mappa{margin:34px 0 8px}
.mappa-t{font-size:10.5px;letter-spacing:2px;text-transform:uppercase;color:var(--a1);font-weight:800}
.mappa-s{margin:10px 0 20px;color:var(--muted);font-size:14px;max-width:70ch}
.mappa-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}
.terr{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--mc,var(--a1));
  border-radius:12px;padding:16px 16px 14px;display:flex;flex-direction:column;gap:10px}
.terr.chiusa{border-style:dashed;border-top-style:solid;opacity:.85}
.terr h3{margin:0;font-size:14.5px;font-weight:800;letter-spacing:-.01em}
.terr h3 em{font-style:normal;color:var(--muted);font-weight:600;font-size:12px;margin-left:6px}
.terr-n{display:flex;flex-wrap:wrap;gap:5px;align-items:center}
.nodo{display:inline-block;font-size:12px;font-weight:600;line-height:1.25;padding:6px 9px;border-radius:7px;
  background:var(--panel2);border:1px solid var(--line);color:var(--ink);text-decoration:none;max-width:100%}
.nodo:hover{border-color:var(--mc,var(--a1));color:var(--mc,var(--a1))}
.nodo.chiuso{border-style:dashed;color:var(--muted);cursor:default}
.nodo.chiuso:before{content:'\\1F512';margin-right:5px;opacity:.75}
.nodo.molti{background:transparent;border-style:dashed}
.freccia{color:var(--muted);font-size:12px;opacity:.75}
@media print{.mappa{display:none}}
</style>"""


def mappa(m):
    """Una fascia sopra il catalogo: i temi come territori, e le frecce dove il
    manifest sa gia' che un artefatto viene prima di un altro."""
    e = html.escape
    colori = ["var(--a1)", "var(--a2)", "var(--a3)", "var(--a4)", "var(--a5)"]
    fuori = [MAPPA_STILE, '<section class="mappa">',
             '<div class="mappa-t">La mappa</div>',
             '<p class="mappa-s">Cinque territori. Dove un contenuto viene prima di un altro, '
             'la freccia lo dice; le zone tratteggiate si aprono partecipando a un corso.</p>',
             '<div class="mappa-g">']

    for n, t in enumerate(m["temi"]):
        figli = sorted([a for a in m["artefatti"] if a["tema"] == t["id"]],
                       key=lambda a: (a.get("ordine", 99), a["titolo"]))
        if not figli:
            continue
        chiusa = all(a["accesso"] == "riservato" for a in figli)
        fuori.append(f'<div class="terr{" chiusa" if chiusa else ""}" style="--mc:{colori[n % 5]}">'
                     f'<h3>{e(t["titolo"])}<em>{len(figli)}</em></h3><div class="terr-n">')

        # oltre sei nodi il territorio diventa illeggibile: si raccoglie in uno solo
        if len(figli) > 6:
            fuori.append(f'<a class="nodo molti" href="#tema-{e(t["id"])}">'
                         f'{len(figli)} contenuti &#8594;</a>')
        else:
            ordinati = [a for a in figli if a.get("ordine")]
            for i, a in enumerate(figli):
                if i and a in ordinati and figli[i - 1] in ordinati:
                    fuori.append('<span class="freccia">&#8594;</span>')
                if a["accesso"] == "riservato" or not a.get("indirizzo"):
                    fuori.append(f'<span class="nodo chiuso">{e(a["titolo"])}</span>')
                else:
                    fuori.append(f'<a class="nodo" href="{e(verso("index.html", a["indirizzo"]))}">'
                                 f'{e(a["titolo"])}</a>')
        fuori.append("</div></div>")

    fuori += ["</div></section>"]
    return "\n".join(fuori)


def catalogo(m):
    """L'elenco per la pagina d'ingresso: un gruppo per tema."""
    e = html.escape
    fuori = []
    for t in m["temi"]:
        figli = sorted([a for a in m["artefatti"] if a["tema"] == t["id"]],
                       key=lambda a: (a.get("ordine", 99), a["titolo"]))
        if not figli:
            continue
        fuori.append(f'\n<section class="cat-tema" id="tema-{e(t["id"])}">\n  <h2>{e(t["titolo"])}</h2>'
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

    rilievi = valida(m)
    if rilievi:
        print("Il manifest non è coerente: niente viene generato.\n")
        for r in rilievi:
            print(f"  ✖ {r}")
        sys.exit(1)

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
            testo = sostituisci(testo, "mappa", mappa(m), "prima-body")
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
