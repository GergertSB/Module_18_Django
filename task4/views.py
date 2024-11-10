from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fourth_task/main_page.html')

def index1(request):
    game = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'game': game,
    }
    return render(request, 'fourth_task/shop_page.html', context)

def index2(request):
    return render(request, 'fourth_task/cart_page.html')

def index3(request):
    return render(request, 'fourth_task/menu.html')