# Restaurant Reservation Management System

## Overview

A full-featured restaurant reservation management system developed in Python as part of my A-Level Computer Science Non-Exam Assessment (NEA).

The application enables customers to book and cancel reservations through an intuitive graphical interface while providing staff and restaurant owners with powerful management tools. The system incorporates secure authentication, SMS notifications, business analytics, and predictive forecasting to support real-world restaurant operations.

## Key Features

### Customer Reservation System

- Create restaurant reservations through a user-friendly interface
- Cancel existing reservations
- Interactive calendar-based booking system
- Reservation scheduling up to 30 days in advance
- Multiple reservation time slots
- Dynamic party-size management
- Validation for children under four years old
- Real-time input validation
- CAPTCHA verification for additional security

### SMS Notifications

- Automatic reservation confirmation via SMS
- Reservation details sent directly to customers
- New booking notifications sent to management
- Built using the Twilio API

### Staff Portal

- Secure staff authentication
- CAPTCHA-protected login system
- View all reservations scheduled for the current day
- Access customer booking information including:
  - Customer details
  - Reservation date and time
  - Party size
  - Number of children under four

### Owner Dashboard

- Secure owner authentication
- View all reservations scheduled for the current day
- Access historical reservation records
- Reservation management tools
- Staff account administration
- Owner account administration
- Business analytics dashboard
- Demand forecasting system

### Account Management

#### Staff Management

- Add new staff accounts
- Remove existing staff accounts
- Store staff details securely in the database

#### Owner Management

- Add owner accounts
- Remove owner accounts
- Manage administrative access levels

### Password Recovery

The application includes an SMS-based password recovery system.

Users can:

- Verify their identity using their registered name and phone number
- Recover forgotten passwords
- Receive authentication details via SMS without administrator intervention

### Business Analytics & Forecasting

The owner dashboard includes a predictive analytics module that analyses historical reservation data and forecasts future demand.

Features include:

- Historical reservation analysis
- Reservation trend tracking
- Future reservation forecasting
- Average customer group size analysis
- Interactive graphical reports
- Prediction tables
- Business performance insights

The system uses a Linear Regression model from Scikit-Learn to identify booking trends and estimate future reservation volumes based on historical data.

## Technologies Used

### Core Technologies

- Python
- SQLite3

### GUI Development

- Tkinter
- CustomTkinter

### Database Management

- SQLite

### External Libraries

- TkCalendar
- Pillow (PIL)
- CAPTCHA
- Twilio

### Data Analysis

- Pandas
- NumPy

### Data Visualisation

- Matplotlib

### Machine Learning

- Scikit-Learn
- Linear Regression

## Programming Concepts Demonstrated

This project demonstrates:

- Graphical User Interface (GUI) Development
- Event-Driven Programming
- Database Design and Management
- SQL Queries
- CRUD Operations
- Data Validation
- User Authentication
- Role-Based Access Control
- CAPTCHA Security
- API Integration
- Exception Handling
- Data Analysis
- Data Visualisation
- Machine Learning Fundamentals
- Predictive Analytics

## System Architecture

The system stores and manages:

- Reservation Records
- Staff Accounts
- Owner Accounts
- Authentication Credentials

Data is managed using SQLite databases and accessed through parameterised SQL queries.

## Reservation Workflow

1. Customer enters reservation details.
2. Input validation is performed.
3. CAPTCHA verification is completed.
4. Reservation information is stored in the database.
5. Confirmation SMS is sent to the customer.
6. Notification SMS is sent to management.
7. Reservation becomes available in staff and owner dashboards.

## Recordings  

- Reservation recording: Reservations Video - Made with Clipchamp.mp4
- Cancelation recording: Cancelation video.mp4
- Login recording (owner, staff, predictions): Login Window.webm
- Forgot Password recording (TWILIO Trial ran out, so no messages can sent sent currently: Forgot Password video - Made with Clipchamp

## Installation

Clone the repository:

```bash
git clone https://github.com/LakshSaxena27/Restaurant_Reservation_System.git
```

Install the required dependencies:

```bash
pip install customtkinter
pip install tkcalendar
pip install pillow
pip install captcha
pip install twilio
pip install pandas
pip install numpy
pip install matplotlib
pip install scikit-learn
```

Run the application:

```bash
python Main_Menu.py
```

## Future Improvements

- Customer account registration system
- Web-based version of the application
- Online payment integration
- Real-time table availability tracking
- Email notifications
- Reservation modification functionality
- Cloud-hosted database support
- More advanced forecasting models

## Skills Demonstrated

- Python Development
- Database Design
- SQL
- Desktop Application Development
- API Integration
- Data Analysis
- Machine Learning
- Software Testing
- User Authentication
- Security Concepts
- Business Analytics
- Object-Oriented Programming Principles

## Author

**Laksh Saxena**

---

*Developed to demonstrate software development, database management, user authentication, API integration, data analytics, and predictive forecasting within a real-world restaurant management scenario.*

A-Level Computer Science NEA Project

---
