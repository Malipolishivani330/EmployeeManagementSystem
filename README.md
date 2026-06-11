# 🚀 Employee Management System

A modern, full-stack **Employee Management System** built with **Django**, **Django REST Framework**, **Bootstrap 5**, and **SQLite**, designed to simplify employee record management through an intuitive dashboard, secure REST APIs, and responsive user interface.

---

## 🌐 Live Demo

**Render Deployment:**
`https://employeemanagementsystem-koqw.onrender.com

**GitHub Repository:**
`https://github.com/Malipolishivani330/EmployeeManagementSystem

---

# 📌 Project Overview

The Employee Management System is a web application developed to manage employee information efficiently. It provides administrators with the ability to create, update, search, and manage employee records while displaying real-time dashboard statistics.

The project demonstrates full-stack web development concepts including backend architecture, REST API development, database management, authentication, responsive UI design, and cloud deployment.

---

# 🎯 Key Objectives

* Manage employee information digitally
* Reduce manual record maintenance
* Provide quick employee search and filtering
* Display organization statistics dynamically
* Build secure REST APIs
* Demonstrate production-ready Django development

---

# 🛠 Tech Stack

## Backend

* Python 3
* Django
* Django REST Framework (DRF)

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons

## Database

* SQLite

## Authentication

* Django Admin Authentication
* JWT (JSON Web Token)

## Deployment

* Git
* GitHub
* Render
* Gunicorn

## Development Tools

* VS Code
* Postman

---

# 🏗 Architecture

The project follows Django's **MTV (Model–Template–View)** architecture.

Model → Database Layer

View → Business Logic

Template → User Interface

This separation keeps the application scalable, modular, and maintainable.

---

# 📂 Project Structure

```
EmployeeManagementSystem/
│
├── employees/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   └── static/
│
├── ems/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ✨ Features

## Employee Dashboard

* Total Employees
* Total Departments
* Highest Salary
* Average Salary
* Active Employees
* Inactive Employees

## Employee Management

* Add Employee
* Update Employee
* Delete Employee
* View Employee Details

## Advanced Search

Search employees using:

* Name
* Email
* Phone Number
* Department
* Designation

## Dashboard Analytics

Automatically calculates:

* Employee Count
* Department Count
* Maximum Salary
* Average Salary
* Active Employees
* Inactive Employees

using Django ORM aggregate functions.

---

# 🔐 Authentication & Security

The application supports:

* Django Admin Authentication
* JWT Authentication for APIs

Protected endpoints ensure secure access to employee data.

---

# 🌐 REST API

Built using Django REST Framework.

Supports:

* GET
* POST
* PUT
* PATCH
* DELETE

Additional capabilities:

* Search
* Filtering
* Ordering
* Pagination

This makes the backend suitable for future mobile or frontend integrations.

---

# 🗄 Database Design

The Employee model stores:

* Name
* Email
* Phone
* Address
* Department
* Designation
* Salary
* Joining Date
* Active Status

The schema is designed for efficient querying and scalability.

---

# 🎨 User Interface

The frontend is developed using Bootstrap 5 with custom CSS.

Highlights include:

* Responsive Design
* Professional Dashboard
* Interactive Cards
* Hover Animations
* Search Bar
* Styled Tables
* Mobile Friendly Layout

---

# ⚡ Search Functionality

The search feature uses Django ORM with `Q()` objects to perform multi-field searches.

Users can search employees by:

* Name
* Email
* Phone
* Department
* Designation

This provides fast and flexible filtering.

---

# 📊 Dashboard Statistics

Dashboard metrics are generated dynamically using:

* Count()
* Avg()
* Max()

This ensures that all statistics remain synchronized with the database.

---

# 🚀 Deployment Process

The application was deployed using Render.

### Development Workflow

1. Developed locally using VS Code
2. Managed source code with Git
3. Pushed project to GitHub
4. Connected GitHub repository with Render
5. Installed dependencies using `requirements.txt`
6. Configured Gunicorn as the production server
7. Successfully deployed to Render

---

# 💻 Local Installation

Clone the repository:

```bash
git clone https://github.com/your-username/EmployeeManagementSystem.git
```

Navigate into the project:

```bash
cd EmployeeManagementSystem
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 📈 Performance Considerations

* Optimized ORM queries
* Aggregate calculations
* Search optimization
* Modular architecture
* RESTful API design
* Pagination support

---

# 📚 Skills Demonstrated

This project showcases experience in:

* Python Programming
* Django Development
* Django REST Framework
* REST API Design
* JWT Authentication
* ORM Queries
* CRUD Operations
* Bootstrap 5
* HTML & CSS
* Responsive UI Development
* Database Design
* Search & Filtering
* Git & GitHub
* Cloud Deployment
* Production Configuration

---

# 🔮 Future Improvements

* PostgreSQL Integration
* Employee Profile Images
* Attendance Management
* Leave Management
* Payroll Module
* Email Notifications
* PDF & Excel Reports
* Graphical Analytics Dashboard
* Docker Support
* CI/CD Pipeline
---

# 🎓 What I Learned

While developing this project, I gained practical experience in:

* Full-stack Django development
* Building REST APIs
* JWT Authentication
* Database management
* Responsive UI design
* Git version control
* Cloud deployment using Render
* Production-ready application architecture

---

# 👩‍💻 Developer

**Shivani**

This project reflects my hands-on experience in designing and developing scalable web applications using Django and modern web technologies. It demonstrates backend development, REST API implementation, database operations, responsive frontend design, and cloud deployment in a real-world application.
