from django.db.models.query_utils import RegisterLookupMixin
from django.http import request
from django.shortcuts import redirect, render
from .models import Master, User, Note
import random

default_data = {
    'app_name': 'My StikyNote'
}

# default page
def index(request):
    return render(request, 'index.html', default_data)

# register page
def register_page(request):
    return render(request, 'register_page.html', default_data)

# profile data
def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    sticky_note_list = Note.objects.filter(User=user)

    default_data['profile_data'] = user
    default_data['sticky_notes'] = sticky_note_list[::-1]
    default_data['total_notes'] = len(sticky_note_list)

# profile page
def profile_page(request):
    profile_data(request)
    return render(request, 'profile_page.html', default_data)

# update profile
def update_profile(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)

        user.FullName = request.POST['fullname']
        user.Mobile = request.POST['mobile']
        user.Address = request.POST['address']
        user.Country = request.POST['country']
        user.State = request.POST['state']
        user.Pin = request.POST['pin']

        user.save()

        return redirect(profile_page)
    else:
        return redirect(profile_page)

# otp generate
def create_otp(request):
    otp = random.randint(1000, 9999)
    print('Your OTP is: ', otp)
    request.session['otp'] = otp

# otp page
def otp_page(request):
    return render(request, 'otp_page.html', default_data)

# note page
def note_page(request):
    profile_data(request)
    return render(request, 'notes.html', default_data)

# create new note
def create_note(request):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)
    
    if request.method == 'POST':
        Note.objects.create(
            User = user,
            Title = request.POST['title'],
            Content = request.POST['content'],
        )

        return redirect(note_page)
    else:
        pass

# edit note
def edit_note(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)
    
    if request.method == 'POST':
        note = Note.objects.get(id = pk)

        note.Title = request.POST['title']
        note.Content = request.POST['content']

        note.save()

        return redirect(note_page)
    else:
        pass

# delete note
def delete_note(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    note = Note.objects.get(id=pk, User=user)

    note.delete()

    return redirect(note_page)

# verify otp
def verify_otp(reqeust):
    if reqeust.method == 'POST':
        if int(reqeust.POST['otp']) == reqeust.session['otp']:
            master = Master.objects.get(Email = reqeust.session['email'])
            master.IsActive = True
            master.save()

            User.objects.create(Master=master)
            default_data['msg'] = "Your account has activated successfully."
            return redirect(register_page)
        else:
            default_data['msg'] = "Your OTP does'nt matched."
            return redirect(otp_page)
    else:
        return redirect(register_page)

# registration functionality
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        master = Master.objects.create(Email=email, Password=password)

        request.session['email'] = email
        default_data['msg'] = f"OTP sent to {email}."

        create_otp(request)
        return redirect(otp_page)
    else:
        return redirect(register_page)

# login page
def login_page(request):
    return render(request, 'login_page.html', default_data)

# login functionality
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print(email, password)

        try:
            master = Master.objects.get(Email=email, Password=password)
            request.session['email'] = master.Email

            return redirect(profile_page)

        except Master.DoesNotExist as err:
            print('Error: ', err)

            return redirect(login_page)

        
    else:
        return redirect(login_page)

# logout functionality
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)