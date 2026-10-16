# Bookings: stop losing appointments in the DMs

For anyone who sells time: beauty, barbers, coaches, therapists, teachers, real estate showings, photographers.

## The setup that works

1. **A booking page** with services (name, length, price), working hours and days off. Clients see only open times and book in a minute.
2. **The link in bio** with "Book" as the first button.
3. **An automation** so "¿tienes horario?" / "any openings?" gets the booking button instantly (see [automations.md](automations.md)).
4. **Confirmation and reminders** so people show up, and a way to reschedule without messaging you.

## Write mode

Help them define: services (clear names, length, price, what's included), buffer time between appointments, a cancellation policy in two lines, and the DM replies for price and availability (see [replies-and-dms.md](replies-and-dms.md)).

Policy template:
- ES: «Puedes cambiar o cancelar tu cita hasta {24} horas antes desde el enlace de tu confirmación. Si no avisas, se pierde el anticipo.»
- EN: "You can reschedule or cancel up to {24} hours before from your confirmation link. No-shows lose the deposit."
- PT: «Você pode remarcar ou cancelar até {24} horas antes pelo link da confirmação. Se não avisar, o sinal não é devolvido.»
- FR: «Vous pouvez modifier ou annuler votre rendez-vous jusqu'à {24} h avant, depuis le lien de confirmation. En cas d'absence, l'acompte est conservé.»

In France, beauty clients are used to booking online with time slots: the booking page in the bio is what they expect. In Brazil, answer «valor?» with the price in the first reply.

## Build mode

1. `get_booking_setup` to see services, hours and the public page.
2. Propose services and hours; on yes, `create_booking_service` and `update_booking_hours`.
3. For days off, `block_time`. To book someone by hand, `get_available_times` then `create_booking`.
4. Then offer the automation for "availability" messages and the "Book" button in the link in bio.
