from django.urls import path
from . import views
from.views import home
from.views import Cart
from.views import CheckOut
from .views import OrderNow
from.middlewares.auth import auth_middleware
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [

    # path("",views.home,name="homepage"),
    path('', home.as_view(),name="homepage"),
    path('cart/', Cart.as_view(),name="cart"),
    path('checkout/', CheckOut.as_view(),name="checkout"),
    path('orders/', auth_middleware(OrderNow.as_view()),name="orders"),
    path("payment/",views.paymentNow,name="payment"),

    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
   
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)