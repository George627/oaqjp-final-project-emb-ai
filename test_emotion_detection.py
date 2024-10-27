from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_joy(self):
        first_result = emotion_detector("I am glad this happened")
        self.assertEqual(first_result['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        second_result = emotion_detector("I am really mad about this")
        self.assertEqual(second_result['dominant_emotion'], 'anger')
        
    def test_emotion_disgust(self):
        third_result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(third_result['dominant_emotion'], 'disgust')
    
    def test_emotion_sadness(self):
        fourth_result = emotion_detector("I am so sad about this")
        self.assertEqual(fourth_result['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        fifth_result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fifth_result['dominant_emotion'], 'fear')
    
unittest.main()