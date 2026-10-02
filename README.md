 SMART Q – Smart Hospital Queue Management System

> A digital hospital queue management system designed to reduce patient waiting time and improve patient flow through smart token generation, live queue tracking, and doctor-side queue management.

---

 About the Project

SMART Q is a web-based Smart Hospital Queue Management System that helps hospitals manage patient queues digitally.

Instead of patients waiting without knowing their position in the queue, SMART Q allows patients to:

- Register and create an account
- Login securely
- Select a department and doctor
- Generate a digital queue token
- View their current token
- Track their queue status
- Check patients ahead of them
- View estimated waiting time

Doctors can manage the queue by calling the next patient and updating the consultation status.

The system is designed to make hospital visits more organized, transparent, and efficient.

---

Problem Statement

Traditional hospital queue systems often require patients to wait for long periods without knowing:

- Their position in the queue
- How many patients are ahead of them
- Approximately how long they need to wait
- When their turn will arrive

This can result in overcrowding, unnecessary waiting, and inefficient patient flow.

 Our Solution

SMART Q provides a digital queue management system where patients can generate tokens and monitor their queue status through a web interface.

---

Key Features

 Patient Module

- Patient registration
- Secure patient login
- Password hashing
- Patient dashboard
- Doctor and department selection
- Digital token generation
- Queue status
- Current token display
- Patients-ahead information
- Estimated waiting time
- Logout functionality

 Doctor Module

- Doctor login
- View waiting patients
- Call next patient
- Update patient queue status
- Complete consultation

 Queue Management

- Automatic token numbering
- Patient queue tracking
- Waiting status
- Queue position management
- Live queue updates
- Consultation completion tracking

---

 Technologies Used

 Frontend

- HTML5
- CSS3
- JavaScript

Backend

- Python
- Flask

Database

- SQLite

 Security

- Werkzeug password hashing
- Flask sessions
- Backend validation
- Parameterized SQL queries

Payment

- Razorpay Test Mode *(planned/integration stage)*

---

 Project Structure

```text
smart-q/
│
├── app.py
├── database.py
├── database.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── patient_dashboard.html
│   ├── generate_token.html
│   ├── token_success.html
│   ├── doctor_dashboard.html
│   └── admin_dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
Patient
   ↓
Registration
   ↓
Login
   ↓
Patient Dashboard
   ↓
Select Department & Doctor
   ↓
Generate Token
   ↓
Token Added to Queue
   ↓
View Queue Status
   ↓
Doctor Calls Next Patient
   ↓
Patient Consultation
   ↓
Consultation Completed
How to Run the Project
1. Clone the repository
git clone https://github.com/bhaktikhadkikar/smart-q-hospital-queue.git
2. Open the project
cd smart-q-hospital-queue
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows PowerShell
venv\Scripts\activate
5. Install Flask
pip install flask
6. Create the database
python database.py
7. Run the application
python app.py
8. Open the website

Open the following address in your browser:

http://127.0.0.1:5000
