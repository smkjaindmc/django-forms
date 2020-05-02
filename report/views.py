from django.shortcuts import render, redirect
from .forms import Form
from .models import Data

def test(request):

    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            data = Data(name = form.cleaned_data['name'] ,reports = form.cleaned_data['reports'], hours =  form.cleaned_data['hours'] , today_progress = form.cleaned_data['today_progress'], today_doc = form.cleaned_data['today_doc'] , concern = form.cleaned_data['concern'], next_plan = form.cleaned_data['next_plan'], next_doc = form.cleaned_data['next_doc'])
            data.save()
            return redirect('submit/')

    else:
        form = Form()
    
    context = {'form' : form}
    return render(request, 'test.html', context)

    

def submit(request):
    result = Data.objects.all()
    l = len(result)
    res = result[l-1]
    context = {
        'result' : result,
        'len' : l
    }
    return render(request, 'submit.html', context)
