#!/usr/bin/env python3
"""Caption check for Instagram (Spanish or English). No dependencies.

Shows what the feed shows before "... more" (about 125 characters), then
checks length, the first line, hashtags, the call to action and search words.

  python3 caption_check.py caption.txt
  python3 caption_check.py caption.txt --keywords "profe de inglés,clases en línea"
  echo "text" | python3 caption_check.py -
"""
import argparse
import re
import sys
import textwrap

VENTANA = 125
MAX_LARGO = 2200
HASHTAG = re.compile(r"(?<!\w)#\w+", re.UNICODE)

# A call to action is a SENTENCE of the last paragraph that starts with one of
# these verbs, so "link in bio" or "I'll send it" in the middle of a sentence
# do not count.
CTA = [
    # Spanish
    r"comenta", r"escr[ií]be(me)?", r"reserva", r"agenda", r"gu[aá]rd(a|alo)", r"comparte",
    r"env[ií]a(me)?", r"resp[oó]nde(me)?", r"descarga", r"inscr[ií]bete", r"pide", r"compra",
    r"entra", r"toca", r"haz clic",
    # English
    r"comment", r"dm me", r"book", r"save", r"share", r"send me", r"reply", r"download",
    r"sign up", r"order", r"buy", r"tap", r"click", r"grab",
]
CEBO = [
    r"etiqueta a \d", r"menciona a \d", r"dale like si", r"like si est[aá]s", r"comparte si",
    r"tag \d", r"tag (a|your) friend", r"like if you", r"follow for more", r"s[ií]gueme para m[aá]s",
]
SALUDO = re.compile(r"^\s*(hola+|holi|hey|hi|hello|buen(os|as) (d[ií]as|tardes|noches)|qu[eé] tal)\b", re.I)


def leer(archivo):
    if archivo == "-":
        return sys.stdin.read()
    datos = open(archivo, "rb").read()
    try:
        return datos.decode("utf-8")
    except UnicodeDecodeError:
        return datos.decode("latin-1")


def ok(etiqueta, texto):
    print(f"  PASS  {etiqueta:<14} {texto}")


def aviso(etiqueta, texto):
    print(f"  WARN  {etiqueta:<14} {texto}")


def llamados(texto):
    """Calls to action in the last paragraph that is not only hashtags."""
    parrafos = [p for p in re.split(r"\n\s*\n", texto) if HASHTAG.sub("", p).strip()]
    final = HASHTAG.sub("", parrafos[-1] if parrafos else "").lower()
    oraciones = []
    for o in re.split(r"(?<=[.!?])\s+|\n", final):
        o = o.strip().lstrip("¡¿\"«'-•*0123456789. ")
        if o:
            oraciones.append(o)
    encontrados = []
    verbos = "|".join(CTA)
    for o in oraciones:
        if not re.match(r"(" + verbos + r")\b", o):
            continue
        # «Comenta GUÍA, escríbeme y reserva» = three calls in one sentence.
        for m in re.finditer(r"(?:^|,\s*|\s(?:y|o|and|or)\s+)(" + verbos + r")\b", o):
            encontrados.append(m.group(1))
    return encontrados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo", help="file with the caption, or - for stdin")
    ap.add_argument("--keywords", default="", help="comma-separated search words that should appear")
    a = ap.parse_args()
    texto = leer(a.archivo).strip("\n")
    plano = re.sub(r"\s+", " ", texto).strip()

    print("\n  WHAT THE FEED SHOWS / LO QUE SE VE EN EL FEED")
    print("  +" + "-" * 56 + "+")
    for linea in textwrap.wrap(plano[:VENTANA], 54) or [""]:
        print(f"  | {linea:<54} |")
    print("  +" + "-" * 45 + " ... more +\n")

    n = len(texto)
    (ok if n <= MAX_LARGO else aviso)("LENGTH", f"{n} / {MAX_LARGO} characters")

    primera = texto.splitlines()[0] if texto else ""
    if SALUDO.search(primera):
        aviso("FIRST LINE", "starts with a greeting: open with the hook instead")
    elif primera.lstrip().startswith("#"):
        aviso("FIRST LINE", "starts with hashtags")
    elif len(primera) > VENTANA:
        aviso("FIRST LINE", f"{len(primera)} characters: it gets cut at ~{VENTANA}")
    else:
        ok("FIRST LINE", f"{len(primera)} characters, fits in the window")

    concretos = re.findall(r"\d+", plano[:VENTANA])
    if concretos:
        ok("CONCRETE", f"{len(concretos)} number(s) in the visible window")
    else:
        aviso("CONCRETE", "no number, price or name in the visible window")

    tags = HASHTAG.findall(texto)
    if not tags:
        aviso("HASHTAGS", "none: add 3-5 specific ones at the end")
    elif len(tags) > 5:
        aviso("HASHTAGS", f"{len(tags)}: keep 3-5 specific ones")
    else:
        ok("HASHTAGS", f"{len(tags)}: " + " ".join(tags))

    ctas = llamados(texto)
    if not ctas:
        aviso("CALL TO ACTION", "none at the end: close with ONE action (comment a word, book, save)")
    elif len(ctas) > 1:
        aviso("CALL TO ACTION", f"{len(ctas)} ({', '.join(ctas)}): keep one")
    else:
        ok("CALL TO ACTION", ctas[0])

    palabra = re.search(r"\b(comenta|comment|escribe|dm me|resp[oó]nde(me)?|reply)\s+[«\"']?([A-ZÁÉÍÓÚÑ]{3,})", plano)
    if palabra:
        print(f"  INFO  {'KEYWORD':<14} «{palabra.group(3)}»: it needs an automation that answers it (reference/automations.md)")

    bajo = plano.lower()
    cebo = [p for p in CEBO if re.search(p, bajo)]
    if cebo:
        aviso("BAIT", "engagement bait found: remove it")
    else:
        ok("BAIT", "no engagement bait")

    if a.keywords:
        pedidas = [k.strip() for k in a.keywords.split(",") if k.strip()]
        faltan = [k for k in pedidas if k.lower() not in bajo]
        if faltan:
            aviso("SEARCH WORDS", "missing: " + ", ".join(faltan))
        else:
            ok("SEARCH WORDS", f"{len(pedidas)}/{len(pedidas)} present")
    print()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
