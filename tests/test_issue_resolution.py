```python
import unittest
from src.issue_resolution import resolveIssue

class TestIssueResolution(unittest.TestCase):

    def setUp(self):
        self.issue = {
            "issueId": "123",
            "userId": "456",
            "description": "Unable to join breakout room",
            "status": "open"
        }

    def test_resolve_issue(self):
        result = resolveIssue(self.issue)
        self.assertEqual(result['status'], 'resolved')

if __name__ == '__main__':
    unittest.main()
```