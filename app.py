from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def profile():
    return "danilo diaz rios"

if __name__ == "__main__":
    app.run()






