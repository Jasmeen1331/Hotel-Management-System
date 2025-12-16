#!/usr/bin/env python3
"""
Hotel Management System - Phoenix Hotel

A comprehensive hotel management application with GUI interface for:
- Customer registration and management
- Room booking and reservation system
- Admin dashboard with analytics
- Database integration for data persistence

Author: Jasmeen (Student ID: 21236862)
University of Central Lancashire

Note: This is a simplified version. For full implementation with all features,
please see the original files (hotel1.py) which include:
- Complete MySQL database integration
- Image handling and hotel branding
- Calendar integration for date selection
- Comprehensive booking management
- Customer data validation
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sys

# Configuration Constants
ADMIN_USERNAME = "ADMIN"
ADMIN_PASSWORD = "1234"
HOTEL_NAME = "HOTEL PHOENIX"

class HotelManagementSystem:
    """
    Main application class for Hotel Management System.
    
    Features:
    - Admin authentication
    - Customer registration
    - Booking management
    - Room allocation
    - Data persistence (requires MySQL setup)
    """
    
    def __init__(self, root):
        """
        Initialize the Hotel Management System.
        
        Args:
            root (tk.Tk): The root window
        """
        self.root = root
        self.root.geometry("1450x800")
        self.root.title("MY HOTEL")
        
        # Initialize data structures
        self.customers = {}
        self.bookings = {}
        
        self.create_login_screen()
    
    def create_login_screen(self):
        """
        Create the initial login screen for the hotel system.
        """
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2C3E50")
        main_frame.place(x=0, y=0, width=1450, height=800)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text=f"Welcome To {HOTEL_NAME}",
            font=("Times", 32, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title_label.pack(pady=50)
        
        # Login Frame
        login_frame = tk.Frame(main_frame, bg="#34495E", bd=5)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Username
        username_label = tk.Label(
            login_frame,
            text="Username",
            font=("Algerian", 15),
            bg="#34495E",
            fg="white"
        )
        username_label.grid(row=0, column=0, padx=20, pady=20, sticky="e")
        
        self.username_entry = tk.Entry(login_frame, font=("Times", 15), width=25)
        self.username_entry.grid(row=0, column=1, padx=20, pady=20)
        
        # Password
        password_label = tk.Label(
            login_frame,
            text="Password",
            font=("Algerian", 15),
            bg="#34495E",
            fg="white"
        )
        password_label.grid(row=1, column=0, padx=20, pady=20, sticky="e")
        
        self.password_entry = tk.Entry(login_frame, font=("Times", 15), width=25, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=20)
        
        # Buttons
        button_frame = tk.Frame(login_frame, bg="#34495E")
        button_frame.grid(row=2, column=0, columnspan=2, pady=30)
        
        admin_login_btn = tk.Button(
            button_frame,
            text="Admin Login",
            command=self.admin_login,
            font=("Algerian", 15),
            bg="#E74C3C",
            fg="white",
            padx=20,
            pady=10
        )
        admin_login_btn.pack(pady=10)
        
        user_login_btn = tk.Button(
            button_frame,
            text="Login As User",
            command=self.user_login,
            font=("Algerian", 15),
            bg="#3498DB",
            fg="white",
            padx=20,
            pady=10
        )
        user_login_btn.pack(pady=10)
        
        register_btn = tk.Button(
            button_frame,
            text="Register New User",
            command=self.show_registration,
            font=("Algerian", 15),
            bg="#2ECC71",
            fg="white",
            padx=20,
            pady=10
        )
        register_btn.pack(pady=10)
        
    def admin_login(self):
        """
        Handle admin login authentication.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.show_admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid admin credentials!")
    
    def user_login(self):
        """
        Handle user login authentication.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.customers and self.customers[username]['password'] == password:
            self.show_user_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid user credentials!")
    
    def show_registration(self):
        """
        Display customer registration window.
        """
        reg_window = tk.Toplevel(self.root)
        reg_window.geometry("800x700")
        reg_window.title("New Customer Registration")
        
        # Title
        title = tk.Label(
            reg_window,
            text="Customer Registration Form",
            font=("Times", 20, "bold"),
            bg="#34495E",
            fg="white"
        )
        title.pack(fill=tk.X, pady=10)
        
        # Form Frame
        form_frame = tk.Frame(reg_window, bg="#ECF0F1")
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        fields = [
            ("Reference ID:", "ref_id"),
            ("Full Name:", "name"),
            ("Father's Name:", "father_name"),
            ("Gender:", "gender"),
            ("Mobile Number:", "mobile"),
            ("Email ID:", "email"),
            ("ID Proof:", "id_proof"),
            ("ID Number:", "id_number"),
            ("Address:", "address"),
            ("Set Password:", "password")
        ]
        
        entries = {}
        
        for idx, (label_text, field_name) in enumerate(fields):
            label = tk.Label(
                form_frame,
                text=label_text,
                font=("Times", 12),
                bg="#ECF0F1"
            )
            label.grid(row=idx, column=0, padx=10, pady=10, sticky="e")
            
            if field_name == "password":
                entry = tk.Entry(form_frame, font=("Times", 12), width=30, show="*")
            else:
                entry = tk.Entry(form_frame, font=("Times", 12), width=30)
            entry.grid(row=idx, column=1, padx=10, pady=10)
            entries[field_name] = entry
        
        def register_customer():
            """Register a new customer."""
            data = {key: entry.get() for key, entry in entries.items()}
            
            if all(data.values()):
                if data['name'] in self.customers:
                    messagebox.showerror("Error", "Customer already exists!")
                else:
                    self.customers[data['name']] = data
                    messagebox.showinfo("Success", "Customer registered successfully!")
                    reg_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please fill all fields!")
        
        # Register Button
        register_btn = tk.Button(
            reg_window,
            text="Register",
            command=register_customer,
            font=("Algerian", 15),
            bg="#2ECC71",
            fg="white",
            padx=30,
            pady=10
        )
        register_btn.pack(pady=20)
    
    def show_admin_dashboard(self):
        """
        Display admin dashboard with management options.
        """
        dashboard = tk.Toplevel(self.root)
        dashboard.geometry("1450x800")
        dashboard.title(HOTEL_NAME)
        
        # Title
        title = tk.Label(
            dashboard,
            text=f"{HOTEL_NAME} - Admin Dashboard",
            font=("Times", 24, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title.pack(fill=tk.X, pady=10)
        
        # Sidebar
        sidebar = tk.Frame(dashboard, bg="#34495E", width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Time Display
        time_label = tk.Label(
            sidebar,
            font=("Times", 15),
            bg="black",
            fg="yellow"
        )
        time_label.pack(fill=tk.X, pady=10)
        
        def update_time():
            """Update time display."""
            current_time = datetime.now().strftime("%H:%M:%S")
            time_label.config(text=current_time)
            time_label.after(1000, update_time)
        
        update_time()
        
        # Menu Buttons
        menu_buttons = [
            ("CUSTOMER", lambda: self.show_customer_management(dashboard)),
            ("BOOKINGS", lambda: self.show_booking_management(dashboard)),
            ("REPORTS", lambda: messagebox.showinfo("Info", "Reports feature")),
            ("ABOUT", lambda: messagebox.showinfo("About", f"Designed By Jasmeen\nStudent ID: 21236862\nUniversity of Central Lancashire")),
            ("LOGOUT", dashboard.destroy)
        ]
        
        for text, command in menu_buttons:
            btn = tk.Button(
                sidebar,
                text=text,
                font=("Times", 15),
                bg="black",
                fg="yellow",
                command=command,
                width=20,
                height=2
            )
            btn.pack(pady=5)
        
        # Main Content Area
        content = tk.Frame(dashboard, bg="#ECF0F1")
        content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        welcome_label = tk.Label(
            content,
            text="Welcome to Admin Dashboard\n\nSelect an option from the menu",
            font=("Times", 20),
            bg="#ECF0F1"
        )
        welcome_label.place(relx=0.5, rely=0.5, anchor="center")
    
    def show_customer_management(self, parent):
        """
        Display customer management window.
        """
        messagebox.showinfo("Info", f"Total Customers: {len(self.customers)}")
    
    def show_booking_management(self, parent):
        """
        Display booking management window.
        """
        messagebox.showinfo("Info", f"Total Bookings: {len(self.bookings)}")
    
    def show_user_dashboard(self, username):
        """
        Display user dashboard for booking management.
        """
        messagebox.showinfo("Welcome", f"Welcome {username}!\n\nUser dashboard coming soon...")


def main():
    """
    Main function to initialize and run the Hotel Management System.
    """
    print("========================================")
    print("     HOTEL MANAGEMENT SYSTEM")
    print("========================================")
    print("\nInitializing application...")
    print("\nNote: This is a simplified demonstration version.")
    print("For full features including:")
    print("  - MySQL database integration")
    print("  - Image branding and hotel photos")
    print("  - Complete booking system with calendar")
    print("  - Payment processing")
    print("  - Comprehensive reporting")
    print("\nPlease refer to hotel1.py for the complete implementation.\n")
    print("========================================\n")
    
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        sys.exit(1)
