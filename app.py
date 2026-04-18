from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Hardcoded credentials for Milestone 1
USERS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'}
}


def login_required(f):
    """Decorator to protect routes - require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorator to protect routes - require admin role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        if session.get('role') != 'admin':
            return redirect(url_for('user_dashboard'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page - handle both form display and credential check"""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Check credentials
        if username in USERS and USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = USERS[username]['role']
            
            # Role-based redirect
            if USERS[username]['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout - clear session and redirect to login"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/user/dashboard')
@login_required
def user_dashboard():
    """User dashboard - protected route"""
    if session.get('role') != 'user':
        return redirect(url_for('admin_dashboard'))
    return render_template('user/dashboard.html', username=session.get('user'))


@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    """Admin dashboard - protected route for admins only"""
    return render_template('admin/dashboard.html', username=session.get('user'))


if __name__ == '__main__':
    app.run(debug=True)
