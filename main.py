from fastapi import FastAPI, HTTPException, Form, File, UploadFile
import asyncpg
from uuid import uuid4

app = FastAPI()

# PostgreSQL Configuration
POSTGRES_DSN = "postgresql://postgres:12345@localhost/postgres"


async def get_postgres_pool():
    return await asyncpg.create_pool(POSTGRES_DSN)


@app.post("/register/")
async def register_user(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    profile_picture: UploadFile = File(...),
):
    user_id = str(uuid4())

    postgres_pool = await get_postgres_pool()

    try:
        async with postgres_pool.acquire() as connection:
            async with connection.transaction():  # Start a transaction
                # Check if the email already exists
                email_exists = await connection.fetchval(
                    "SELECT COUNT(*) FROM users WHERE email=$1", email
                )
                if email_exists:
                    raise HTTPException(status_code=400, detail="Email already registered.")

                # Check if the phone already exists
                phone_exists = await connection.fetchval(
                    "SELECT COUNT(*) FROM users WHERE phone=$1", phone
                )
                if phone_exists:
                    raise HTTPException(status_code=400, detail="Phone already registered.")

                # Convert profile picture to bytes
                profile_picture_data = await profile_picture.read()

                # Insert user data into the "Users" table using a prepared statement
                stmt = await connection.prepare(
                    "INSERT INTO users (user_id, full_name, email, password, phone) VALUES ($1, $2, $3, $4, $5)"
                )
                await stmt.fetchval(user_id, full_name, email, password, phone)

                # Save profile picture data and user_id to the "Profile" table using a prepared statement
                stmt = await connection.prepare(
                    "INSERT INTO profile (user_id, profile_picture) VALUES ($1, $2)"
                )
                await stmt.fetchval(user_id, profile_picture_data)

        return {"message": "User registered successfully.", "user_id": user_id}

    except Exception:
        return {"message": "There was an error during user registration."}
