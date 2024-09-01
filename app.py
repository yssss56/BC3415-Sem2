from flask import Flask,render_template,request
from openai import OpenAI
import os
import requests

api = os.getenv("OPENAI_API_TOKEN")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_FAQ",methods=["GET","POST"])
def financial_FAQ():
    return(render_template("financial_FAQ.html"))

@app.route("/openai",methods=["GET","POST"])
def openai_route():
    q = request.form.get("q")
    
    try:
        client = OpenAI(api_key=api)

        # Make the OpenAI API call
        response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"{q}"}
                ],
                max_tokens=300,
                stop=None,
                temperature=0.7
            )
        response_text = response.choices[0].message.content.strip() if response.choices else "No response from the model."

    except Exception as e:
        response_text = f"An error occurred: {str(e)}"

    return render_template("openai.html", r=response_text)

if __name__ == "__main__":
    app.run()
