from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # this inbuilt views is used for login 
from .forms import LoginForm
urlpatterns = [
   
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('profile/', views.profile, name='profile'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',
    authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #(3) showing image and upload in webpage dynemicaly adding this configurations 
