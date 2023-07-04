```python
import random
from src.issue_resolution import resolveIssue

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.greetings = ['Hello', 'Hi', 'Hey', 'Hi there']
        self.farewells = ['Goodbye', 'Bye', 'See you later', 'Take care']

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def handle_query(self, query):
        if 'issue' in query:
            return resolveIssue(query)
        elif 'recommendation' in query:
            return self.recommend(query)
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def recommend(self, query):
        # This function will use AI algorithms to provide personalized recommendations
        # For simplicity, we are returning a static message
        return "Based on your interests, we recommend the following sessions..."

chatbot = Chatbot('EventBot')
print(chatbot.greet())
print(chatbot.handle_query('I have an issue with registration'))
print(chatbot.handle_query('Can you recommend some sessions?'))
print(chatbot.farewell())
```