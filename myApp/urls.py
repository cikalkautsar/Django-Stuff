from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # URL untuk halaman utama
    path('education/', views.education, name='education'), # URL untuk halaman pendidikan
    path('workexperience/', views.workexperience, name='workexperience'), # URL untuk pengalaman kerja
    path('socialmedia/', views.socialmedia, name='socialmedia'), # URL untuk media sosial
]
