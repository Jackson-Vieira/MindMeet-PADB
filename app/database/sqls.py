# Create initials table here

CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

CREATE_TABLE_PATIENT = """
CREATE TABLE IF NOT EXISTS patient (
    id SERIAL PRIMARY KEY
)
"""

CREATE_TABLE_PSYCHOLOGIST = """
CREATE TABLE IF NOT EXISTS psychologist (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    is_staff BIT NOT NULL,
    is_superuser BIT NOT NULL,
    is_active BIT NOT NULL,
    data_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

CREATE_TABLE_PATIENT_REQUEST_SESSION = """
CREATE TABLE IF NOT EXISTS patient_request_session (
    id SERIAL PRIMARY KEY,
    psychologist_id VARCHAR(50) NOT NULL,
    patient_id VARCHAR(50) NOT NULL,
    start_date_time VARCHAR(50) NOT NULL,
    end_date_time VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL,
    reason VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (psychologist_id) REFERENCES psychologist (id),
    FOREIGN KEY (patient_id) REFERENCES patient (id)
)
"""

CREATE_TABLE_HISTORY_SESSION = """
CREATE TABLE IF NOT EXISTS history_session (
    id SERIAL PRIMARY KEY,
    psychologist_id VARCHAR(50) NOT NULL,
    patient_id VARCHAR(50) NOT NULL,
    start_date_time VARCHAR(50) NOT NULL,
    end_date_time VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    description VARCHAR(50) NOT NULL,
    reason VARCHAR(50) NOT NULL,
    anonymous BIT NOT NULL,
    FOREIGN KEY (psychologist_id) REFERENCES psychologist (id),
    FOREIGN KEY (patient_id) REFERENCES patient (id)
)
"""

CREATE_TABLE_AGENDA = """
CREATE TABLE IF NOT EXISTS agenda (
    id SERIAL PRIMARY KEY,
    psychologist_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (psycholog_id) REFERENCES psychologist (id)
)
"""
CREATE_TABLE_AGENDA_DAY_HOUR = """
CREATE TABLE IF NOT EXISTS agenda_day_hour (
    id SERIAL PRIMARY KEY,
    agenda_id VARCHAR(50) NOT NULL,
    week_day VARCHAR(10) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (agenda_id) REFERENCES agenda (id)
)
"""
