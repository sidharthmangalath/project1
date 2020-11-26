from django.urls import path
from.import views
urlpatterns=[
    path('home',views.firstfunction),
    path('customer',views.customer),
    path('form',views.displayform),
    path('formvalid',views.formvalidation),
    path('cricket',views.playerstatics),
    path('api/',views.DetailStudent.as_view()),
    path('<int:pk>/',views.DetailStudent1.as_view())


]
