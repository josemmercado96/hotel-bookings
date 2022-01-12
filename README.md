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

Los estados de la reserva son los siguientes:

> - Pendiente (P)
> - Pagado (PO)
> - Eliminado o Cancelado (D)

Los tipos de pagos aceptados son:

> - Tarjeta de Crédito (CC)
> - Efectivo (CASH)
> - Transferencia Bancaria (WT)

Para concretar una reserva debemos tener habitaciones creadas dentro de nuestra base de datos,
por lo cual contamos con un endpoint para crear diferentes habitaciones

`POST http://127.0.0.1:8000/rooms/`

al cual se le debe pasar el siguiente body

    {
        "code_room": "A2",
        "beds": 1,
        "is_suite": false
    }

También podemos listar las habitaciones con el endpoint de la misma dirección con el verbo GET.

También debemos tener los clientes registrados, para ello tambien se cuenta con un endpoint

`POST http://127.0.0.1:8000/clients/`

    {
        "dni": "8213442",
        "name": "Jose Maria",
        "is_company": false
    }

Igualmente con el verbo GET se pueden listar los clientes.

Para registrar la reservación debemos consumir el siguiente servicio

`POST http://127.0.0.1:8000/bookings/`

    {
        "start_date": "2022-01-15",
        "amount": 250.00,
        "days": 2,
        "room": 1,
        "client": 2,
        "payment_method": "CASH",
        "state": "P"
    }

De la misma forma podemos listar con el verbo GET las diferentes reservas.

Si no pasamos el estado por defecto, este toma el estado Pendiente (P) por defecto,
lo mismo con el método de pago el cual tomará por defecto Efectivo (CASH).

Una vez se tiene la reserva agendada y en estado Pendiente, podemos pagar o cancelarlo,
esto con los dos servicios siguientes

`PUT http://127.0.0.1:8000/bookings/1/pay`
`PUT http://127.0.0.1:8000/bookings/1/cancel`

_Una vez las reservas sean pagadas o canceladas, no se pueden modificar sus estados_
