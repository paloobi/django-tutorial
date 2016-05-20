from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  output = ', '.join([q.question_text for q in latest_question_list])
  return HttpResponse("<h1>Latest 5 Questions</h1>" + output)

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  return HttpResponse("You're looking at the results for question %s." % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

