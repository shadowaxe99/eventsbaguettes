```python
import unittest
from unittest.mock import patch
from src import social_media_support

class TestSocialMediaSupport(unittest.TestCase):

    @patch('src.social_media_support.SocialMediaSupport.post_update')
    def test_post_update(self, mock_post_update):
        # Arrange
        update_message = "Event Update: The keynote speech will start at 10am."
        mock_post_update.return_value = True

        # Act
        result = social_media_support.SocialMediaSupport().post_update(update_message)

        # Assert
        self.assertTrue(result)
        mock_post_update.assert_called_once_with(update_message)

    @patch('src.social_media_support.SocialMediaSupport.respond_to_query')
    def test_respond_to_query(self, mock_respond_to_query):
        # Arrange
        query = "When does the event start?"
        response = "The event starts at 9am."
        mock_respond_to_query.return_value = response

        # Act
        result = social_media_support.SocialMediaSupport().respond_to_query(query)

        # Assert
        self.assertEqual(result, response)
        mock_respond_to_query.assert_called_once_with(query)

if __name__ == '__main__':
    unittest.main()
```