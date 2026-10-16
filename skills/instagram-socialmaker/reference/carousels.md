# Carousels

Carousels get saved and shared, and every swipe keeps the post alive. They are the best format for "how to", lists, before/after and mini-guides.

## Structure (6-8 slides)

| Slide | Job |
| --- | --- |
| 1. Cover | The hook in 4-8 big words + a reason to swipe ("→", "5 steps", "the last one is the one") |
| 2. The problem | Why it matters to this viewer, one sentence |
| 3-6. The value | One point per slide. A title of 3-6 words + 1-2 lines. Numbers when possible |
| 7. Summary | The whole thing in one glance (people screenshot this) |
| 8. CTA | One action: comment a word, save, book |

## Rules

- One point per slide, readable without zooming: max ~25 words per slide.
- The cover must make sense alone in the grid (the profile grid crops to a portrait rectangle; keep text centered).
- Same style on every slide: 1 font for titles, 1 for text, 1 accent color.
- Write the caption separately (see [captions.md](captions.md)); do not repeat the slides word for word.

## Write mode

Deliver: slide-by-slide copy (title + body), the cover hook options, a visual note per slide (photo, icon, chart), and the caption.

## Build mode

SocialMaker can design it as an editable draft:
1. `get_carousel_toolkit` to see fonts, styles and what the design tool supports.
2. Ask for the user's brand colors and photos (or use their media library).
3. `create_carousel` with the slides and the caption; `preview_carousel` to show it; adjust with `update_carousel`.
4. Give the link to open it in SocialMaker. If they want it out, schedule or publish it from here: [publishing.md](publishing.md).
