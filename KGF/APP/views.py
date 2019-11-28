from django.shortcuts import render
from APP import forms
#from django.http import HttpResponseRedirect

# create your views her


def Thank_View(request):
    return render(request, 'Bye.html')


def Emp_View(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'Bye.html')
    else:
        form = forms.EmpForm()
    return render(request, 'Register.html', {'form': form})

