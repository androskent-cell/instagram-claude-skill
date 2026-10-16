#!/usr/bin/env python3
"""Caption check for Instagram (Spanish, English, Portuguese or French). No dependencies.

Shows what the feed shows before "... more" (about 125 characters), then
checks length, the first line, hashtags, the call to action, search words,
a price hidden in the DM and, in French, the no-break spaces.

  python3 caption_check.py caption.txt
  python3 caption_check.py caption.txt --keywords "profe de inglés,clases en línea"
  python3 caption_check.py caption.txt --lang pt
  echo "text" | python3 caption_check.py -
"""
import argparse
import os
import re
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from humanize import detectar_idioma  # noqa: E402  (same folder, no dependencies)

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
    # Portuguese
    r"comente", r"chama", r"(me )?manda", r"salva", r"compartilha", r"garante", r"clica",
    r"segue", r"baixa", r"vem", r"encomenda", r"marca quem",
    # French
    r"commentez?", r"[ée]cris(-moi)?", r"[ée]crivez(-moi)?", r"envoie(-moi|-le)?", r"envoyez(-moi|-le)?",
    r"enregistrez?", r"partagez?", r"r[ée]servez?", r"abonne-toi", r"abonnez-vous", r"r[ée]ponds",
    r"r[ée]pondez", r"dis-le-moi", r"dites(-le)?-moi", r"cliquez?", r"t[ée]l[ée]chargez?", r"commandez?",
]
CEBO = [
    r"etiqueta a \d", r"menciona a \d", r"dale like si", r"like si est[aá]s", r"comparte si",
    r"tag \d", r"tag (a|your) friend", r"like if you", r"follow for more", r"s[ií]gueme para m[aá]s",
    r"marca \d", r"marque \d", r"curt[ae] se\b", r"curte e compartilha", r"compartilha se\b",
    r"tague \d", r"taguez \d", r"identifie \d", r"like si\b", r"partage si\b",
]
SALUDO = re.compile(
    r"^\s*(hola+|holi|hey|hi|hello|buen(os|as) (d[ií]as|tardes|noches)|qu[eé] tal|"
    r"oi+|ol[áa]|e a[íi]|bom dia|boa (tarde|noite)|bonjour|salut|coucou|bonsoir)\b",
    re.I,
)
# "DM for price" in four languages: illegal in Brazil and France, and it loses sales everywhere.
PRECIO_ESCONDIDO = re.compile(
    r"pre[cç]o (no|por|via) (direct|dm|inbox|privado)|valor (no |por |via )?(direct|inbox)|"
    r"precio (por|al|en) (inbox|dm|privado|interno|md)|precios? por (dm|md|inbox)|"
    r"prix en (dm|mp|priv[ée])|tarifs? en (dm|mp|priv[ée])|dm (me )?for (the )?price|price in (the )?dm",
    re.I,
)
PALABRA_PRECIO = {"PRECIO", "PRECIOS", "PREÇO", "PRECO", "VALOR", "PRICE", "PRICES", "PRIX", "TARIFS", "TARIFAS"}
MONEDA = re.compile(
    r"(R\$|US\$|\$|€|£|CHF|S/)\s?\d|\d[\d.,\s]*\s?(€|reais|euros?|pesos|soles|CHF|USD|MXN|COP|ARS|CLP)\b", re.I
)
# The verb in any case («Comenta», "comment"), the keyword in capitals.
PALABRA_CLAVE = re.compile(
    r"\b(?i:comenta|comente|comment|commente|commentez|escribe|dm me|resp[oó]nde(me)?|reply|"
    r"r[ée]ponds|r[ée]pondez|manda|envie)\s+[«\"']?\s?(?P<palabra>[A-ZÁÉÍÓÚÑÃÕÂÊÔÇÀÈÙÛÎÏËŒ]{3,})"
)
FINO = chr(0x202F)
DURO = chr(0x00A0)


