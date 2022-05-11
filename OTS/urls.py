from OTS.views import *
from django.urls import path
urlpatterns = [
    path('newQuestion/',newQuestion),
    path('viewQuestion/',viewQuestion),
    path('saveQuestion/',saveQuestion),
    path('editQuestion/',editQuestion),
    path('editsaveQuestion/',editsaveQuestion),
    path('deleteQuestion/',deleteQuestion),
    path('signup/',signup),
    path('saveuser/',saveuser),
    path('login/',login),
    path('logout/',logout),
    path('',home),
    path('main/',main),
    path('loginvalidation/',loginvalidation),
    path('starttest/',starttest),
    path('testresult/',testresult),


]