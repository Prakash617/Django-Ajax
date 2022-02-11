
from ast import Try
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class HomeView(View):
    def get(self, request, *args ,**kwargs):
        context ={
            'name' :'prakash'
        }
        return render(request, 'home.html', context)
    
class AllArticlesView(View):
    def get(self, request, *args ,**kwargs):
        context ={
            'allarticles' :Article.objects.all().order_by('-id')
        }
        return render(request, 'allarticle.html', context)
    
class CreateArticlesView(View):
    def post(self, request, *args ,**kwargs):
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print('title:',title,'description: ', desc)
        
        try:
            
            Article.objects.create(title = title, desc =desc)
            resp = {
                
                'status' : 'success',
            }
            
        except Exception as e:
            print(e)
            resp = {
            
            'status' : 'fail',
        }
        
        return  JsonResponse(resp)