def leer(archivo):
    if archivo == "-":
        return sys.stdin.read()
    datos = open(archivo, "rb").read()
    try:
        texto = datos.decode("utf-8")
    except UnicodeDecodeError:
        texto = datos.decode("latin-1")
    # Windows line endings would come back doubled when printed.
    return texto.replace("\r\n", "\n")


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
        o = o.strip().lstrip("¡¿\"«'-•*0123456789. " + DURO + FINO)
        if o:
            oraciones.append(o)
    encontrados = []
    verbos = "|".join(CTA)
    for o in oraciones:
        if not re.match(r"(" + verbos + r")\b", o):
            continue
        # «Comenta GUÍA, escríbeme y reserva» = three calls in one sentence.
        for m in re.finditer(r"(?:^|,\s*|\s(?:y|o|e|ou|et|and|or)\s+)(" + verbos + r")\b", o):
            encontrados.append(m.group(1))
    return encontrados


def espacios_franceses(texto):
    """Signs ? ! : ; without the no-break space French needs (URLs and 18:30 do not count)."""
    sin = re.findall(r"[^\s\d:/][?!;:](?=\s|$)", texto)
    comunes = re.findall(r"\S [?!;:](?=\s|$)", texto)
    return len(sin) + len(comunes)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo", help="file with the caption, or - for stdin")
    ap.add_argument("--keywords", default="", help="comma-separated search words that should appear")
    ap.add_argument("--lang", choices=["auto", "es", "en", "pt", "fr", "fr-ca"], default="auto",
                    help="language of the caption (default: detect it)")
    a = ap.parse_args()
    texto = leer(a.archivo).strip("\n")
    plano = re.sub(r"\s+", " ", texto).strip()
    idioma = detectar_idioma(texto) if a.lang == "auto" else a.lang

    print("\n  WHAT THE FEED SHOWS / LO QUE SE VE EN EL FEED")
    print("  +" + "-" * 56 + "+")
    for linea in textwrap.wrap(plano[:VENTANA], 54) or [""]:
        print(f"  | {linea:<54} |")
    print("  +" + "-" * 45 + " ... more +\n")
    print(f"  INFO  {'LANGUAGE':<14} {idioma}{' (detected)' if a.lang == 'auto' else ''}")

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
        aviso("HASHTAGS", f"{len(tags)}: Instagram allows 5 at most, keep 3-5 specific ones")
    else:
        ok("HASHTAGS", f"{len(tags)}: " + " ".join(tags))
    con_tilde = [t for t in tags if re.search(r"[^\x00-\x7f]", t)]
    if con_tilde:
        aviso("HASHTAG ACCENTS", " ".join(con_tilde) + ": people type them without accents (#imoveis, #ongleslyon)")

    ctas = llamados(texto)
    if not ctas:
        aviso("CALL TO ACTION", "none at the end: close with ONE action (comment a word, book, save)")
    elif len(ctas) > 1:
        aviso("CALL TO ACTION", f"{len(ctas)} ({', '.join(ctas)}): keep one")
    else:
        ok("CALL TO ACTION", ctas[0])

    palabra = PALABRA_CLAVE.search(plano)
    if palabra:
        print(f"  INFO  {'KEYWORD':<14} «{palabra.group('palabra')}»: it needs an automation that answers it (reference/automations.md)")

    bajo = plano.lower()
    hay_precio = bool(MONEDA.search(plano))
    if PRECIO_ESCONDIDO.search(bajo):
        aviso("PRICE", "price hidden in the DM: show it in the post (required in Brazil and France, and it sells more)")
    elif palabra and palabra.group("palabra").upper() in PALABRA_PRECIO and not hay_precio:
        aviso("PRICE", "the keyword asks for the price but the caption shows none: add it («a partir de R$ 90», «à partir de 45 €»)")

    cebo = [p for p in CEBO if re.search(p, bajo)]
    if cebo:
        aviso("BAIT", "engagement bait found: remove it")
    else:
        ok("BAIT", "no engagement bait")

    if idioma == "fr":
        faltan = espacios_franceses(texto)
        if faltan:
            aviso("FR SPACES", f"{faltan} sign(s) ? ! : ; without the no-break space: run humanize.py, it adds them")
        else:
            ok("FR SPACES", "no-break spaces before ? ! : ;")

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
