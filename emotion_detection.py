import requests
import json

def emotion_detector(text_to_analyze):
   
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']
    
    score = 0
    
    for emotion in emotions:
        if(score < emotions[emotion]):
            score = emotions[emotion]
            highest = {'dominant_emotion': emotion}

    emotions.update(highest)
    
    return emotions