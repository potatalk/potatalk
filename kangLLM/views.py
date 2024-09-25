from django.shortcuts import render
from django.views import View


class KangLLMView(View):
    def get(self,request):
        print(request)
        return render(request, 'message/kangLLM.html')