# CinePy

## Descrição

O projeto tem o intuito fornecer um sistema capaz de facilitar a visualização de dados, a tomada de decisões e controle de salas de cinemas. O usuário administrador possuirá o privilégio de cadastrar diretores, gêneros, filmes, salas de cinema, horário de sessões e sessões. O usuário padrão poderá efetuar a compra de ingressos.

## Diagrama de classes

![Diagrama de classes](IMG/class_diagram.png)

## Deploy

https://cinepy-devweb2.herokuapp.com/

## Users

Superuser
- login: admin
- senha: admin

Admin
- login: admin1
- senha: mypassw123

Common
- login: buyer1
- senha: mypassw123

## Endpoints
- token/
- token/refresh/
- genre/
- director/
- cinema/
- movietime/
- movie/
- session/
- order/