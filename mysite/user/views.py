from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User
from .validators import contains_special_character, contains_uppercase_letter, contains_lowercase_letter, contains_number
# Create your views here.

#####로그인#####
def signin(request):
    if request.method == 'GET':
        user = request.user.is_authenticated 
        if user:
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html')
        
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        #이메일, 패스워드 빈칸
        if email == '' or password == '':
            return render(request, 'user/account/signin.html', {'error':'이메일 혹은 패스워드를 입력해주세요.'})
        
        #없는 이메일로 로그인 할 경우 에러 
        exist_user =auth.get_user_model().objects.filter(email=email)
        if exist_user:
            pass
        else:
            return render(request, 'user/account/signin.html', {'error':'이메일 혹은 패스워드를 확인 해주세요.'})
                
        #권한 부여
        username = User.objects.get(email=email)
        user = auth.authenticate(request, username=username, password=password) 
        if user is not None:  
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/account/signin.html', {'error':'이메일 혹은 패스워드를 확인 해주세요.'})
        
#####회원가입#####
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
        repeatpassword = request.POST.get('repeatpassword', '')
        
        if password != repeatpassword:
            return render(request, 'user/account/signup.html', {'error': '패스워드를 확인 해 주세요.'})
        else:
            if email == '' or username == '' :
                return render(request, 'user/account/signup.html', {'error': '이메일과 사용자 이름은 적어주셔야 합니다.'})
            
            if contains_special_character(username) :
                return render(request, 'user/account/signup.html', {'error': '사용자 이름에 특수문자를 포함할 수 없습니다.'})
            
            email_exist_user = auth.get_user_model().objects.filter(email=email)
            username_exist_user = auth.get_user_model().objects.filter(username=username)
            
            if email_exist_user or username_exist_user :
                return render(request, 'user/account/signup.html', {'error': '이메일 또는 사용자이름이 이미 존재합니다. '})
            
            if ( len(password) < 8 or len(password) > 17 
                or not contains_uppercase_letter(password)
                or not contains_lowercase_letter(password)
                or not contains_number(password) 
                or not contains_special_character(password) 
            ):
                return render(request, 'user/account/signup.html', {'error':'비밀번호는 8자 이상 16자이하의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.' })

            else:
                User.objects.create_user(email=email, username=username, password=password)
                return redirect('/account/signin/')

#####로그아웃#####
@login_required(login_url='user:signin')
def logout(request):
    auth.logout(request)
    return redirect('/account/signin/')