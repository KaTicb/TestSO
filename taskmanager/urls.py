from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from.views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/auth/register/employee', EmployeeRegisterAPI.as_view(), name='register_employee'),
    path('api/auth/login/employee', EmployeeLoginAPI.as_view(), name='login_employee'),

    path('api/auth/register/customer', CustomerRegisterAPI.as_view(), name='register_customer'),

    path('api/task', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task_list'),
    # path('api/task/<int:pk>', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
    #      name='task_detail'),
]
