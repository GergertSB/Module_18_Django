from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_templ(request):
    return render(request, 'second_task/func_template.html')

def index(request):
    title = 'Мой сайт'
    text = ' My text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'second_task/func_template.html', context)

class Сlas_templ(TemplateView):
    template_name = 'second_task/class_template.html'