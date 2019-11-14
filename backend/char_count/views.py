from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def char_count(request):
    text = request.GET.get("text", "")

    return JsonResponse({"count": len(text)})