from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'third_task/main_page.html')

def index1(request):
    game1 = 'Atomic Heart'
    game2 = ' Cyberpunk 2077'
    game3 = ' PayDay 2'
    context = {
        'g1': game1,
        'g2': game2,
        'g3': game3,
    }
    return render(request, 'third_task/shop_page.html', context)

def index2(request):
    return render(request, 'third_task/cart_page.html')