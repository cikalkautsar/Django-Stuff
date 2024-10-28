# myApp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myApp/home.html')  # Menampilkan halaman Home

def education(request):
    return render(request, 'myApp/education.html')  # Menampilkan halaman Pendidikan

def workexperience(request):
    return render(request, 'myApp/workexperience.html')  # Menampilkan halaman Pengalaman Kerja

def socialmedia(request):
    return render(request, 'myApp/socialmedia.html')  # Menampilkan halaman Sosial Media
