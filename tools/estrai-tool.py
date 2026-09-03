#!/usr/bin/env python3
"""Estrae uno strumento da un corso e ne fa un artefatto autonomo.

Dentro il corso uno strumento vive in una cartella: dipende dal foglio di stile
condiviso e rimanda alle lezioni. In vetrina deve reggersi da solo. Questo
script incorpora lo stile, taglia i rimandi al materiale del corso e dichiara la
provenienza, senza toccare l'originale.

Le voci da estrarre stanno in manifest.json: sono gli artefatti con "estrazione".

    python3 tools/estrai-tool.py                estrae tutto quello che manca
    python3 tools/estrai-tool.py --tutti        rifà anche quelli già presenti
    python3 tools/estrai-tool.py tok-token      solo questo
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
MANIFEST = RADICE / "manifest.json"


def incorpora_stile(testo, sorgente):
    """Sostituisce ogni <link rel=stylesheet> locale con il suo contenuto."""
    def dentro(m):
        rel = m.group(1)
        if rel.startswith(("http://", "https://", "//")):
            return m.group(0)          # non dovrebbe accadere: lo segnala il controllo
        f = (sorgente.parent / rel).resolve()
        if not f.exists():
            raise SystemExit(f"{sorgente.name}: foglio di stile assente ({rel})")
        return f"<style>\n/* incorporato da {Path(rel).name} */\n{f.read_text(encoding='utf-8')}\n</style>"
    return re.sub(r'<link[^>]+rel="stylesheet"[^>]*href="([^"]+)"[^>]*>', dentro, testo)


def taglia_rimandi(testo, gemelli):
    """Ricollega i rimandi agli strumenti che escono anch'essi in vetrina, e
    neutralizza quelli al materiale del corso lasciando il testo leggibile.

    `gemelli` mappa il nome del file dentro il corso sull'indirizzo pubblico."""
    def dentro(m):
        href, corpo = m.group(1), m.group(2)
        if href.startswith(("#", "http://", "https://", "mailto:")):
            return m.group(0)
        pubblico = gemelli.get(Path(href).name)
        if pubblico:
            return f'<a href="{html.escape(Path(pubblico).name)}">{corpo}</a>'
        return f'<span class="rimando-tolto">{corpo}</span>'
    return re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', dentro, testo, flags=re.S)


NOTA = """
<style>
.rimando-tolto{color:inherit;opacity:.75}
.tool-provenienza{max-width:70rem;margin:2.5rem auto 0;padding:14px 18px;border:1px dashed #333c52;
  border-radius:10px;background:rgba(255,255,255,.03);color:#8a93a6;
  font:400 12.5px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
.tool-provenienza b{color:#c9d1de}
</style>
<div class="tool-provenienza">Questo strumento fa parte di <b>{corso}</b>{lezione}.
Qui è pubblicato da solo: gli esercizi, i materiali e la conduzione fanno parte del corso.</div>
"""


def estrai(art, sorgenti, gemelli):
    corso = sorgenti.get(art["estrazione"]["corso"])
    if not corso:
        raise SystemExit(f"{art['id']}: sorgente '{art['estrazione']['corso']}' non dichiarata in manifest.sorgenti")
    origine = (RADICE / corso / art["estrazione"]["file"]).resolve()
    if not origine.exists():
        raise SystemExit(f"{art['id']}: originale assente\n  {origine}")

    testo = origine.read_text(encoding="utf-8")
    testo = incorpora_stile(testo, origine)
    testo = taglia_rimandi(testo, gemelli)

    lez = art["estrazione"].get("lezione")
    nota = NOTA.replace("{corso}", html.escape(art["estrazione"]["corso_titolo"])) \
               .replace("{lezione}", f", lezione {lez}" if lez else "")
    i = testo.rfind("</body>")
    testo = testo[:i] + nota + testo[i:]

    destinazione = RADICE / art["indirizzo"]
    destinazione.write_text(testo, encoding="utf-8")
    return destinazione, len(testo)


def main():
    ap = argparse.ArgumentParser(description="Estrae gli strumenti dai corsi")
    ap.add_argument("id", nargs="*", help="estrai solo questi identificativi")
    ap.add_argument("--tutti", action="store_true", help="rifà anche quelli già presenti")
    a = ap.parse_args()

    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sorgenti = m.get("sorgenti", {})
    da_fare = [x for x in m["artefatti"] if x.get("estrazione")]
    if a.id:
        da_fare = [x for x in da_fare if x["id"] in a.id]
        if not da_fare:
            sys.exit("nessun artefatto con quell'identificativo")

    # gli strumenti estratti dallo stesso corso restano collegati fra loro
    gemelli = {Path(x["estrazione"]["file"]).name: x["indirizzo"]
               for x in m["artefatti"] if x.get("estrazione")}

    fatti, saltati = [], 0
    for art in da_fare:
        if not a.tutti and not a.id and (RADICE / art["indirizzo"]).exists():
            saltati += 1
            continue
        f, n = estrai(art, sorgenti, gemelli)
        fatti.append((f.name, n))

    for nome, n in fatti:
        print(f"  {nome} ({n // 1024} KB)")
    print(f"{len(fatti)} strumenti estratti, {saltati} già presenti")
    if fatti:
        print("Ora: python3 tools/costruisci-sito.py")


if __name__ == "__main__":
    main()
