# XPayBack Software Engineering Assignment

Welcome to the XPayBack Software Engineering Assignment repository! This project is a FastAPI-based web application for user registration.

## Introduction

This project is designed to demonstrate a web application that allows users to register and upload profile pictures. It uses the FastAPI framework along with PostgreSQL for data storage.

## Features

- User registration with unique email and phone validation
- Profile picture upload and storage in PostgreSQL database
- Fetching user details and profile picture using user ID

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/aakashroy007/xpayback_swe_assignment.git
   ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
   ```
4. Set up your PostgreSQL database and update the configuration in app/settings.py.

## Usage
Make sure to run the PostgreSQL before running the FastAPI application.

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```
Now, you can access the FastAPI endpoints for user registration and user retrieval.
## API Endpoints
- POST /register/: Register a new user.
- GET /user/{user_id}/: Fetch user details and profile picture.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the project, please open an issue or submit a pull request.