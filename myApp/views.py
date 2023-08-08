from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Programmers
from myApp.forms import programForm

# Create your views here.


def myform(request):
    return render(request, 'forms.html')


def view_data(request):
    prog_data = Programmers.objects.all().values()
    return render(request, 'viewdata.html', {'prog_data': prog_data})


def store_data(request):
    if request.method == "POST":
        form = programForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/myApp/view')
            except:
                pass
    else:
        form = programForm()
    return render(request, '/myApp/myform')


def updatedata(request, rollno):
    data = Programmers.objects.get(Prog_Roll_no=rollno)
    return render(request, 'updatedata.html', {'data': data})


def updaterecord(request, rollno):
    data = Programmers.objects.get(Prog_Roll_no=rollno)
    form = programForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect("/myApp/view")
    return render(request, 'updatedata.html', {'data': data})


def delete_data(request, rollno):
    data = Programmers.objects.get(Prog_Roll_no=rollno)
    data.delete()
    return redirect('/myApp/view')
