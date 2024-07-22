# Rigster - Custom PC Building Web Application

## Project Overview
Rigster is a Flask-based web application for custom PC building and user management. It allows users to browse products, build custom PCs, and manages user accounts with different roles.

## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

## Local Setup
1.	Clone the repository
2.	git clone https://github.com/ShaneZD/DB_Assignment
3.	CD -> Assignment folder
4.	Create a virtual environment: python -m venv venv
5.  Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
6. Install the required packages: pip install -r requirements.txt

7. Set up the database:
   The application uses SQLite by default. The database file (`rigster.db`) will be created automatically when you run the application for the first time.

8. Run the application: python app.py
8a. Access the application: Open a web browser and go to `http://localhost:5000`
RENDER URL: https://db-assignment.onrender.com
## Key Features 
1. User Management - Create, read, update, and delete user accounts - Role-based user management (Admin and User roles) - Secure password hashing 
2. Product Catalog - Browse PC components and peripherals - Filter and sort product listings (WIP – unfinished)
3. Custom PC Builder - Interactive PC configuration tool - Real-time price calculation - Component compatibility checks
4. Responsive Design - Mobile-friendly interface - Adaptive layout for various screen sizes 
5. Testimonial Carousel - Animated display of customer testimonials 
6. Contact Form - User-friendly contact form with form validation 
7. FAQ Section - Informative frequently asked questions
8. Newsletter Subscription - Allow users to subscribe to newsletters (display only, WIP)
9. Social Media Integration - Links to social media profiles (display only)
10. About Page - Company story and team information
