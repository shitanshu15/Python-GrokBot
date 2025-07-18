import sys
import re
import random
from datetime import datetime

# Check Python version
if sys.version_info < (3, 6):
    print("Error: Python 3.6 or higher is required.")
    sys.exit(1)

# Define pattern-response pairs for the chatbot
patterns = [
    # Greetings
    (r'(hi|hello|hey|greetings)(\W|$)', 
     ['Hello! How can I assist you today?', 'Hi there! What’s on your mind?', 'Hey! Ready to chat?']),
    
    # Farewells
    (r'(bye|goodbye|see you|exit|quit)(\W|$)', 
     ['Goodbye! Have a great day!', 'See you later!', 'Bye bye!']),
    
    # Questions about the chatbot
    (r'(who|what) (are|is) (you|this)(\W|$)', 
     ['I’m GrokBot, a simple chatbot built with Python!', 'I’m a Python-powered chatbot here to answer your questions!']),
    
    # Questions about time
    (r'(what|tell) (is|me) (the|) (time|date)(\W|$)', 
     [f"The current time is {datetime.now().strftime('%H:%M:%S')} on {datetime.now().strftime('%Y-%m-%d')}."]),
    
    # Questions about weather (mock responses, as no API is used)
    (r'(weather|temperature) (in|for|at) (\w+)', 
     ['I’m not connected to a weather API, but it’s probably sunny somewhere!', 
      'Weather info isn’t available, but imagine a nice breeze in {}!', 
      'Can’t fetch the weather for {}, but it’s perfect for coding!']),
    
    # General knowledge questions about Python
    (r'(what|who) is (python|Python)(\W|$)', 
     ['Python is a versatile programming language used for web development, data science, and more!', 
      'Python? It’s the cool snake of programming languages, super easy to learn!']),
    
    # Fallback for unknown queries
    (r'.*', 
     ['I’m not sure about that one. Try asking about the weather, time, or Python!', 
      'Hmm, could you rephrase that? I’m all ears… or rather, all text!', 
      'Not sure how to answer that. What else can I help with?'])
]

# Function to preprocess user input (simple lowercase conversion)
def preprocess_input(user_input):
    try:
        return user_input.lower().strip()
    except Exception as e:
        print(f"Error processing input: {e}")
        return user_input.lower()

# Function to find a response based on user input
def get_response(user_input):
    processed_input = preprocess_input(user_input)
    for pattern, responses in patterns:
        match = re.search(pattern, processed_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if '{}' in response and len(match.groups()) >= 3:
                return response.format(match.group(3))
            return response
    return random.choice(patterns[-1][1])

# Main chatbot function
def chatbot():
    print("Welcome to GrokBot! Type 'exit' or 'quit' to stop.")
    print(f"Current time: {datetime.now().strftime('%H:%M:%S %Z')} on {datetime.now().strftime('%Y-%m-%d')}")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                print("GrokBot: Goodbye! Thanks for chatting!")
                break
            response = get_response(user_input)
            print(f"GrokBot: {response}")
        except (EOFError, KeyboardInterrupt):
            print("GrokBot: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again.")
            continue

# Run the chatbot
if __name__ == "__main__":
    print("Starting GrokBot...")
    try:
        chatbot()
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Please ensure you are running this script in a terminal or command prompt with Python 3.6+.")
        sys.exit(1)
