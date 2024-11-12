import streamlit as st
from api_handler import generate_curry_recipe

# Streamlit app title
st.title("Taste Hub")

# User input fields
main_ingredient = st.text_input("Main Ingredient (e.g., chicken, potatoes)")
spice_level = st.selectbox("Spice Level", ["Mild", "Medium", "Spicy"])
cuisine = st.selectbox("Cuisine Type", ["Indian", "Thai", "Japanese", "Other"])
servings = st.number_input("Serving Size", min_value=1, value=4)

# Generate button
if st.button("Here is your dish"):
    user_input = {
        "main_ingredient": main_ingredient,
        "spice_level": spice_level,
        "cuisine": cuisine,
        "servings": servings
    }
    recipe = generate_curry_recipe(user_input)
    if recipe:
        st.subheader("Generated Food Recipe")
        st.text(recipe)
    else:
        st.error("Failed to generate recipe. Please try again.")
