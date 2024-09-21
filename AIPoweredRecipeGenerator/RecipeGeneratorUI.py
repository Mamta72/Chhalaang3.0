import streamlit as st
import Recipy

st.title("Interactive Recipe Generator")
st.write("This AI-powered tool helps you generate personalized recipes based on your preferences.")

# User Profile and Preferences UI
st.session_state.recipe_generated = False
def user_profile_ui():
    st.sidebar.header("User Profile and Preferences")

    # Input fields for user profile
    user_name = st.sidebar.text_input("Enter your name:")
    meat_preferences = st.sidebar.multiselect(
        "Select your favorite meat type:", 
        ['Chicken', 'Mutton', 'Fish', 'Prawns', 'Beef', 'Pork']
    )
    dietary_restrictions = st.sidebar.multiselect(
        "Select dietary restrictions:", 
        [ 'Gluten-Free']
    )
    spice_tolerance = st.sidebar.slider("Select your spice tolerance (1-5):", 1, 5)
    skill_level = st.sidebar.selectbox(
        "Select your cooking skill level:", 
        ["Beginner", "Intermediate", "Expert"]
    )
   # cooking_style = st.sidebar.slider("Select your cooking style")
    cooking_style_level = st.sidebar.selectbox(
        "Select your cooking style:", 
        ["Boiled", "Roasted", "Fried","Grilled","Steamed"]
    )

    # Save button
    save_preferences = st.sidebar.button("Save Preferences")

    if save_preferences:
        st.sidebar.success("Preferences saved successfully!")
        return {
            "name": user_name,
            "meats": meat_preferences,
            "dietary_restrictions": dietary_restrictions,
            "spice_tolerance": spice_tolerance,
            "skill_level": skill_level,
            "cooking_style_level":cooking_style_level
        }

    return None

# Recipe Generation UI
def recipe_generation_ui(user_prefs):
    # Initialize session state if it's not set
    # if "recipe_generated" not in st.session_state:
    #     st.session_state.recipe_generated = False

    if "saved" not in st.session_state:
        st.session_state.saved = False

    if "shared" not in st.session_state:
        st.session_state.shared = False

    if user_prefs:
        st.subheader(f"Welcome, {user_prefs['name']}! Let's create your personalized recipe.")

        # Dropdowns for cuisine and cooking method
        cuisine = st.selectbox("Choose a cuisine:", ["Indian", "Italian", "Chinese", "Mexican", "American"])
        cooking_method = st.selectbox("Select a cooking method:", ["Grilling", "Baking", "Frying", "Steaming", "Boiling"])

        # Input field for ingredients
        ingredients = st.text_input("Enter available ingredients (comma-separated):", "onion, garlic, tomato")
        # generateBtn=st.button("Generate Recipe")
        # print("Generate Button Start",generateBtn )
        drawBtn(user_prefs)
        # Button to trigger recipe generation
        # if generateBtn:
        #     st.success("Preferences saved successfully 2!")
        #     print("Button click")
            # st.session_state.recipe_generated = True
            # response = Recipy.chatbot(user_prefs)  # Assuming Recipy.chatbot generates a recipe based on user_prefs
            # st.session_state.recipe = f"{response} (Cuisine: {cuisine}, Method: {cooking_method}, Ingredients: {ingredients})"
            # st.session_state.saved = False  # Reset saved state after generating a new recipe
            # st.session_state.shared = False  # Reset shared state after generating a new recipe

       
if "clicked" not in st.session_state:
    st.session_state["clicked"] = False

def drawBtn(user_prefs):
    print(user_prefs)
    option= user_prefs
    st.button("Generate Recipe", on_click= onSearch, args= [option])
    
def onSearch(opt):
    print("Button Clicked")
    response = Recipy.chatbot(opt)
    print(f"UI{response}")
    st.session_state["clicked"] = True
    st.session_state.recipe_generated=True
    st.session_state.recipe=response
    
    
if st.session_state["clicked"]:
    st.success("Done!")
    st.write(st.session_state.recipe)

# Main App UI
def main_ui():
    

    # Call UI for user profile
    user_prefs = user_profile_ui()

    # Call UI for recipe generation if preferences are available
    recipe_generation_ui(user_prefs)
     # Show generated recipe and additional buttons
    if st.session_state.recipe_generated:
            st.success(f"Recipe Generated: {st.session_state.recipe}")

            # Save button
            if st.button("Save Recipe") and not st.session_state.saved:
                st.session_state.saved = True
                st.success("Recipe saved to your collection!")

            # Share button
            if st.button("Share on Social Media") and not st.session_state.shared:
                st.session_state.shared = True
                st.success("Recipe shared on social media!")

            # Show messages based on actions
            if st.session_state.saved:
                st.info("Recipe has already been saved.")
            if st.session_state.shared:
                st.info("Recipe has already been shared.")
# Run the UI app
if __name__ == '__main__':
    main_ui()
