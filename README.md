# Instagram skill for Claude (Español · English · Português · Français)

**Other Instagram skills write. This one also builds.** Reels, hooks, captions, carousels, stories, DMs, profile audit and a weekly plan, in Spanish, English, Portuguese or French. Connect SocialMaker and Claude creates the real thing in your account: the "comment GUIDE and get it by DM" automation, your link in bio, the carousel, the catalog with orders by WhatsApp, your booking page, and it schedules or publishes the post.

Free and open source (MIT). Made by [Andros Blandon](https://socialmaker.ai), founder of SocialMaker.

[Español](#español) · [English](#english) · [Português](#português) · [Français](#français)

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
| «Publícalo mañana a las 6» | **Con SocialMaker, lo programa o lo publica** después de mostrarte el resumen |
| «Plan de la semana» | Qué publicar cada día, con ganchos y las automatizaciones que lo acompañan |

Incluye dos herramientas que de verdad corren (Python, sin instalar nada): `caption_check.py` te muestra lo que se ve en el feed antes de «… más» y revisa el caption, y `humanize.py` le quita el tono de IA a tus textos en español, inglés, portugués y francés.

### Instalar en la app de Claude (web, escritorio o celular)

1. Descarga [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. En Claude: **Configuración (Settings) → Capacidades (Capabilities)** y activa **Ejecución de código y creación de archivos (Code execution and file creation)**.
3. **Personalizar (Customize) → Skills → + → Subir una skill (Upload a skill)** y elige el ZIP.
4. Escríbele a Claude: «Hazme el guion de un reel sobre…».

### Conectar SocialMaker (para que Claude lo haga por ti)

1. En Claude: **Personalizar (Customize) → Conectores (Connectors) → Agregar → Agregar conector personalizado (Add custom connector)**.
2. Nombre: `SocialMaker`. URL: `https://socialmaker.ai/mcp`.
3. **Conectar**, entra a tu cuenta de SocialMaker y elige qué puede hacer Claude. Para que publique, pon **Programar y publicar** en «Ver y cambiar».
4. En el chat: **+ → Conectores (Connectors)** y enciende SocialMaker.

El conector funciona con los planes Pro y Max de [SocialMaker](https://socialmaker.ai). Claude nunca te pide la contraseña de Instagram y siempre te pregunta antes de crear, encender o publicar algo.

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
| "Post it tomorrow at 6" | **With SocialMaker, schedules or publishes it** after showing you the summary |
| "Plan my week" | What to post each day, with hooks and the automations that support it |

Two tools that actually run (Python, nothing to install): `caption_check.py` shows what the feed shows before "… more" and checks the caption, and `humanize.py` strips the AI tone from your drafts in English, Spanish, Portuguese and French.

### Install in the Claude app (web, desktop or mobile)

1. Download [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. In Claude: **Settings → Capabilities**, turn on **Code execution and file creation**.
3. **Customize → Skills → + → Upload a skill** and pick the ZIP.
4. Ask Claude: "Write a Reel script about…".

### Connect SocialMaker (so Claude does it for you)

1. In Claude: **Customize → Connectors → Add → Add custom connector**.
2. Name: `SocialMaker`. URL: `https://socialmaker.ai/mcp`.
3. **Connect**, sign in to SocialMaker and choose what Claude may do. To let it publish, set **Schedule and publish** to "View and edit".
4. In a chat: **+ → Connectors** and turn SocialMaker on.

The connector works with the SocialMaker Pro and Max plans. Claude never asks for your Instagram password and always asks before creating, turning on or publishing anything.

### Claude Code

```
/plugin marketplace add androskent-cell/instagram-claude-skill
/plugin install instagram-socialmaker@socialmaker
```

---

## Português

### O que ela faz

| Você pede | O Claude |
| --- | --- |
| «Faz o roteiro de um reel de 30 segundos pro meu salão» | 3 ganchos com nota, o roteiro com tempos, o texto na tela e a chamada para ação |
| «Escreve a legenda» | Escreve e confere: o que aparece antes do «… mais», uma só chamada para ação, 3 a 5 hashtags |
| «Um carrossel sobre como agendar» | Capa, slides e legenda. Com o SocialMaker, ele desenha e deixa pronto pra editar |
| «Analisa meu perfil» | Nota de 0 a 20, as 3 correções mais importantes e a bio reescrita |
| «Quero que quem comentar GUIA receba meu PDF» | Escreve a automação inteira. **Com o SocialMaker, cria na sua conta** e pergunta antes de ativar |
| «Monta meu catálogo com essa foto da tabela de preços» | Organiza por categorias. **Com o SocialMaker, publica com pedido pelo WhatsApp** |
| «Coloca meus horários e serviços» | **Com o SocialMaker, configura sua agenda** |
| «Posta amanhã às 18h» | **Com o SocialMaker, agenda ou publica** depois de te mostrar o resumo |
| «Plano da semana» | O que postar em cada dia, com ganchos e as automações que acompanham |

Feita para o Brasil, não traduzida: você e «a gente», Pix e parcelado, preço visível no post (o Procon não aceita «preço no direct»), #publi quando é parceria paga e nada de sorteio sem autorização.

Duas ferramentas que rodam de verdade (Python, sem instalar nada): `caption_check.py` mostra o que aparece no feed antes do «… mais» e confere a legenda, e `humanize.py` tira o tom de IA dos seus textos.

### Instalar no app do Claude (web, computador ou celular)

1. Baixe o [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. No Claude: **Settings → Capabilities** e ative **Code execution and file creation**.
3. **Customize → Skills → + → Upload a skill** e escolha o ZIP.
4. Escreva para o Claude: «Faz o roteiro de um reel sobre…».

### Conectar o SocialMaker (para o Claude fazer por você)

1. No Claude: **Customize → Connectors → Add → Add custom connector**.
2. Nome: `SocialMaker`. URL: `https://socialmaker.ai/mcp`.
3. **Connect**, entre na sua conta do SocialMaker e escolha o que o Claude pode fazer. Para ele publicar, coloque **Agendar e publicar** em «Ver e alterar».
4. No chat: **+ → Connectors** e ative o SocialMaker.

O conector funciona com os planos Pro e Max do [SocialMaker](https://socialmaker.ai). O Claude nunca pede a senha do seu Instagram e sempre pergunta antes de criar, ativar ou publicar alguma coisa.

### Claude Code

```
/plugin marketplace add androskent-cell/instagram-claude-skill
/plugin install instagram-socialmaker@socialmaker
```

---

## Français

### Ce qu'elle fait

| Vous demandez | Claude |
| --- | --- |
| « Écris le script d'un Reel de 30 secondes pour mon salon » | 3 accroches notées, le script minuté, le texte à l'écran et l'appel à l'action |
| « Écris la légende » | Il l'écrit et la vérifie : ce qui s'affiche avant « … plus », un seul appel à l'action, 3 à 5 hashtags |
| « Un carrousel sur la réservation » | Couverture, slides et légende. Avec SocialMaker, il le met en page, prêt à modifier |
| « Analyse mon profil » | Une note sur 20, les 3 corrections prioritaires et la bio réécrite |
| « Quand quelqu'un commente GUIDE, envoie mon PDF » | Il écrit toute l'automatisation. **Avec SocialMaker, il la crée dans votre compte** et demande avant de l'activer |
| « Fais mon catalogue à partir de cette photo de tarifs » | Il le classe par catégories. **Avec SocialMaker, il le publie avec commande par WhatsApp** |
| « Mets mes horaires et mes prestations » | **Avec SocialMaker, il configure votre page de réservation** |
| « Publie-le demain à 18 h » | **Avec SocialMaker, il le programme ou le publie** après vous avoir montré le récapitulatif |
| « Mon planning de la semaine » | Quoi publier chaque jour, avec les accroches et les automatisations qui vont avec |

Pensée pour la France, pas traduite : tu ou vous choisi une fois pour toutes, espaces insécables, prix TTC visibles sans les demander, mention « Collaboration commerciale » quand une marque paie, ton sobre et concret.

Deux outils qui fonctionnent vraiment (Python, rien à installer) : `caption_check.py` montre ce qui s'affiche dans le fil avant « … plus » et vérifie la légende, et `humanize.py` enlève le ton IA de vos textes et ajoute les espaces insécables.

### Installer dans l'app Claude (web, ordinateur ou mobile)

1. Téléchargez [instagram-socialmaker.zip](https://github.com/androskent-cell/instagram-claude-skill/raw/main/dist/instagram-socialmaker.zip).
2. Dans Claude : **Settings → Capabilities**, activez **Code execution and file creation**.
3. **Customize → Skills → + → Upload a skill** et choisissez le ZIP.
4. Écrivez à Claude : « Écris le script d'un Reel sur… ».

### Connecter SocialMaker (pour que Claude le fasse à votre place)

1. Dans Claude : **Customize → Connectors → Add → Add custom connector**.
2. Nom : `SocialMaker`. URL : `https://socialmaker.ai/mcp`.
3. **Connect**, connectez-vous à SocialMaker et choisissez ce que Claude peut faire. Pour qu'il publie, réglez **Programmer et publier** sur « Voir et modifier ».
4. Dans une conversation : **+ → Connectors** et activez SocialMaker.

Le connecteur fonctionne avec les forfaits Pro et Max de [SocialMaker](https://socialmaker.ai). Claude ne demande jamais votre mot de passe Instagram et demande toujours avant de créer, d'activer ou de publier quoi que ce soit.

### Claude Code

```
/plugin marketplace add androskent-cell/instagram-claude-skill
/plugin install instagram-socialmaker@socialmaker
```

---

### What it will not do / Lo que no hace / O que ela não faz / Ce qu'elle ne fait pas

It does not log into Instagram, follow or like for you, or DM people who did not write first: those things get accounts restricted. / No entra a tu Instagram, no sigue ni da «me gusta» por ti, y no le escribe a quien no te escribió primero. / Não entra no seu Instagram, não segue nem curte por você e não manda mensagem para quem não falou com você primeiro. / Elle ne se connecte pas à votre Instagram, ne suit pas et n'aime pas à votre place, et n'écrit pas aux personnes qui ne vous ont pas écrit en premier.

### License

MIT. Use it, change it, share it.
