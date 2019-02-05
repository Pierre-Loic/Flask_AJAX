from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# ----------STEP 1------------
# The user opens the home page
# ----------------------------
@app.route('/')
def main():
    return render_template("main.html")

# ----------------STEP 2------------------
# +++++In HTML template (main.html)+++++++
# The user fills the input box with a word
# ----------------------------------------

# ------------------STEP 3----------------------
# ++++++++In HTML template (main.html)++++++++++
# An AJAX request is sent to the url /test_ajax/
# ----------------------------------------------

@app.route('/test_ajax/', methods=['POST'])
def test():
    # -----------------------STEP 4-------------------------
    # Data are collected from the request and sent to an API
    # ------------------------------------------------------
    base_url = "http://fr.wikipedia.org/w/api.php"
    params_url = {"action": "opensearch",
                  "search": request.form["question"]}
    liste=requests.get(url=base_url, params=params_url)
    # ------------STEP 5--------------------
    # API Data are sent back to the template 
    # --------------------------------------
    return jsonify({'data': render_template('reponse.html', liste=liste)})
    # -------------STEP 6-----------------
    # +++In HTML template (main.html)+++++
    # div#reponse is updated with API data 
    # ------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
