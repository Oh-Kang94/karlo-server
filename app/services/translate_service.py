import googletrans


class TranslateService:
    translator = googletrans.Translator()

    @staticmethod
    def translate_text_to_en(text: str):
        translatedText = TranslateService.translator.translate(
            text, dest='en', src='auto').text
        return translatedText
