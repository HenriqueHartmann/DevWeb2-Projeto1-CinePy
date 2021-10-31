from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.response import Response
from core.models import Genre

import json

@method_decorator(csrf_exempt, name="dispatch")
class GenreView(View):
    def get(self, request, id=None):
        if id:
            qs = Genre.objects.get(id=id)
            data = {
                "id": qs.id,
                "name": qs.name
            }
            return JsonResponse(data)
        else:
            data = list(Genre.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")
            
    def post(self, request):
        json_data = json.loads(request.body)
        new_genre = Genre.objects.create(**json_data)
        data = { "id": new_genre.id, "name": new_genre.name }
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Genre.objects.get(id=id)
        qs.name = json_data["name"] # if "name" in json_data else qs.name
        qs.save()
        data = {
            "id": qs.id,
            "name": qs.name
        }
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Genre.objects.get(id=id)
        qs.delete()
        data = {
            "message": "Item deleted successfully"
        }
        return JsonResponse(data)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get(self, request, id):
        genre = get_object_or_404(Genre.objects.all(), id=id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        genre = get_object_or_404(Genre.objects.all(), id=id)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        genre = get_object_or_404(Genre.objects.all(), id=id)
        genre.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class GenreListGeneric(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
