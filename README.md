
# Student Welfare Protrol

Hi,
My name is Sathya Krishna, as a part of the Microsoft engage mentorship program, I have built a Student Welfare portal which it can be used in any university for managing different activities.

## Table of contents
* [Demo](#Demo)
* [Installation](#Installation)
* [Credentials](#Credentials)
* [Documents](#Documents)
* [Images](#Featues-with-Images)

## Demo

- [website](https://engage-student-welfare.herokuapp.com/)

Note: This repository is not the repository used for the deployment, because for the production I had used AWS and Heroku API keys so repository can't be public.


Video Link: [YouTube Link](https://youtu.be/nOpr2SCJiic)
## Installation

Git steps

```bash
  git clone https://github.com/krishna13052001/engage-sutudent-welfare
```

Project Installation with django.


Navigate into the folder and open the cmd where manage.py is located
```bash
   pip install -r requirements.txt
```

While Running above command, If any problem occured regarding pillow Installation from requirements.txt [Red color is indicator for problem]

Try:

```bash
   pip install Pillow
```
If problem doesn't resolve then try:
```bash
  pip uninstall pillow
  python -m pip install Pillow
```

To Run the site.
```bash
   python manage.py runserver
```



If any problem while Running the command python manage.py runserver , and if it indicates the manage.py not found then
try:

```bash
    use cd to navigate between the folder and you cmd directory should contains the manage.py
```


## Credentials

We have 4 different types of users
   - Student 
   - Faculty
   - Librarian
   - Admin

Admin doesn't have Registration Process.

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



  From the home we can able to toggle between Login and Sign Up.
  Users' can access the website through their unique username and password which is set during the registration and enters the portal.
  Admin Doesn't have registraion only student, faculty, librarian can able to register to the webapplication.

  * Sign Up
<img src="https://github.com/krishna13052001/engage-images/blob/master/signup.jpg">

```bash
  New users registers themselves with their name, email address, a unique username, safe password and selects their role in the college.
```

A Normal user can able to convert as admin user using admin account to login to default admin.<br> use this link: [adminLink](https://engage-student-welfare.herokuapp.com/admin/)

With Credentials:
Username: admin
Password: admin
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminLogin.jpg" alt="Image Not Loaded" >

On Successfull Login:
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminHome.jpg" alt="Image Not Loaded">

Now Click on the Users, and select any user and select the below option:
<img src="https://github.com/krishna13052001/engage-images/blob/master/adminChange.jpg" alt="Image Not Loaded">

  * Forgot Password <br>
  Users' who forgot their password can change it by using this option which will be done by verifying their email.
  Click on the Forgot password on the Home page then you will redirect to changePassword page

  <img src="https://github.com/krishna13052001/engage-images/blob/master/changePassword.jpg" alt="Image Not Loaded">

  Now, Enter the OTP which recived to mail.
    if you enter wrong otp then you will redirect to 404 page<br>
    or else,<br>
     you can able to to change the password

- Student Features
  Student have different features like enrolling in courses, verifying their courses, requesting services etc.
  * Your Course
    Students can check in which courses they're enrolled in and also check the corresponding faculty of that course, check their attendance and also grades for that course.
  <img src="https://github.com/krishna13052001/engage-images/blob/master/studentDashboard.jpg" alt="Image Not Loaded">

  * Library <br>
    It shows list of available books in the library(uploaded by the librarian) and student can request books from the librarian and this page also shows books which has to be returned in the 		library and time remaining for submitting the book.
  <img src="https://github.com/krishna13052001/engage-images/blob/master/studentLib.jpg" alt="Image Not Loaded">
  <img src="https://github.com/krishna13052001/engage-images/blob/master/studentLib2.jpg" alt="Image Not Loaded">
  
  * Request Service<br>
    Student can request services from admin or ask for leave and other queries using this page. This page also displays a list of the past requests made by the student.
  <img src="https://github.com/krishna13052001/engage-images/blob/master/studentServiceRequest.jpg" alt="Image Not Loaded">

  * Anouncements<br>
    This page displays all the announcements made by the faculty,librarian or administration.
  <img src="https://github.com/krishna13052001/engage-images/blob/master/studentAno.jpg" alt="Image Not Loaded">
    
  