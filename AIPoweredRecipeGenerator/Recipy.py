import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the model and tokenizer
model_name = "MBZUAI/LaMini-Flan-T5-248M"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Function to generate a response
def generate_response(user_input):
    # Encode the user input and generate a response
    inputs = tokenizer.encode(f"chatbot: {user_input}", return_tensors="pt")
    outputs = model.generate(inputs, max_length=10000, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
   # outputs = model.generate(inputs, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
   
    # Decode and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #response = tokenizer.decode(outputs[0])
    return response

# Chat loop
def chatbot(userPreference):
    print("Backend")
    print(userPreference)
    #print("Welcome to Licius Chicken Recipe Generator")
    
    # while True:
    #     user_input = input("You: ")
        
    #     if user_input.lower() == 'exit':
    #         print("Chatbot: Goodbye!")
    #         break
    #query=f"You:Generate Recipe for cook non-veg food which will include meat : {userPreference['meats']}, and shoud be  {userPreference['dietary_restrictions']}  and have {userPreference['spice_tolerance']}"    
    query = f"You: Generate a non-veg recipe using meat: {', '.join(userPreference['meats'])}, which should respect dietary restrictions: {', '.join(userPreference['dietary_restrictions'])}, and have a spice tolerance level of {userPreference['spice_tolerance']}, and have a cooking style of {userPreference['cooking_style_level']}."

    print(query)
    response = generate_response(query)
    print(f"Chatbot: {response}")
    return response

if __name__ == "__main__":
    chatbot()
