🏠 H.A.M.P.S

Home Access Management & Protection System (Backend API)

📌 Project Overview

H.A.M.P.S is a backend system built with Django REST Framework that enables users to manage and control internet access for devices connected to a home network.
The system models router-level access control by grouping devices, applying time-based restriction rules, and maintaining a full audit trail of actions.

This project focuses on backend engineering principles, including secure APIs, rule enforcement logic, scheduling, and logging.

🎯 Core Features
✅ Device Management

Register and manage devices on a network

Store hostname, IP address, MAC address, device type, and connection type

Track device activity and last seen time

✅ Device Grouping

Devices can be assigned to predefined groups:

Kids

Teens

Adults

Guests

Grouping enables rule-based access control.

✅ Restriction Rules

Create and manage restriction rules per group

Enable or disable internet access per group

Optional time-based schedules (e.g. block after 21:00)

Rules can be activated or deactivated dynamically

✅ Rule Application Engine

Apply rules to all devices in a group

Enforces schedule validation

Updates device access state (is_blocked)

Prevents rule execution outside active schedules

✅ Activity Logging

Logs all critical actions (block, unblock, rule changes)

Provides a full audit trail

Logs are user-scoped and immutable

✅ Security

Token-based authentication

All endpoints require authentication

Users can only access their own devices, rules, and logs

🛠️ Technology Stack

Python

Django

Django REST Framework

Token Authentication

SQLite (development)

📂 Project Structure
HAMPS/
├── devices/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── rules/
│   ├── models.py
│   └── views.py
├── logs/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── hamp_project/
│   └── urls.py
└── README.md

🔐 Authentication

All endpoints require a valid authentication token.

Header format:
Authorization: Token <your_token_here>

🔗 API Endpoints
📱 Devices
Method	Endpoint	Description
GET	/api/devices/	List user devices
POST	/api/devices/	Create a device
GET	/api/devices/<id>/	Retrieve a device
POST	/api/devices/group/assign/	Assign device to group
📶 Router (Mocked)
Method	Endpoint	Description
POST	/api/devices/router/refresh/	Refresh device list
📜 Rules
Method	Endpoint	Description
POST	/api/devices/rules/create/	Create a restriction rule
PATCH	/api/devices/rules/<id>/update/	Update a rule
GET	/api/devices/rules/active/	List active rules
POST	/api/devices/rules/apply/	Apply rule to a group
🧾 Activity Logs
Method	Endpoint	Description
GET	/api/devices/logs/	List activity logs
🧪 Example Workflow (Demo)

Create a device

Assign device to a group

Create a restriction rule for the group

Apply the rule

Verify device state changes

Review activity logs

This demonstrates end-to-end backend control flow.

🧠 Design Notes

The system abstracts router control logic for safety

Actual network blocking is modeled, not enforced physically

The architecture supports future integration with real routers

Emphasis is placed on clean logic, validation, and auditability

🚀 Future Improvements

Real router integration (OpenWRT / MikroTik / pfSense)

Background schedulers (Celery / cron)

Frontend dashboard

Role-based access control

Notification system

## ⚙️ How to Run Locally

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create a superuser (optional):
   python manage.py createsuperuser
6. Start the server:
   python manage.py runserver

## Example:

Open Postman / Thunder Client

Post http://127.0.0.1:8000/api/users/login/
Body
{
  "username": "User01",
  "password": "StrongPass01"
}

Copy the token

Refresh Devices (MAIN DEMO)

Post http://127.0.0.1:8000/api/devices/router/refresh/

The response is 
{
   "message": "Router device list refreshed"
}

👤 Author

Mokete Samuel Maile
Backend Software Engineering Student @ ALX
