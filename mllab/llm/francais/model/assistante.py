import google.generativeai as genai
from mllab.llm.francais.data import system_prompt, word_prompt, conjugation_prompt
from mllab.llm.francais.model.tense import Tense


class Assistante():
    def __init__(self, history=[]):
        self.model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            system_instruction=system_prompt
        )
        self.chat = self.model.start_chat(history=history)

    def get_word_details(self, word):
        return self.chat.send_message(word_prompt(word))
    
    def get_conjugation(self, word, tense=Tense.PRESENT):
        return self.chat.send_message(conjugation_prompt(word, tense))


__all__ = ["Assistante"]