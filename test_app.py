import base64
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    data = {
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "password123",
        "phone": "1234567890"
    }
    response = client.post("/register/", data=data)
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully."

def test_get_user_details():
    user_id = "b53170ce-73fd-4bfe-9610-3b56f7bf0cb7" # YOUR_USER_ID_HERE
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "user_id" in response.json()["data"]
    assert "full_name" in response.json()["data"]
    assert "email" in response.json()["data"]
    assert "phone" in response.json()["data"]

    # Ensure profile_picture is a base64 encoded string
    if "profile_picture" in response.json()["data"]:
        assert isinstance(response.json()["data"]["profile_picture"], str)
        # Verify if the base64 string can be decoded
        try:
            decoded_profile_picture = base64.b64decode(response.json()["data"]["profile_picture"])
        except Exception as e:
            assert False, f"Failed to decode profile_picture: {str(e)}"

def test_get_user_details_invalid_id():
    response = client.get("/users/12345678-1234-1234-1234-123456789012")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."

# Add more test cases as needed

if __name__ == "__main__":
    import pytest
    pytest.main()
