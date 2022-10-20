from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http  import JsonResponse
from .models import User
from .validators import contains_special_character, contains_uppercase_letter, contains_lowercase_letter, contains_number

import requests
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

#####카카오 로그인###
def kakao_social_login(request):

    if request.method == 'GET':
        kakao_id = '8d5aa745f342bec2de9e1f3be94c1f5f'
        redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback' # 인가 코드를 받을 URI
        return redirect(
            f'https://kauth.kakao.com/oauth/authorize?client_id={kakao_id}&redirect_uri={redirect_uri}&response_type=code'
        )



def kakao_social_login_callback(request):
    """
    카카오 소셜 로그인 콜백 함수
    받은 인가 코드, 애플리케이션 정보를 담아 /oath/token/에 post요청하여 접근코드를 받아 처리하는 함수
    """
    try:
        code = request.GET.get('code')
        kakao_id = '8d5aa745f342bec2de9e1f3be94c1f5f'
        redirect_uri = 'http://127.0.0.1:8000/account/login/kakao/callback' # 인가 코드가 리다이렉트된 URI
        token_request = requests.post(
            'https://kauth.kakao.com/oauth/token', {'grant_type': 'authorization_code',
                                                    'client_id': kakao_id, 'redierect_uri': redirect_uri, 'code': code}
        )
        
        token_json = token_request.json()

        error = token_json.get('error', None)

        if error is not None:
            return JsonResponse({"message": "INVALID_CODE"}, status=400)

        access_token = token_json.get("access_token")

    except KeyError:
        return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

    except access_token.DoesNotExist:
        return JsonResponse({"message": "INVALID_TOKEN"}, status=400)

        #------get kakaotalk profile info------#

    user_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"},
    )
    user_json = user_request.json()
    kakao_id = user_json.get('id')
    username = user_json['properties']['nickname']
    email = user_json['kakao_account']['email']


    if User.objects.filter(id=kakao_id).exists():
        user = User.objects.get(id=kakao_id)
        auth.login(request, user)
    else:
        User.objects.create(
            username=username,
            id=kakao_id,
            email = email
        )
        user = User.objects.get(id=kakao_id)
        auth.login(request, user)
    return redirect('/')

#####팔로우#####
@login_required(login_url='user:signin')
def user_list(request):
    if request.method == 'GET':
        user_list = User.objects.all().exclude(username=request.user.username)
        return render(request, 'user/account/user_list.html',{'user_list':user_list})

@login_required(login_url='user:signin')
def process_follow(request, user_id):
    me = request.user
    user = User.objects.get(id=user_id)
    if me in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('/user/userlist/')
