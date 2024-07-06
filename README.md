# RUSTEZ`e - A Django web e-commerce application 🛍️

## Table of Contents

- [Introduction](#introduction)
- [Features](#key-features)
- [Technologies Applied](#technologies-applied)
- [Prerequisites](#prerequisites)
  - [For Application](#prerequisites-for-application)
  - [For Users](#prerequisites-for-users)
- [Installation process](#installation-process)
- [Understanding Django and Stripe API](#understanding-django-and-stripe-api)
  - [Django](#django)
  - [Stripe API](#stripe-api)

## Introduction

This project is an online shopping platform created with Django 4.x, Python 3.x, Bootstrap, and Tailwind CSS, using an SQLite3 database. It enables users to explore a range of products, add items to their shopping cart, and complete their purchases through a streamlined checkout process using Stripe.This application aims to provide a smooth and user-friendly shopping experience, ensuring security and ease of use for both customers and administrators.

## Key Features:

- **User Authentication**: Registration, login, and logout functionality
- **Product Management**: Listing and detail pages for products
- **Search and Filter**: Functionality to search and filter products
- **Order Processing**: Order placement and checkout process
- **Payment Integration**: Secured payment gateway integrated with Stripe
- **Admin Panel**: Management of products, categories, and orders

## Technologies Applied

- **Server-side**: Django 4.x with Python 3.x
- **Client-side**: Bootstrap and Tailwind CSS for styling
- **Data Storage**: SQLite3 database
- **View Layer**: Django Template Language (DTL)

---

# Prerequisites:

## Prerequisites for Application

Before getting started, make sure you have the following prerequisites:

- Python 3.x installed on your computer
- Django 4.x installed (can be installed using pip)
- Node.js and npm installed (needed for handling frontend dependencies)

## Prerequisites for Users

To utilize the features of this e-commerce web application, users need to:

- **Create an Account** : An active email address for account registration and order confirmations.
- **Log In** : Access the platform by logging in with their credentials
- **Proceed to Checkout** : A valid payment method (e.g., credit card, debit card) to complete purchases

---

## Installation Process

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/<your-username>django-certification-course-e-commerce-application.git
   ```

2. **Create a virtual environment**:

   ```sh
   venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**:

   ```sh
   npm install
   ```

5. **Apply migrations**:

   ```sh
   python manage.py migrate
   ```

6. **Create a superuser**:

   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server**:

   ```sh
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Understanding Django and Stripe API

### Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Here's a brief overview of its core features:

- **Model-View-Template (MVT) Architecture**: Django follows the MVT architectural pattern which helps in organizing the codebase. The model represents the data structure, the view handles the logic, and the template manages the user interface.

- **ORM (Object-Relational Mapping)**: Django's ORM allows developers to interact with the database using Python objects and methods instead of writing raw SQL queries.
- **Admin Interface**: Django provides a built-in admin interface to manage application data and perform administrative tasks. It is customizable and can be tailored to fit specific project needs.

- **Security**: Django includes robust security features out-of-the-box, such as protection against SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking.

### Stripe API

Stripe is a powerful and flexible payment processing platform. The Stripe API allows developers to integrate payment processing capabilities into their applications. Here are some key aspects of the Stripe API:

- **Payment Processing**: Stripe enables handling various types of payments, including credit and debit cards, digital wallets, bank transfers, and more. It supports multiple payment methods and currencies, making it ideal for global e-commerce.
- **Secure Transactions**: Stripe ensures secure transactions by adhering to industry standards for encryption and data protection. It is PCI DSS (Payment Card Industry Data Security Standard) compliant, providing a high level of security for online payments.

- **Developer-Friendly**: Stripe offers well-documented APIs and SDKs (Software Development Kits) for multiple programming languages and platforms. The API is designed to be intuitive, making it easy for developers to implement payment processing in their applications.

https://github.com/vishals25/django-certification-course-e-commerce-application/assets/142819017/9cad39c4-1e7a-46a4-959e-55affa71a9d3


- **Customization**: Stripe provides extensive customization options, allowing developers to tailor the payment experience to their
  Users.
- **Dashboard**: Stripe provides a comprehensive dashboard to monitor and manage payments, subscriptions, customers, and other financial operations. The dashboard offers detailed insights and analytics to help businesses make informed decisions.

**The Django and Stripe API interface:**

![stripe_api](https://github.com/vishals25/django-certification-course-e-commerce-application/assets/142819017/1f3b3b5a-c975-40bd-85c8-89d9e0c2c6ff)

## The video attachments of the Application developed above:

Thank you for checking out this project! Happy coding!

