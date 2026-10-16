# Schedule and publish

With SocialMaker connected (and the "Schedule and publish" permission turned on), Claude can put a post on the user's Instagram and/or Facebook: at a time, or right now. It uses SocialMaker's own scheduler, the same one in the app.

## What can be published

| Content | How |
| --- | --- |
| A carousel or single image designed in SocialMaker | `create_carousel` (see [carousels.md](carousels.md)), then `schedule_post` with its id |
| The user's own photos or videos | They upload them (or you pass a file with the upload tools), then `schedule_post` with the media ids, in order (up to 10) |
| A Reel | One video from the media library (3 to 60 seconds for the feed) |
| A story | One video or up to 10 images, with `story: true` |

## The flow

1. **Content ready.** The design or the files, and the caption checked with [captions.md](captions.md) (and `scripts/caption_check.py`).
2. **When.** Ask the day and time and the user's time zone if you don't know it. If they ask "when is best", suggest when their audience is online (their Instagram insights show it) and avoid inventing a universal "best time".
3. **Show the summary and wait for a yes:**
   ```
   Account: @their_account (Instagram)
   When: Tuesday, October 20, 6:00 p.m. (Mexico City)
   Content: carousel "5 mistakes…" (8 slides)
   Caption: «…»
   Publish it like this?
   ```
4. **Only on yes:** `schedule_post` with the time as ISO 8601 with offset (`2026-10-20T18:00:00-06:00`) or `"now"`.
5. Give the planner link. A carousel published "now" takes about a minute (it is rendered first) and goes out by itself.

## Afterwards

- `list_scheduled_posts` shows what is scheduled, published or failed, with the link once it is live.
- `cancel_scheduled_post` stops a scheduled one (ask first).
- If a post failed, read the error to the user in plain words (for example, the account needs to be reconnected in SocialMaker).

## If the permission is off

The tool will say the user has not allowed scheduling. Tell them: in SocialMaker, disconnect Claude and connect again, and choose "View and edit" for **Schedule and publish** (it starts off on purpose, because publishing is public).

## Never

- Publish without an explicit yes to the final summary.
- Change the caption after the yes without showing it again.
- Publish the same content twice to the same account.
