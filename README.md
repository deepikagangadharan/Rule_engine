# Rule Engine Application

## Objective
Develop a simple rule engine application to determine user eligibility based on attributes like age, department, income, and spend using Abstract Syntax Tree (AST).

## Installation

1. Clone the repository:
   git clone https://github.com/your_username/rule_engine.git
   cd rule_engine

2. Create a virtual environment:
   python -m venv my_virtual_env
   source my_virtual_env/bin/activate  # On Windows use: my_virtual_env\Scripts\activate

3. Install required packages:
   pip install -r requirements.txt

4. Set up your MySQL database and update settings.py with your credentials.

5. Run migrations:
   python manage.py migrate

6. Start the server:
   python manage.py runserver
