from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.http import *
from numpy import append
from OTS.models import Question, User
import random
# Create your views here.
def createAdmin():
    user=User()
    user.username='admin'
    user.password='admin'
    user.role='ADMIN'
    user.realname='Super User'
    user.save()
def testresult(request):
    total_attempt=0
    total_right=0
    total_wrong=0
    qno_list=[]
    for k in request.POST:
        if k.startswith("qno"):
            qno_list.append(int(request.POST[k]))
    for n in qno_list:
        question=Question.objects.get(qno=n)
        try:
            if question.answer == request.POST['q'+str(n)]:
                total_right+=1
            else:
                total_wrong+=1
            total_attempt+=1
        except:
            pass
    d={'total_attempt':total_attempt,'total_right':total_right,'total_wrong':total_wrong}
    res=render(request,'testresult.html',d)
    return res
def starttest(request):
    no_of_que=5
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    questions_list=question_pool[:no_of_que]
    res=render(request,'starttest.html',{'questions':questions_list})
    return res
def home(request):
    res=render(request,'home.html')
    return res
def main(request):
    try:
        realname=request.session['realname']
    except KeyError:
        return HttpResponseRedirect('http://localhost:8000/OTS/login/')
    res=render(request,'main.html',{'realname':realname})
    return res
def signup(request):
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']='Username Already Taken'
    except:
        d1['errmsg']=''
    res=render(request,'signup.html',d1)
    return res 
def saveuser(request):
    user=User()
    u=User.objects.filter(username=request.POST['username'])
    if not u:
        user.username=request.POST['username']
        user.realname=request.POST['realname']
        user.password=request.POST['password']
        user.role="LEARNER"
        user.save()
        urls='http://localhost:8000/OTS/login/'
    else:
        urls="http://localhost:8000/OTS/signup?error=1"
    return  HttpResponseRedirect(urls)
def login(request):
    user=User.objects.filter(username="admin")
    if not user:
        createAdmin()
    res=render(request,'login.html')
    return res
def loginvalidation(request):
    try:
        u=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        request.session['username']=u.username
        request.session['realname']=u.realname
        request.session['role']=u.role
        url='http://localhost:8000/OTS/main/'
    except:
        url='http://localhost:8000/OTS/login/'
    return  HttpResponseRedirect(url)
def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/OTS/login/')
def newQuestion(request):
    res=render(request,'new_question.html')
    return res
def saveQuestion(request):
    question=Question()
    question.que=request.POST['question']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/viewQuestion/')
def viewQuestion(request):
    question=Question.objects.all()
    res=render(request,'view_question.html',{'questions':question})
    return res
def editQuestion (request):
    qno=request.GET['qno']
    question=Question.objects.get(qno=qno)
    res=render(request,'edit_question.html',{'question':question})
    return res
def editsaveQuestion (request):
    question=Question()
    question.qno=request.POST['qno']
    question.que=request.POST['question']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/viewQuestion/')   
def deleteQuestion(request):
    qno=request.GET['qno']
    question=Question.objects.get(qno=qno)
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/OTS/viewQuestion/')   