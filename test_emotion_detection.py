import unittest
from EmotionDetection.emotion_detection import emotion_detector  # Ensure this import matches your package structure

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy', "Expected 'joy' as the dominant emotion")
        
        # Test case 2
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger', "Expected 'anger' as the dominant emotion")
        
        # Test case 3
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust', "Expected 'disgust' as the dominant emotion")
        
        # Test case 4
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness', "Expected 'sadness' as the dominant emotion")
        
        # Test case 5
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear', "Expected 'fear' as the dominant emotion")

if __name__ == "__main__":
    unittest.main()
