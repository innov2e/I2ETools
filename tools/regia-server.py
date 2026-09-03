#!/usr/bin/env python3
"""Pannello locale per la regia d'aula.

Serve il pannello e le pagine del sito su 127.0.0.1, e basta: non ascolta
sulla rete, non va pubblicato, non ha autenticazione perché non ne ha bisogno
— ci arrivi solo da questo computer.

    python3 tools/regia-server.py          # apre il pannello nel browser
    python3 tools/regia-server.py --porta 9000

Da lì: scrivi la nota, scegli la sezione in cui va, salva, ricostruisci.
"""
import argparse
import html
import json
import re
import subprocess
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

RADICE = Path(__file__).resolve().parent.parent
REGIA = RADICE / "regia"
PANNELLO = Path(__file__).resolve().parent / "regia-pannello.html"
MARCATORE = re.compile(r"<!--\s*regia:\s*([a-z0-9-]+)\s*-->")
SEZIONE = re.compile(r'<section\s+id="([a-z0-9-]+)"', re.I)
TITOLO_SEZ = re.compile(r"<h2[^>]*>(.*?)</h2>", re.I | re.S)


# ---------------------------------------------------------------- lettura

def pagine_pubbliche():
    return sorted(f for f in RADICE.glob("*.html") if not f.name.endswith(".docente.html"))


def blocchi_regia(nome):
    """{id: testo} delle note di una pagina."""
    f = REGIA / nome
    if not f.exists():
        return {}
    testo = f.read_text(encoding="utf-8")
    tagli = list(MARCATORE.finditer(testo))
    return {
        m.group(1): testo[m.end(): tagli[i + 1].start() if i + 1 < len(tagli) else len(testo)].strip()
        for i, m in enumerate(tagli)
    }


def sezioni(nome):
    """Le sezioni della pagina, con titolo leggibile e nota già presente."""
    testo = (RADICE / nome).read_text(encoding="utf-8")
    fuori = []
    for m in SEZIONE.finditer(testo):
        fine = testo.find("</section>", m.end())
        corpo = testo[m.end():fine if fine > 0 else len(testo)]
        t = TITOLO_SEZ.search(corpo)
        titolo = re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else m.group(1)
        segnaposto = MARCATORE.search(corpo)
        fuori.append({
            "id": m.group(1),
            "titolo": html.unescape(titolo),
            "nota": segnaposto.group(1) if segnaposto else None,
        })
    return fuori


def stato_pagina(nome):
    note = blocchi_regia(nome)
    testo = (RADICE / nome).read_text(encoding="utf-8")
    t = re.search(r"<title>(.*?)</title>", testo, re.I | re.S)
    return {
        "file": nome,
        "titolo": html.unescape(re.sub(r"\s+", " ", t.group(1)).strip()) if t else nome,
        "sezioni": sezioni(nome),
        "note": note,
        "orfane": sorted(set(note) - {s["nota"] for s in sezioni(nome)}),
    }


# ---------------------------------------------------------------- scrittura

def scrivi_regia(nome, note: dict):
    REGIA.mkdir(exist_ok=True)
    f = REGIA / nome
    testo = ("<!-- Regia d'aula: NON distribuire.\n"
             "     Scritta dal pannello, iniettata da tools/costruisci-aula.py. -->\n")
    for chiave in sorted(note):
        testo += f"\n<!-- regia: {chiave} -->\n{note[chiave].strip()}\n"
    f.write_text(testo, encoding="utf-8")


def metti_segnaposto(nome, sezione_id, nota_id):
    """Inserisce <!-- regia: id --> in fondo alla sezione scelta, se non c'è già."""
    percorso = RADICE / nome
    testo = percorso.read_text(encoding="utf-8")
    m = SEZIONE.search(testo, 0)
    while m and m.group(1) != sezione_id:
        m = SEZIONE.search(testo, m.end())
    if not m:
        raise ValueError(f"sezione '{sezione_id}' non trovata in {nome}")
    fine = testo.find("</section>", m.end())
    if fine < 0:
        raise ValueError(f"sezione '{sezione_id}' non chiusa in {nome}")
    corpo = testo[m.end():fine]
    if MARCATORE.search(corpo):
        testo = testo[:m.end()] + MARCATORE.sub(f"<!-- regia: {nota_id} -->", corpo, count=1) + testo[fine:]
    else:
        testo = testo[:fine] + f"  <!-- regia: {nota_id} -->\n\n" + testo[fine:]
    percorso.write_text(testo, encoding="utf-8")


def togli_segnaposto(nome, nota_id):
    percorso = RADICE / nome
    testo = percorso.read_text(encoding="utf-8")
    percorso.write_text(
        re.sub(r"[ \t]*<!--\s*regia:\s*" + re.escape(nota_id) + r"\s*-->\n?\n?", "", testo),
        encoding="utf-8")


def costruisci(nome=None):
    cmd = [sys.executable, str(RADICE / "tools" / "costruisci-aula.py")] + ([nome] if nome else [])
    e = subprocess.run(cmd, capture_output=True, text=True, cwd=RADICE)
    return {"ok": e.returncode == 0, "log": (e.stdout + e.stderr).strip()}


# ---------------------------------------------------------------- http

class Pannello(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(RADICE), **k)

    def log_message(self, *a):
        pass

    def _json(self, dati, codice=200):
        corpo = json.dumps(dati, ensure_ascii=False).encode("utf-8")
        self.send_response(codice)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def _corpo(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        rotta = urlparse(self.path)
        if rotta.path in ("/", "/pannello"):
            corpo = PANNELLO.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            self.end_headers()
            self.wfile.write(corpo)
            return
        if rotta.path == "/api/pagine":
            self._json([stato_pagina(p.name) for p in pagine_pubbliche()])
            return
        if rotta.path == "/api/pagina":
            nome = parse_qs(rotta.query).get("file", [""])[0]
            if not (RADICE / nome).exists():
                return self._json({"errore": "pagina inesistente"}, 404)
            self._json(stato_pagina(nome))
            return
        super().do_GET()

    def do_POST(self):
        rotta = urlparse(self.path).path
        try:
            d = self._corpo()
            if rotta == "/api/nota":
                nome, chiave = d["file"], d["id"]
                note = blocchi_regia(nome)
                if d.get("id_precedente") and d["id_precedente"] != chiave:
                    note.pop(d["id_precedente"], None)
                    togli_segnaposto(nome, d["id_precedente"])
                note[chiave] = d["testo"]
                scrivi_regia(nome, note)
                metti_segnaposto(nome, d["sezione"], chiave)
                return self._json(stato_pagina(nome))
            if rotta == "/api/nota/elimina":
                nome, chiave = d["file"], d["id"]
                note = blocchi_regia(nome)
                note.pop(chiave, None)
                scrivi_regia(nome, note) if note else (REGIA / nome).unlink(missing_ok=True)
                togli_segnaposto(nome, chiave)
                return self._json(stato_pagina(nome))
            if rotta == "/api/costruisci":
                return self._json(costruisci(d.get("file")))
        except Exception as e:                      # il pannello mostra l'errore
            return self._json({"errore": f"{type(e).__name__}: {e}"}, 500)
        self._json({"errore": "rotta sconosciuta"}, 404)


def main():
    ap = argparse.ArgumentParser(description="Pannello locale per la regia d'aula")
    ap.add_argument("--porta", type=int, default=8765)
    ap.add_argument("--senza-browser", action="store_true")
    a = ap.parse_args()

    srv = ThreadingHTTPServer(("127.0.0.1", a.porta), Pannello)
    url = f"http://127.0.0.1:{a.porta}/"
    print(f"Pannello regia su {url}   (solo questo computer — Ctrl+C per chiudere)")
    if not a.senza_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nchiuso")


if __name__ == "__main__":
    main()
