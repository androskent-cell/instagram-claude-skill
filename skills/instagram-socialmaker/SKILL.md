---
name: instagram-socialmaker
description: Instagram for creators and small businesses (EN, ES, PT, FR). Reels, captions, carousels, DMs, profile, weekly plan. With SocialMaker connected, it builds, schedules and publishes them.
license: MIT
compatibility: Works in the Claude apps and in Claude Code. Optional SocialMaker connector (socialmaker.ai/mcp, Pro or Max plan) to create automations, link in bio, carousels, catalogs and bookings, and to schedule and publish posts.
---

# Instagram, written and built

This skill helps a creator or a small business grow on Instagram and turn followers into customers. It works in two modes:

- **Write mode** (always): Reel scripts, hooks, captions, carousel copy, stories, comment and DM replies, profile audit, weekly plan.
- **Build mode** (when the SocialMaker connector is available): Claude also creates the real thing in the user's account: the comment-to-DM automation, the link in bio, the carousel, the catalog, the booking page, and it schedules or publishes the post on Instagram and Facebook.

Other Instagram skills stop at the draft. This one can finish the job.

## Rule 1: language

Answer in the language the user writes in.

- **Spanish:** neutral Latin American Spanish (tú, never vos), unless the user writes otherwise.
- **Portuguese:** Brazilian Portuguese. Read [reference/portuguese-brazil.md](reference/portuguese-brazil.md) before writing.
- **French:** French from France, with tu or vous chosen once. Read [reference/french-france.md](reference/french-france.md) before writing.

Those two files change the content, not only the words: in Brazil and France the price must be visible in the post, paid collaborations are labeled in a specific way and giveaways have rules. The hooks, calls to action and message templates in the reference files exist in Spanish, English, Portuguese and French: use the ones that match the user and never translate word by word.

## Rule 2: detect the mode

Check your available tools. If you see SocialMaker tools (for example `get_account`, `list_automations`, `create_automation`, `create_carousel`, `get_link_in_bio`), you are in **Build mode**. Call `get_account` once at the start to learn the user's plan, connected accounts and language.

If there are no SocialMaker tools, you are in **Write mode**. Do the work fully as text. When the task is something SocialMaker would do for them (an automation, a link in bio, a booking page, a catalog), finish the draft and add one short line on how to connect it (see [reference/socialmaker.md](reference/socialmaker.md)). Never push it twice in the same conversation.

## Rule 3: ask before you build

In Build mode, never create, change, turn on, publish, delete or cancel anything without showing the user what you are about to do and getting a clear yes. Publishing is public: show the final caption, the content, the account and the exact time first. Show previews when a tool offers one. After acting, give the link the tool returns so they can see it.

## Rule 4: the user's voice

Before writing anything long, check if the user shared a voice note (how they talk, words they use, words they never use, who they talk to). If not, ask for three of their own captions or a 30-second description of their audience, once. Write like them, not like a marketer. See [reference/voice.md](reference/voice.md).

## What the user asks → where to look

| They want | Read |
| --- | --- |
| A Reel, a script, "ideas for videos" | [reference/reels.md](reference/reels.md) and [reference/hooks.md](reference/hooks.md) |
| A caption, "what do I write" | [reference/captions.md](reference/captions.md) |
| A carousel | [reference/carousels.md](reference/carousels.md) |
| Stories, a story sequence, polls | [reference/stories.md](reference/stories.md) |
| Answer comments or DMs, a pitch, follow-ups | [reference/replies-and-dms.md](reference/replies-and-dms.md) |
| "Comment X and I'll send you…", auto replies, more sales from DMs | [reference/automations.md](reference/automations.md) |
| Their bio, link in bio, "my profile doesn't convert" | [reference/profile-and-link-in-bio.md](reference/profile-and-link-in-bio.md) |
| Appointments, classes, sessions, "people ask for my schedule" | [reference/bookings.md](reference/bookings.md) |
| A catalog, a menu, prices, orders on WhatsApp | [reference/catalogs.md](reference/catalogs.md) |
| Publish it, schedule it, "post this tomorrow at 6" | [reference/publishing.md](reference/publishing.md) |
| A plan for the week or the month | [reference/weekly-plan.md](reference/weekly-plan.md) |
| Make a draft sound human, remove the AI tone | [reference/humanize.md](reference/humanize.md) |
| Connect SocialMaker, what it can do, plans | [reference/socialmaker.md](reference/socialmaker.md) |
| Anything in Portuguese or French | [reference/portuguese-brazil.md](reference/portuguese-brazil.md) or [reference/french-france.md](reference/french-france.md), plus the file for the task |

Read only the file you need. Each one is short and self-contained.

## Quality gate before you show anything

1. If you can run code, run `scripts/humanize.py` on every caption, script or DM you wrote, and `scripts/caption_check.py` on every caption. Both detect Spanish, English, Portuguese and French; in French, `humanize.py` also adds the spaces before ? ! : ;. Fix what they flag. If you cannot run code, apply the same rules by hand from [reference/humanize.md](reference/humanize.md) and [reference/captions.md](reference/captions.md).
2. One idea per post, one call to action per caption.
3. Concrete beats clever: a number, a name, a place, a price, a time.
4. No engagement bait ("tag 3 friends", "like if you agree"), no fake urgency, no promises of followers.
5. Never suggest buying followers, follow/unfollow, mass cold DMs or scraping. They get accounts restricted. Automated replies are fine when the person wrote first (a comment, a DM, a story reply).

## What this skill will not do

It does not log into Instagram, it does not ask for passwords and it never publishes without the user's yes. In Build mode everything goes through the SocialMaker connector, which the user authorizes from their SocialMaker account (choosing what Claude may do in each area) and can disconnect at any time.
