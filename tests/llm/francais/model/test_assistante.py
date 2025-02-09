from mllab.llm.francais.model import Assistante, WordDetailsModel, ConjugationModel, Tense


class TestAssistanteModel:
    def test_model_returns_word_details_for_noun(self):
        model = Assistante()
        response = model.get_word_details('dog')
        assert response == WordDetailsModel(word="chien", type="noun", gender="male", transcription="/ʃjɛ̃/")

    def test_model_returns_word_details_for_verb(self):
        model = Assistante()
        response = model.get_word_details('go')
        assert response == WordDetailsModel(word="aller", type="verb", gender="n/a", transcription="/ale/")

    def test_model_returns_word_details_for_number(self):
        model = Assistante()
        response = model.get_word_details('5')
        assert response == WordDetailsModel(word="cinq", type="number", gender="n/a", transcription="sɛ̃k")

    def test_model_returns_conjugation_for_present_tense(self):
        model = Assistante()
        response = model.get_conjugation('go', tense=Tense.PRESENT)
        assert response == ConjugationModel(tense='Présent', conjugation=[
            'Je vais', 'Tu vas', 'Il/Elle/On va', 'Nous allons', 'Vous allez', 'Ils/Elles vont'
        ])
