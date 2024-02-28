from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# TODO : 경로를 backend.account.serializers 로 지정할 때 모듈을 찾을 수 없는 버그 발생
from .serializers import AccountRegisterSerializer, AccountTokenObtainPairSerializer


class AccountRegisterAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny, )
    serializer_class = AccountRegisterSerializer


class AccountTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = AccountTokenObtainPairSerializer
