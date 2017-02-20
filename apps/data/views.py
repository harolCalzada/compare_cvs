# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob as tb
from .tfidf import tfidf
from .models import Curriculum
from .utils import clean_word


def home(request):
    print ('hola mundo')
    curriculums = Curriculum.objects.all()

    bloblist = [tb(curriculum.algoritmo_texto) for curriculum in curriculums]
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

    return render(request, 'home.html', locals())


def clean(request):
    curriculums = Curriculum.objects.all()[:5]
    clean_list = [clean_word(curriculum.algoritmo_texto) for curriculum in curriculums]
    for i, list in enumerate(clean_list):
        print("Words in documents {0}::::::::::::::".format(i + 1))
        print(list)

    return render(request, 'clean.html', locals())







