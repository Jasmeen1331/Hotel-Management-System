# Hotel Management System - Phoenix Hotel

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

A comprehensive hotel management system with an intuitive GUI interface designed for Hotel Phoenix. This application streamlines hotel operations including customer registration, room booking management, and administrative dashboard with real-time analytics.

## Features

### 👥 Customer Management
- **Customer Registration**: Complete registration system with ID verification
- **Profile Management**: Update and manage customer information
- **Data Validation**: Robust input validation for data integrity
- **Search & Filter**: Quick customer lookup by name, ID, or mobile number

### 🏨 Booking System
- **Room Reservations**: Easy-to-use booking interface
- **Date Selection**: Calendar integration for check-in/check-out dates
- **Room Types**: Support for multiple room categories (Single, Double, Deluxe, Suite)
- **Billing**: Automatic calculation of total charges including taxes
- **Booking Status**: Real-time tracking of reservations

### 📊 Admin Dashboard
- **Authentication**: Secure admin login system
- **Customer Overview**: View all registered customers
- **Booking Management**: Track and manage all reservations
- **Reports**: Generate analytics and booking reports
- **Real-time Clock**: Display current time in the dashboard

### 💾 Database Integration
- **MySQL Backend**: Reliable data persistence
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Data Security**: Secure password storage and authentication
- **Backup Support**: Database backup and recovery capabilities

## Technologies Used

- **Python 3.7+**: Core programming language
- **Tkinter**: GUI framework for desktop application
- **MySQL**: Database management system
- **mysql-connector-python**: Database connectivity
- **Pillow (PIL)**: Image handling for hotel branding
- **tkcalendar**: Calendar widget for date selection

## Installation

### Prerequisites

```bash
python --version  # Python 3.7 or higher required
mysql --version   # MySQL 5.7 or higher required
```

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Jasmeen1331/Hotel-Management-System.git
cd Hotel-Management-System
```

2. **Install required packages**

```bash
pip install -r requirements.txt
```

3. **Set up MySQL Database**

```sql
-- Create database
CREATE DATABASE hotel1;

-- Create tables
USE hotel1;

CREATE TABLE details (
    RefNo INT PRIMARY KEY,
    CustName VARCHAR(100),
    FatherName VARCHAR(100),
    Gender VARCHAR(10),
    MobileNo BIGINT,
    Email VARCHAR(100),
    IDProof VARCHAR(50),
    IDNo INT,
    Address TEXT,
    password VARCHAR(100)
);

CREATE TABLE bookings1 (
    MobileNo BIGINT,
    CustName VARCHAR(100),
    CheckIndate DATE,
    CheckOutdate DATE,
    Roomtype VARCHAR(50),
    NoOfRoom INT,
    Days INT,
    RoomNo INT,
    Breakfast VARCHAR(50),
    TaxeandBill INT
);
```

4. **Configure database connection**

Update the database credentials in the code:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Update with your MySQL password
    database="hotel1"
)
```

5. **Run the application**

```bash
python hotel_management_system.py
```

## Usage

### Admin Login
- **Username**: ADMIN
- **Password**: 1234

### For Customers
1. Click on "Register New User"
2. Fill in all required information
3. Set a secure password
4. Login with your credentials to make bookings

### Making a Booking
1. Login to the system
2. Navigate to "BOOKINGS"
3. Enter customer mobile number
4. Select check-in and check-out dates
5. Choose room type and number of rooms
6. Add breakfast option if required
7. System calculates total bill automatically
8. Confirm and complete booking

## Project Structure

```
Hotel-Management-System/
├── hotel_management_system.py    # Main application file
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore file
```

## Key Features Implementation

### Authentication System
```python
# Admin login with predefined credentials
ADMIN_USERNAME = "ADMIN"
ADMIN_PASSWORD = "1234"

# User authentication via database
def user_login():
    username = username_entry.get()
    password = password_entry.get()
    # Verify credentials against database
```

### Customer Registration
- Validates all input fields
- Checks for duplicate entries
- Securely stores customer data
- Generates unique reference IDs

### Booking Management
- Automatic date validation
- Room availability checking
- Dynamic pricing calculation
- Booking confirmation and receipt generation

## Database Schema

### Details Table
| Field | Type | Description |
|-------|------|-------------|
| RefNo | INT | Unique customer reference ID |
| CustName | VARCHAR | Customer full name |
| FatherName | VARCHAR | Father's name |
| Gender | VARCHAR | Gender (Male/Female/Other) |
| MobileNo | BIGINT | Contact number |
| Email | VARCHAR | Email address |
| IDProof | VARCHAR | ID proof type |
| IDNo | INT | ID proof number |
| Address | TEXT | Full address |
| password | VARCHAR | Login password |

### Bookings1 Table
| Field | Type | Description |
|-------|------|-------------|
| MobileNo | BIGINT | Customer mobile number |
| CustName | VARCHAR | Customer name |
| CheckIndate | DATE | Check-in date |
| CheckOutdate | DATE | Check-out date |
| Roomtype | VARCHAR | Room category |
| NoOfRoom | INT | Number of rooms |
| Days | INT | Duration of stay |
| RoomNo | INT | Assigned room number |
| Breakfast | VARCHAR | Breakfast inclusion |
| TaxeandBill | INT | Total bill amount |

## Future Enhancements

- [ ] Online payment gateway integration
- [ ] Email notification system for bookings
- [ ] SMS alerts for booking confirmations
- [ ] Advanced reporting and analytics
- [ ] Multi-hotel branch management
- [ ] Mobile app version
- [ ] Room service management
- [ ] Housekeeping module
- [ ] Employee management system
- [ ] Revenue management and forecasting

## Security Features

- Password-protected admin access
- Secure database connections
- Input validation to prevent SQL injection
- Error handling for robust operation
- User authentication before booking access

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Database Connection Error**
- Verify MySQL is running: `sudo systemctl status mysql`
- Check database credentials in the code
- Ensure database "hotel1" exists

**Module Import Errors**
- Install all requirements: `pip install -r requirements.txt`
- Verify Python version: `python --version`

**GUI Display Issues**
- Ensure Tkinter is installed (comes with Python)
- Update display drivers if needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Jasmeen** (Student ID: 21236862)  
Final Year Computer Science Student  
University of Central Lancashire

## Acknowledgments

- Python Tkinter documentation
- MySQL community
- tkcalendar library contributors
- Pillow (PIL) development team

## Contact

For questions, suggestions, or collaboration:
- GitHub: [@Jasmeen1331](https://github.com/Jasmeen1331)
- University: University of Central Lancashire

## Screenshots

*Note: Screenshots of the application interface will be added soon*

---

⭐ **Star this repository if you find it helpful for hotel management or learning purposes!**

---

**Project Status**: Active Development  
**Last Updated**: December 2025  
**Version**: 1.0.0
