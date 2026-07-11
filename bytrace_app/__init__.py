from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import os
from bytrace_app.db import get_connection

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("FLASK_DEBUG") == "1"

connection = get_connection()
cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS events (
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
    ) """
)

connection.commit()
cursor.close()
connection.close()

from bytrace_app import routes