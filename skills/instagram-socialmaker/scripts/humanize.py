#!/usr/bin/env python3
"""Make a draft sound human (Spanish or English). No dependencies.

Fixes: invisible characters, long dashes used as pauses, stock AI phrases.
Flags (for a human rewrite): "it's not just X, it's Y", greeting openers,
emoji at the start of every line, uniform sentence length, engagement bait.

  python3 humanize.py draft.txt            # prints the clean text
  python3 humanize.py draft.txt --report   # and every change + flags
  echo "text" | python3 humanize.py - --report
"""
import argparse
import re
import statistics
import sys

# Zero-width spaces and joiners, word joiner, byte-order mark, soft hyphen,
# Mongolian vowel separator, invisible operators and Unicode tag characters
# (written as numbers so no editor can strip them from this file).
_CODIGOS = (0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0x00AD, 0x180E)
INVISIBLES = re.compile(
    "[" + "".join(map(chr, _CODIGOS)) + chr(0x2061) + "-" + chr(0x2064) + chr(0xE0000) + "-" + chr(0xE007F) + "]"
)

# phrase -> replacement ("" deletes). Matched case-insensitively.
FRASES = {
    # Spanish
    "en el mundo actual": "hoy",
    "en la era digital": "hoy",
    "sin lugar a dudas": "",
    "es importante destacar que": "",
    "es importante mencionar que": "",
    "cabe mencionar que": "",
    "cabe destacar que": "",
    "lleva tu negocio al siguiente nivel": "haz crecer tu negocio",
    "llevar tu negocio al siguiente nivel": "hacer crecer tu negocio",
    "potencia tu marca": "haz crecer tu marca",
    "sumérgete en": "mira",
    "desbloquea": "consigue",
    "un antes y un después": "un gran cambio",
    "no te lo puedes perder": "",
    "¡vamos allá!": "",
    # English
    "in today's fast-paced world": "today",
    "in today's digital age": "today",
    "it's important to note that": "",
    "it is important to note that": "",
    "take your business to the next level": "grow your business",
    "game-changer": "big change",
    "game changer": "big change",
    "let's dive in": "",
    "dive into": "look at",
    "delve into": "look at",
    "unlock": "get",
    "elevate your": "improve your",
    "embark on a journey": "start",
    "in conclusion,": "",
    "stop scrolling": "",
    "follow for more": "",
}
NO_SOLO = re.compile(r"\b(no es s[oó]lo|it'?s not just|it is not just)\b[^.!?\n]{1,60}[,;:]\s*(es|it'?s|it is)\b", re.I)
SALUDO = re.compile(r"^\s*(hola+|hey|hi|hello|en el (post|video) de hoy|in today'?s (post|video))\b", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CEBO = re.compile(r"etiqueta a \d|menciona a \d|dale like si|tag \d|like if you|follow for more", re.I)


def leer(archivo):
    if archivo == "-":
        return sys.stdin.read()
    datos = open(archivo, "rb").read()
    try:
        return datos.decode("utf-8")
    except UnicodeDecodeError:
        return datos.decode("latin-1")


def ordenar(texto):
    """Tidy what the deletions leave behind."""
    texto = re.sub(r"[ \t]{2,}", " ", texto)
    texto = re.sub(r" +([,.;:!?])", r"\1", texto)
    texto = re.sub(r",\s*,", ",", texto)
    texto = re.sub(r",(?=\s*[.!?]|[ \t]*$)", "", texto, flags=re.M)
    texto = re.sub(r"([!?])\.+", r"\1", texto)
    texto = re.sub(r"(^|[.!?]\s+)[,;:]\s*", r"\1", texto, flags=re.M)
    texto = re.sub(r"^[ \t]+", "", texto, flags=re.M)
    # Capital letter at the start of each sentence (after ¡ or ¿ too).
    texto = re.sub(
        r"(^|[.!?]\s+)([¡¿«\"]?)([a-záéíóúñ])",
        lambda m: m.group(1) + m.group(2) + m.group(3).upper(),
        texto,
        flags=re.M,
    )
    return texto.strip()


def limpiar(texto, cambios):
    n = len(INVISIBLES.findall(texto))
    if n:
        texto = INVISIBLES.sub("", texto)
        cambios.append(f"removed {n} invisible character(s)")
    nuevo, n = re.subn(r"\s*—\s*", ", ", texto)
    if n:
        texto = nuevo
        cambios.append(f"replaced {n} long dash(es) with commas")
    for frase, reemplazo in FRASES.items():
        patron = re.compile(re.escape(frase), re.I)
        if patron.search(texto):
            texto = patron.sub(reemplazo, texto)
            cambios.append(f"«{frase}» -> «{reemplazo or '(deleted)'}»")
    return ordenar(texto)


def banderas(texto):
    out = []
    if NO_SOLO.search(texto):
        out.append("«no es solo X, es Y» / \"it's not just X, it's Y\": say it plainly")
    lineas = [l for l in texto.splitlines() if l.strip()]
    if lineas and SALUDO.search(lineas[0]):
        out.append("opens with a greeting or a preamble: open with the hook")
    con_emoji = sum(1 for l in lineas if EMOJI.match(l.strip()))
    if len(lineas) >= 3 and con_emoji >= len(lineas) * 0.6:
        out.append("emoji at the start of almost every line: keep 0-2")
    frases = [f for f in re.split(r"(?<=[.!?])\s+", texto) if len(f.split()) > 2]
    if len(frases) >= 5 and statistics.pstdev([len(f.split()) for f in frases]) < 2.5:
        out.append("every sentence is about the same length: mix short and long")
    if CEBO.search(texto):
        out.append("engagement bait («etiqueta a 3», \"tag 3 friends\"): remove it")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo", help="file with the draft, or - for stdin")
    ap.add_argument("--report", action="store_true", help="print the changes and the flags")
    a = ap.parse_args()
    cambios = []
    limpio = limpiar(leer(a.archivo), cambios)
    print(limpio)
    if a.report:
        print("\n--- changes ---")
        print("\n".join(f"  - {c}" for c in cambios) or "  (none)")
        print("--- flags (rewrite by hand) ---")
        print("\n".join(f"  - {b}" for b in banderas(limpio)) or "  (none)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
