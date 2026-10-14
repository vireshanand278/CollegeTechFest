from flask import Flask,render_template,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify(
        status="OK",
        application="college tech event"
    )


if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
    


