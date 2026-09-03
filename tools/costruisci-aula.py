#!/usr/bin/env python3
"""Costruisce la copia per chi conduce l'aula.

Una sorgente, due file in uscita:

  pagina.html                  pubblico, senza una riga di regia
  pagina.docente.html          con le note inline, autoconsistente, offline

Il file di regia conserva solo il testo della nota: la cornice grafica
(<div class="docente">) la ricostruisce questo script.

Le note vivono in regia/<pagina>.html, suddivise da marcatori

    <!-- regia: <id> -->

e vengono iniettate nei segnaposto omonimi della pagina pubblica.

Uso:
    python3 tools/costruisci-aula.py                 # tutte le pagine con regia
    python3 tools/costruisci-aula.py memoria-e-contesto-ai.html
"""
import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
REGIA = RADICE / "regia"
MARCATORE = re.compile(r"<!--\s*regia:\s*([a-z0-9-]+)\s*-->")
CORNICE = ('  <div class="docente">\n    <div class="dt">{titolo}</div>\n'
           '{corpo}\n  </div>')
TITOLO_PREDEFINITO = "Nota per chi conduce"


def blocchi(sorgente: Path) -> dict[str, str]:
    """Spezza un file di regia nei suoi blocchi, indicizzati per id."""
    testo = sorgente.read_text(encoding="utf-8")
    tagli = list(MARCATORE.finditer(testo))
    return {
        m.group(1): testo[m.end(): tagli[i + 1].start() if i + 1 < len(tagli) else len(testo)].strip()
        for i, m in enumerate(tagli)
    }


def costruisci(pagina: Path) -> Path | None:
    sorgente = REGIA / pagina.name
    if not sorgente.exists():
        return None

    note = blocchi(sorgente)
    testo = pagina.read_text(encoding="utf-8")
    mancanti, usati = [], set()

    def sostituisci(m):
        chiave = m.group(1)
        if chiave not in note:
            mancanti.append(chiave)
            return m.group(0)
        usati.add(chiave)
        corpo = "\n".join("    " + r for r in note[chiave].splitlines())
        return CORNICE.format(titolo=TITOLO_PREDEFINITO, corpo=corpo)

    testo, quanti = MARCATORE.subn(sostituisci, testo)
    if mancanti:
        sys.exit(f"regia mancante in {sorgente.name} per: {', '.join(mancanti)}")

    orfani = set(note) - usati
    if orfani:
        print(f"  attenzione: blocchi di regia senza segnaposto: {', '.join(sorted(orfani))}")

    uscita = pagina.with_suffix(".docente.html")
    uscita.write_text(testo, encoding="utf-8")
    print(f"  {pagina.name} + {quanti} blocchi -> {uscita.name} ({len(testo) // 1024} KB)")
    return uscita


def elenco_pagine():
    """Le pagine pubbliche del sito, escluse le copie generate."""
    return sorted(f for f in RADICE.glob("*.html") if not f.name.endswith(".docente.html"))


def main():
    if not REGIA.exists():
        sys.exit("cartella regia/ assente: niente da costruire")

    if len(sys.argv) > 1:
        pagine = [RADICE / a for a in sys.argv[1:]]
    else:
        pagine = sorted(RADICE / f.name for f in REGIA.glob("*.html"))

    print("Costruzione delle copie per chi conduce:")
    fatte = [u for p in pagine if p.exists() and (u := costruisci(p))]
    if not fatte:
        sys.exit("nessuna pagina costruita")
    print(f"\n{len(fatte)} file pronti. Non committarli: restano locali o vanno nel repo privato.")


if __name__ == "__main__":
    main()
