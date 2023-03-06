import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

class sentiment:
    def __init__(self,text):
        self.text = text

    def Analysis(self):
        
        return sid.polarity_scores(self.text)['compound'] 

    