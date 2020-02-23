"""
TO DO

The score of a document's sentiment indicates the overall emotion of a document.
The magnitude of a document's sentiment indicates how much emotional content is present within the document,
and this value is often proportional to the length of the document.
    - score range is between -1.0 (negative) and 1.0 (positive).
    - magnitude rangeg is between 0.0 and +inf.
For more information: https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values

For list of supported languages: https://cloud.google.com/natural-language/docs/languages

"""

import os
import requests
from bs4 import BeautifulSoup

from conf import GOOGLE_APPLICATION_CREDENTIALS_PATH

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Setting the environmental variable for google libraries
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS_PATH


class TextSentiment:
    _sent_label = 0
    _sent_score = 1

    def __init__(self):
        self.client = language.LanguageServiceClient()
        self.doc_type = 'HTML'

    @staticmethod
    def _get_url_text(html):
        """
        The function receives the URL and extracts text from it.
        Source code: https://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
        :param html: web page content
        :type html: string
        :return: content of the web page
        :rtype: string
        """
        soup = BeautifulSoup(html, 'lxml')
        # clean all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    def analyze(self, text):
        """
        Function gets text, analyze it and returns it's sentiment score and magnitude score.
        :param text: The text content to analyze
        :type text: string
        :return: Returns sentiment score and  magnitude score.
        :rtype: tuple(float, float)
        """
        # text prep
        document = types.Document(content=text, type=self.doc_type)
        # Detects the sentiment of the text
        annotations = self.client.analyze_sentiment(document=document).document_sentiment
        sentiment_score = annotations.score
        magnitude = annotations.magnitude
        return sentiment_score, magnitude

    def get_sentiment(self, url):
        """
        Function gets url and calculates sentiment score of the web page content
        :return: the label of the sentiment score
        :rtype: string
        """
        sentiment_score = 0
        try:
            text = self._get_url_text(url)
            sentiment_score, _ = self.analyze(text)
            
        except requests.exceptions.HTTPError as err:
            print(f'Error: {err}')
        except Exception as err:
            print(f'Error: {err}')

        return sentiment_score
