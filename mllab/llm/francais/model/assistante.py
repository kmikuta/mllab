from google.genai import types, Client
from mllab.llm.francais.data import system_prompt, word_prompt, conjugation_prompt
from mllab.llm.francais.model.tense import Tense
from pydantic import BaseModel


class WordDetailsModel(BaseModel):
  word: str
  type: str
  gender: str
  transcription: str


class ConjugationModel(BaseModel):
    tense: str
    conjugation: list[str]


MODEL = "gemini-2.0-flash"


class Assistante():
    def __init__(self):
        self.client = Client()

    def get_word_details(self, word):
        return self._generateContent(word_prompt(word), schema=WordDetailsModel)
    
    def get_conjugation(self, word, tense=Tense.PRESENT):
        return self._generateContent(conjugation_prompt(word, tense), ConjugationModel)
    
    def _generateContent(self, contents, schema):
         return self.client.models.generate_content(
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type='application/json',
                response_schema=schema
            ),
            model=MODEL
        )


__all__ = ["Assistante"]