# Tech World Blog

**Tech World Blog** is a modern, dynamic blogging platform built using Django and Bootstrap, designed to provide users with engaging content on the latest trends in technology. The platform allows users to read, filter, and navigate blog posts by category, while offering a fully functional admin interface for managing content.

## Project Overview

The goal of this project is to create a scalable, user-friendly blog with robust backend logic and a clean, responsive frontend. Key features include:
- **Responsive Design**: Built with Bootstrap to ensure a seamless experience across all devices.
- **Dynamic Content Management**: Allows for easy content creation, editing, and deletion through the Django admin interface.
- **User Interaction**: Includes features like a contact form, and filtered blog categories, enhancing user engagement.

---

## Table of Contents

1. [Tech Stack](#tech-stack)
2. [Features](#features)
3. [Installation](#installation)

---

## Tech Stack

The **Tech World Blog** project utilizes a robust combination of modern technologies to ensure high performance, scalability, and maintainability:

- **Backend**:
  - **Django** (v4.x): Python web framework for building secure, scalable, and maintainable web applications. Utilized for routing, template rendering, and ORM (Object-Relational Mapping) to interact with the database.
  - **Python** (v3.x): The programming language used to build the backend logic, including form handling, business logic, and database management.

- **Frontend**:
  - **HTML5 & CSS3**: Core web technologies for building the structure and design of web pages.
  - **Bootstrap 4/5**: A front-end framework for responsive design, ensuring a seamless experience across mobile, tablet, and desktop devices.
  - **JavaScript (ES6+)**: Adds interactivity to the site, with dynamic behaviors such as form validation, pagination handling, etc.

- **Database**:
  - **SQLite** (default with Django): A lightweight database for development. You can easily switch to PostgreSQL or MySQL for production.

- **Development Tools**:
  - **Django Admin**: Provides an easy-to-use interface for managing content, including blog posts and categories.
  - **Git**: Version control system for tracking and managing project changes.
  - **Docker** (optional): For containerizing the application, ensuring consistent development environments.

---

## Features

### User Features

- **Home Page**: Display a list of recent blog posts with pagination and filters for categories.
- **Category Filtering**: Filter blog posts by different technology-related categories (e.g., Web Development, Machine Learning, Data Science).
- **Post Detail View**: Click on any blog post to view the full content with related posts displayed.
- **Contact Form**: Users can reach out to the team with inquiries through a simple contact form.
- **About Page**: Provides a brief overview of the blog’s mission, goals, and contributors.

### Admin Features

- **Content Management**: Admin can add, edit, or delete blog posts and manage slugs & categories through the Django admin panel.
- **User Inquiries**: View and manage inquiries submitted via the contact form.
- **Data Insights**: Admin can track the number of blog post views, user interactions, and other metrics.

---

## Installation

### Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.x
- pip (Python package installer)
- Git (optional, for version control)
- Virtual Environment (recommended)

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thivsiv/TechWorld.git
   
