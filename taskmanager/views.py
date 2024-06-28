from .models import Task
from .serializers import *
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(employee=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class CustomerRegisterAPI(generics.GenericAPIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'user': CustomerSerializer(user, context=self.get_serializer_context()).data,
                         'token': get_tokens_for_user(user)}, status=201)


class EmployeeRegisterAPI(generics.GenericAPIView):
    serializer_class = EmployeeRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'user': EmployeeSerializer(user, context=self.get_serializer_context()).data,
                         'token': get_tokens_for_user(user)}, status=201)


class EmployeeLoginAPI(generics.GenericAPIView):
    serializer_class = EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({'user': EmployeeSerializer(user, context=self.get_serializer_context()).data,
                         'token': get_tokens_for_user(user)}, status=200)
