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

from bytrace_app import routes