from libretranslatepy import LibreTranslateAPI

API_URL = "https://translate.api.skitzen.com/"

def lang_detect(sample):
    
    """
    Returns language code (str) for the given sample (str).

        Example:
            detect_lang("Hello world!") -> en
    """ 

    lt = LibreTranslateAPI(API_URL)
    result = lt.detect(sample)
    current_lang = (result[0])["language"]
    return current_lang

def translate(text, source_lang, target_lang):
        
    """
    Returns translated text (str) for the input.
        Params:
            text: str - text to be translated
            source_lang: str - source language code (e.g. "en")
            target_lang: str - target language code (e.g. "en")
    """ 

    lt = LibreTranslateAPI(API_URL)
    translated_text = lt.translate(text, source_lang, target_lang)
    return translated_text
