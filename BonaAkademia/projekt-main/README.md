# BonaAkademia 2022

## Projekt

Aby uruchomic projekt nalezy:

- zainstalować docker desktop: https://docs.docker.com/compose/install/compose-desktop/
- wykonać w katalogu głównym projektu polecenie `docker compose up --build`
- projekt bedzie widoczny pod adresem
  - http://localhost:8080/ (front)
  - http://localhost:8000/ (api)

## Ustawienia

Ustawienia projektu dostępne w `/envs/.env.dev`

## Docker

Przydatne komendy:

- `docker compose ps` - lista
- `docker compose up` - uruchomienie z logami
- `docker compose stop` - zatrzymanie
- `docker compose down` - zatrzymanie i usunięcie

- `docker logs -f {{nazwa_kontenera}}` - logi z kontenera
- `docker exec -it {{nazwa_kontenera}} bash` - uruchomienie bash-a w kontenerze

## Server dev

adres servera developerskiego:

- http://10.157.1.116/ (front)
- http://10.157.1.116:8000/ (api)

## Opis

@TODO
