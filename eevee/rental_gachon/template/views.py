from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse


from django.contrib.auth.models import User
from django.shortcuts import redirect


def index(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'index.html')
    return render(request, 'index.html', {"login_id": email})



def login(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'login_form.html')
    return render(request, 'login_form.html', {"login_id": email})


def logout(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'login_form.html')
    return render(request, 'logout_form.html', {"login_id": email})


def logout_process(request):
    del request.session['login_id']
    return render(request, 'index.html')


def check_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                request.session['login_id'] = email
                return render(request, 'index.html', {"login_id": email})
            else:
                status = "Password가 틀렸습니다"
                return render(request, 'login_form.html', {"status": status })
        except User.DoesNotExist:
            status = "존재하지 않는 아이디입니다."
            return render(request, 'login_form.html', {"status": status})



def user_registration_process(request):
    if request.method == 'POST':

        email = request.POST["email"]
        try:
            User.objects.get(username=email)
            status = "이미 존재하는 아이디입니다"
            return render(request, 'login_form.html', {"status": status})
        except User.DoesNotExist:
            user_name = request.POST["user_name"]
            nickname = request.POST["nickname"]
            password = request.POST["password"]
            student_number = request.POST["student_number"]
            new_user = User.objects.create_user(email, email, password)
            new_user.nickname = nickname
            new_user.user_name = user_name
            new_user.student_number = student_number
            new_user.save()
            request.session['login_id'] = email
            return render(request, 'index.html', {"login_id": email})


def status(request):
    if request.method == 'GET':
        print("Hello world!")


