# Flask Blog

A web application built with **Python Flask**, implementing user authentication, account management, and content management features.

---

## 🚀 Features

### 🔑 User Authentication
- Signup & Login functionality  
- Secure password hashing with **Flask-Bcrypt**  
- Email validation using **email-validator**

### 👤 User Account Management
- Update username, email, and profile picture  
- Profile picture processing with **Pillow (PIL)**  

### 📝 Content Management System (CMS)
- Create, Read, Update, Delete (**CRUD**) posts  
- Database integration with **Flask-SQLAlchemy**

### 🎨 Frontend
- Templates rendered with **Jinja2**  
- Responsive design using **HTML/CSS**

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Database:** SQLite / MySQL with SQLAlchemy ORM  
- **Security:** Flask-Bcrypt, Flask-WTF (form handling)  
- **Libraries/Extensions:**  
  - flask  
  - flask-sqlalchemy  
  - flask-wtf  
  - flask-bcrypt  
  - flask-login  
  - pillow  
  - email-validator  

---

## 📚 Skills Gained
- Web application development with **Python Flask**  
- Database design and ORM integration  
- Authentication & authorization mechanisms  
- Implementing CRUD operations  
- Debugging, optimization, and project management in real-world settings  

---

## 📂 Project Structure

Flask-Blog/
│
├── flaskblog/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ ├── static/
│ │ ├── main.css
│ │ └── profile_pics/
│ └── templates/
│ ├── layout.html
│ ├── home.html
│ ├── login.html
│ ├── register.html
│ ├── account.html
│ └── post.html
│
├── instance/ # Stores SQLite DB & config (auto-created)
│ └── site.db
│
├── run.py # Entry point for running Flask app
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── .gitignore # Ignore cache, venv, db, etc.
└── venv/ # Virtual environment 


---

## 🎥 Demo
📺 [Screen Recording](https://drive.google.com/drive/folders/1D9t8ozeEccIiV5KGNWhm29_q3IxIgOy-?usp=sharing)

---

## 📌 Conclusion
This project strengthened my expertise in **Python web development, database integration, and secure authentication systems**, preparing me for future work in **full-stack web application development**.

