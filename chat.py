import google.generativeai as genai

API_KEY = 'AIzaSyBO2kHw_Aeh059q5i6Hz6NgTZ37FWMU_Mc'

genai.configure(
    api_key=API_KEY,
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    question = input('You: ')
    response = chat.send_message(question)
    print(f'Bot: {response.text}')
