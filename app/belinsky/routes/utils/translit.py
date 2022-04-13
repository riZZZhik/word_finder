"""Transliterate english symbols to Russian."""
import transliterate

from .exceptions import UnknownLanguageError


def translit(text: str, language: str) -> str:
    """Transliterate english symbols to Russian."""
    known_languages = ['ru']
    if language == 'ru':
        return transliterate.translit(text, language)

    raise UnknownLanguageError(language, known_languages)
