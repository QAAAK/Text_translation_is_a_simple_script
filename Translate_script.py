from deep_translator import GoogleTranslator

def Translate(text, lang):
    translated = GoogleTranslator(source='auto', target=lang)
    result = translated.translate(text)
    print(result)

Translate('Hello','russian')
