""" Server for the App """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def mood_detector():

    """ Emotion Analyzer, linked to emotion_detection.py file """
    user_text = request.args.get('textToAnalyze')

    resp = emotion_detector(user_text)

    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    first_return = f"For the given statement, the system response is {resp}. "
    second_return = f"The dominant emotion is {resp['dominant_emotion']}."
    return first_return + second_return

@app.route("/")
def render_home_page():

    """ Homepage render """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
