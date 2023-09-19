import requests

# Your Microsoft Translator API credentials
subscription_key = 15805a960bb440bea654f162c709ffad
endpoint = https://api.cognitive.microsofttranslator.com/

def translate_text(input_text, target_languages):
    translations = {}

    for lang in target_languages:
        url = endpoint + 'translate'
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/json',
        }
        params = {
            'api-version': '3.0',
            'to': lang,
        }
        body = [{'text': input_text}]

        response = requests.post(url, headers=headers, params=params, json=body)
        translation = response.json()

        if response.status_code == 200:
            translations[lang] = translation[0]['translations'][0]['text']
        else:
            print(f"Translation failed for language {lang}. Error: {translation}")

    return translations

if __name__ == "__main__":
    input_text = "Merhaba, nasılsınız?"  # Turkish input text
    target_languages = ["ru", "fa", "ar"]  # Language codes for Russian, Persian, and Arabic

    translations = translate_text(input_text, target_languages)

    print("Original Text (Turkish): " + input_text)
    for lang, translation in translations.items():
        print(f"Translation ({lang}): {translation}")
