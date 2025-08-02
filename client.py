import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid model
model = genai.GenerativeModel('gemini-2.5-pro')
command = '''[8:30 PM, 8/1/2025] Bhavya2: bss badia hi hu
[8:34 PM, 8/1/2025] Khushi Gupta: Kya kr rhi h
[9:08 PM, 8/1/2025] Bhavya2: ek series dekh rhi thi
[9:08 PM, 8/1/2025] Bhavya2: khtm ho gyi aab
[10:24 AM, 8/2/2025] Khushi Gupta: Acha kaunsi
[12:36 PM, 8/2/2025] Bhavya2: Mandala murder
[4:00 PM, 8/2/2025] Khushi Gupta: ye kispe h
[4:00 PM, 8/2/2025] Khushi Gupta: maine ni suna naam
[4:41 PM, 8/2/2025] Bhavya2: Netflix pr h
[4:41 PM, 8/2/2025] Bhavya2: Nayi aayi h
[4:41 PM, 8/2/2025] Bhavya2: Vani kapoor ki'''

# Generate content
prompt = f"You are a person ,Khushi Gupta from india which studies btech in miet doing cse ai and 21 years old, you analyze chat history and on the basis of that you talk or chat or respond like khushi and give short reponses only dont explainn too much .\nUser: {command}"
response = model.generate_content(prompt)

# Print the result
print(response.text)