import pyautogui
import time
import pyperclip
import os
from dotenv import load_dotenv
import google.generativeai as genai

def is_last_message_from_sender(chat_log, sender_name="Mumma"):
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

pyautogui.FAILSAFE = False

pyautogui.click(1147, 1037)
time.sleep(1)

while True:
    start_x, start_y = 686, 196
    end_x, end_y = 1862, 911

    pyautogui.click(start_x, start_y)
    time.sleep(0.2)

    pyautogui.mouseDown(start_x, start_y)
    pyautogui.moveTo(end_x, end_y, duration=1)
    pyautogui.mouseUp()

    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(686, 196)
    time.sleep(0.5)

    chat_history = pyperclip.paste()
    print("Copied text:\n", chat_history)

    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):    
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-2.5-pro')   
        prompt = f"You are a person ,Khushi Gupta from india which studies btech in miet doing cse ai and 21 years old, you analyze chat history and on the basis of that you talk or chat or respond like khushi and give short reponses only dont explainn too much (text message only next chat reply without date and time only message).\nUser: {chat_history}"
        
        try:
            response = model.generate_content(prompt)
            text_response = response.text.strip() if response.text else "Hmm..."
        except Exception as e:
            text_response = "..."

        print(text_response)
        pyperclip.copy(text_response)
        pyautogui.click(851, 950)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)





