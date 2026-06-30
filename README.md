\# 🎉 Event Management System



A full-stack \*\*Event Management System\*\* developed using \*\*Python Django\*\* following the \*\*MVT (Model-View-Template)\*\* architecture. The system allows users to register, explore events, book tickets, make payments, download PDF tickets with QR codes, and receive email confirmations.



This project was developed as an \*\*MCA Semester 2 Mini Project\*\*.



\---



\# 📌 Project Description



The Event Management System is a web application that simplifies event booking and management. Users can browse available events, book one or multiple seats, complete payments, download tickets, and manage their bookings. Administrators can manage events, users, payments, and generate reports through the Django Administration Dashboard.



\---



\# ✨ Features



\## User Features



\- User Registration

\- User Login \& Logout

\- Profile Management

\- Explore Upcoming Events

\- Event Booking

\- Multiple Seat Booking

\- Seat Availability Validation

\- Online Payment Module (Demo)

\- Transaction History

\- Booking Cancellation

\- Download PDF Ticket

\- QR Code on Ticket

\- Email Confirmation with Ticket PDF

\- Dashboard

\- Responsive User Interface using Bootstrap 5



\---



\## Admin Features



\- Django Administration Dashboard

\- Manage Users

\- Manage Events

\- Manage Payments

\- View Bookings

\- PDF Report Generation

\- Excel Report Generation

\- Event Seat Management

\- Prevent Editing of Past Events



\---



\# 🛠 Tech Stack



\### Backend



\- Python

\- Django



\### Frontend



\- HTML5

\- Bootstrap 5

\- JavaScript



\### Database



\- SQLite



\### Libraries Used



\- ReportLab (PDF Generation)

\- OpenPyXL (Excel Report)

\- QRCode

\- Pillow

\- SMTP Email



\---



\# 📂 Project Modules



\- User Authentication

\- Event Management

\- Booking Management

\- Payment Management

\- Ticket Generation

\- Dashboard

\- Reviews

\- Admin Dashboard



\---



\# ⚙️ Installation Steps



\## 1 Clone Repository



```bash

git clone https://github.com/TanviShevade/event-management-system.git



\---



\## 2 Go to Project Folder



```bash

cd EventManagementSystem

```



\---



\## 3 Create Virtual Environment



```bash

python -m venv venv

```



\---



\## 4 Activate Virtual Environment



\### Windows



```bash

venv\\Scripts\\activate

```



\### Linux/Mac



```bash

source venv/bin/activate

```



\---



\## 5 Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## 6 Apply Migrations



```bash

python manage.py makemigrations



python manage.py migrate

```



\---



\## 7 Create Superuser



```bash

python manage.py createsuperuser

```



\---



\## 8 Run Development Server



```bash

python manage.py runserver

```



Visit:



```

http://127.0.0.1:8000/index/

```





```

http://127.0.0.1:8000/

```





Admin Panel:



```

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/admin-dashboard/



```



\---



\## 📷 Project Screenshots



\### 🏠 Home Page

!\[Home](screenshots/Home.png)



\---



\### 📝 User Registration

!\[Registration](screenshots/registration.png)



\---



\### 🔑 User Login

!\[Login](screenshots/login.png)



\---



\### 🎯 User Dashboard

!\[User Dashboard](screenshots/UserDashboard.png)



\---



\### 📅 Events Page

!\[Events](screenshots/eventPage.png)



\---



\### ➕ Add Event (Admin)

!\[Add Event](screenshots/AddEvent.png)



\---



\### 🎟 Book Event

!\[Book Event](screenshots/BookEvent.png)



\---



\### 💳 Payment Page

!\[Payment](screenshots/Payment.png)



\---



\### ✅ Confirm Payment

!\[Confirm Payment](screenshots/ConfirmPayment.png)



\---



\### 🎉 Booking Confirmation

!\[Booking Confirmation](screenshots/BookingConfirmation.png)



\---



\### 📄 Download Ticket (PDF)

!\[Download Ticket](screenshots/DownloadTicket(PDF).png)



\---



\### ❌ Cancel Booking

!\[Cancel Booking](screenshots/CancleBooking.png)



\---



\### 💰 Transaction History

!\[Transaction History](screenshots/TransactionHistory.png)



\---



\### 🔄 Refund Status

!\[Refund Status](screenshots/RefundStatus.png)



\---



\### 👤 Update Profile

!\[Update Profile](screenshots/UpdateProfile.png)



\---



\## 👨‍💼 Admin Panel



\### 🔐 Admin Login

!\[Admin Login](screenshots/AdminLogin.png)



\---



\### 📊 Admin Dashboard

!\[Admin Dashboard](screenshots/AdminDashboard.png)



\---



\### 📈 Dashboard Statistics

!\[Dashboard Statistics](screenshots/AdminDashboard1.png)



\---



\### ⚙️ Manage Dashboard

!\[Manage Dashboard](screenshots/AdminDashboard2.png)



\---



\### 💳 Manage Payments

!\[Manage Payments](screenshots/ManagePayment.png)



\---



\### 📅 Past Events (User)

!\[Past Events](screenshots/PastEvent.png)



\---



\### 📅 Past Events (Admin)

!\[Past Events Admin](screenshots/PastEventAdmin.png)

\# 🚀 Future Enhancements



\- Venue Management

\- Real Payment Gateway Integration (Razorpay/Stripe)

\- Event Search \& Filters

\- SMS Notification

\- Event Wishlist

\- Analytics Dashboard

\- User Reviews \& Ratings

\- Event Reminder Emails





\---



\# 📚 Project Architecture



The project follows the \*\*Django MVT (Model-View-Template)\*\* architecture.



```

User

&#x20;  │

&#x20;  ▼

URL

&#x20;  │

&#x20;  ▼

View

&#x20;  │

&#x20;  ▼

Model

&#x20;  │

&#x20;  ▼

Database (SQLite)

&#x20;  │

&#x20;  ▼

Template (HTML + Bootstrap)

```



\---



\# 📁 Project Structure



```

EventManagementSystem/

│

├── users/

├── events/

├── bookings/

├── payments/

├── tickets/

├── dashboard/

├── admin\_dashboard/

├── reviews/

├── templates/

├── static/

├── media/

├── db.sqlite3

├── manage.py

└── requirements.txt

```



\---



\# 👨‍💻 Author



Tanvi Shevade



MCA Student



Python | Django Developer



GitHub: https://github.com/TanviShevade



LinkedIn: https://www.linkedin.com/in/tanvi-shevade-aabbb6280



\---



\# ⭐ If you like this project



Please consider giving this repository a ⭐ on GitHub.

