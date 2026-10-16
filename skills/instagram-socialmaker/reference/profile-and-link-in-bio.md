# Profile audit and link in bio

A visitor decides in about 3 seconds if they follow, write or leave. Score the profile, then fix the biggest gap first.

## Profile score (out of 20)

| Part | 2 = good | 0 = fix now |
| --- | --- | --- |
| Name field | Name + what you do («Ana · Profe de inglés») (it is searchable) | Only a name or a brand nobody searches |
| Photo | Face or clear logo, readable small | Busy image, text inside |
| Bio line 1 | Who you help + result | Quotes, emojis only |
| Bio line 2 | Proof or offer (years, clients, price from) | Missing |
| CTA | «Reserva aquí ↓» / "Book here ↓" pointing to the link | Missing |
| Link | One page with everything (link in bio) | A raw website or nothing |
| Highlights | 3-5: Precios, Reservas, Clientes, Cómo funciona | Old or unnamed |
| Pinned posts | 3 that explain who you are and what you sell | Random |
| Grid | Covers readable, consistent style | No pattern |
| Category / contact | Professional account, correct category, contact buttons | Personal account |

Output the score, then the top 3 fixes with the rewritten text ready to paste.

## Bio formulas

- ES: «Te ayudo a {resultado} sin {dolor}. {Prueba}. Reserva ↓»
- EN: "I help {who} {result} without {pain}. {Proof}. Book below ↓"
- PT: «Te ajudo a {resultado} sem {dor}. {Prova}. Agenda aqui ↓» (real estate adds «CRECI 123456-F»)
- FR: «J'aide {qui} à {résultat} sans {douleur}. {Preuve}. Réservez ici ↓» (or tu, to match the account)

The name field is searchable: «Ana · Manicure em Moema», «Léa | Ongles Lyon 7e».

## The link in bio page

One page, in this order: the main action (book, buy, join), the free lead magnet, WhatsApp, the catalog or menu, proof (reviews, results), social links. Max 5-7 buttons; the first one is the money one.

Brazil: a WhatsApp button («Chama no zap») is expected. France: prices reachable without asking, and a professional who sells needs «Mentions légales» (and CGV if they take orders) linked from the page.

**Build mode:** `get_link_in_bio` to read the current page, then propose changes; on yes use `update_link_in_bio_profile`, `add_link_in_bio_button`, `update_link_in_bio_button` or the design tools. `get_link_in_bio_stats` shows which buttons get clicks (when the plan includes it): remove what nobody taps.
