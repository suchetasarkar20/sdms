# Django Student Attendance System

This is a Student Attendance System Developed for Educational Purpose using Python (Django).

And if you like this project then ADD a STAR ⭐️ to this project 👆

## Features of this Project

### A. Admin Users Can

1. See Overall Summary Charts of Stuudents Performance, Staffs Perfomrances, Courses, Subjects, Leave, etc.
2. Manage Staffs (Add, Update and Delete)
3. Manage Students (Add, Update and Delete)
4. Manage Course (Add, Update and Delete)
5. Manage Subjects (Add, Update and Delete)
6. Manage Sessions (Add, Update and Delete)
7. View Student Attendance
8. Review and Reply Student/Staff Feedback
9. Review (Approve/Reject) Student/Staff Leave

### B. Staff/Teachers Can

1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.
2. Take/Update Students Attendance
3. Add/Update Result
4. Apply for Leave
5. Send Feedback to HOD

### C. Students Can

1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Result
4. Apply for Leave
5. Send Feedback to HOD

## Support Developer

1. Add a Star 🌟 to this 👆 Repository

## How to Install and Run this project?

### Pre-Requisites:

1. Install Git Version Control
   [ https://git-scm.com/ ]
2. Install Python Latest Version
   [ https://www.python.org/downloads/ ]
3. Install Pip (Package Manager)
   [ https://pip.pypa.io/en/stable/installing/ ]

_Alternative to Pip is Homebrew_

### Installation

**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First

```
$  pip install virtualenv
```

Create Virtual Environment

For Windows

```
$  python -m venv venv
```

For Mac

```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows

```
$  venv\scripts\activate
```

For Mac

```
$  venv\bin\activate
```

**3. Clone this project**

```
$  git clone https://github.com/ritikbanger/django-student-attendance-system.git
```

Then, Enter the project

```
$  cd django-student-attendance-system
```

**4. Install Requirements from 'requirements.txt'**

```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file
- Then, On allowed hosts, Add [‘*’].

```python
ALLOWED_HOSTS = ['*']
```

_No need to change on Mac._

**6. Now Run Server**

Command for PC:

```python
$ python manage.py runserver
```

Command for Mac:

```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)

```
$  python manage.py createsuperuser
```

Then Add Email, Username and Password

**or Use Default Credentials**

_For HOD /SuperAdmin_
Email: admin@gmail.com
Password: admin

_For Staff_
Email: staff@gmail.com
Password: staff

_For Student_
Email: student@gmail.com
Password: student

## Copyrights

Coded by @ritikBanger, @mohitTaimni, and @ronitKhowal

Developed for Poornima Group, Jaipur

Copyright 2022 @ritikbanger
