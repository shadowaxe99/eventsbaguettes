```python
import requests
from google.cloud import translate_v2 as translate

class TranslationService:
    def __init__(self):
        self.translate_client = translate.Client()

    def detect_language(self, text):
        result = self.translate_client.detect_language(text)
        return result['language']

    def translate_text(self, text, target_language):
        if self.detect_language(text) == target_language:
            return text

        result = self.translate_client.translate(text, target_language)
        return result['translatedText']

    def translate_event_data(self, eventData, target_language):
        translated_event_data = {}
        for key, value in eventData.items():
            if isinstance(value, str):
                translated_event_data[key] = self.translate_text(value, target_language)
            else:
                translated_event_data[key] = value
        return translated_event_data
```