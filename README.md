# MindMeet-PADB

## Descrição
O projeto MindMeet-PADB é um aplicativo de gerenciamento de tarefas que permite aos usuários criar e gerenciar tarefas em um quadro. O aplicativo é construído usando o framework FastAPI e o banco de dados PostgreSQL.

## Objetivo da atividade
O objetivo deste projeto é fornecer uma plataforma para agendamento de teleconsultas entre psicólogos e clientes. O sistema permite que os usuários adicionem ou removam agendamentos do banco de dados.

## UML
```mermaid
erDiagram

    PATIENT

    PSYCHOLOGIST {
        int id PK
        string email
        string full_name
        string city
        boolean is_staff
        boolean is_superuser
        boolean is_active
        datetime date_joined   
    }
    
    APPOINTMENTS {
        int id PK
        string psychologist_id FK
        string patient_id FK
        string agenda_day_hour_id FK
        string status
        string reason
        boolean anonymous
        datetime created_at
        datetime updated_at
    }

    REQUESTS-APPOINTMENTS {
        int id PK
        string psychologist_id FK
        string patient_id FK
        int agenda_day_hour_id FK
        string status
        string reason
        datetime created_at
        datetime updated_at
    }

    AGENDA {
        int id PK
        string psychologist_id FK
        datetime created_at
        datetime updated_at
    }

    AGENDA-DAY-HOUR {
        int id PK
        string agenda_id FK
        datetime start_date_time
        datetime end_date_time
    }

    PATIENT ||--o{ REQUESTS-APPOINTMENTS : "request"
    PSYCHOLOGIST ||--o{ REQUESTS-APPOINTMENTS : "accepts or rejects request"
    PSYCHOLOGIST ||--o{ APPOINTMENTS : "conducts"
    PATIENT ||--o{ APPOINTMENTS : "participates in"
    PSYCHOLOGIST ||--|| AGENDA : "has"
    AGENDA ||--o{ AGENDA-DAY-HOUR : "consists of"
```



## References 
- https://www.psycopg.org/psycopg3/docs/index.html
- https://docs.pydantic.dev/latest/
- https://fastapi.tiangolo.com/


- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-identity-column/
