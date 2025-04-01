from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Function to incorporate sentiment_analyzer in app 
    """
    
    text_to_analyze = request.args.get("textToAnalyze")
    res = sentiment_analyzer(text_to_analyze)
    if res["label"] is None and res["score"] is None: 
        return "Invalid input! Try again."
    return "Text is {} with a score of {}".format(res["label"].split("_")[1], res["score"])

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)