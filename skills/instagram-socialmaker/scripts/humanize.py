#!/usr/bin/env python3
"""Make a draft sound human (Spanish, English, Portuguese or French). No dependencies.

Fixes: invisible characters, long dashes used as pauses, stock AI phrases,
and in French the no-break spaces before ? ! : ; and inside « ».
Flags (for a human rewrite): "it's not just X, it's Y", greeting openers,
emoji at the start of every line, uniform sentence length, engagement bait,
stacked exclamation marks.

  python3 humanize.py draft.txt            # prints the clean text
  python3 humanize.py draft.txt --report   # and every change + flags
  python3 humanize.py draft.txt --lang fr  # force the language (es, en, pt, fr, fr-ca)
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
# French spaces: narrow no-break before ? ! ; and no-break before : and inside « ».
FINO = chr(0x202F)
DURO = chr(0x00A0)

# phrase -> replacement ("" deletes). Matched case-insensitively, as whole
# words, longest first inside each language. An apostrophe matches ' and ’.
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
    # Portuguese (Brazil)
    "em um mundo cada vez mais digital": "hoje",
    "no mundo atual": "hoje",
    "nos dias de hoje": "hoje",
    "é importante ressaltar que": "",
    "é importante notar que": "",
    "vale ressaltar que": "",
    "vale destacar que": "",
    "vamos mergulhar em": "vamos ver",
    "vamos mergulhar": "vamos ver",
    "leve seu negócio para o próximo nível": "faça seu negócio crescer",
    "levar seu negócio para o próximo nível": "fazer seu negócio crescer",
    "elevar seu negócio a outro nível": "fazer seu negócio crescer",
    "não perca essa oportunidade única": "",
    "não perca essa oportunidade": "",
    "estamos animados em anunciar que": "",
    "estamos animados em anunciar": "chegou",
    "sinta-se à vontade para entrar em contato": "qualquer dúvida, me chama",
    "não hesite em entrar em contato": "qualquer dúvida, me chama",
    "espero que esta mensagem o encontre bem": "",
    "em resumo,": "",
    "em suma,": "",
    "descubra como": "veja como",
    # French
    "dans le monde d'aujourd'hui": "aujourd'hui",
    "dans le monde actuel": "aujourd'hui",
    "à l'ère du numérique": "aujourd'hui",
    "il est important de noter que": "",
    "il convient de souligner que": "",
    "il est crucial de comprendre que": "",
    "plongeons au cœur de": "voyons",
    "plongeons dans": "voyons",
    "n'hésitez pas à nous contacter": "écrivez-nous",
    "n'hésitez pas à me contacter": "écrivez-moi",
    "n'hésite pas à me contacter": "écris-moi",
    "un véritable game changer": "un vrai changement",
    "passez au niveau supérieur": "",
    "embarquez avec nous": "suivez-nous",
    "en conclusion,": "",
    "en résumé,": "",
    "en somme,": "",
}
NO_SOLO = re.compile(
    r"\b(no es s[oó]lo|it'?s not just|it is not just|n[ãa]o [ée] (s[oó]|sobre)|ce n['’]est pas( seulement| juste)?)\b"
    r"[^.!?\n]{1,60}[,;:]\s*(es|it'?s|it is|[ée]|c['’]est)\b",
    re.I,
)
SALUDO = re.compile(
    r"^\s*(hola+|hey|hi|hello|en el (post|video) de hoy|in today'?s (post|video)|oi+|ol[áa]|e a[íi]|"
    r"no (post|v[íi]deo) de hoje|bonjour|salut|coucou|bonsoir|dans (la vid[ée]o|le post) d['’]aujourd['’]hui)\b",
    re.I,
)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CEBO = re.compile(
    r"etiqueta a \d|menciona a \d|dale like si|tag \d|like if you|follow for more|"
    r"marca \d|marque \d|curt[ae] se\b|curte e compartilha|compartilha se\b|"
    r"tague \d|taguez \d|identifie \d|like si\b|partage si\b",
    re.I,
)

# Words that tell the languages apart (none shared between two of them).
PALABRAS = {
    "es": set("el los las del y por una es muy más pero también aquí hoy cómo qué con mis tus usted".split()),
    "pt": set("você não é do da dos das os em com uma mais também aqui isso seu sua pra né tá gente meu minha".split()),
    "fr": set("le les des et est vous pour une avec pas dans je ce du au sur qui votre ton mes c'est j'ai".split()),
    "en": set("the and you your to for is with this of it my that on are i'm".split()),
}
LETRAS = {"es": "ñ¿¡", "pt": "ãõ", "fr": "èùœë"}


def detectar_idioma(texto):
    """es, en, pt or fr: the language with the most distinctive words and letters."""
    bajo = texto.lower().replace("’", "'")
    palabras = re.findall(r"[a-zà-öø-ÿœ']+", bajo)
    puntos = {k: sum(1 for p in palabras if p in v) for k, v in PALABRAS.items()}
    for k, letras in LETRAS.items():
        puntos[k] += 3 * sum(bajo.count(c) for c in letras)
    mejor = max(puntos, key=lambda k: puntos[k])
    return mejor if puntos[mejor] > 0 else "en"


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


def patron(frase):
    cuerpo = re.escape(frase).replace("'", "['’]")
    return re.compile(r"(?<!\w)" + cuerpo + r"(?!\w)", re.I)


def ordenar(texto):
    """Tidy what the deletions leave behind."""
    texto = re.sub(r"[ \t]{2,}", " ", texto)
    texto = re.sub(r" +([,.;:!?])", r"\1", texto)
    texto = re.sub(r",\s*,", ",", texto)
    texto = re.sub(r",(?=\s*[.!?]|[ \t]*$)", "", texto, flags=re.M)
    texto = re.sub(r"([!?])\.+", r"\1", texto)
    texto = re.sub(r"(^|[.!?]\s+)[,;:]\s*", r"\1", texto, flags=re.M)
    texto = re.sub(r"^[ \t]+", "", texto, flags=re.M)
    # Capital letter at the start of each sentence (after ¡ ¿ « or a quote too).
    texto = re.sub(
        r"(^|[.!?]\s+)([¡¿«\"]?\s?)([a-zà-öø-ÿœ])",
        lambda m: m.group(1) + m.group(2) + m.group(3).upper(),
        texto,
        flags=re.M,
    )
    return texto.strip()


def espacios_frances(texto, quebec=False):
    """No-break spaces of French typography. URLs, times (18:30) and emoticons
    are left alone: a sign only counts when a space or the end comes after it."""
    espacios = "[ " + DURO + FINO + "]"
    if not quebec:
        texto = re.sub(r"(\S)" + espacios + r"?([?!;]+)(?=\s|$|[»\"])", r"\1" + FINO + r"\2", texto)
    texto = re.sub(r"([^\s\d:/])" + espacios + r"?:(?=\s|$)", r"\1" + DURO + ":", texto)
    texto = re.sub("«" + espacios + r"*(?=\S)", "«" + DURO, texto)
    texto = re.sub(r"(?<=\S)" + espacios + "*»", DURO + "»", texto)
    return texto


def limpiar(texto, cambios, idioma):
    n = len(INVISIBLES.findall(texto))
    if n:
        texto = INVISIBLES.sub("", texto)
        cambios.append(f"removed {n} invisible character(s)")
    nuevo, n = re.subn(r"\s*—\s*", ", ", texto)
    if n:
        texto = nuevo
        cambios.append(f"replaced {n} long dash(es) with commas")
    for frase, reemplazo in FRASES.items():
        p = patron(frase)
        if p.search(texto):
            texto = p.sub(reemplazo, texto)
            cambios.append(f"«{frase}» -> «{reemplazo or '(deleted)'}»")
    texto = ordenar(texto)
    if idioma in ("fr", "fr-ca"):
        nuevo = espacios_frances(texto, quebec=idioma == "fr-ca")
        if nuevo != texto:
            texto = nuevo
            cambios.append("French typography: no-break spaces before " + (": and inside « »" if idioma == "fr-ca" else "? ! : ; and inside « »"))
    return texto


def banderas(texto):
    out = []
    if NO_SOLO.search(texto):
        out.append("«no es solo X, es Y» / \"it's not just X, it's Y\" / «não é X, é Y» / «ce n'est pas X, c'est Y»: say it plainly")
    lineas = [l for l in texto.splitlines() if l.strip()]
    if lineas and SALUDO.search(lineas[0]):
        out.append("opens with a greeting or a preamble: in a caption or a script, open with the hook (fine in a DM)")
    con_emoji = sum(1 for l in lineas if EMOJI.match(l.strip()))
    if len(lineas) >= 3 and con_emoji >= len(lineas) * 0.6:
        out.append("emoji at the start of almost every line: keep 0-2")
    frases = [f for f in re.split(r"(?<=[.!?])\s+", texto) if len(f.split()) > 2]
    if len(frases) >= 5 and statistics.pstdev([len(f.split()) for f in frases]) < 2.5:
        out.append("every sentence is about the same length: mix short and long")
    if CEBO.search(texto):
        out.append("engagement bait («etiqueta a 3», \"tag 3 friends\", «marca 3 amigos», «tague 3 amis»): remove it")
    if re.search(r"[!?][\s" + FINO + r"]*[!?][\s" + FINO + r"]*[!?]|!!", texto):
        out.append("stacked exclamation marks: one is enough")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo", help="file with the draft, or - for stdin")
    ap.add_argument("--report", action="store_true", help="print the changes and the flags")
    ap.add_argument("--lang", choices=["auto", "es", "en", "pt", "fr", "fr-ca"], default="auto",
                    help="language of the draft (default: detect it); fr-ca = Quebec spacing")
    a = ap.parse_args()
    original = leer(a.archivo)
    idioma = detectar_idioma(original) if a.lang == "auto" else a.lang
    cambios = []
    limpio = limpiar(original, cambios, idioma)
    print(limpio)
    if a.report:
        print(f"\n--- language: {idioma}{' (detected)' if a.lang == 'auto' else ''} ---")
        print("--- changes ---")
        print("\n".join(f"  - {c}" for c in cambios) or "  (none)")
        print("--- flags (rewrite by hand) ---")
        print("\n".join(f"  - {b}" for b in banderas(limpio)) or "  (none)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
