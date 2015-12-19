# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
from django.views.generic import FormView, TemplateView
from words.words import get_good_words

__author__ = 'igor'



class WordForm(TemplateView):
    template_name = "word_form.html"

    def get(self, request, **kwargs):
        return self.render_to_response({})

    def post(self, request, **kwargs):
        if "word" in request.POST:
            word = request.POST["word"]
            word = word.lower()
            word = word.encode('utf-8')
            length = int(request.POST["length"]) if "length" in request.POST and len(request.POST["length"])>0 else 0
            words_list = get_good_words(word, length)
            print len(words_list)
            return self.render_to_response({"words_list":words_list, "word":word, "length":length})
        else:
            return self.render_to_response({})