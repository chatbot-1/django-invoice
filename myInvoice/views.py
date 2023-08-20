from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# from .forms import *

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username!!')
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid/Incorrect Username or Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('/')


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('/login/')

    return render(request, 'signup.html')


def delete_provider(request, id):
    queryset = Provider.objects.get(id=id)
    queryset.delete()
    return redirect('addService')

def update_provider(request, id):
    queryset = Provider.objects.get(id = id)

    if request.method == 'POST':
        client_id = request.POST.get('client')
        client = Client.objects.get(id = client_id)
        comp_name = request.POST.get('company')
        handle = request.POST.get('handle')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        account = request.POST.get('account')
        ifsc = request.POST.get('ifsc')

        queryset.client = client
        queryset.comp_name = comp_name
        queryset.handle = handle
        queryset.email = email
        queryset.phone = phone
        queryset.address = address
        queryset.account = account
        queryset.ifsc = ifsc

        queryset.save()
        return redirect('addService')
    context = {'prov': queryset, 'clients': Client.objects.all()}
    return render(request, 'updateProvider.html', context)


def service(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        client = Client.objects.get(id=client_id)
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')

        user = Service.objects.create(
            client=client,
            description=description,
            quantity=quantity,
            amount=amount,
        )
        user.save()
        return redirect('service')
    return render(request, 'service.html', {'clients': Client.objects.all()})

def provider(request):
    provideObj = Provider.objects.all()
    if request.method == 'POST':
        client_id = request.POST.get('client')
        client = Client.objects.get(id = client_id)
        comp_name = request.POST.get('company')
        handle = request.POST.get('handle')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        account = request.POST.get('account')
        ifsc = request.POST.get('ifsc')

        user = Provider.objects.create(
            client = client,
            comp_name = comp_name,
            handle = handle,
            email = email,
            phone = phone,
            address = address,
            account = account,
            ifsc = ifsc
        )
        user.save()
        return redirect('addService')
    return render(request, 'addService.html', {'clients':Client.objects.all(), 'providerObj':provideObj})

def client(request):
    if request.method == 'POST':
        comp_name = request.POST.get('comp_name')
        gst = request.POST.get('gst')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address = request.POST.get('address')

        user = Client.objects.create(
            comp_name=comp_name,
            gst=gst,
            country=country,
            state=state,
            address=address,
        )
        user.save()
        return redirect('client')

    return render(request, 'client.html')