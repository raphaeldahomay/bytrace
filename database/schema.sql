CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    converter_type VARCHAR(100),
    clicked_element VARCHAR(255),
    input_value TEXT,
    output_value TEXT,
    status VARCHAR(50),
    user_ip VARCHAR(100),
    user_agent TEXT,
    previous_page_url TEXT,
    target_page_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP