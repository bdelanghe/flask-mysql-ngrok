# Flask MySQL Todo App

A bare bones todo application built with Flask, MySQL, and ngrok integration, configured with devenv for development.

## Features

- Create, read, update, and delete todos
- Mark todos as completed/incomplete
- Simple, clean web interface
- MySQL database backend
- ngrok integration for external access

## Prerequisites

- [devenv](https://devenv.sh/) installed
- ngrok account (for external access)

## Setup

### 1. Initialize devenv

```bash
devenv init
```

This will set up the development environment with:
- Python 3.11
- MySQL 8.0
- ngrok
- All required dependencies

### 2. Enter the development environment

```bash
devenv shell
```

### 3. Install Python dependencies

```bash
devenv up  # Start MySQL service
devenv task setup  # Install Python packages
```

Or manually:
```bash
pip install -r requirements.txt
```

### 4. Database Setup

The database is automatically initialized when you run the app. The `devenv.nix` configuration:
- Creates a MySQL database named `todoapp`
- Creates a user `todoapp` with password `todoapp`
- Grants all privileges to the user

The `models.py` file will automatically create the `todos` table on first run.

### 5. Run the Application

```bash
python app.py
```

Or use the devenv task:
```bash
devenv task run
```

The app will be available at `http://localhost:5000`

## Using ngrok

To expose your local Flask app to the internet using ngrok:

### 1. Get your ngrok authtoken

Sign up at [ngrok.com](https://ngrok.com) and get your authtoken.

### 2. Configure ngrok

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

### 3. Start ngrok tunnel

In a separate terminal (or after starting the Flask app):

```bash
devenv task ngrok
```

Or manually:
```bash
ngrok http 5000
```

ngrok will provide you with a public URL (e.g., `https://abc123.ngrok.io`) that forwards to your local Flask app.

## Project Structure

```
/
├── devenv.nix          # Development environment configuration
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── app.py             # Main Flask application
├── config.py          # Configuration management
├── models.py          # Database models and operations
└── templates/
    └── index.html     # Frontend UI
```

## Environment Variables

The following environment variables can be set (defaults are provided in `config.py`):

- `MYSQL_HOST` - MySQL host (default: 127.0.0.1)
- `MYSQL_PORT` - MySQL port (default: 3306)
- `MYSQL_USER` - MySQL user (default: todoapp)
- `MYSQL_PASSWORD` - MySQL password (default: todoapp)
- `MYSQL_DATABASE` - MySQL database name (default: todoapp)
- `FLASK_ENV` - Flask environment (default: development)
- `SECRET_KEY` - Flask secret key (default: dev-secret-key)

You can create a `.env` file in the project root to override these values.

## Database Schema

The `todos` table has the following structure:

- `id` - INT, PRIMARY KEY, AUTO_INCREMENT
- `text` - TEXT, NOT NULL
- `completed` - BOOLEAN, DEFAULT FALSE
- `created_at` - TIMESTAMP, DEFAULT CURRENT_TIMESTAMP

## Development

### Running in Development Mode

The app runs in debug mode by default when using `python app.py`. This enables:
- Auto-reload on code changes
- Detailed error messages
- Debug toolbar (if installed)

### Stopping Services

To stop the MySQL service:
```bash
devenv down
```

## Troubleshooting

### MySQL Connection Issues

If you encounter MySQL connection errors:
1. Ensure MySQL is running: `devenv up`
2. Check that the database and user were created correctly
3. Verify environment variables match your MySQL configuration

### Port Already in Use

If port 5000 is already in use, you can change it in `app.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

Update the ngrok command accordingly if you change the port.

## License

This is a simple example project for educational purposes.

