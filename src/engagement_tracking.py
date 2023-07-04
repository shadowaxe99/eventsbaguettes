```python
import pandas as pd
from datetime import datetime

class EngagementTracker:
    def __init__(self):
        self.analyticsData = pd.DataFrame(columns=['user_id', 'event_id', 'engagement_score', 'last_updated'])

    def track_engagement(self, user_id, event_id, engagement_score):
        current_time = datetime.now()
        if (self.analyticsData['user_id'] == user_id) & (self.analyticsData['event_id'] == event_id).any():
            self.analyticsData.loc[(self.analyticsData['user_id'] == user_id) & (self.analyticsData['event_id'] == event_id), ['engagement_score', 'last_updated']] = [engagement_score, current_time]
        else:
            new_row = {'user_id': user_id, 'event_id': event_id, 'engagement_score': engagement_score, 'last_updated': current_time}
            self.analyticsData = self.analyticsData.append(new_row, ignore_index=True)

    def get_engagement_score(self, user_id, event_id):
        if (self.analyticsData['user_id'] == user_id) & (self.analyticsData['event_id'] == event_id).any():
            return self.analyticsData.loc[(self.analyticsData['user_id'] == user_id) & (self.analyticsData['event_id'] == event_id), 'engagement_score'].values[0]
        else:
            return None

    def get_all_engagement_scores(self):
        return self.analyticsData
```