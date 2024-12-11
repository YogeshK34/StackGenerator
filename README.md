# Tech Stack Generator

![Tech Stack Generator Banner](https://your-image-url.com/tech-stack-banner.jpg)

## Description

Tech Stack Generator is a full-stack web application that allows developers to create and share personalized tech stack cards. Built with Next.js for the frontend and Django for the backend, this project demonstrates the integration of modern web technologies to create an interactive and engaging user experience.

## Features

- Interactive tech stack selection interface
- Dynamic card generation with user's name and selected technologies
- Shareable tech stack cards
- Responsive design for various screen sizes
- Backend API for card generation and storage

## Tech Stack

- Frontend:
  - Next.js
  - React
  - Framer Motion
  - Tailwind CSS
- Backend:
  - Django
  - Django REST Framework
- Database:
  - SQLite (default, can be changed to PostgreSQL for production)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js (v14 or later)
- Python (v3.8 or later)
- pip (Python package manager)
- npm (Node package manager)

## Installation

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tech-stack-generator.git
   cd tech-stack-generator

   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```

3. Install backend dependencies:

   ```bash
   pip install django djangorestframework django-cors-headers

   ```

4. Apply Database Migrations:

   ```bash
   python manage.py makemgrations
   python manage.py migrate

   ```

5. Start the Django Developement Server:
   ```bash
   python manage.py runserver


   ```
