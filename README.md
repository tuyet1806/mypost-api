# 📝 Mypost API - Django REST Framework

This is a simple RESTful API built with Django that allows users to log in to view all posts and also post **anonymously**. Built using Django REST Framework and supports JWT token authentication.

## 🚀 Features

- JWT Authentication (login via token)
- Post creation with or without login
- Anonymous posting option
- View list of all posts
- Update or delete posts
- Hide username for anonymous posts

## 🧱 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT
- SQLite (default)
- Docker (optional)

## ⚙️ Installation (Local Development)

1. Clone the Repository
git clone https://github.com/tuyet1806/mypost-api.git
cd mypost-api

2. Create Virtual Environment and Install Dependencies
python -m venv env
env\Scripts\activate  # On Windows
pip install -r requirements.txt

3. Run Migrations and Create Superuser
python manage.py migrate
python manage.py createsuperuser

4. Start the Development Server
python manage.py runserver
Visit: http://localhost:8000

🔐 JWT Token Auth
Get Token
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}

Refresh Token
POST /api/token/refresh/
{
    "refresh": "your_refresh_token"
}

📌 Main Endpoints
Method	Endpoint	Description
GET	/posts/	Get all posts
POST	/create_post/	Create a new post
PUT	/update_post/<id>/	Update a specific post
DELETE	/delete_post/<id>/	Delete a specific post
You can post without being logged in (anonymous post)

💡 Notes
If the post is marked as anonymous (is_anonymous=True), the username will be hidden from other users.

If the user is authenticated, the post will be linked to their account.

📂 Docker Support (Optional)
docker build -t mypost-api .
docker run -p 8000:8000 mypost-api
📬 Contact
GitHub: tuyet1806
