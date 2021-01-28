from django.shortcuts import render,HttpResponseRedirect
from userinfo.models import userinfo
from userinfo.forms import dataForm

# Create your views here.

# This Function Will Add New Person And Show Details Of Persons
def home(request):
    if request.method == "POST":
        userObj = dataForm(request.POST)
        if userObj.is_valid():
            name = userObj.cleaned_data['name']
            email = userObj.cleaned_data['email']
            password = userObj.cleaned_data['password']
            data = userinfo(name=name,email=email,password=password)
            data.save()
            userObj = dataForm()
    else:
        userObj = dataForm()
    userd = userinfo.objects.all()
    return render(request,"userinfo/add_show.html",{'form':userObj,"data":userd})

# This function will  Edit/Update data
def update(request,id):
    if request.method == "POST":
        details = userinfo.objects.get(pk=id)
        updateObj = dataForm(request.POST,instance=details)
        if updateObj.is_valid():
            updateObj.save()
            return HttpResponseRedirect('/')
    else:
        details = userinfo.objects.get(pk=id)
        updateObj = dataForm(instance=details)
    return render(request,"userinfo/update_data.html",{'update_d':updateObj})


# This function  will Delet data
def delete(request,id):
    print(id)
    if request.method == "POST":
        personObj = userinfo.objects.get(pk=id)
        personObj.delete()
        return HttpResponseRedirect('/')