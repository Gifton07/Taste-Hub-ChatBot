import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_curry_recipe(user_input):
    # Get the API key from environment variables
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file.")
    
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'
    
    # Prepare the request payload
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Generate a curry recipe based on the following details:\n"
                                f"Main Ingredient: {user_input['main_ingredient']}\n"
                                f"Spice Level: {user_input['spice_level']}\n"
                                f"Cuisine Type: {user_input['cuisine']}\n"
                                f"Serving Size: {user_input['servings']} servings\n"
                    }
                ]
            }
        ]
    }

    # Set headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        recipe = response_data['candidates'][0]['content']['parts'][0]['text']
        return recipe
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
