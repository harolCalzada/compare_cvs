
from django.shortcuts import render
from django.http import HttpResponse
from nltk.tokenize import word_tokenize
from .models import Curriculum
from .tfidf import tfidf


def home(request):
    curriculums = Curriculum.objects.all()
    tokenized_curriculums = [word_tokenize(curriculum.algoritmo_texto) for curriculum in curriculums]
    for i, curriculum in enumerate(tokenized_curriculums):
        print ("Top words in document {}".format(i+1))
        scores = {word: tfidf(word, curriculum, tokenized_curriculums) for word in curriculum}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
    return render(request, 'home.html', locals())


# def restaurante_list(request):
#     print ('restaurante list api')
#     serializer = None
#     result = {'status': 'error'}
#     time.sleep(5)
#     if request.method == 'GET':
#         restaurantes = Restaurante.objects.all()
#         serializer = RestaurantSerializer(restaurantes, many=True)
#         result = {'status': 'success', 'data': serializer.data}
#     return JSONResponse(result)


# def restaurante_detail(request, id):
#     print ('restaurante detail')
#     serializer = None
#     result = {'status': 'error'}
#     if request.method == 'GET':
#         restaurante = Restaurante.objects.filter(id=id)
#         if restaurante:
#             serializer = RestaurantSerializer(restaurante[0])
#             result = {'status': 'success', 'data': serializer.data}
#     print ('result ', result)
#     return JSONResponse(result)
