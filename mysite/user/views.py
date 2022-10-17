from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User
from .validators import contains_special_character, contains_uppercase_letter, contains_lowercase_letter, contains_number
# Create your views here.

def index(request):
    return render(request, 'user/account/index.html')

def signin(request):
    if request.method == 'GET':
        user = request.user.is_authenticated #bool값으로 True냐 False냐...
        if user:
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html')
        
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        username = User.objects.get(email=email)
        password = request.POST.get('password', '')
        me = auth.authenticate(request, username=username, password=password) 
        #authenticate를 오버라이딩해서 username을 email로 받을 수 있게 하는 방법이 있다! (정석 루트)
        if me is not None:  
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html', {'error':'이메일 혹은 패스워드를 확인 해주세요.'})
    
def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/account/signup.html')
    elif request.method == "POST":
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        
        if password != password2:
            return render(request, 'user/account/signup.html', {'error': '패스워드를 확인 해 주세요.'})
        else:
            if ( len(password) < 8 or len(password) > 17 
                or not contains_uppercase_letter(password)
                or not contains_lowercase_letter(password)
                or not contains_number(password) 
                or not contains_special_character(password) 
            ):
                return render(request, 'user/account/signup.html', {'error':'비밀번호는 8자 이상 16자이하의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.' })
            
            if email == '' or username == '' :
                return render(request, 'user/account/signup.html', {'error': '이메일과 사용자 이름은 적어주셔야 합니다.'})

            if contains_special_character(username) :
                return render(request, 'user/account/signup.html', {'error': '사용자 이름에 특수문자를 포함할 수 없습니다.'})
            
            email_exist_user = User.objects.filter(email=email)
            username_exist_user = User.objects.filter(username=username)
            
            if email_exist_user or username_exist_user :
                return render(request, 'user/account/signup.html', {'error': '이메일 또는 사용자이름이 이미 존재합니다. '})

            else:
                User.objects.create_user(email=email, username=username, password=password)
                return redirect('/account/signin/')

@login_required(login_url='user:signin')
def logout(request):
    auth.logout(request)
    return redirect('/account/signin/')