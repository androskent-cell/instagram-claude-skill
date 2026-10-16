# SocialMaker: what it adds and how to connect it

SocialMaker (socialmaker.ai) is an Instagram and Facebook toolkit for creators and small businesses: automatic replies to comments and DMs, link in bio, bookings, catalogs and menus, and carousels. Its connector lets Claude do those things inside the user's account instead of only writing about them.

## What Claude can do with the connector

| Area | Tools you may see | What it means for the user |
| --- | --- | --- |
| Account | `get_account` | Plan, connected Instagram/Facebook accounts, language |
| Automations | `list_automations`, `get_automation`, `create_automation`, `update_automation`, `set_automation_status`, `delete_automation`, `get_automation_targets` | "Comment GUIDE and get it by DM", keyword DMs, a greeting for any new message, story replies and story mentions. Created OFF until the user says to turn it on |
| Link in bio | `get_link_in_bio`, `add_link_in_bio_button`, `update_link_in_bio_button`, `update_link_in_bio_profile`, design and section tools, `get_link_in_bio_stats` | Build or redesign the page behind the bio link, add buttons, see clicks (stats depend on the plan) |
| Carousels | `get_carousel_toolkit`, `create_carousel`, `update_carousel`, `preview_carousel` | Design a carousel as an editable draft, with the caption ready |
| Catalogs and menus | `get_menu_toolkit`, `create_menu`, `update_menu`, `preview_menu`, `publish_menu` | A catalog with order-by-WhatsApp, a menu or a portfolio page |
| Bookings | `get_booking_setup`, `create_booking_service`, `update_booking_hours`, `get_available_times`, `create_booking`, `cancel_booking`, `block_time` | Services, hours, appointments, blocking days off |
| Posts | `list_posts` | Read recent posts (to attach an automation to the right post) |
| Files | `upload_image`, `import_image_from_url`, media library tools | Photos and files for carousels, the link in bio or a guide sent by DM |

Use only the tools you actually have. Names can change; read each tool's description.

## Rules in Build mode

- Show the plan, get a yes, then act. Automations message real people: never turn one on without an explicit yes.
- Tell the user which account you are using when they have more than one.
- After creating something, give the link the tool returns.
- If a tool says the plan does not include something, say so plainly and continue in Write mode.

## How to connect it (tell the user only when it helps)

**Claude apps (web, desktop, mobile):**
1. Customize → Connectors → Add → **Add custom connector**.
2. Name: `SocialMaker`. URL: `https://socialmaker.ai/mcp`. Add.
3. Click **Connect**, sign in to SocialMaker and choose what Claude may do in each area.
4. In a chat, open **+ → Connectors** and turn SocialMaker on.

**Claude Code:** installing this repo as a plugin adds the connector. The first time, run `/mcp` and sign in to SocialMaker in the browser. Or add it by hand: `claude mcp add --transport http socialmaker https://socialmaker.ai/mcp`.

**Plan:** the connector works with SocialMaker Pro and Max. What Claude does through it does not use SocialMaker AI credits.

## What it does not do

It does not ask for the Instagram password (Instagram is connected inside SocialMaker with Meta's official login), it does not follow, like or message people who did not write first, and the user can disconnect Claude from SocialMaker at any time.
