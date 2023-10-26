CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    data_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

CREATE_TABLE_REQUESTS_APPOINTMENTS = """
CREATE TABLE IF NOT EXISTS requests_appointments (
    id SERIAL PRIMARY KEY,
    psychologist_id INTERGER NOT NULL,
    patient_id INTERGER NOT NULL,
    agenda_day_hour_id INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    reason VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agenda_day_hour_id) REFERENCES agenda_day_hour (id)
    FOREIGN KEY (psychologist_id) REFERENCES users (id) ON DELETE PROTECT
    FOREIGN KEY (patient_id) REFERENCES users (id) ON DELETE PROTECT
)
"""

CREATE_TABLE_APPOINTMENTS = """
CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    agenda_day_hour_id INTEGER NOT NULL,
    psychologist_id INTERGER NOT NULL,
    patient_id INTERGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    reason VARCHAR(50) NOT NULL,
    anonymous BIT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agenda_day_hour_id) REFERENCES agenda_day_hour (id)
    FOREIGN KEY (psychologist_id) REFERENCES users (id) ON DELETE PROTECT
    FOREIGN KEY (patient_id) REFERENCES users (id) ON DELETE PROTECT
)
"""

CREATE_AGENDA_TABLE = """
CREATE TABLE IF NOT EXISTS agenda (
    id SERIAL PRIMARY KEY,
    psychologist_id INTERGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (psychologist_id) REFERENCES users (id) ON DELETE CASCADE
)
"""

CREATE_TABLE_AGENDA_DAY_HOUR = """
CREATE TABLE IF NOT EXISTS agenda_day_hour (
    id SERIAL PRIMARY KEY,
    agenda_id INTEGER NOT NULL,
    start_date_time TIMESTAMP NOT NULL,
    end_date_time TIMESTAMP NOT NULL,
    FOREIGN KEY (agenda_id) REFERENCES agenda (id) ON DELETE CASCADE
)
"""
