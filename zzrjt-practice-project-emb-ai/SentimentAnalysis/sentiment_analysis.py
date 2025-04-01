import requests
import json 

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json = myobj, headers=header)
    formatted_res = json.loads(res.text)
    if res.status_code == 500:
        return {"label" : None, "score" : None}
    return {"label" : formatted_res["documentSentiment"]["label"], "score" : formatted_res["documentSentiment"]["score"]}