from django.urls import path
from . import views
from .views import CategoryView, CategoryTitle, ProductDetail, CustomerRegistrationView, ProfileView, AddressView, UpdateAddress
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("category/<slug:val>/", CategoryView.as_view(), name="category"),
    path("category-title/<val>/", CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('updateAddress/<int:pk>/', UpdateAddress.as_view(), name='updateAddress'),
    path('address/', AddressView.as_view(), name='address'),
    
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.show_cart, name='checkout'),  # Should be separate view if checkout differs

    
    # Authentication
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordChangedone'), name='passwordchange'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordChangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordChangedone.html'), name='passwordChangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
