```python
import unittest
from unittest.mock import patch
from src import customer_support

class TestCustomerSupport(unittest.TestCase):

    @patch('src.customer_support.send_email')
    @patch('src.customer_support.send_social_media_message')
    def test_handle_customer_query(self, mock_send_email, mock_send_social_media_message):
        # Arrange
        query = "How to register for an event?"
        email = "test@example.com"
        social_media_handle = "@test_user"

        # Act
        customer_support.handle_customer_query(query, email, social_media_handle)

        # Assert
        mock_send_email.assert_called_once_with(email, "Response to your query", "Here is the information on how to register for an event.")
        mock_send_social_media_message.assert_called_once_with(social_media_handle, "Here is the information on how to register for an event.")

    @patch('src.customer_support.send_email')
    def test_send_event_updates(self, mock_send_email):
        # Arrange
        email = "test@example.com"
        event_update = "The event schedule has been updated."

        # Act
        customer_support.send_event_updates(email, event_update)

        # Assert
        mock_send_email.assert_called_once_with(email, "Event Update", event_update)

    @patch('src.customer_support.send_email')
    def test_send_recommendations(self, mock_send_email):
        # Arrange
        email = "test@example.com"
        recommendations = "We recommend you to attend the keynote speech."

        # Act
        customer_support.send_recommendations(email, recommendations)

        # Assert
        mock_send_email.assert_called_once_with(email, "Personalized Recommendations", recommendations)

if __name__ == '__main__':
    unittest.main()
```