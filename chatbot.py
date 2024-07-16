from fuzzywuzzy import fuzz
from knowledge_base import knowledge_base

def get_best_match(user_question, questions):
    best_match = None
    best_ratio = 0

    for question in questions:
        ratio = fuzz.token_sort_ratio(user_question.lower(), question.lower())
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = question

    return best_match if best_ratio > 60 else None

def chatbot(user_input):
    best_match = get_best_match(user_input, knowledge_base.keys())
    
    if best_match:
        return knowledge_base[best_match]
    else:
        return "I'm sorry, I don't have information about that. Can you please rephrase your question or ask something else?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot(user_input)
    print("Bot:", response)