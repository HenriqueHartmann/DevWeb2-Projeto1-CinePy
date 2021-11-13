from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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
