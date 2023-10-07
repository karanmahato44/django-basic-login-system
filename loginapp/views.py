from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse

from .models import Contact


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login_user'))

    labels = []
    rizz_data = []

    queryset = Contact.objects.order_by('-rizz')
    for contact in queryset:
        labels.append(contact.name)
        rizz_data.append(contact.rizz)

    return render(request, 'index.html', {'labels': labels, 'rizz_data': rizz_data})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rizz = request.POST.get('rizz')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'rizz': rizz,
            'message': message,
        }

        contact = Contact(name=name, email=email, rizz=rizz, message=message)
        contact.save()
        messages.success(request, 'added new contact')
        return render(request, 'contacts.html', {'data': data})

    return redirect(reverse('index'))


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'login successful. welcome back!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'login failed. please check your credentials.')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect(reverse('login_user'))
