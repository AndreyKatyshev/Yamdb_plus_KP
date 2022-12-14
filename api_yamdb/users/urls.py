from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SignupView, TokenView, UserViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

# auth_urls = [
#     path('signup/', SignupView.as_view()),
#     path('token/', TokenView.as_view())
# ]

auth = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/auth/', include(auth_urls)),
    path('v2/', include(auth)),
]
