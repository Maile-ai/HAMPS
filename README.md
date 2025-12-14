# 🏠 HAMPS — Home Access Management & Protection System (API)

HAMPS is a **Django REST Framework (DRF)** backend API designed to manage and protect home network access. It enables authenticated users to register devices, apply group-based security rules, refresh router data, and maintain a full audit trail through logging.

This project was developed as a **Backend Capstone Project** and demonstrates real-world API design, authentication, authorization, logging, and policy enforcement.

---

## 🚀 Features

### 🔐 Authentication & Users

* Token-based authentication
* User registration and login
* Secure access to all protected endpoints

### 📟 Device Management

* Register devices (routers, phones, laptops, IoT, etc.)
* Devices are **automatically linked to the authenticated user**
* Users can only view and manage their own devices

### 🧩 Group-Based Rules Engine

* Create security rules per **device group** (e.g. guests, kids)
* Enable or disable rules dynamically
* Fetch only **active rules**
* Designed to simulate real network access control

### 🔄 Router Refresh Action

* Action-based endpoint to simulate router device list refresh
* Demonstrates non-CRUD API behavior

### 🧾 Logging & Auditing

* Automatic logging of critical actions:

  * Device creation
  * Rule creation and updates
  * Router refresh
* Provides an audit trail for security and monitoring

---

## 🛠 Tech Stack

* **Python 3**
* **Django 5.x**
* **Django REST Framework (DRF)**
* **Token Authentication**
* **SQLite (development)**

---

## 📂 Project Structure

```
hamps_project/
├── devices/        # Device & router logic
├── rules/          # Group-based rules engine
├── users/          # Authentication & user management
├── logs/           # Activity logging
├── hamp_project/   # Project settings & URLs
└── manage.py
```

---

## 🔑 Authentication Flow

1. Register a user
2. Login to receive an authentication token
3. Use the token in request headers:

```
Authorization: Token <your_token_here>
```

All sensitive endpoints require authentication.

---

## 📡 API Endpoints

### 👤 Users

| Method | Endpoint               | Description             |
| ------ | ---------------------- | ----------------------- |
| POST   | `/api/users/register/` | Register a new user     |
| POST   | `/api/users/login/`    | Login and receive token |

---

### 📟 Devices

| Method | Endpoint                     | Description              |
| ------ | ---------------------------- | ------------------------ |
| GET    | `/api/devices/`              | List user devices        |
| POST   | `/api/devices/`              | Create a new device      |
| GET    | `/api/devices/<id>/`         | Retrieve a single device |
| POST   | `/api/devices/group/assign/` | Assign device to a group |

---

### 🔄 Router

| Method | Endpoint                       | Description                |
| ------ | ------------------------------ | -------------------------- |
| POST   | `/api/devices/router/refresh/` | Refresh router device list |

---

### 🧩 Rules

| Method | Endpoint                          | Description               |
| ------ | --------------------------------- | ------------------------- |
| POST   | `/api/devices/rules/create/`      | Create a group-based rule |
| GET    | `/api/devices/rules/active/`      | List active rules         |
| PATCH  | `/api/devices/rules/<id>/update/` | Update / disable a rule   |

---

### 🧾 Logs

| Method | Endpoint     | Description                                   |
| ------ | ------------ | --------------------------------------------- |
| GET    | `/api/logs/` | View activity logs (admin or permitted users) |

---

## 🧪 Testing

The API was tested using **Thunder Client** and **Django Admin**:

* Authentication flow validated
* Device creation and isolation verified
* Rules lifecycle tested (create → active → disable)
* Router refresh action confirmed
* Logs confirmed for all critical actions

---

## 🔒 Security Considerations

* Token authentication required for all sensitive endpoints
* Users cannot access or modify other users’ data
* Ownership enforced server-side
* Full audit logging enabled

---

## 🎯 Capstone Objectives Met

✔ RESTful API design
✔ Authentication & authorization
✔ Realistic business logic
✔ Logging & audit trail
✔ Clean project structure
✔ Incremental Git commit history

---

## 📌 Future Improvements

* Real router integration (OpenWRT / MikroTik)
* Time-based rule scheduling
* Frontend dashboard
* Role-based permissions
* Notification system

---

## 👨‍💻 Author

**Mokete Maile**
Backend Developer (Django / DRF)

---

> HAMPS — securing home network access through policy-driven design.
