"""
Flask web server for emotion detection application.
Provides routes for processing emotion detection and rendering index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Handles emotion detection for the given text input.
    Returns a formatted string response with emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please provide a valid input."

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    # Format response text for valid responses
    response_text = (
        f"For the given statement, the system response is 'anger': {response.get('anger', 0)}, "
        f"'disgust': {response.get('disgust', 0)}, 'fear': {response.get('fear', 0)}, "
        f"'joy': {response.get('joy', 0)}, 'sadness': {response.get('sadness', 0)}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
