import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define a dictionary for predefined responses
faq_dict = {
    "Hello": "Hi, how can I assist you today?",
    "What is your name?": "I am a chatbot, here to assist you.",
    "Who are you?": "I am a chatbot",
    "How are you?": "I'm doing fine! How can I help you?",
    "What can you do?": "I can answer some basic questions and greet you!",
    "When will I receive my order?": "You will receive your order in 3 working days from the time of ordering.",
    "Where is my order?": "You can track your order status in the 'My Orders' section of your account.",
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase for a full refund, provided the product is in unused condition.",
    "How can I cancel my order?": "You can cancel your order within 24 hours by visiting the 'Order Details' section in your account.",
    "What payment methods do you accept?": "We accept credit/debit cards, PayPal, and Apple Pay.",
    "Can I change the shipping address after placing an order?": "Unfortunately, you cannot change the shipping address once the order is placed, but you can contact our support team for assistance.",
    "Do you offer gift cards?": "Yes, we offer gift cards in various denominations. You can purchase them from our Gift Cards section.",
    "How do I apply a discount code?": "You can apply a discount code during checkout in the 'Promo Code' section.",
    "Is there free shipping?": "Yes, we offer free shipping on orders over $50.",
    "How can I contact customer support?": "You can reach customer support through the 'Contact Us' page on our website or by emailing support@ecommerce.com.",
    "Do you ship internationally?": "Yes, we ship to many international locations. You can check our shipping options at checkout.",
    "Can I modify my order after it's been placed?": "Once an order is placed, it cannot be modified, but you can cancel it within a limited time.",
    "Do you offer gift wrapping?": "Yes, we offer gift wrapping services for an additional fee at checkout.",
    "How can I leave feedback on a product?": "You can leave feedback by going to the product page and submitting a review in the 'Reviews' section.",
    "Can I track my return?": "Yes, you can track your return by checking the status in the 'Returns' section of your account.",
    "Do you offer loyalty programs?": "Yes, we have a loyalty program that rewards you with points for every purchase. You can redeem the points for discounts on future orders.",
    "What is your privacy policy?": "You can find our privacy policy at the bottom of our website, which outlines how we handle your personal information.",
    "How do I unsubscribe from emails?": "You can unsubscribe from our promotional emails by clicking the unsubscribe link at the bottom of any email you receive from us.",
    "Do you have a size guide?": "Yes, we provide size guides on each product page to help you find the perfect fit.",
    "Are the products genuine?": "Yes, we source our products directly from authorized suppliers to ensure their authenticity.",
    "Can I purchase an item that is out of stock?": "If an item is out of stock, you can sign up for notifications to be alerted when it becomes available again.",
    "How do I redeem a coupon?": "You can enter your coupon code during checkout in the 'Promo Code' field to apply the discount.",
    "How can I update my account details?": "You can update your account details by logging into your account and going to the 'Account Settings' section.",
    "How can I change my password?": "If you forgot your password, click on 'Forgot Password' on the login page to reset it."
}


# Function to get the chatbot's response based on cosine similarity
def get_chatbot_response(user_input,threshold=0.45):
    # Prepare the corpus (user input + predefined questions)
    corpus = list(faq_dict.keys())
    corpus.append(user_input)  # Add user input to the corpus

    # Convert the corpus to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate the cosine similarity between user input and predefined questions
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Find the most similar question
    most_similar_index = cosine_similarities.argmax()
    highest_similarity = cosine_similarities[0][most_similar_index]  # Get the similarity value
    if highest_similarity<threshold:
        return "Sorry, I don't understand your question. Please ask something else."


    # Return the corresponding answer from the FAQ dictionary
    response = faq_dict[list(faq_dict.keys())[most_similar_index]]
    return response

# Example usage
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = get_chatbot_response(user_input)
            print("Chatbot:", response)
