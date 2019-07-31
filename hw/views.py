from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from hw.models import Student,Blog
from django.utils import timezone

# Create your views here.
def firstPage(request):
    return render(request,'firstPage.html')


def ppt(request,student_name):
    students = Student.objects.filter(name=student_name).first()
    return render(request,'ppt.html', {'student':students})

def report(request,student_name):
    students = Student.objects.filter(name=student_name).first()
    return render(request,'ppt.html',{'student':students})

def signup(request):
    if request.method =='POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error': "이미 사용하고 있는 이름입니다."})
            
            except User.DoesNotExist:

                user = User.objects.create_user(
                    request.POST['username'],password=request.POST['password1']
                )

                student=Student()
                student.name = request.POST['username']


                student.subject11 = request.POST['mon1']
                student.subject12 = request.POST['tue1']
                student.subject13 = request.POST['wed1']
                student.subject14 = request.POST['thu1']
                student.subject15 = request.POST['fri1']
                
                student.subject21 = request.POST['mon2']
                student.subject22 = request.POST['tue2']
                student.subject23 = request.POST['wed2']
                student.subject24 = request.POST['thu2']
                student.subject25 = request.POST['fri2']
                
                student.subject31 = request.POST['mon3']
                student.subject32 = request.POST['tue3']
                student.subject33 = request.POST['wed3']
                student.subject34 = request.POST['thu3']
                student.subject35 = request.POST['fri3']

                student.subject41 = request.POST['mon4']
                student.subject42 = request.POST['tue4']
                student.subject43 = request.POST['wed4']
                student.subject44 = request.POST['thu4']
                student.subject45 = request.POST['fri4']

                student.subject51 = request.POST['mon5']
                student.subject52 = request.POST['tue5']
                student.subject53 = request.POST['wed5']
                student.subject54 = request.POST['thu5']
                student.subject55 = request.POST['fri5']

                student.subject61 = request.POST['mon6']
                student.subject62 = request.POST['tue6']
                student.subject63 = request.POST['wed6']
                student.subject64 = request.POST['thu6']
                student.subject65 = request.POST['fri6']

                student.subject71 = request.POST['mon6']
                student.subject72 = request.POST['tue7']
                student.subject73 = request.POST['wed7']
                student.subject74 = request.POST['thu7']
                student.subject75 = request.POST['fri7']


                student.save()
                auth.login(request,user)#로그인상태로 바꿈
                return render(request,'home.html',{'student':student})

    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            students = Student.objects.filter(name=username).first()
            return render(request,'home.html',{'student':students})
        else:
            return render(request,'login.html', {'error': "아이디나 비밀번호를 확인해 주세요"})

    return render(request,'login.html')

def home(request, student_name):
    students = Student.objects.filter(name=student_name).first()
    return render(request, 'home.html', {'student':students})

def detail(request, student_name, blog_id):
    students = Student.objects.filter(name=student_name).first()
    blog_detail = get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'detail.html', {'student':students, 'blog':blog_detail})
    
def create(request, student_name):
    students = Student.objects.filter(name=student_name).first()

    blog = Blog() # 객체 틀 하나 가져오기
    blog.title = request.GET['title']  # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 객체 저장하기

    # 새로운 글 url 주소로 이동
    return render(request, 'qna.html', {'student':students})

def new(request, student_name):
    students = Student.objects.filter(name=student_name).first()
    return render(request, 'new.html', {'student':students})

def edit(request,student_name,blog_id):
    students = Student.objects.filter(name=student_name).first()
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'edit.html', {'student':students, 'blog':blog})

def update(request,student_name,blog_id):
    students = Student.objects.filter(name=student_name).first()
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.title = request.GET['title'] # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 저장하기

    # 새로운 글 url 주소로 이동
    return render(request, 'qna.html', {'student':students})

def delete(request, student_name, blog_id):
    students = Student.objects.filter(name=student_name).first()
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.delete()
    return render(request, 'qna.html', {'student':students})

def qna(request, student_name):
    blogs=Blog.objects.all().order_by('-id')
    students = Student.objects.filter(name=student_name).first()
    return render(request, 'qna.html', {'student':students , 'blogs':blogs })