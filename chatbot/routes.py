from flask import render_template, request,Blueprint
from chatbot import get_chatbot_response  # Function to interact with the chatbot
root = Blueprint("main", __name__)
@root.route("/")
def home():
    return render_template("index.html")  # Home page where the user can input queries

@root.route("/ask", methods=["POST"])
def ask():
    user_query = request.form["user_query"]
    response = get_chatbot_response(user_query)  # Get the response from chatbot
    return render_template("index.html", response=response)  # Display response in the UI
