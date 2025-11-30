import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    """Create and return a MySQL database connection"""
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise

def init_db():
    """Initialize the database and create the todos table if it doesn't exist"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Database initialized successfully")
        
    except Error as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_all_todos():
    """Retrieve all todos from the database"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
        todos = cursor.fetchall()
        
        return todos
    except Error as e:
        print(f"Error fetching todos: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_todo(text):
    """Add a new todo to the database"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO todos (text, completed) VALUES (%s, %s)"
        cursor.execute(insert_query, (text, False))
        connection.commit()
        
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding todo: {e}")
        raise
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_todo(todo_id, completed):
    """Update a todo's completion status"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        update_query = "UPDATE todos SET completed = %s WHERE id = %s"
        cursor.execute(update_query, (completed, todo_id))
        connection.commit()
        
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error updating todo: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_todo(todo_id):
    """Delete a todo from the database"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        delete_query = "DELETE FROM todos WHERE id = %s"
        cursor.execute(delete_query, (todo_id,))
        connection.commit()
        
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error deleting todo: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

