# tests/test_integration.py
import pytest
from flask import Flask
from chatbot.app import app  # Import your Flask app here

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_form_submission(client):
    response = client.post('/ask', data={'user_query': 'What is your return policy?'})
    assert b'Our return policy allows returns' in response.data


