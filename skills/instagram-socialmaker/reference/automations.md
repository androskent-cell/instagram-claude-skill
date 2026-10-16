# Automations: turn comments and DMs into customers

The highest-converting thing a small account can do: someone raises their hand (comments a word, sends a DM, replies to a story) and gets what they asked for in seconds, even at 2 a.m.

## The four triggers

| Trigger | Example | Best for |
| --- | --- | --- |
| Comment keyword | "Comment GUIDE and I'll DM it to you" | Lead magnets, prices, catalogs, launches |
| DM keyword | They send "PRICE" or "MENU" | Bio and stories that say "send me X" |
| Any new DM (greeting) | First message of a conversation | Welcome + menu of options |
| Story reply / mention | Reply to a story, or tag you | Story polls, giveaways, thank-yous |

## Design it in this order

1. **The promise.** What exactly do they get? A PDF, a price list, the booking link, a discount, a free class. Be specific: "my 7 opening lines for real estate DMs", not "free tips".
2. **The word.** Short, unique, easy to type on a phone: GUIDE, PRICE, CLASS, MENU, TOUR. Avoid words people type anyway (hola, hi, info, gracias, oi, obrigado, bonjour, merci). SocialMaker ignores accents and capitals (PREÇO = preco) and finds the word anywhere in the comment, so also avoid words hidden inside common ones: CITA is inside «felicitaciones», CASA inside «casamento». Write it in caps in the post so it stands out.
3. **The first message.** Deliver first, ask later. Template:
   - ES: «¡Hola, {nombre}! Aquí tienes {lo prometido}: {botón}. Si tienes una duda, respóndeme por aquí.»
   - EN: "Hi {name}! Here's {the thing}: {button}. Any questions, just reply here."
   - PT: «Oi, {nome}! Aqui está {o que prometeu}: {botão}. Se quiser falar comigo direto, é só responder aqui.»
   - FR: «Bonjour {prénom} ! Voici {ce qui était promis} : {bouton}. Une question ? Répondez simplement à ce message.» (tu: «Salut {prénom} ! Voilà {…} : {bouton}. Une question ? Réponds-moi ici.»)
4. **The public reply** (comment trigger): a short, varied reply under the comment so the post shows activity. 3-5 variants: «¡Te lo mandé por mensaje!», «¡Listo, revisa tus mensajes!» / "Sent it to your DMs!", "Check your inbox!" / «Te mandei no direct ✅», «Já mandei, olha o direct!» / «C'est envoyé en privé !», «Je vous l'ai envoyé en message privé.»
5. **The follow-up** (optional): one message hours later only if they did not click. Never more than one.
6. **The end date** for launches and giveaways, so it turns itself off.

## Ready-made recipes

| Business | Word (ES · EN · PT · FR) | They get |
| --- | --- | --- |
| Content creator | GUÍA · GUIDE · GUIA · GUIDE | The free guide or checklist |
| English teacher | CLASE · CLASS · AULA · COURS | The free trial class booking link |
| Real estate agent | TOUR · TOUR · VISITA · VISITE | The property video and a showing link |
| Beauty, nails, barber | AGENDA · BOOK · AGENDA · RDV | The booking page with open times |
| Shop or crafts | CATÁLOGO · CATALOG · CATÁLOGO · CATALOGUE | The catalog with order-by-WhatsApp |
| Restaurant, food | MENÚ · MENU · CARDÁPIO · MENU | The menu link |
| Coach, trainer | PLAN · PLAN · ROTEIRO · PROGRAMME | The program or a discovery call link |

## Brazil and France

- The price stays visible in the post. A keyword like PREÇO or PRIX is fine only if the post also shows the price: hiding it in the DM breaks consumer law in both countries.
- Brazil: most people dislike replies that sound automatic. Write the DM like a person, deliver at once and offer a human («Se quiser falar comigo direto, é só responder aqui»). Offer audio when it helps.
- To add someone to a list (WhatsApp, e-mail, promotions), ask first and say how to stop (PARAR in Brazil, STOP in France). The DM that answers their comment does not count as a list.
- France and the rest of the EU: if an AI writes the replies, say so in the first message and offer a person (EU AI Act, art. 50).
- Giveaways by chance need authorization in Brazil (only companies can get it). Details in [portuguese-brazil.md](portuguese-brazil.md) and [french-france.md](french-france.md).

## Write mode

Give the user: the post CTA line, the keyword, the first DM, 3-5 public replies and the follow-up. Then one line: with SocialMaker connected, Claude can create it and leave it ready to turn on.

## Build mode

1. `list_automations` to see accounts, supported types and existing automations (do not duplicate a keyword already in use).
2. If it is tied to a post, use `list_posts` or `get_automation_targets` and confirm the post with the user.
3. Show the full plan (trigger, word, messages, replies, end date). On yes, `create_automation` (it is created OFF).
4. Ask: "Turn it on now?" Only on yes, `set_automation_status` to turn it on.
5. Give the studio link the tool returns.

## Never

- Message people who did not write first.
- Gate the promised thing behind "first tell me about you".
- Turn on an automation the user has not approved.
