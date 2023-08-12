"""Gives the translation from French(France) to and from English(US)
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english, /):
    """English (US) to French (France) Translator using Deep Translator

    Args:a
        english (string): Text to convert

    Returns:
        string: French translation
    """
    str_ = "".join(MyMemoryTranslator(
        source='en-US', target='fr-FR').translate(english))
    return str_


def french_to_english(french, /):
    """French (France) to English (US) Translator using Deep Translator

    Args:
        french (string): Text to convert

    Returns:
        string: English translation
    """
    str_ = "".join(MyMemoryTranslator(
        source='fr-FR', target='en-US').translate(french))
    return str_
