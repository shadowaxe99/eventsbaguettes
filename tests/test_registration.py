```python
import unittest
from src.registration import registerUser, UserSchema

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "event": "AI Conference 2022"
        }
        self.user_schema = UserSchema()

    def test_register_user(self):
        # Validate user data
        errors = self.user_schema.validate(self.user_data)
        self.assertEqual(errors, {})

        # Register user
        registration_status, message = registerUser(self.user_data)

        # Check registration status
        self.assertTrue(registration_status)

        # Check registration message
        self.assertEqual(message, "Registration successful. Please check your email for confirmation.")

if __name__ == "__main__":
    unittest.main()
```