from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator

# Create your views here.


QUESTIONS = [
    {
        "id": i,
        "title": f"Question {i}",
        "text": f"This is question number {i}"
    } for i in range(30)
]

def index(request):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, 7)
    page_obj = paginator.page(page_num)
    
    return render(request, "index.html", {"questions": page_obj, "num_pages": paginator.num_pages})

def hot(request):
    questions = QUESTIONS[5:]
    return render(request, "hot.html", {"questions": questions})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, "question_detail.html", {"question": item})