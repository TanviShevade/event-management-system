# 🎉 Event Management System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-Educational-orange)

A full-stack **Event Management System** developed using **Python, Django, HTML, Bootstrap, JavaScript, and SQLite** following the **Model-View-Template (MVT)** architecture.

The system enables users to browse events, book tickets, complete payments, download PDF tickets with QR codes, receive email confirmations, and manage bookings through a user-friendly interface. Administrators can efficiently manage events, users, bookings, payments, and reports.

> 🎓 Developed as an **MCA Semester II Mini Project**.

---

# 📖 Project Overview

Managing events manually can be time-consuming and error-prone. This Event Management System provides a centralized platform where users can register, explore events, book tickets, and manage their bookings online.

The application also provides an administrative dashboard for managing events, users, bookings, payments, and generating reports.

---

# ✨ Features

## 👤 User Features

- User Registration & Login
- Secure Authentication
- Profile Management
- Browse Upcoming Events
- Book Event Tickets
- Multiple Seat Booking
- Seat Availability Validation
- Online Payment Module (Demo)
- Transaction History
- Cancel Bookings
- Download PDF Tickets
- QR Code Generated on Tickets
- Email Confirmation with Ticket
- User Dashboard
- Responsive Bootstrap UI

---

## 👨‍💼 Admin Features

- Django Admin Dashboard
- Manage Users
- Manage Events
- Manage Bookings
- Manage Payments
- Generate PDF Reports
- Generate Excel Reports
- Event Seat Management
- Prevent Editing of Past Events

---

# 🛠 Tech Stack

## Backend

- Python
- Django

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Database

- SQLite

## Libraries Used

- ReportLab
- OpenPyXL
- QRCode
- Pillow
- SMTP Email

---

# 📂 Project Modules

- User Authentication
- Event Management
- Booking Management
- Payment Management
- Ticket Generation
- Dashboard
- Reviews
- Admin Dashboard

---

# 📁 Project Structure

```text
EventManagementSystem/
│
├── users/
├── events/
├── bookings/
├── payments/
├── tickets/
├── dashboard/
├── admin_dashboard/
├── reviews/
├── templates/
├── static/
├── media/
├── screenshots/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/TanviShevade/event-management-system.git

cd event-management-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## 7. Run Development Server

```bash
python manage.py runserver
```

Open in your browser:

```
http://127.0.0.1:8000/
```

Home Page

```
http://127.0.0.1:8000/index/
```

Django Admin

```
http://127.0.0.1:8000/admin/
```

Custom Admin Dashboard

```
http://127.0.0.1:8000/admin-dashboard/
```

---

# 📸 Project Screenshots

## 🏠 Home Page

![Home](screenshots/Home.png)

---

## 📝 User Registration

![Registration](screenshots/registration.png)

---

## 🔐 User Login

![Login](screenshots/login.png)

---

## 👤 User Dashboard

![Dashboard](screenshots/UserDashboard.png)

---

## 📅 Events Page

![Events](screenshots/eventPage.png)

---

## ➕ Add Event (Admin)

![Add Event](screenshots/AddEvent.png)

---

## 🎟 Event Booking

![Book Event](screenshots/BookEvent.png)

---

## 💳 Payment

![Payment](screenshots/Payment.png)

---

## ✅ Payment Confirmation

![Payment Confirmation](screenshots/ConfirmPayment.png)

---

## 🎉 Booking Confirmation

![Booking Confirmation](screenshots/BookingConfirmation.png)

---

## 📄 Download Ticket (PDF)

![Download Ticket](screenshots/DownloadTicket(PDF).png)

---

## ❌ Cancel Booking

![Cancel Booking](screenshots/CancleBooking.png)

---

## 💰 Transaction History

![Transaction History](screenshots/TransactionHistory.png)

---

## 💵 Refund Status

![Refund Status](screenshots/RefundStatus.png)

---

## 👤 Update Profile

![Update Profile](screenshots/UpdateProfile.png)

---

# 👨‍💼 Admin Screens

## 🔐 Admin Login

![Admin Login](screenshots/AdminLogin.png)

---

## 📊 Admin Dashboard

![Admin Dashboard](screenshots/AdminDashboard.png)

---

## 📈 Dashboard Analytics

![Dashboard Analytics](screenshots/AdminDashboard1.png)

---

## ⚙️ Dashboard Management

![Dashboard Management](screenshots/AdminDashboard2.png)

---

## 💳 Manage Payments

![Manage Payments](screenshots/ManagePayment.png)

---

## 📅 Past Events

### User View

![Past Events User](screenshots/PastEvent.png)

### Admin View

![Past Events Admin](screenshots/PastEventAdmin.png)

---

# 🌐 Live Demo

🚧 **Coming Soon**

- Frontend: Deploying on Render
- Backend: Deploying on Render

---

# 🔮 Future Enhancements

- Venue Management
- Razorpay / Stripe Payment Gateway
- Event Search & Filters
- SMS Notifications
- Event Wishlist
- Analytics Dashboard
- User Reviews & Ratings
- Event Reminder Emails

---

# 🏛 Architecture

The project follows the **Django Model-View-Template (MVT)** architecture.

```text
User
   │
   ▼
URLs
   │
   ▼
Views
   │
   ▼
Models
   │
   ▼
SQLite Database
   │
   ▼
Templates (HTML + Bootstrap)
```

---

# 👩‍💻 Developer

**Tanvi Shevade**

🎓 MCA Student

💻 Aspiring Full Stack Developer

### Connect with Me

- **GitHub:** https://github.com/TanviShevade
- **LinkedIn:** https://www.linkedin.com/in/tanvi-shevade-aabbb6280

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub. It motivates me to build more open-source projects.

---

# 📄 License

This project was developed as an **MCA Semester II Mini Project** for educational and learning purposes.
