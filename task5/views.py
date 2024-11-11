from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister


users = ['User1', 'User2', 'User3', 'User4', 'UrbanUser']


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        # получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # проверяем данные
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html',{'message':f'{username}, ваши данные успешно приняты!'})
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # проверяем данные
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, f'{username}, ваши данные успешно приняты!')
        else:
            info['form'] = form
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

