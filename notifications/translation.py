from modeltranslation.translator import translator, TranslationOptions
from .models import Message


class MessageTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    required_languages = ('en',)


translator.register(Message, MessageTranslationOptions)
