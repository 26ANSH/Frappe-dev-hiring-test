# Frappe-dev-hiring-test
This Repo is the Solution for [Dev Hiring Test](https://frappe.io/dev-hiring-test). `For github Externship 2021`
## Project directory layout

    .
    ├── app.py              # Main App ~ Flask App
    │          
    ├── Website             # Main Application folder
    │   ├── __init__.py     # Application starter
    │   ├── static          # Static Files ~ JS, CSS, SVG
    │   ├── templates       # Html Pages ~ Jinja Templates
    │   ├── api.py
    │   ├── members.py
    │   ├── books.py
    │   ├── models.py
    │   ├── database.db
    │   └── views.py
    │ 
    ├── .github              # Github Actions - Azure App Services
    ├── requiremnts.txt      # Python Modules required for running the App
    └── README.md

## Tech Used 
1. Frontend - Jinja, Tailwind
2. Backend - Flask
## Live

Hosted on Microsoft Azure App Service [Click Here](https://26ansh-lms.azurewebsites.net). `https://26ansh-lms.azurewebsites.net`
## How to Run

After Cloning the Code Files on Your PC

1. Install all modules specified in requirements.txt
``` 
pip3 install -r requirements.txt
```

2. You are All Set up to Strt your App
```
python3 app.py
```

## App Demo

1. Login for Library Admin
<img src="/screenshots/login.png" alt="drawing" />

2. Browse Books - Using the API With filtering Options
<img src="/screenshots/Browse.png" alt="drawing"/>

3. Dashboard
<img src="/screenshots/dashboard.png" alt="drawing" />

4. Importing Books
<img src="/screenshots/import.png" alt="drawing" />

5. Books in Database
<img src="/screenshots/books.png" alt="drawing"/>

6. Deleting a Book
<img src="/screenshots/delete.png" alt="drawing" />

7. Cretaing New Users
<img src="/screenshots/user.png" alt="drawing" />

8. Issue and Returning a Book
<img src="/screenshots/issue.png" alt="drawing" />
<img src="/screenshots/issue-1.png" alt="drawing" />

9. Check all Book Transaction and Payments
<img src="/screenshots/transactions.png" alt="drawing" />

10. Page not Found
<img src="/screenshots/404.png" alt="drawing" />
