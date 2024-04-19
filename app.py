from flask import Flask, jsonify,json

app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "aminespinoza10"},
            {"instagramUser": "aminespinoza10"},
            {"xUser": "aminespinoza"},
            {"linkedin": "amin-espinoza"},
            {"githubUser": "aminespinoza10"}
        ],
        "blog": "https://aminespinoza.com",
        "author": "Miranda Espinoza"
    }
    return json.dumps(value)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)