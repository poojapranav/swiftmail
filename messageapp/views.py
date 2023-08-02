from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from messageapp.models import Msg
#import get_object_or_404
# Create your views here.
def testing(request):
    return HttpResponse("hello linked successfully")
def demoDict(request):
    my_dict={'john':70,'peter':45,'david':50}
    return render(request,'demo.html',{'m':my_dict})
def create(request):
    #print("request is:",request.method)
    if request.method=='GET':
        return render(request,'create.html')
    else:
        #fetch data from form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        # print(n)
        # print(mail)
        # print(mob)
        # print(msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        #return HttpResponse("data inserted successfully")
        return redirect('/dashboard')
def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    #return HttpResponse("data fetch from database")
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
def delete(request,rid):
    #print("id to be deleted:",rid)
    #return HttpResponse("id to be deleted:"+rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
def edit(request,rid):
    #print("id to be edited:",rid)
    #return HttpResponse("id to be edited:"+rid)
    if request.method=="GET":
        #m=Msg.objects.filter(id=rid)
        m = get_object_or_404(Msg, id=rid)
        #print(m)
        #context={}
        #context['data']=m
        return render(request,'edit.html',{'data':m})
    else:
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        k=Msg.objects.filter(id=rid).update(name=n,email=mail,mobile=mob,msg=msg)
        #k.save()
        return redirect('/dashboard')
def updatedata(request,rid):
    d=Msg.objects.get(id=rid)
    if request.method=='POST':
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        k=Msg.objects.filter(id=rid).update(name=n,email=mail,mobile=mob,msg=msg)
        return redirect('/dashboard')
    return render(request,'edit.html',{'data':d})
