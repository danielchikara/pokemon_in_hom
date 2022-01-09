# pokemon_in_hom

## Admin django

**User:** admin@mail.com

**Password:** ^eN5E[JpsKe{?nBD

[](https://pokemon-inhom.herokuapp.com/admin/)

Documentacion Inhom Pokemon: https://suave-phlox-72b.notion.site/Pokemon-0ab8947697f145f796bd827be3bbe038  

Requisitos funcionales: https://suave-phlox-72b.notion.site/Requisitos-Funcionales-7349f3dda0f0463dbbc9a53dbf4861c7

Documentación API: https://documenter.getpostman.com/view/10921323/UVXerxnL
https://www.postman.com/mgd-2021/workspace/inhom-web/overview

Biblioteca de Postman: https://www.postman.com/mgd-2021/workspace/inhom-web/overview


## En la terminal 
Instalación de requerimientos  con su entorno virtual de preferencia  install requirements.txt  

Para migración de base de datos  sh migrate.sh  

uso de fixture  tipo de pokemon  python3 manage.py  loaddata type.json  

para el uso de la base de datos de prueba  python3 manage.py  test --keepdb

## Autenticación
La autenticación es por medio token. Solo esta disponible para crear actualizar,eliminar pokemons y logout del sistema


## Ramas
la rama main se encarga del desarrollo local y la heroku_configs  es la rama de despliegue
