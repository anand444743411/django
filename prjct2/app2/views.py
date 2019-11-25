
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
    #from django.contrib.auth.models import Details
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import RegistrationForm
from .models import Details
# from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():#
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phonenumber = request.POST.get('phonenumber')
            gender = request.POST.get('gender')
            city = request.POST.get('city')
            password = request.POST.get('password')
            # password1 = request.POST.get('password1')
            user = Details.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                             phonenumber=phonenumber, gender=gender, city=city, password=password)
            user.save()
            return render(request, 'auth/created.html', {'form': form})

        else:
            return render(request, 'auth/signup.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'auth/signup.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(Details.objects.filter(username = username ).exists()):
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse('employee_list'))
                return render(request, 'employee/details.html', {'user': user})
            else:
               return render(request, "auth/login.html")
        else:
            messages.error(request,"Provide valid credentials")
            return render(request, "auth/login.html")
    else:
        return render(request,"auth/login.html")


@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url="/login/")
def employee_list(request):
    context = {}
    context['users'] = Details.objects.all()
    context['title'] = 'Employees'
    return render(request, 'employee/details.html', context)


@login_required(login_url="/login/")
def employee_details(request, id=None):
    context = {}
    context['title'] = 'Employees'
    context['user'] = get_object_or_404(Details, id=id)
    return render(request, 'employee/details.html', context)


# @login_required(login_url="/login/")
def employee_add(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', {"user_form": user_form})
    else:
        user_form = RegistrationForm()
        return render(request, 'employee/add.html', {"user_form": user_form})


@login_required(login_url="/login/")
def employee_edit(request, id=None):
    user = get_object_or_404(Details, id=id)
    if request.method == 'POST':
        # user_form = Registrationform(request.POST, instance=user)
        # if user_form.is_valid():
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.city=request.POST.get('city')
        user.save()
            # return HttpResponseRedirect(reverse('employee_details'))
        return render(request, 'employee/details.html', {"user": user})
        # else:
        #     messages.error(request, "Form is not valid")
        #     return render(request, 'employee/edit.html', {"user": user})
    else:
        user_form = RegistrationForm(instance=user)
        return render(request, 'employee/edit.html', {"user_form": user_form})

@login_required(login_url="/login/")
def employee_delete(request, id=None):
    user = get_object_or_404(Details, id=id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,'employee/details.html', {'form':form})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'employee/change_password.html', {'form': form})

