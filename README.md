
# Student Welfare Protrol

Hi,
My name is Sathya Krishna, as a part of the Microsoft engage mentorship program, I have built a Student Welfare portal where it can be used in any university for managing different activities related to the university.

## Table of contents
* [Author](#Author)
* [Demo](#Demo)
* [Installation](#Installation)
* [Credentials](#Credentials)
* [Documents](#Documents)
* [Images](#Featues with Images)

## Author

My self Sathya Krishna pursuing my final year B.Tech in IIIT Kottayam in specialized in CSE department
- [@krishna13052001 - Github](https://github.com/krishna13052001)
- [@Sathya Krishna  - Linkedin ](https://www.linkedin.com/in/sathya-krishna-2001/)


## Demo

- [website](https://engage-student-welfare.herokuapp.com/)

Note: This repository is not the repository used for the deployment because for the production i had used some API keys so repository can't public.


Video Link: [YouTube Link](https://youtu.be/nOpr2SCJiic)
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

- Authentication
  * Login Page
<img src="https://github.com/krishna13052001/engage-images/blob/master/home.jpg" alt="Image Not Loaded" />


```bash
  From the home we can able to toggle between Login and Register.
  Users' can access the website through their unique username and password which is set during the registration and enters the portal.
  Admin Doesn't have registraion only student, faculty, librarian can able to register to the webapplication.
```
  * Sign Up
<img src="https://github.com/krishna13052001/engage-images/blob/master/signup.jpg">

```bash
  New user registers themselves with their name, email address, a unique username, safe password and selects their role in the college.
```

A Normal user can able to convert as admin user using admin account to login to default admin use this link: [adminLink](https://engage-student-welfare.herokuapp.com/admin/)

With Credentials:
Username: admin
Password: admin
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminLogin.jpg" alt="Image Not Loaded" >

On Successfull Login:
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminHome.jpg" alt="Image Not Loaded">

Now Clike on the Users, and select any user and select the below option:
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminChange.jpg" alt="Image Not Loaded">

  * Forget Password
  Click on the Forgot password on the Home page then you will redirect to changePassword
  <img src="https://github.com/krishna13052001/engage-images/blob/master/changePassword.jpg" alt="Image Not Loaded">

  Now, Enter the OTP which recive to mail
  <img scr="https://github.com/krishna13052001/engage-images/blob/master/startRecovery.jpg" alt="Image Not Loaded">

  Now, Enter the New Password.

