from django.urls import path
from .views import create_note, delete_note, edit_note, index, login, logout, note_page, profile_page, register_page, login_page, register, otp_page, update_profile, verify_otp

urlpatterns = [
    path('', index),
    path('register_page/', register_page, name='register_page'),
    path('register/', register, name='register'),

    path('otp_page/', otp_page, name='otp_page'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    
    path('login_page/', login_page, name='login_page'),
    path('login/', login, name='login'),
    path('profile_page/', profile_page, name='profile_page'),
    path('update_profile/', update_profile, name='update_profile'),

    path('logout/', logout, name='logout'),
    path('note_page/', note_page, name='note_page'),
    path('new_note/', create_note, name='new_note'),
    path('edit_note/<int:pk>/', edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', delete_note, name='delete_note'),
]