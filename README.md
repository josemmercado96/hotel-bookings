# hotel-bookings

Este es un proyecto de prueba para simular un flujo de reservas de un hotel.

consta de un simple modelo de tres tablas las cuales son:

- Clients
- Rooms
- Bookings

| Clients          | Rooms           | Bookings                 |
| ---------------- | --------------- | ------------------------ |
| dni string(10)   | code string(10) | start_date date          |
| name string(100) | beds int        | amount decimal           |
| is_company bool  | is_suite bool   | days int                 |
|                  |                 | payment_method string(4) |
|                  |                 | state string(2)          |
|                  |                 | room Room                |
|                  |                 | client Client            |

`asdasd`
