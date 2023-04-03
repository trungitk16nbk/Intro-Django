from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_http_method import HttpMethodMixin 
from django.db import OperationalError
from .models import Student
import json

class StudentView(HttpMethodMixin, View):
    def post(self, request):
        try:
            student_data = json.loads(request.body)
            student = Student(name = student_data['name'],  age = student_data['age'], gender = student_data['gender'])
            student.save()
            response = {
                'status': 'success',
                'message': 'Student added successfully!',
                'student_id': student.id
            }
            return JsonResponse(response)
        except OperationalError:
            response = {
                'status': 'fail',
                'message': 'Database error'
            }
            return JsonResponse(response)
        except Student.DoesNotExist:
            response = {
                'status': 'fail',
                'message': 'Student not found!'
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Unknow error'
            }
            return JsonResponse(response)        
        pass
    
    
    def get(self, request):
        try: 
            student_id = request.GET.get('id')
            student = Student.objects.get(id = student_id, FlagDel = False)
            
            Student_data = {
                'id' : student.id,
                'name' : student.name,
                'age' : student.age,
                'gender' : student.gender
            }
            return JsonResponse(Student_data, safe=False)
        except OperationalError:
            response = {
                'status': 'fail',
                'message': 'Database error'
            }
            return JsonResponse(response)
        
        except Student.DoesNotExist:
            response = {
                'status': 'fail',
                'message': 'Student not found!'
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Unknow error'
            }
            return JsonResponse(response)
        pass
    
    def put(self, request):
        try:
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
            return JsonResponse(response)
        except OperationalError:
            response = {
                'status': 'fail',
                'message': 'Database error'
            }
            return JsonResponse(response)
        except Student.DoesNotExist:
            response = {
                'status': 'fail',
                'message': 'Student not found!'
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Unknow error'
            }
            return JsonResponse(response)        
        pass
    def delete(self, request):
        try:
            student_id = request.GET.get('id') 
            student = Student.objects.get(id = student_id, FlagDel = False)
            student.FlagDel = True
            student.save()
            response = {
            'status': 'success',
            'message': 'Delte student successfully!'
            }
            return JsonResponse(response)
            
        except OperationalError:
            response = {
                'status': 'fail',
                'message': 'Database error'
            }
            return JsonResponse(response)
        
        except Student.DoesNotExist:
            response = {
                'status': 'fail',
                'message': 'Student not found!'
            }
            return JsonResponse(response)
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Unknow error'
            }
            return JsonResponse(response)
        pass