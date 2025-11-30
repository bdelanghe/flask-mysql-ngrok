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

The database is automatically created by devenv. After starting MySQL, initialize the database user:

```bash
devenv task init-db
```

This creates:
- A MySQL user `todoapp` with password `todoapp`
- Grants all privileges on the `todoapp` database

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

ngrok is automatically started when you run `devenv up`, which exposes your local Flask app to the internet.

### 1. Get your ngrok authtoken

Sign up at [ngrok.com](https://ngrok.com) and get your authtoken from the [dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).

### 2. Configure ngrok authtoken

You can configure ngrok in one of two ways:

**Option A: Using ngrok config file (recommended)**

Create a `ngrok.yml` file in the project root (copy from `ngrok.yml.example`):

```bash
cp ngrok.yml.example ngrok.yml
```

Then edit `ngrok.yml` and add your authtoken:

```yaml
version: 3

agent:
  authtoken: your_ngrok_authtoken_here
```

**Option B: Using environment variable**

Create a `.env` file in the project root (copy from `.env.example`):

```bash
cp .env.example .env
```

Then edit `.env` and add your ngrok authtoken:

```
NGROK_AUTHTOKEN=your_ngrok_authtoken_here
```

Both `ngrok.yml` and `.env` files are already in `.gitignore` and won't be committed to git.

### 3. Start services

When you run `devenv up`, both MySQL and ngrok will start automatically. ngrok will:
- Use `ngrok.yml` if it exists, or fall back to `NGROK_AUTHTOKEN` from `.env`
- Provide you with a public URL (e.g., `https://abc123.ngrok.io`) that forwards to your local Flask app on port 80

**Note:** Make sure your Flask app is running (`python app.py`) before accessing the ngrok URL, otherwise you'll get a connection error.

**Note:** Running on port 80 may require sudo privileges. If you encounter permission errors, you can change the port in `app.py` and update the ngrok configuration accordingly.

### 4. Browser Warning Page (Free Domains)

ngrok free domains (`.ngrok-free.dev`) show a browser warning page that requires clicking "Visit Site" to proceed. This is a security feature and cannot be bypassed for browser access.

**For Browser Access:**
- Simply click "Visit Site" on the warning page when accessing the URL in a browser
- This is a one-time action per browser session

**For Programmatic Access (API clients, webhooks, curl, etc.):**
You can bypass the warning by sending the `ngrok-skip-browser-warning` header with your requests:

```bash
# Using curl
curl -H "ngrok-skip-browser-warning: true" https://your-domain.ngrok-free.dev

# Using Python requests
import requests
headers = {"ngrok-skip-browser-warning": "true"}
response = requests.get("https://your-domain.ngrok-free.dev", headers=headers)

# Using JavaScript fetch
fetch("https://your-domain.ngrok-free.dev", {
  headers: {
    "ngrok-skip-browser-warning": "true"
  }
})
```

**Note:** To avoid the warning page entirely, you'll need a paid ngrok plan with a custom domain.

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

