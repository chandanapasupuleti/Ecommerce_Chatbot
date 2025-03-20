import pytest
from chatbot.chatbot import get_chatbot_response, faq_dict

def test_faq_dict():
    # Check for unique FAQ keys
    assert len(faq_dict) == len(set(faq_dict.keys())), "Duplicate questions found!"
    for question in faq_dict:
        assert isinstance(faq_dict[question], str), f"Answer for '{question}' is not a string"

def test_get_chatbot_response():
    response = get_chatbot_response("What is your return policy?")
    assert response == "Our return policy allows returns within 30 days of purchase for a full refund, provided the product is in unused condition.", f"Expected response: 'Our return policy allows returns...'. Got: {response}"

def test_unknown_question():
    response = get_chatbot_response("What are your store hours?")
    assert response == "Sorry, I don't understand your question. Please ask something else.", f"Expected unknown response, got: {response}"
