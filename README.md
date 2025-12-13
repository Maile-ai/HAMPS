# H.A.M.P.S  
## Home Access Management & Protection System  
Backend Engineering Capstone Project

---

## 1. Project Overview

H.A.M.P.S (Home Access Management & Protection System) is a backend system designed to help users manage and control access to devices connected to a home Wi-Fi network.

The system automatically discovers connected devices, groups them by age category, and applies internet access restrictions and schedules. It exposes a secure REST API built with Django REST Framework and integrates with a router’s internal configuration interface through abstracted backend logic.

This project was built **from scratch during the capstone phase** to demonstrate backend engineering, automation, and system design skills.

---

## 2. Problem Statement

Modern households struggle to control and monitor internet usage across multiple devices, especially for children and guests. Most router interfaces are complex and not automation-friendly.

H.A.M.P.S solves this problem by:
- Centralizing device management
- Automating access control
- Providing a secure API layer
- Abstracting router complexity

---

## 3. Core Features

### 3.1 Device Discovery
- Fetches connected devices from the router interface
- Parses and stores:
  - Hostname
  - IP address
  - MAC address
  - Device type
  - Connection type (Wi-Fi / Ethernet)
  - DHCP lease time remaining
- Saves devices into the backend database

### 3.2 Device Grouping
Devices can be assigned to:
- Kids
- Teens
- Adults
- Guests

Grouping enables rule-based access control and scheduling.

### 3.3 Internet Access Restrictions
- Block or unblock internet access for devices or groups
- Apply scheduled restrictions (e.g. no internet for Kids after 21:00)
- Enable or disable rule sets
- Generate logs for every automated action

### 3.4 Router Integration Layer
- Communicates with the router using authenticated HTTP requests
- Fetches device lists and updates access rules
- Uses session-based authentication (credentials never exposed)
- Abstracts router communication through backend helper functions

---

## 4. System Architecture

H.A.M.P.S follows a layered backend architecture:

- API Layer (Django REST Framework)
- Business Logic Layer (rules, grouping, scheduling)
- Router Integration Layer (HTTP abstraction)
- Database Layer (Django ORM)

The system is designed to be extendable to dashboards or mobile apps in the future.

---

## 5. Models

### 5.1 Device
- hostname
- ip_address
- mac_address
- device_type
- connection_type
- lease_remaining
- group
- last_seen

### 5.2 RestrictionRule
- group
- active
- block_internet
- schedule_start
- schedule_end

### 5.3 AccessLog
- device
- action
- timestamp

---

## 6. API Endpoints

### Device Management
- `GET /api/devices/` – List all devices
- `GET /api/devices/<id>/` – Retrieve a single device
- `POST /api/devices/group/assign/` – Assign device to a group

### Router Integration
- `POST /api/router/refresh/` – Fetch updated device list
- `POST /api/router/block/` – Block device or group
- `POST /api/router/unblock/` – Remove restrictions

### Rule Management
- `POST /api/rules/create/`
- `PUT /api/rules/<id>/update/`
- `GET /api/rules/active/`

---

## 7. Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (development)
- Git & GitHub
- Virtual Environment (venv)

---

## 8. Project Structure

HAMPS/
├── hamp_project/
├── devices/
├── users/
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md

yaml
Copy code

---

## 9. Development Setup

### Clone Repository
```bash
git clone https://github.com/<your-username>/HAMPS.git
cd HAMPS
Create Virtual Environment
bash
Copy code
python -m venv venv
Activate Virtual Environment
bash
Copy code
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux / macOS
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Run Migrations
bash
Copy code
python manage.py migrate
Start Server
bash
Copy code
python manage.py runserver
10. Deployment
Platform
PythonAnywhere

Deployment Steps
Create a PythonAnywhere account

Upload project files or clone GitHub repository

Create a virtual environment

Install dependencies

Configure WSGI file

Run migrations

Collect static files

Set environment variables

Restart application

Live URL
👉 https://maile.pythonanywhere.com/

11. Capstone Progress – Part 4 Reflection
What I Built This Week
Implemented core models for devices, rules, and logs

Built device discovery and storage logic

Created REST API endpoints for device management

Structured the project for scalability

Deployed the backend to PythonAnywhere

Challenges Faced
Understanding router data formats

Designing safe router integration without exposing credentials

Structuring permissions and API logic correctly

How I Solved Them
Abstracted router logic into helper functions

Used Django REST Framework best practices

Tested endpoints incrementally

Referred to official Django documentation

Next Steps
Improve router automation logic

Add scheduling using background tasks

Enhance error handling

Finalize documentation and testing

12. Timeline
Week 1: Setup & models

Week 2: Device APIs & grouping

Week 3: Access control logic

Week 4: Scheduling & automation

Week 5: Testing & documentation

13. Security Considerations
Router credentials are never exposed

Session-based authentication is used

Sensitive operations require authentication

Designed with future production hardening in mind

14. Future Enhancements
Frontend dashboard

Mobile app integration

Real-time monitoring

Advanced parental controls

Notifications system

15. Author
Mokete Maile
Backend Engineering Capstone Project
ALX Software Engineering Program

16. License
Educational and demonstration purposes only.