# Smart Campus Service Desk System

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

✅ **Hardcoded Authentication**
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




