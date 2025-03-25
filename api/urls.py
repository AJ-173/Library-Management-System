from django.contrib import admin
from django.urls import path,include
from account_app.views import admin_signup, admin_login, admin_logout
from rest_framework.routers import DefaultRouter
from lmsapp.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
   path('signup/', admin_signup, name='admin_signup'),
    path('login/', admin_login, name='admin_login'),
    path('logout/',admin_logout, name='admin_logout'),
    path('', include(router.urls)),

]