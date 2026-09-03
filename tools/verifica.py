#!/usr/bin/env python3
"""Verifica le promesse che il sito fa su ogni artefatto.

Non è un controllo di stile: sono le quattro cose che, se saltano, rompono
qualcosa che abbiamo dichiarato per iscritto.

  V1  nessuna risorsa esterna caricata   la pagina deve funzionare senza rete
  V2  nessun collegamento locale rotto   la pagina si sposta e resta intera
  V3  nessuna regia nel materiale pubblico
  V4  data di aggiornamento visibile     è il controllo su cui regge la freschezza
  V5  artefatto dichiarato nel manifest  quello che non è dichiarato non esiste
  V6  navigazione allineata al manifest

Sono ammessi i rimandi su cui il lettore clicca: è vietato ciò che il browser
carica da solo.

    python3 tools/verifica.py            verifica tutto
    python3 tools/verifica.py pagina.html
"""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

RADICE = Path(__file__).resolve().parent.parent
MANIFEST = RADICE / "manifest.json"

BLOCCANTE, GRAVE, AVVISO = "BLOCCANTE", "GRAVE", "AVVISO"
SEGNI = {BLOCCANTE: "✖", GRAVE: "⚠", AVVISO: "·"}

# ciò che il browser carica da solo: rompe la promessa di funzionare senza rete
CARICATE = re.compile(
    r"""<(?:script[^>]+src|link[^>]+href|img[^>]+src|iframe[^>]+src|
         source[^>]+src|video[^>]+src|audio[^>]+src)\s*=\s*["'](https?:|//)""",
    re.I | re.X)
IMPORTA = re.compile(r"""@import\s+(?:url\()?["']?(https?:|//)""", re.I)
RETE = re.compile(r"\b(?:fetch|XMLHttpRequest|WebSocket|EventSource)\s*\(", re.I)
REGIA = re.compile(r'class="docente"|Nota per chi conduce', re.I)
COLLEGAMENTI = re.compile(r'(?:href|src)="([^"]+)"')


def riga_di(testo, posizione):
    return testo.count("\n", 0, posizione) + 1


def zone_di_script(testo):
    """Gli intervalli occupati da <script>: là dentro un href è codice che
    costruisce HTML, non un collegamento da verificare."""
    return [(m.start(), m.end()) for m in re.finditer(r"<script\b.*?</script>", testo, re.S | re.I)]


def dentro_script(zone, posizione):
    return any(a <= posizione < b for a, b in zone)


def controlla(f, dichiarati):
    """Restituisce i rilievi di una pagina."""
    s = f.read_text(encoding="utf-8")
    rel = f.relative_to(RADICE).as_posix()
    zone = zone_di_script(s)
    r = []

    for m in CARICATE.finditer(s):
        r.append((BLOCCANTE, "V1", riga_di(s, m.start()), "risorsa esterna caricata"))
    for m in IMPORTA.finditer(s):
        r.append((BLOCCANTE, "V1", riga_di(s, m.start()), "foglio di stile importato dalla rete"))
    for m in RETE.finditer(s):
        r.append((AVVISO, "V1", riga_di(s, m.start()), f"chiamata di rete: {m.group(0)[:-1]}"))

    for m in COLLEGAMENTI.finditer(s):
        h = m.group(1)
        if h.startswith(("http://", "https://", "//", "#", "data:", "mailto:", "tel:")):
            continue
        if dentro_script(zone, m.start()):
            continue
        meta = (f.parent / unquote(h.split("#")[0].split("?")[0])).resolve()
        if not meta.exists():
            r.append((BLOCCANTE, "V2", riga_di(s, m.start()), f"collegamento rotto: {h}"))

    for m in REGIA.finditer(s):
        r.append((BLOCCANTE, "V3", riga_di(s, m.start()), "regia dentro una pagina pubblica"))

    if rel != "index.html" and "sito:pie" not in s:
        r.append((GRAVE, "V4", 0, "manca il piè di pagina con data, firma e licenza"))

    if rel not in dichiarati and rel != "index.html":
        r.append((GRAVE, "V5", 0, "artefatto non dichiarato nel manifest: non compare in nessuna navigazione"))

    return r


def main():
    if not MANIFEST.exists():
        sys.exit("manifest.json assente")
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    dichiarati = {a["indirizzo"] for a in m["artefatti"] if a.get("indirizzo")}

    if len(sys.argv) > 1:
        pagine = [RADICE / a for a in sys.argv[1:]]
    else:
        pagine = sorted(p for p in RADICE.glob("**/*.html")
                        if ".docente." not in p.name
                        and not any(x.startswith((".", "_")) or x == "tools"
                                    for x in p.relative_to(RADICE).parts))

    tutti = []
    for f in pagine:
        for sev, cid, riga, msg in controlla(f, dichiarati):
            tutti.append((sev, f.relative_to(RADICE).as_posix(), cid, riga, msg))

    # V6: la navigazione riflette il manifest?
    e = subprocess.run([sys.executable, str(RADICE / "tools" / "costruisci-sito.py"), "--verifica"],
                       capture_output=True, text=True, cwd=RADICE)
    if e.returncode != 0:
        for r in e.stdout.splitlines()[1:]:
            if r.strip():
                tutti.append((GRAVE, r.strip(), "V6", 0, "navigazione non allineata: manca costruisci-sito.py"))

    ordine = {BLOCCANTE: 0, GRAVE: 1, AVVISO: 2}
    tutti.sort(key=lambda x: (ordine[x[0]], x[1], x[3]))

    for sev, dove, cid, riga, msg in tutti:
        pos = f"{dove}:{riga}" if riga else dove
        print(f"{SEGNI[sev]} {sev:9} {cid}  {pos}\n            {msg}")

    conta = {s: sum(1 for x in tutti if x[0] == s) for s in (BLOCCANTE, GRAVE, AVVISO)}
    print(f"\n{len(pagine)} pagine verificate — "
          f"{conta[BLOCCANTE]} bloccanti, {conta[GRAVE]} gravi, {conta[AVVISO]} avvisi")
    if conta[BLOCCANTE] or conta[GRAVE]:
        sys.exit(1)
    print("Conforme.")


if __name__ == "__main__":
    main()
