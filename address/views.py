from ast import Add
from atexit import register
from re import M
from django.shortcuts import render, redirect
from . models import AddAddress, Register
from . decorator import auth_user
from django.db.models import Q
import json


def signup(request):
    msg = ''
    if request.method == 'POST':
        reg_username = request.POST['regname']
        reg_email = request.POST['regemail']
        reg_password = request.POST['regpass']
        user_exist = Register.objects.filter(email=reg_email)
        if user_exist:
            msg = "Email already exist"
        else:
            register = Register(username=reg_username,
                                email=reg_email, password=reg_password)
            register.save()
    return render(request, 'address/signup.html', {'msg': msg, })


def login(request):
    msg = ''
    if request.method == 'POST':
        log_email = request.POST['logemail']
        log_password = request.POST['logpass']
        user_exist = Register.objects.filter(
            email=log_email, password=log_password).exists()
        if user_exist:
            user_detail = Register.objects.get(
                email=log_email, password=log_password)
            request.session['user_id'] = user_detail.id
            return redirect("address:address_book")
        else:
            msg = 'invalid email or password'

    return render(request, 'address/login.html', {'err_msg': msg, })


@auth_user
def address_book(request):
    address_book = AddAddress.objects.filter(
        user_id=request.session['user_id'])

    return render(request, 'address/address_book.html', {'address': address_book, })


@auth_user
def add_address(request):
    msg = ""
    if request.method == 'POST':

        image = request.FILES['image']
        username = request.POST['uname']
        phone = request.POST['phone']
        email_id = request.POST['email']
        place = request.POST['place']
        address = request.POST['address']
        userid = Register.objects.get(id=request.session['user_id'])
        add_address = AddAddress(user_id=userid, image=image, username=username,
                                 number=phone, email_id=email_id, place=place, address=address)
        add_address.save()
        return redirect('address:address_book')

    if request.method == 'GET':
        return render(request, 'address/add_address.html')


@auth_user
def view_address(request, id):
    view_address = AddAddress.objects.get(id=id)

    if request.method == 'POST':

        address_id = request.POST['view_id']
        address = AddAddress.objects.get(id=address_id)
        address.delete()
        return redirect('address:address_book')

    return render(request, 'address/view_address.html', {'view_address': view_address, })


@auth_user
def edit_address(request, edit_id):
    edit_address = AddAddress.objects.get(id=edit_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = edit_address.image

        username = request.POST['uname']
        phone = request.POST['phone']
        email_id = request.POST['email']
        place = request.POST['place']
        address = request.POST['address']

        edit_address.image = image
        edit_address.username = username
        edit_address.number = phone
        edit_address.email_id = email_id
        edit_address.place = place
        edit_address.address = address
        edit_address.save()

        return redirect("address:address_book")
    return render(request, 'address/edit_address.html', {'edit_address': edit_address})


@auth_user
def search(request):

    if request.method == 'GET':
        user_name = request.GET.get('search')
        status = AddAddress.objects.filter(
            Q(username__icontains=user_name) | Q(address__icontains=user_name))
        return render(request, "address/search.html", {"username": status, })

    return render(request, "address/search.html")


def logout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('address:login')


def test1(request):

    return render(request, "address/test_geo_coordinates.html")
