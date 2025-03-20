# tests/test_ui.py
import pytest
from chatbot.app import app  # Import your Flask app here
from bs4 import BeautifulSoup
# This is a fixture to set up the test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ui_homepage(client):
    # Send a GET request to the homepage
    response = client.get('/')
    
    # Check if the response is successful (status code 200)
    assert response.status_code == 200

    # Check if the page contains specific text
    assert b'Welcome to the E-commerce Chatbot!' in response.data
    assert b'input type="text"' in response.data
    assert b'input type="submit"' in response.data

def test_form_submission(client):
    # Send a POST request with a sample user query
    response = client.post('/ask', data={'user_query': 'What is your return policy?'})
    
    # Check if the response contains the expected answer
    assert b'Our return policy allows returns within 30 days' in response.data

def test_invalid_query(client):
    # Send a POST request with an invalid query
    response = client.post('/ask', data={'user_query': 'What color is the sky?'})
    
    # Check if the response contains a fallback answer
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check if the fallback message is in the HTML content
    assert "Sorry, I don't understand your question." in soup.get_text()

def test_input_placeholder(client):
    # Send a GET request to check if the input placeholder is correct
    response = client.get('/')
    assert b'placeholder="Type your question here..."' in response.data

def test_submit_button(client):
    # Send a GET request to check if the submit button exists
    response = client.get('/')
    assert b'value="Submit"' in response.data

