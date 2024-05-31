# E-Commerce Website

https://github.com/Hoang-Phuc-Tran/Ecommerce-Project/assets/120700092/8dc2d4b8-e78a-47c7-99cb-83bb75f60d85

<h1> https://shoppingonline.up.railway.app/ </h1>

Welcome to the E-Commerce Website! This project showcases a fully functional online shopping platform developed using HTML, CSS, JavaScript, Bootstrap, and the Django web framework. Experience a seamless shopping experience with this user-friendly and visually appealing e-commerce platform.

## Features

- **Product Listings**: Browse through an extensive range of products. Each listing provides detailed descriptions, multiple images, and options for different variations like size and color.
- **User Accounts**: Users can register and manage their profiles, view their order history, and save favorite products. Account registration is secured with email verification.
- **Shopping Cart**: Supports adding products using session keys, dynamically updating the cart, and persisting cart data across sessions. Users can increment or decrement the number of items directly from the cart.
- **Secure Checkout**: Implements a secure checkout process, automatically assigns items in the cart, and supports multiple payment options through a payment gateway integration.
- **Responsive Design**: The website is fully responsive, ensuring a good shopping experience across various devices and screen sizes.
- **Search and Pagination**: Integrated search functionality to find products easily, with advanced pagination features.
- **Admin Dashboard**: An admin panel for managing products, orders, users, and reviews. Includes features for adding product variations, order management, and more.

## Detailed Sections

### Session-Based Cart Management
- Manage shopping cart using session keys with features for increment/decrement and removal of items.

### User Authentication and Management
- User registration with email confirmation, login/logout functionality, and password recovery through secure links.
- Account activation link expiration and re-sending functionality for non-activated accounts.
- Two-factor authentication for submitting user reviews.

### Order Processing
- Automated generation of unique order numbers.
- Detailed order viewing and management functionality for both users and administrators.
- Post-order functionalities include order confirmations, status updates, and the ability to handle returns and refunds.

### Payments and Security
- Integration with external payment gateways to handle transactions securely.
- Security features like token-based verification for sensitive operations and secure password reset mechanisms.

## Technical Overview

### Backend
- **Django**: Utilizes Django for backend operations, leveraging Django models for data management, views for logic handling, and templates for rendering content.
- **Testing**: Uses Django's TestCase for backend testing and Selenium for automated frontend testing to ensure feature reliability and usability.

### CI/CD
- **GitHub Actions**: Implements Continuous Integration using GitHub Actions to run tests, ensuring that all merges into main branches are error-free.
- **Railway**: Continuous Deployment is handled via Railway, which automatically deploys the website after successful integration tests, ensuring that the production site is always up-to-date.

## Getting Started

To set up a local copy of the project, follow these steps:

1. Clone the repository:
git clone https://github.com/Hoang-Phuc-Tran/Ecommerce-Project.git

2. Install dependencies:
pip install -r requirements.txt

3. Apply migrations:
python manage.py migrate

4. Run the development server:
python manage.py runserver

markdown
Copy code

## Contributions

We welcome contributions to the project. To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
