import requests
import json

def get_word_data(word):

    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    return json.loads(response.content)

def get_meanings(meaning):

    meaning_dict = dict()
    meaning_dict["pos"] = meaning["partOfSpeech"]

    definitions = []
    for definition in meaning["definitions"]:
        def_exmp_dict = dict()
        def_exmp_dict["definition"] = definition["definition"]
        if "example" in definition:
            def_exmp_dict["example"] = definition["example"]
        else:
            def_exmp_dict["example"] = ''
        definitions.append(def_exmp_dict)
    meaning_dict["def"] = definitions
    if meaning["antonyms"]:
        meaning_dict["ant"] = meaning["antonyms"]
    if meaning["synonyms"]:
        meaning_dict["syn"] = meaning["synonyms"]
    return meaning_dict