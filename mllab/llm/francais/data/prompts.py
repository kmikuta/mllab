system_prompt = "You are an assistant helping to learn french."

word_prompt_parts = [
    "When asked how to say something in french, use the following format:"
    "The word type can be a verb, a noun, an adjective or a number",
    "The gender can be male or female."
    "The transcription is a phonetic transcription.",
    "When word is not a noun, provide gender as n/a.",
]

word_prompt = lambda w: " ".join(word_prompt_parts) + f" How to say '{w}' in french?"

conjugation_prompt_parts = [
    "When asked for conjugation, use the following format:",
    "The tense is a name of the tense conjugation relates to."
    "Always provide conjugation by pronouns as a list."
]

conjugation_prompt = lambda w, t: " ".join(conjugation_prompt_parts) + f"Provide conjugation for '{w}' in {t}."

__all__ = ["system_prompt", "conjugation_prompt", "word_prompt"]
