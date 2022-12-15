from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('login', views.login),
    path('signup', views.signup),
    path('ShowProduct/<id>',views.ShowProduct),
    path('ViewDetails/<id>',views.ViewDetails),
    path('signout',views.signout),
    path('addToCart',views.addToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('MakePayment',views.MakePayment),
]