from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

from shop.models import Products
from blog.models import News

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Products, ProductTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(News, NewsTranslationOptions)

