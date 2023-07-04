```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class RecommendationSystem:
    def __init__(self, userData, eventData):
        self.userData = userData
        self.eventData = eventData

    def create_tfidf_matrix(self, data, feature):
        tfidf = TfidfVectorizer(stop_words='english')
        data[feature] = data[feature].fillna('')
        tfidf_matrix = tfidf.fit_transform(data[feature])
        return tfidf_matrix

    def get_cosine_similarity(self, tfidf_matrix):
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return cosine_sim

    def recommend_events(self, userId, cosine_sim):
        indices = pd.Series(self.eventData.index, index=self.eventData['eventName']).drop_duplicates()
        idx = indices[userId]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        event_indices = [i[0] for i in sim_scores]
        return self.eventData['eventName'].iloc[event_indices]

    def generate_recommendations(self):
        tfidf_matrix = self.create_tfidf_matrix(self.eventData, 'eventDescription')
        cosine_sim = self.get_cosine_similarity(tfidf_matrix)
        recommendations = {}
        for user in self.userData['userId']:
            recommendations[user] = self.recommend_events(user, cosine_sim)
        return recommendations
```