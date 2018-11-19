from django.contrib.auth.views import ( 
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView,)
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
# from django.urls import path
from collection import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('cheeses/<slug>/', views.cheese_detail, name='cheese_detail'),
    path('cheeses/<slug>/edit', views.edit_cheese, name='edit_cheese'),
#     path('accounts/password/reset/', password_reset,
# {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
# path('accounts/password/reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
	path('accounts/password/reset/done/', PasswordResetView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
	path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
	path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name="password_reset_complete"),
	path('accounts/', include('registration.backends.simple.urls')),
	path('admin/', admin.site.urls), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
