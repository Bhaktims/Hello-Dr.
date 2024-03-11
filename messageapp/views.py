
from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Message


# Create your views here.

def test(request):
    return HttpResponse("test is done")

def create(request):
    # print("Request is :",request.method)
    if request.method == "GET":
    #  print("In if section")
        return render(request,'create.html')
    else:
        #fetch data from the form
        n =  request.POST['uname']
        e =  request.POST['uemail']
        m =  request.POST['umob']
        d = request.POST['udt']
        ms = request.POST['msg']
        #print(n,e,m,d,ms)
        #Validation
        # insert records
        x = Message.objects.create(name=n,email=e,mobile=m,date=d,msg=ms)
        x.save()
        return redirect('/')

def dashboard(request):
    x = Message.objects.all()
    #print(x)
    context ={}
    context['data'] = x
    return render(request,'dashboard.html',context)

def delete(request,rid):
    x = Message.objects.filter(id=rid)
    print(x)
    x.delete()
    return redirect('/dashboard')

def edit(request,rid):

    if request.method=="GET":
        m = Message.objects.filter(id=rid)
        context={}
        context["data"]=m
        return render(request,'edit.html',context)
    else:
        n =  request.POST['uname']
        e =  request.POST['uemail']
        m =  request.POST['umob']
        d = request.POST['udt']
        ms = request.POST['msg']
        x = Message.objects.filter(id=rid)
        x.update(name=n,email=e,mobile=m,date=d,msg=ms)
        return redirect('/')
    
def home(request):
    
    return render(request,'home.html')
    