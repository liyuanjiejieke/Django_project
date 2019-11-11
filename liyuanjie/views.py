from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def index(request):
    # 获取前端post过来的用户名和密码
    name= request.POST.get("name",None)
    password= request.POST.get("password",None)
    # 吧用户名和密码组装成字典
    data = {'name':name,'password':password}
    list.append(data)


    return render(request,'hello.html',{'form':list})
