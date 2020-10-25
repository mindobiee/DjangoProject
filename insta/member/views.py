
from django.shortcuts import render
# Create your views here.

from .forms import UserCreateForm  # UserCreateForm를 import한다.
from django.contrib.auth.models import User  # User 모델을 import한다.

# Django 내부에 구현된 authenticate(유저인증_
# login(해당하는 유저 객체를 session에 담기),
# logout(유저객체 session에서 제거) import하기
from django.contrib.auth import authenticate, login, logout
# Django 내부에 구현된 AuthenticationForm import하기
from django.contrib.auth.forms import AuthenticationForm


# urls.py에 정의한 path와 매칭되는 메소드를 views.py에서 정의


def create_user(request):
    if request.method == 'POST':  # 요청이 POST형식이면 if문안의 내용실행
        try:  # objects.create_user 메소드에서 이미 "User"가 존재 할 경우의 예외 처리를 위한 try문
            # 파라미터를 받아서 변수에 담기
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']

            # User를 생성한다. 이때 기존에 User가 존재하는 등의 예외처리 상황이 나올 수 있음
            new_user = User.objects.create_user(username, email, password)
            # 생성된 유저를 DB에 저장한다.
            new_user.save()
            # 회원가입이 완료되었다면 메시지와 함께 결과 화면 페이지로 이동시킨다
            return render(request, 'registration/signup_done.html', {'message': '회원가입이 완료됨'})

        except:
            # 예외처리 발생 상황시 메시지와 함께 결과 화면 페이지로 이동시킨다
            return render(request, 'registration/signup_done.html', {'message': '회원이 이미 있음'})
    else:  # 요청이 POST 방식이 아닐 경우 회원가입 페이지로 이동한다.
            # UserCreateForm을 form 변수에 담는다.
        form = UserCreateForm()
        # 회원가입 페이지로 폼의 데이터와 함께 이동한다.
        return render(request, 'registration/signup.html', {'form': form})



# urls.py에서 선언한 path에 매칭되는 logout메소드를 작성
def sign_out(request):
    logout(request) # Django 내부에 logout 로직이 구현되어 있어 불러다 쓰기만 하면 된다.
    # return HttpResponse(status=200)
    return render(request, 'home/base.html')


# urls.py에서 선언한 path에 매칭되는 login메소드를 작성
def sign_in(request):
    if request.method == 'POST': # 요청이 POST라면 조건문 안이 실행된다.
        # username과 password를 확인하여 해당 User객체를 user변수에 담기
        user = authenticate(request, username=request.POST.get('username',''), password=request.POST.get('password',''))
        if user is not None:
            login(request, user) # Django 내부에 login 로직이 구현되어 있어 불러다 쓰기만 하면된다.
        return render(request, 'registration/login.html', {'message': "로그인 되었습니다."})
    else: # 요청이 GET이라면 else안이 실행된다.
        form = AuthenticationForm() # Django에서 지원하는 로그인 form
        return render(request, 'registration/login.html', {'form': form})
