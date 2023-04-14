from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db import OperationalError
from .models import Student
import json


def myDecorator(func):
    def swapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            response = {
                'status': 'fail',
                'message': 'Database error'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            response = {
                'status': 'fail',
                'message': 'Student not found!'
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Unknow error'
            }
            return Response(response, status=status.HTTP_200_OK)      
    return  swapper      
            
            
class StudentView(APIView):
    parser_classes = [JSONParser]
    
    @myDecorator
    def post(self, request):
        student_data = json.loads(request.body)
        student = Student(name = student_data['name'],  age = student_data['age'], gender = student_data['gender'])
        student.save()
        response = {
            'status': 'success',
            'message': 'Student added successfully!',
            'student_id': student.id
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    @myDecorator
    def get(self, request):
        student_id = request.GET.get('id')
        student = Student.objects.get(id = student_id, FlagDel = False)
            
        response = {
            'id' : student.id,
            'name' : student.name,
            'age' : student.age,
           'gender' : student.gender
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
    @myDecorator
    def put(self, request):
        student_data = json.loads(request.body)
        student_id = student_data['id']
        student = Student.objects.get(id = student_id, FlagDel = False)
        student.name = student_data['name']
        student.age = student_data['age']
        student.gender = student_data['gender']
        student.FlagDel = False
        student.save()
        response = {
        'status': 'success',
        'message': 'Student information updated successfully!'
        }
        return Response(response, status=status.HTTP_200_OK)  
    
    
    @myDecorator
    def delete(self, request):
        student_id = request.GET.get('id') 
        student = Student.objects.get(id = student_id, FlagDel = False)
        student.FlagDel = True
        student.save()
        response = {
        'status': 'success',
        'message': 'Delte student successfully!'
        }
        return Response(response, status=status.HTTP_200_OK)
            
