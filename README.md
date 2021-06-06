# Emart | E-commerce Website
A scalable Django Ecommerce Website

## Live
[emart](http://aditi17.pythonanywhere.com/)

## Functionality

- Register via Email Verification
- Login with Email Address
- Product Categories
- Add To Cart with Django Sessions
- Paypal Payment Gateway
- Invoice of Customer Orders
- Admin Panel Protection via Admin-Honeypot
- User Dashboard For Managing User Orders, Editing Profile & Changing Passwords
- Pagination & Search
- Session Timeout For User Inactivity
- Sending Emails For Forgot Password & Account Verification
- And many more



## Installing

### Clone the project


git clone https://github.com/AditiAgarwal17/emart_django.git
cd mart


### Install dependencies & activate virtualenv


pip install pipenv

pip install -r requirements.txt


### Apply migrations


python manage.py makemigrations
python manage.py migrate

### Running


python manage.py runserver
