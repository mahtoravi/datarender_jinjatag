from django.shortcuts import render

# Create your views here.
data ="this data is assumption"
dname="ravi"
d ={'assumption':data,"name":dname,"a":10,"b":20,"c":30}
def data_render(request):
    return render (request,'data_render.html',context=d)
def login(request):
    return render(request,'login.html',context=d)