```python
import unittest
from src.translation_service import TranslationService

class TestTranslationService(unittest.TestCase):

    def setUp(self):
        self.translation_service = TranslationService()

    def test_translate_text(self):
        result = self.translation_service.translate_text('Hello', 'en', 'es')
        self.assertEqual(result, 'Hola')

    def test_invalid_language_code(self):
        with self.assertRaises(ValueError):
            self.translation_service.translate_text('Hello', 'en', 'abc')

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            self.translation_service.translate_text('', 'en', 'es')

if __name__ == '__main__':
    unittest.main()
```