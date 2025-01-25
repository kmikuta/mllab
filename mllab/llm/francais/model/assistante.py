import google.generativeai as genai
from mllab.llm.francais.data import system_prompt


class Assistante():
    def __init__(self, history=[]):
        self.model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            system_instruction=system_prompt
        )
        self.chat = self.model.start_chat(history=history)

    def send_message(self, message):
        return self.chat.send_message(message)
