"""
TO DO

The score of a document's sentiment indicates the overall emotion of a document.
The magnitude of a document's sentiment indicates how much emotional content is present within the document,
and this value is often proportional to the length of the document.

For list of supported languages: https://cloud.google.com/natural-language/docs/languages

"""

import os
from conf import GOOGLE_APPLICATION_CREDENTIALS_PATH
from bs4 import BeautifulSoup

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Setting the environmental variable for google libraries
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS_PATH


class TextSentiment:
    # type = enums.Document.Type.HTML
    _type = enums.Document.PLAIN_TEXT

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def parse_html(self, source_text):
        """
        TO DO
        :param source_text: The text content to analyze
        :type source_text:
        :return:
        :rtype:
        """
        soup = BeautifulSoup(source_text)  # TO DO check input form
        return soup.text

    def analyze(self, text):
        """
        Function gets text, analyze it and returns it's sentiment score and magnitude score.
        :param text: The text content to analyze
        :type text: string
        :return: Returns sentiment score and  magnitude score.
        :rtype: tuple(float, float)
        """
        # text prep
        document = types.Document(content=text, type=self._type)
        # Detects the sentiment of the text
        annotations = self.client.analyze_sentiment(document=document).document_sentiment
        sentiment_score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude
        return sentiment_score, magnitude














