# Trending carousels: generated pictures, editable text

The carousels that stop the scroll right now share one recipe: a striking picture (a real-looking person, an impossible scene, a sticker cutout) and a few HUGE, thick words. This file is how to make them so the result is still an editable design: the picture comes from an image generator with no letters in it, and every word, underline and arrow goes on top in SocialMaker, where the user can change it later.

Use it when the user asks for a carousel that looks "viral", "trending" or "like the ones creators post", or for a carousel with AI images. For the structure and the copy of any carousel see [carousels.md](carousels.md).

## Three rules

1. **Pictures have no letters.** No words, numbers, logos or fake screens in the generated image. Letters baked into a picture come out wrong and nobody can edit or translate them.
2. **The letters are the hook.** Headlines are big, thick and fill the space they have, one to three words per line. A small title floating in an empty area is the most common failure.
3. **One look per carousel:** the cover takes the picture, the inner slides stay calmer (a flat color or a paper, one giant word or number, one or two short lines). A carousel that shows "N styles" can change look on every slide.

## The looks

| Look | The picture you generate | What goes on top, editable | Best for |
| --- | --- | --- | --- |
| Headline behind the subject | A cutout of a person or a product on a transparent background, cut at the waist | A giant two-line headline that passes behind the person, plus two short lines on color strips | Covers, personal brands |
| Impossible scene | One photo-real scene that cannot exist (someone working on a giant phone among the clouds), with a calm third | A giant white headline on the calm third and one short line near the bottom | Covers that must stop the scroll |
| Photo + hand doodles | A dark or softly blurred photo with the subject in the lower half | A bold title, a hand-drawn underline, an arrow and a short handwritten note | Tips, behind the scenes |
| Blank sign | A person who holds a blank cardboard sign, a sheet or a small whiteboard, seen from the front | The message written on the sign in a marker font, filling it | Quotes, offers, announcements |
| Sticker on grid paper | A cutout of a person or a product | Grid paper, a white sticker border and a hard shadow on the cutout, two heavy fonts in two colors, star doodles | Playful brands, lists |
| Giant words + one object | One glossy object on a transparent background | Three lines of giant condensed capitals with the object below | "This vs that", products |
| One colored word | None | One bold sentence with a single word in the accent color and a lot of air | Opinions, hot takes |
| Problem and solution cards | None | A one-word title and two rounded cards (the problem dark, the solution in the accent color) | Inner slides |

Formats that carry these looks well: "N ideas" or "N mistakes" with the number big, before vs after, "boring vs viral", one statement per slide.

## Image prompts that work

One prompt per picture. Always say: who is in it (age, look, what they do, expression), the place and the light, the framing, **where the empty space is and what tone it has**, and that there is no text.

- **A person, photo-real:** `Photo of a florist, about 30, mustard apron, warm smile, in her shop with morning window light, 50mm lens, vertical 4:5. The top third is a plain cream wall with nothing on it. No text, no letters, no logos.`
- **A cutout:** `A fitness coach, about 28, cut at the waist, looking at the camera, on a fully transparent background. No backdrop, no floor shadow, no text.`
- **A blank sign:** `A cafe owner holding a large blank cardboard sign with both hands, seen straight from the front. The sign is empty and takes the lower half of the picture. Vertical 4:5. Nothing written anywhere.`
- **An impossible scene:** `Photo-real: a young man sits on a giant phone that floats among the clouds and works on his laptop. Vertical 4:5. The top third is clear blue sky. No text.`

Real-looking people work better than cartoons or 3D clay for a business account, unless the brand is illustrated. Keep the same person, light and palette on every slide (give the generator the previous picture to match). Decide where each text will sit BEFORE generating: light letters need a dark plain area, dark letters a light one.

## Build mode

1. `get_carousel_toolkit` with the topic `trends`: it has the exact recipe of each look. Read its `letters` too.
2. **Pictures first.** Generate them and upload each one with `upload_image` (or the upload tool your app offers). Never build the carousel with shapes or stock photos standing in for the art.
   - **In ChatGPT**, generating pictures ends your message, and a message that starts with @SocialMaker has no image generator. So: the user asks in plain words, you generate the pictures, and when they reply "continue" you upload them and build.
   - **Without an image generator** (Claude), say it in one line and use the user's photos or their media library. The looks with no picture need nothing else.
3. `create_carousel`:
   - Give every headline the area it must fill as its box (`position` with x, y, width and height in px) and `style.fit: true`. SocialMaker measures the real font and gives it the largest size that fits. Never guess the font size of a headline.
   - Choose the lines yourself with `<br>`. The sentence on a sign needs none: it spreads itself to fill the sign.
   - Heavy fonts: Anton, Bebas Neue, Archivo Black, Montserrat 900. Permanent Marker or Kalam on signs and notes.
   - Underlines, circles and arrows are named doodles (`doodle: "underline"`, `"circle"`, `"arrow"`). They come out with the fine tips of a real pen and the user can recolor them.
   - Supporting lines sit on a plain area of the photo, on a soft gradient or on their own color strip. Never on a separate translucent rectangle: the words spill out of it.
4. Read `fitted` in the answer. A headline that fills little of the width of its box needs a taller box or fewer lines.
5. `preview_carousel`, fix every item in `problems` with `update_carousel` and look again until it is clean. Then give the user the link to open it in the editor.
6. Write the caption apart ([captions.md](captions.md)). To post it: [publishing.md](publishing.md).

Because the pictures carry no letters, the same carousel works in another language: send the same slides again with the texts translated.

## Write mode

Deliver a build sheet the user can follow in any design tool: for each slide the look, the image prompt, the exact words with their line breaks, the fonts and colors, and where each piece sits. Then the caption. Add one line, once, on how SocialMaker would build it as an editable draft (see [socialmaker.md](socialmaker.md)).

## Never

- Never copy another creator's picture, texts or handle. Match a style with the user's own topic and words.
- Never put a real, recognizable person (a celebrity, a competitor) in a generated picture.
- Never promise reach. The look wins the first second; the idea earns the swipe.
