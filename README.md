# 🏃 Strava Lite — Data-Driven Workout Tracker

> **REST API Platform** | Associated with St. Francis College · CS-515

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![REST API](https://img.shields.io/badge/REST-API-00b4d8?style=flat-square&logoColor=white)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Status](https://img.shields.io/badge/Status-Completed-00b4d8?style=flat-square)](https://github.com/preethidommaraju/CS-515-A-Final-Project-Strava-Lite)

---

## 📌 Overview

**Strava Lite** is a lightweight, data-driven workout tracking REST API inspired by Strava's fitness platform. Built with **Python Flask**, it provides a clean and scalable backend service for managing user activity data — allowing users to **register**, **retrieve**, and **remove** workout activities through well-defined REST endpoints.

The project demonstrates core backend engineering principles including **modular architecture**, **RESTful design patterns**, **error handling**, and **data validation**.

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────┐
│                  STRAVA LITE ARCHITECTURE             │
├──────────────────────────────────────────────────────┤
│                                                       │
│  Client (Postman / Browser / Frontend)               │
│       │                                               │
│       ▼  HTTP Requests                                │
│  ┌─────────────────────┐                             │
│  │      app.py          │  ← Flask Application       │
│  │  (Entry Point)       │    Initialization           │
│  └─────────────────────┘                             │
│       │                                               │
│       ▼                                               │
│  ┌─────────────────────┐                             │
│  │     routes.py        │  ← URL Routing &            │
│  │  (Route Handlers)    │    Request Handling         │
│  └─────────────────────┘                             │
│       │                                               │
│       ▼                                               │
│  ┌─────────────────────┐                             │
│  │      api.py          │  ← Business Logic &         │
│  │  (API Logic)         │    Data Operations          │
│  └─────────────────────┘                             │
│       │                                               │
│       ▼                                               │
│  ┌─────────────────────┐                             │
│  │   Data Store         │  ← In-memory / PostgreSQL  │
│  └─────────────────────┘                             │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Status Code |
|:---:|:---|:---|:---:|
| `POST` | `/users/register` | Register a new user | `201 Created` |
| `GET` | `/users/<user_id>` | Retrieve user details | `200 OK` |
| `DELETE` | `/users/<user_id>` | Remove a user | `200 OK` |
| `POST` | `/activities` | Log a new workout activity | `201 Created` |
| `GET` | `/activities/<user_id>` | Get all activities for user | `200 OK` |
| `GET` | `/activities/<activity_id>` | Get specific activity | `200 OK` |
| `DELETE` | `/activities/<activity_id>` | Remove an activity | `200 OK` |

---

## 🔬 Key Features

- 🔐 **User Management** — Register, retrieve and remove users
- 🏋️ **Activity Tracking** — Log and manage workout activities
- ✅ **Input Validation** — Validates all incoming request data
- 🚨 **Error Handling** — Proper HTTP status codes and error messages
- 📦 **Modular Architecture** — Clean separation of concerns (app, routes, api)
- 🔄 **RESTful Design** — Follows REST API best practices

---

## 🛠️ Tech Stack

| Category | Tools |
|:---|:---|
| **Backend Framework** | Flask 2.3 |
| **Language** | Python 3.10 |
| **API Design** | REST, JSON |
| **Database** | PostgreSQL |
| **Testing** | Postman |
| **Version Control** | Git, GitHub |

---

## 📁 Project Structure

```
CS-515-A-Final-Project-Strava-Lite/
│
├── app.py               # Flask application entry point
├── routes.py            # URL routes and request handlers
├── api.py               # Business logic and data operations
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/preethidommaraju/CS-515-A-Final-Project-Strava-Lite.git
cd CS-515-A-Final-Project-Strava-Lite

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The API will be available at `http://localhost:5000`

---

## 📊 Sample API Usage

**Register a User:**
```bash
POST /users/register
{
  "name": "Preethi",
  "email": "preethi@example.com"
}
```

**Log an Activity:**
```bash
POST /activities
{
  "user_id": "123",
  "activity_type": "Running",
  "duration": 30,
  "distance": 5.2
}
```

**Get User Activities:**
```bash
GET /activities/123
```

---

## 🐛 Challenges & Solutions

| Challenge | Solution |
|:---|:---|
| 404 error when user didn't exist | Added user ID validation check before processing requests |
| Invalid data in requests | Implemented input validation with proper error messages |
| Modular code organization | Separated concerns into app.py, routes.py, and api.py |

---

## 🔑 Key Learnings

- ✅ Designed and implemented **RESTful API** from scratch
- ✅ Applied **modular Flask architecture** for clean code organization
- ✅ Implemented proper **HTTP status codes** and error handling
- ✅ Practiced **API testing** using Postman
- ✅ Strengthened **Python backend development** skills

---

## 🔮 Future Improvements

- [ ] Add **JWT authentication** for secure user sessions
- [ ] Integrate **PostgreSQL** for persistent data storage
- [ ] Add **workout analytics** — weekly/monthly summaries
- [ ] Build **frontend dashboard** using React
- [ ] Deploy on **AWS EC2** with Docker containerization
- [ ] Add **unit tests** using pytest

---

## 👩‍💻 Author

**Preethi Dommaraju**
- 🌐 Portfolio: [preethidommaraju.vercel.app](https://preethidommaraju.vercel.app)
- 💼 LinkedIn: [linkedin.com/in/preethidommaraju](https://linkedin.com/in/preethidommaraju)
- 🐙 GitHub: [github.com/preethidommaraju](https://github.com/preethidommaraju)

---

*© 2024 Preethi Dommaraju · St. Francis College · CS-515*
