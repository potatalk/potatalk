from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


# 메인 화면 접근
class MainView(View):
    def get(self, request):
        return render(request, 'main/main.html')