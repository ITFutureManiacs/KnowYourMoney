# KnowYourMoney
This is an application to control your home budget. It allows user to add income and expenses and creates a balance.

# Getting started
To run this apllication You have two ways. First using docker and second standard with virtual environment.

I. Assuming u have Docker installed on your machine You can run this project with simply two commands:
    In workdir of project prompt: docker compose up --build
    In browser: localhost:8000.

    If you dont have Docker installed visit:
        https://www.docker.com/products/docker-desktop/

        and install Docker.
II. You can start this project more traditional way if You want:

    1. To run this application you need to have installed Python. If you don't have it already, please visit 
        Python.org to download it.
    
    
    2. Download 
         
       - You need to clone repository to your local destination
       
               $ cd path/to/your/workspace
       
               git clone https://github.com/ITFutureManiacs/KnowYourMoney.git
    
    3. Requirements
       - Once your virtual environment is activated and project is cloned you need to install requirements:
                    
             pip install -r requirements.txt
    
        - and migrate database:
    
              python manage.py migrate

   
     

# Usage
- To use this application with prepared records in the database
  you need to type (while you're in your workspace directory):

        python manage.py loaddata users
        python manage.py loaddata currencies
        python manage.py loaddata categories
        python manage.py loaddata sources
        python manage.py loaddata expenses
        python manage.py loaddata incomes

  Prepared login data are:

        username: admin, password: admin , email: admin@admin.com - superuser
        username: fixJohn, password: FixPassForJohn, email: john@zantos.com
        username": fixAnna, password: FixPassForAnna, email: anna@faro.com,
        username: fixKamil, password": FixPassForKamil, email: kamil@kowalski.com,
  
        
- You can also update your own data using superuser:

        python manage.py createsuperuser

 
- or after running server you can registrate and use app as a normal user.

       python manage.py runserver


- Main functionalities:
  - Income and expenses balance
  - Income view
  - Expenses view
  - User registration/login
  - Updating user profile
  - Password change
  - Adding income in different currencies
  - Adding expenses in different currencies
  - Filtering list of expenses
  - Filtering list of income
  - Adding categories of expenses
  - Adding sources of income

- To do:
  - adding a bar chart to the balance view summarizing monthly income/expenses
  - adding category pie chart for expenses


- Technologies used:
  - Python 3.10.6
  - Django == 4.2.2
  - HTML
  - Bootstrap
# How does it look like:!

![obraz](https://github.com/ITFutureManiacs/KnowYourMoney/assets/136881676/52f34dee-8a66-4915-bd4a-579efa80b5de)
![obraz](https://github.com/ITFutureManiacs/KnowYourMoney/assets/136881676/9a08464b-6f6f-4ca8-9928-7d39f48c2807)
![obraz](https://github.com/ITFutureManiacs/KnowYourMoney/assets/136881676/c562a730-4115-47be-9a47-c16eace985f0)
![obraz](https://github.com/ITFutureManiacs/KnowYourMoney/assets/136881676/17581f7f-b61b-40c6-8275-6fe662caa004)
![obraz](https://github.com/ITFutureManiacs/KnowYourMoney/assets/136881676/143d1b62-c12e-45cf-9727-28de0dd008a6)



