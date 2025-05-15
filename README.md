User-Profile App with Google & GitHub OAuth
This is a minimal full-stack User Profile application built using Flask, deployed to AWS Lambda using the Serverless Framework. It supports OAuth login via Google and GitHub, stores user information in PostgreSQL, and displays a basic dashboard listing all registered users.

🔧 Tech Stack
Backend: Flask (Python) on AWS Lambda via Serverless Framework
Frontend: Server-rendered HTML (Jinja templates)
OAuth Providers: Google, GitHub
Database: PostgreSQL
Auth: JWT tokens for session management
Secrets Management: AWS Secrets Manager
Deployment: Serverless Framework + API Gateway + Lambda

Features
OAuth 2.0 Authorization Code Grant flow for Google and GitHub
Secure storage of user data in PostgreSQL
JWT-based session management
Server-rendered HTML pages
Hosted on AWS Lambda via Serverless Framework

Environment Variables
Use a .env file for local development or AWS Secrets Manager for production. Example .env:
POSTGRES_USER = ""
POSTGRES_PASSWORD = ""
POSTGRES_DB = ""
POSTGRES_HOST = ""
POSTGRES_PORT = ""
SECRET_KEY = ""
GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""

Setup Instructions
1. 🧬 Clone and Install
   git clone https://github.com/your-username/user-profile-app.git
   cd user-profile-app
   pip install -r requirements.txt

2. to run the application locally
  flask run



🌐 API Endpoints
Method	Endpoint	Description
GET	/auth/google/start	Redirects to Google OAuth consent screen
GET	/auth/google/callback	Handles Google OAuth callback
GET	/auth/github/start	Redirects to GitHub OAuth consent screen
GET	/auth/github/callback	Handles GitHub OAuth callback


 Frontend Pages
/ – Login Page (Google & GitHub buttons)
![Screenshot 2025-05-16 020053](https://github.com/user-attachments/assets/8af12d4d-fd7b-4f22-8530-2af44c34ae2c)


on google login
![Screenshot 2025-05-16 020306](https://github.com/user-attachments/assets/7c27658a-504a-4266-a32e-0778ef18aa91)
![Screenshot 2025-05-16 020320](https://github.com/user-attachments/assets/029a27d9-ad16-43a4-b3b6-093c1f08db5a)

/dashboard – Dashboard showing all users (protected)
![Screenshot 2025-05-16 020350](https://github.com/user-attachments/assets/a67cfbb9-074f-44d4-a6be-32eb10b19ea9)


Project Structure
clickpe-assignment/
app.py                 # Main Flask application file
models.py              # Database models/schemas
wsgi_handler.py        # WSGI handler for serverless deployment
serverless_wsgi.py     # Serverless WSGI integration
config/               # Configuration directory
static/              # Static files (CSS, JS, images)
templates/           # HTML templates
Configuration Files
      serverless.yml      # Serverless Framework configuration
      .serverless-wsgi    # Serverless WSGI config
      requirements.txt    # Python dependencies (main)
      requirements_new.txt # Additional Python dependencies
      package.json        # Node.js dependencies
      package-lock.json   # Node.js dependencies lock file

Virtual Environment
      venv/              # Python virtual environment

Generated Directories
      .serverless/       # Serverless deployment artifacts
      __pycache__/       # Python bytecode cache
      node_modules/      # Node.js modules

Documentation
      README.md          # Project documentation




created by
Dipanshu Vishwakarma

