import flask
from quiz_generator import get_quiz_sentence

# initialize our Flask application and pre-trained model
app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/generate", methods=["POST"])
def predict():
    response = {
        "success": False,
        "Content-Type": "application/json"
    }

    if flask.request.method == "POST":
        if flask.request.get_json().get("word"):

            word = flask.request.get_json().get("word")
            title, quiz_sentence, answers = get_quiz_sentence(word)

            response["title"] = title
            response["sentence"] = quiz_sentence
            response["answers"] = answers

            response["success"] = True

    return flask.jsonify(response)


if __name__ == "__main__":
    app.run()