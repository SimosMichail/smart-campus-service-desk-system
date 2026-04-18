# Smart Campus Service Desk System - Milestone 1

A secure Flask web application with role-based access control, session management, and hardcoded authentication for Milestone 1.

## Project Structure

```
Project/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
├── README.md                       # This file
├── templates/
│   ├── base.html                  # Base template with nav and footer
│   ├── index.html                 # Home page
│   ├── login.html                 # Login page
│   ├── user/
│   │   └── dashboard.html         # User dashboard
│   └── admin/
│       └── dashboard.html         # Admin dashboard
└── static/
    └── style.css                  # Custom CSS styles
```

## Features

✅ **Hardcoded Authentication** (Milestone 1)
- Admin account: `admin / admin123`
- User account: `user / user123`

✅ **Session Management**
- Secure session handling
- Automatic redirect based on user role

✅ **Role-Based Access Control**
- Admin dashboard (only for admins)
- User dashboard (only for regular users)
- Protected routes with decorators

✅ **Responsive Design**
- Bootstrap 5 integration
- Mobile-friendly interface
- Custom CSS styling

✅ **Required Routes**
- `GET /` - Home page
- `GET /login` - Login form
- `POST /login` - Handle login credentials
- `GET /logout` - Clear session and redirect
- `GET /user/dashboard` - Protected user dashboard
- `GET /admin/dashboard` - Protected admin dashboard

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Demo Test Cases

### Test Case 1: Admin Login
1. Go to `http://localhost:5000/login`
2. Enter credentials:
   - Username: `admin`
   - Password: `admin123`
3. You should be redirected to `/admin/dashboard`

### Test Case 2: User Login
1. Go to `http://localhost:5000/login`
2. Enter credentials:
   - Username: `user`
   - Password: `user123`
3. You should be redirected to `/user/dashboard`

### Test Case 3: Invalid Credentials
1. Try logging in with wrong credentials
2. An error message should appear

### Test Case 4: Protected Routes
1. Try accessing `/user/dashboard` without logging in
2. You should be redirected to `/login`
3. Try accessing `/admin/dashboard` as a regular user
4. You should be redirected to user dashboard

### Test Case 5: Logout
1. Log in successfully
2. Click "Logout" in navigation
3. Session should be cleared, redirected to login

## Security Notes

⚠️ **Milestone 1 (Current)**
- Credentials are hardcoded (suitable for development/testing only)
- Secret key is hardcoded (change in production)

📋 **Milestone 2 (Future)**
- Replace hardcoded credentials with MySQL database queries
- Implement proper password hashing (bcrypt)
- Use environment variables for configuration

## Git Instructions

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit: Flask project structure with authentication"
```

### Team Collaboration
Each team member should:
1. Create a local branch for their work
2. Commit with meaningful messages
3. Push changes to the repository
4. All team members should have commits in the repository

Example:
```bash
git checkout -b feature/add-user-management
# Make changes...
git add .
git commit -m "Add user management feature"
git push origin feature/add-user-management
```

## Customization Guide

### Adding New Routes
Edit `app.py` and add routes following the existing pattern:
```python
@app.route('/new-route')
@login_required  # Optional: add decorator to protect
def new_route():
    return render_template('new-template.html')
```

### Adding New Pages
1. Create a new HTML file in `templates/`
2. Use `{% extends 'base.html' %}` to inherit from base
3. Define `{% block content %}` with your content

### Styling
- Use Bootstrap classes in templates (already included)
- Add custom styles to `static/style.css`
- Bootstrap documentation: https://getbootstrap.com/

### Adding Team Members
1. Each member should clone the repository
2. Create their own branch for work
3. Commit with their name/message
4. Push to repository

## Troubleshooting

**Issue: Port 5000 already in use**
```bash
python app.py --port 5001
```

**Issue: Module 'flask' not found**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

**Issue: Templates not found**
- Ensure `templates/` folder exists at project root
- Flask looks for templates relative to the app location

## Notes for Team

- This is Milestone 1 of the project
- Focus on getting the authentication flow working
- Test all routes thoroughly
- All team members must have commits in the repository
- In Milestone 2, replace hardcoded login with MySQL database

---

**Created:** April 2026  
**Status:** Milestone 1 - Functional
