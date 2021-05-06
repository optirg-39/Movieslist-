from django.shortcuts import render, HttpResponseRedirect
from .models import Movies, Genres, Collection
from django.contrib.auth.models import User
from .serializers import MoviesSerializer, CollectionSerializer, GenresSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
# Create your views here.
class Collection_Get_APIView(APIView):
    def get(self, request, format =None):
        user = request.user

        coll = Collection.objects.filter(user=user)
        moll = Movies.objects.filter(collection__user = user)

class CollectionAPI(APIView):
    def get(self, request, uuid=None, format =None):
        if not uuid:
            return HttpResponseRedirect('http://127.0.0.1:8000/collection_GET/')
        user = request.user
        coll = Collection.objects.get(uuid=uuid)
        ser = CollectionSerializer(coll)
        sera= ser.data
        return Response({'data2':sera})



    def post(self, request, format =None):
        data = request.body
        data_py = json.loads(data)
        user = User.objects.get(username = 'admin')
        # user =User.objects.get(request.user)
        # user = request.user
        # print(user)
        title = data_py['title']
        description = data_py['description']
        coll = Collection(title=title, user=user, description = description)
        coll.save()
        movies = data_py['movies']
        serializer = MoviesSerializer(data=movies, many=True)
        if serializer.is_valid():
            serializer.save()
            for movie in movies:
                mov_inst = Movies.objects.get(uuid = movie['uuid'])
                str = movie['genres'].split(",")
                for gn in str:
                    genress = Genres(movie= mov_inst, genre = gn)
                    genress.save()
            return Response({"mesg":"Data created"}, status = status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



        #
        # obj_movies = Collection.objects.filter(Q(title=title) & Q(user_id=user.id)).first()
        # movies_coll = data_py['movies']
        # ser_mov = MoviesSerializer(data=movies_coll, many=True)
        # if ser_mov.is_valid():
        #     ser_mov.save()
        #     return Response({"collection_uuid": 'uuid of the collection item'})
    #
    # def put(self, request, uid, format =None):
    #     id = uid
    #     coll = Collection.objects.get(uuid = id)
    #     ser_col = Collection_sez(coll, data=request.data)
    #     if ser_col.is_valid():
    #         ser_col.save()
    #         return Response({
    #             'title': ser_col['title'],
    #             'discription': ser_col['discription'],
    #             'movies': list
    #         })
    # def delete(self, request, uid, format =None):
    #     delt = Collection.objects.get(uuid = uid)
    #     delt.delete()
    #     return Response({
    #         "Deleted": "Successfully"
    #     })
