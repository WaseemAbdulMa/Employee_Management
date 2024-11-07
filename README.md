# Office Employee Management

## Overview
The Office Employee Management system is a web application developed to manage and automate the records of employees within an organization. Built with the Django framework, it provides functionalities for adding, viewing, filtering, and removing employee records while ensuring secure access through user authentication.

## Key Features
- **User Authentication and Authorization:**
  - User registration and login.
  - Secure logout functionality.
- **Employee Management:**
  - Add new employee records.
  - View a list of all employees.
  - Remove employees from the system.
  - Filter employees based on their department.
- **Form Handling and Validation:**
  - Utilizes Django forms for input validation and data handling.

## Technologies Used
- **Backend:** Django Framework, Django ORM
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Authentication:** Django's built-in user authentication system

## Installation

### Prerequisites
- Python 3.x
- Django
- MySQL

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/office-employee-management.git
    cd office-employee-management
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Configure your database settings in `settings.py`.
    - Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### User Authentication
- **Sign Up:** Navigate to the registration page to create a new account.
- **Login:** Use your credentials to log in to the system.
- **Logout:** Log out securely when finished.

### Employee Management
- **Add Employee:** Fill in the form with employee details and submit to add a new record.
- **View All Employees:** Access the list of all employees.
- **Remove Employee:** Select an employee to remove from the system.
- **Filter Employees:** Filter the employee list by department.

## Code Overview

### Views
- `index`: Renders the homepage.
- `all_emp`: Displays all employees (login required).
- `add_emp`: Adds a new employee (login required).
- `remove_emp`: Removes an employee (login required).
- `filter_emp`: Filters employees by department (login required).
- `sign_up`: Handles user registration.
- `user_login`: Handles user login.
- `logout_page`: Handles user logout.

### Models
- `Employee`: Represents an employee with fields for name, department, salary, role, etc.
- `Role`: Represents different roles within the organization.
- `Department`: Represents different departments within the organization.



