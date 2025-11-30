from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import init_db, get_all_todos, add_todo, update_todo, delete_todo

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """Display all todos"""
    todos = get_all_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    """Add a new todo"""
    text = request.form.get('text', '').strip()
    
    if not text:
        flash('Todo text cannot be empty', 'error')
        return redirect(url_for('index'))
    
    try:
        add_todo(text)
        flash('Todo added successfully', 'success')
    except Exception as e:
        flash(f'Error adding todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    """Toggle todo completion status"""
    try:
        # Get current status
        todos = get_all_todos()
        current_todo = next((t for t in todos if t['id'] == todo_id), None)
        
        if current_todo:
            new_status = not current_todo['completed']
            if update_todo(todo_id, new_status):
                flash('Todo updated successfully', 'success')
            else:
                flash('Error updating todo', 'error')
        else:
            flash('Todo not found', 'error')
    except Exception as e:
        flash(f'Error updating todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    """Delete a todo"""
    try:
        if delete_todo(todo_id):
            flash('Todo deleted successfully', 'success')
        else:
            flash('Todo not found', 'error')
    except Exception as e:
        flash(f'Error deleting todo: {str(e)}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

