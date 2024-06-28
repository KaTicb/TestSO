from rest_framework import serializers
from .models import Task, Employee, Customer
from django.contrib.auth import authenticate


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        pass


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['password']


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)
        return user


class EmployeeLoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['password']


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user


class CustomerLoginSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
