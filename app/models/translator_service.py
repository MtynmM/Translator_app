import requests


class TranslatorService:

    _API_URL = "https://api.mymemory.translated.net/get"

    def translate(self, text: str, lang_from: str = "en", lang_to: str = "fa") -> str:
        if text.strip() == "":
            return ""
        parameters = {"q": text, "langpair": f"{lang_from}|{lang_to}"}

        try:
            response = requests.get(self._API_URL, params=parameters)
            response.raise_for_status()

            data = response.json()

            translated_text = data["responseData"]["translatedText"]
            return translated_text

        except Exception:
            return "ترجمه ناموفق بود. لطفا دوباره تلاش کنید.خطا!!!"
