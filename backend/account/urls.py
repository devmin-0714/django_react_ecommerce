from django.urls import path


from rest_framework_simplejwt.views import TokenRefreshView as AccountTokenRefreshAPIView

# TODO : 경로를 backend.account.views 로 지정할 때 모듈을 찾을 수 없는 버그 발생
from .views import AccountRegisterAPIView, AccountTokenObtainPairAPIView

urlpatterns = [
    path('register/', AccountRegisterAPIView.as_view(), name='register'),
    path('token/', AccountTokenObtainPairAPIView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', AccountTokenRefreshAPIView.as_view(), name='token_refresh'),
]
