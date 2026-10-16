# Instagram skill for Claude (Español · English)

**Other Instagram skills write. This one also builds.** Reels, hooks, captions, carousels, stories, DMs, profile audit and a weekly plan, in Spanish or English. Connect SocialMaker and Claude creates the real thing in your account: the "comment GUIDE and get it by DM" automation, your link in bio, the carousel, the catalog with orders by WhatsApp, your booking page.

Free and open source (MIT). Made by [Andros Blandon](https://socialmaker.ai), founder of SocialMaker.

[Español](#español) · [English](#english)

---

## Español

### Qué hace

| Le pides | Claude |
| --- | --- |
| «Hazme el guion de un reel de 30 segundos para mi salón» | Te da 3 ganchos con puntaje, el guion por tiempos, el texto en pantalla y el llamado a la acción |
| «Escribe el caption» | Lo escribe y lo revisa: lo que se ve antes de «… más», un solo llamado a la acción, 3 a 5 hashtags |
| «Un carrusel sobre cómo reservar» | Portada, slides y caption. Con SocialMaker, te lo diseña y queda listo para editar |
| «Revisa mi perfil» | Puntaje de 20, las 3 correcciones más importantes y la bio reescrita |
| «Quiero que si comentan GUÍA les llegue mi PDF» | Escribe la automatización completa. **Con SocialMaker, la crea en tu cuenta** y te pregunta antes de encenderla |
| «Arma mi catálogo con esta foto de precios» | Lo ordena por categorías. **Con SocialMaker, lo publica con pedido por WhatsApp** |
| «Pon mis horarios y servicios» | **Con SocialMaker, configura tu agenda de citas** |
| «Plan de la semana» | Qué publicar cada día, con ganchos y las automatizaciones que lo acompañan |

Incluye dos herramientas que de verdad corren (Python, sin instalar nada): `caption_check.py` te muestra lo que se ve en el feed antes de «… más» y revisa el caption, y `humanize.py` le quita el tono de IA a tus textos en español y en inglés.

### Instalar en la app de Claude (web, escritorio o celular)

1. Descarga [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. En Claude: **Configuración (Settings) → Capacidades (Capabilities)** y activa **Ejecución de código y creación de archivos (Code execution and file creation)**.
3. **Personalizar (Customize) → Skills → + → Subir una skill (Upload a skill)** y elige el ZIP.
4. Escríbele a Claude: «Hazme el guion de un reel sobre…».

### Conectar SocialMaker (para que Claude lo haga por ti)

1. En Claude: **Personalizar (Customize) → Conectores (Connectors) → Agregar → Agregar conector personalizado (Add custom connector)**.
2. Nombre: `SocialMaker`. URL: `https://socialmaker.ai/mcp`.
3. **Conectar**, entra a tu cuenta de SocialMaker y elige qué puede hacer Claude.
4. En el chat: **+ → Conectores (Connectors)** y enciende SocialMaker.

El conector funciona con los planes Pro y Max de [SocialMaker](https://socialmaker.ai). Claude nunca te pide la contraseña de Instagram y siempre te pregunta antes de crear o encender algo.

### Claude Code

```
/plugin marketplace add androskent-cell/instagram-claude-skill
/plugin install instagram-socialmaker@socialmaker
```

---

## English

### What it does

| You ask | Claude |
| --- | --- |
| "Write a 30-second Reel for my salon" | 3 scored hooks, a timed script, on-screen text and the call to action |
| "Write the caption" | Writes it and checks it: what shows before "… more", one call to action, 3-5 hashtags |
| "A carousel about booking" | Cover, slides and caption. With SocialMaker, it designs it as an editable draft |
| "Audit my profile" | A score out of 20, the top 3 fixes and your bio rewritten |
| "When someone comments GUIDE, send my PDF" | Writes the whole automation. **With SocialMaker, it creates it in your account** and asks before turning it on |
| "Build my catalog from this price list photo" | Organizes it by category. **With SocialMaker, publishes it with orders by WhatsApp** |
| "Set my hours and services" | **With SocialMaker, sets up your booking page** |
| "Plan my week" | What to post each day, with hooks and the automations that support it |

Two tools that actually run (Python, nothing to install): `caption_check.py` shows what the feed shows before "… more" and checks the caption, and `humanize.py` strips the AI tone from your drafts in English and Spanish.

### Install in the Claude app (web, desktop or mobile)

1. Download [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. In Claude: **Settings → Capabilities**, turn on **Code execution and file creation**.
3. **Customize → Skills → + → Upload a skill** and pick the ZIP.
4. Ask Claude: "Write a Reel script about…".

### Connect SocialMaker (so Claude does it for you)

1. In Claude: **Customize → Connectors → Add → Add custom connector**.
2. Name: `SocialMaker`. URL: `https://socialmaker.ai/mcp`.
3. **Connect**, sign in to SocialMaker and choose what Claude may do.
4. In a chat: **+ → Connectors** and turn SocialMaker on.

The connector works with the SocialMaker Pro and Max plans. Claude never asks for your Instagram password and always asks before creating or turning anything on.

### Claude Code

```
/plugin marketplace add androskent-cell/instagram-claude-skill
/plugin install instagram-socialmaker@socialmaker
```

---

### What it will not do / Lo que no hace

It does not log into Instagram, follow or like for you, or DM people who did not write first. Those things get accounts restricted. / No entra a tu Instagram, no sigue ni da «me gusta» por ti, y no le escribe a quien no te escribió primero: eso hace que Instagram restrinja tu cuenta.

### License

MIT. Use it, change it, share it.
