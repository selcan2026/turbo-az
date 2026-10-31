from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Car


def home(request):
    cars = Car.objects.all().order_by('-tarix')

    marka = request.GET.get('marka')
    model = request.GET.get('model')
    min_qiymet = request.GET.get('min_qiymet')
    max_qiymet = request.GET.get('max_qiymet')
    il = request.GET.get('il')

    if marka:
        cars = cars.filter(marka__iexact=marka)

    if model:
        cars = cars.filter(model__icontains=model)

    if min_qiymet:
        cars = cars.filter(qiymet__gte=min_qiymet)

    if max_qiymet:
        cars = cars.filter(qiymet__lte=max_qiymet)

    if il:
        cars = cars.filter(il=il)

    return render(request, 'cars/home.html', {'cars': cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/detail.html', {'car': car})


@login_required(login_url='login')
def add_car(request):

    if request.method == 'POST':

        Car.objects.create(
            istifadeci=request.user,
            marka=request.POST.get('marka'),
            model=request.POST.get('model'),
            il=request.POST.get('il'),
            qiymet=request.POST.get('qiymet'),
            muherrik=request.POST.get('muherrik'),
            yurus=request.POST.get('yurus'),
            shekil=request.FILES.get('shekil'),
        )

        messages.success(request, 'Elan uğurla yerləşdirildi!')

        return redirect('home')

    return render(request, 'cars/add_car.html')


@login_required(login_url='login')
def my_cars(request):

    cars = Car.objects.filter(
        istifadeci=request.user
    ).order_by('-tarix')

    return render(request, 'cars/my_cars.html', {
        'cars': cars
    })


@login_required(login_url='login')
def delete_car(request, id):

    car = get_object_or_404(
        Car,
        id=id,
        istifadeci=request.user
    )

    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Elan silindi!')
        return redirect('my_cars')

    return render(request, 'cars/delete_car.html', {
        'car': car
    })


@login_required(login_url='login')
def edit_car(request, id):

    car = get_object_or_404(
        Car,
        id=id,
        istifadeci=request.user
    )

    if request.method == 'POST':

        car.marka = request.POST.get('marka')
        car.model = request.POST.get('model')
        car.il = request.POST.get('il')
        car.qiymet = request.POST.get('qiymet')
        car.muherrik = request.POST.get('muherrik')
        car.yurus = request.POST.get('yurus')

        if request.FILES.get('shekil'):
            car.shekil = request.FILES.get('shekil')

        car.save()

        messages.success(request, 'Elan yeniləndi!')

        return redirect('my_cars')

    return render(request, 'cars/edit_car.html', {
        'car': car
    })


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'cars/register.html', {
        'form': form
    })


def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            login(request, form.get_user())

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'cars/login.html', {
        'form': form
    })


def user_logout(request):

    logout(request)

    return redirect('home')
