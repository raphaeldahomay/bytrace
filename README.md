# ByTrace

ByTrace is a lightweight Flask web application designed to perform various text and binary conversion operations while collecting user interaction events for analysis.

The project was primarily built as a learning exercise to strengthen backend development skills, database integration, event tracking, and deployment practices using Python, Flask, PostgreSQL, JavaScript, and Git.

## Features

### Converters

* Text → Binary
* Binary → Text
* Text → ASCII
* ASCII → Text
* ASCII → Binary
* Binary → ASCII

### Event Tracking

ByTrace records user interactions and conversion activities, including:

* Conversion events
* Navigation events
* User agent information
* IP address information
* Source and destination pages
* Conversion metadata

All events are stored in a PostgreSQL database for future analysis.

## Tech Stack

### Backend

* Python
* Flask
* PostgreSQL
* Psycopg2

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* Git
* GitHub
* Gunicorn
* Python Virtual Environment (venv)

## Project Structure

```text
bytrace/
│
├── bytrace_app/
│   ├── __init__.py
│   ├── routes.py
│   ├── events.py
│   ├── db.py
│   ├── engine.py
│   ├── static/
│   └── templates/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/raphaeldahomay/bytrace.git
cd bytrace
```

### 2. Create a virtual environment

```bash
python -m venv bytrace_env
```

### 3. Activate the virtual environment

Linux / macOS:

```bash
source bytrace_env/bin/activate
```

Windows:

```bash
bytrace_env\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file at the root of the project:

```env
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=
SECRET_KEY=
FLASK_DEBUG=
```

### 6. Create the database schema

```bash
psql -U postgres -d your_database_name -f schema.sql
```

### 7. Run the application

```bash
flask run
```

The application should be available at:

```text
http://127.0.0.1:5000
```

## Purpose

The objective of ByTrace is not to build a production-grade conversion platform, but rather to provide a practical environment for learning:

* Flask application architecture
* PostgreSQL integration
* Event collection and storage
* Frontend-to-backend communication
* Git and GitHub workflows
* Deployment preparation
* Backend development best practices

## Future Improvements

Potential future enhancements include:

* User authentication
* Event dashboard and analytics
* API endpoints
* Additional converters
* Automated testing
* Docker support
* Cloud deployment

## License

This project is intended for educational and personal learning purposes.

> Tip: Use the reset button to load this sample again.