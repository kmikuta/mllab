system_prompt = "You are an assistant helping to learn french used in Switzerland. When asked to provide some answer, do not propose anything extra."

word_prompt_parts = [
    "Indicate if it is verb, noun, adjective or number",
    "Also provide phonetic transcription.",
    "When it is number, provide also the ordinal number."
    "Use the format: word [transcription], verb | noun | adjective | number."
]

word_prompt = lambda w: f"Specify how to say '{w}' in french. " + " ".join(word_prompt_parts)

conjugation_prompt = lambda w, t: f"Provide conjugation for '{w}' by pronouns in {t}. Use list format. Do not provide transcription."

__all__ = ["system_prompt", "conjugation_prompt", "word_prompt"]
