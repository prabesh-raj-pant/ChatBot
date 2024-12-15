import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

from flask import Flask, request, render_template ,jsonify
app = Flask(__name__)  
 
API_kEY=os.getenv("API_KEY",123)
genai.configure(api_key=API_kEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/', methods=['POST', 'GET'])
def index():
    response=None
    if request.method=="POST":
        prompt=request.form['Prompt']
        # print(prompt)
        response = model.generate_content(prompt)
        print(response.text) 
    return render_template("index.html",response=response)


if __name__=='__main__':
   app.run()