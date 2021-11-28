
# Student Welfare Protrol

Hi,
My name is Sathya Krishna, as a part of the Microsoft engage mentorship program, I have built a Student Welfare portal where it can be used in any university for managing different activities related to the university.

## Table of contents
* [Author](#Author)
* [Demo](#Demo)
* [Installation](#Installation)
* [Credentials](#Credentials)

## Author

My self Sathya Krishna pursuing my final year B.Tech in IIIT Kottayam in specialized in CSE department
- [@krishna13052001 - Github](https://github.com/krishna13052001)
- [@Sathya Krishna  - Linkedin ](https://www.linkedin.com/in/sathya-krishna-2001/)


## Demo

https://engage-student-welfare.herokuapp.com/

Note: This repository is not the repository used for the deployment because for the production i had used some API keys so repository can't public.
## Installation

Git steps

```bash
  git clone https://github.com/krishna13052001/engage-sutudent-welfare
```

Project Installation with django
Navigate into the folder and open the cmd where manage.py is located
```bash
   pip install -r requirements.txt
```

To Run the site
```bash
   python manage.py runserver
```

While Running above command any problem pillow Installation from requirements [Red color is indicator for problem]

Try:

```bash
   pip install pillow
```

If problem while Running the command python manage.py runserver and it indicates the manage.py not found then
try:

```bash
    use cd to navigate between the folder and you cmd directory should contains the manage.py
```


    
## Credentials

We are having 4 different types of users
   - Student 
   - Faculty
   - Librarian
   - Admin

Admin does have Registration Process.

Login Details:
```bash
  Username: admin
  Password: admin
```

Student can able to do Registration and Login.

Login Details:
```bash
   Username: student
   Password: student
```

Faculty can able to do Registration and Login.

Faculty Details:
```bash
   Username: faculty
   Password: faculty
```

Librarian can able to do Registration and Login.

Librarian Details:
```bash
   Username: librarian
   Password: librarian
```
## Documents

- [List of Featues](https://docs.google.com/document/d/1D9eFgnfJ0DeSI6RJZR0ki6eRuvuLkPGC/edit?usp=sharing&ouid=116513581242175548881&rtpof=true&sd=true)


## Featues with Images

- <img src="https://drive.google.com/file/d/1H5jel_4YOfp0qCRApRAj-kv3_5HicsDQ/view" alt="Image Not Loaded" />


```bash
  From the home we can able to toggle between Login and Register.

  Admin Doesn't have registraion only student, faculty, librarian can able to register to the webapplication.
```