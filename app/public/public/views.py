from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    question_list = [{"id": "23489y23894t2987", "text": "What was the best CPU you owned?"},
		     {"id": "23489y23894t2988", "text": "How often you had to change CPU?"}]
    context = {'question_list': question_list}
    return render(request, 'public/index.html', context)
