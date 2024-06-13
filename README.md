![JOINclusion Logo](https://github.com/enriquehortalUM/JOINclusion_open_version/blob/main/Logo%2BName.png)

Visit us here: [JOINclusion website](https://dke.maastrichtuniversity.nl/JOINclusion/)

# JOINclusion Open Version

A repository configuring the deployment (with Docker containers) of the JOINclusion project's components (Authoring tool + WebSocket + LRS).

JOINclusion Deployment includes:

1. [Joinclusion Frontend](https://github.com/JohnChristidis/joinclusion-frontend): Web-based Authoring Tool graphic
   interface.
2. [Joinclusion Client](https://github.com/JohnChristidis/joinclusion-client): API server with CRUD (Create, Read,
   Update, Delete) functionality.
3. [Joinclusion WS](https://github.com/JohnChristidis/joinclusion-ws): Websocket to manage the multiplayer aspect of
   JOINclusion game.
4. [MariaDB](https://hub.docker.com/_/mariadb): Database to store Authoring tool data.
5. [LRSQL](https://github.com/yetanalytics/lrsql): xAPI to store JOINclusion game data.

## Dependencies

- Docker installed

## Quick Start

1. Create a .env file (there is an example available ```example.env```)
2. Change the variables values to include information on database name, users, and passwords.
3. Add Authoring tool database schema file (.sql) in the directory ```database_authoring_tool```, for example, the file
   ```joinclusion_schema.sql```
4. Include user and password to LSR
    1. Run the lrs_create_user.sh
5. Run all services:

```docker compose up -d```

Go to URL to access frontend:

```http://localhost:5173/```

4. Stop all services:

```docker compose stop```

## Accessing Data

1. Authoring Tool Database (MariaDB)
    1. Access the .sql file at ```database_authoring_tool/```
2. JOINclusion Game Database (LRS)
    1. Access the .sql file at ```database_lrs/```

## Application Configured Ports

1. Front-end: 5173
2. Maria-DB: 3306
3. Client: 3000
4. LRS: 8080
5. WS: 8082

## JDAT

1. Put the DB file (`lrsql.sqlite.db`) under the `JDAT/JDAT_results` folder
2. Put the SURVEY file (`users.csv`) under the `JDAT/JDAT_results` folder

3. Run the analysis with the command (from the main joinclusion_open_version-main directory)

`docker compose -f analysis-docker-compose.yml run --rm jdat`

4. Access the produced files at the folder `JDAT/JDAT_results`

-----
Authors: 
- **[Annanda Sousa](mailto:annanda.sousa@gmail.com) (Maastricht University) - Refactoring, configuration and packaging**
- Yusuf Can Sermerci (Maastricht University) - JDAT
- John Christidis (University of West Attica) - Serious educational game and Authoring tool

-----

![Funded by the European Union](https://github.com/annanda/joinclusion_open_version/blob/main/EN-Funded%20by%20the%20EU-POS.png)
