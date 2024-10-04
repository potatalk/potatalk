from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM


class InformationView(View):
    def get(self, request):
        return render(request, 'information/joo-information.html')

class MessageView(View):
    def get(self, request):
        return render(request, 'message/joo-message.html')
