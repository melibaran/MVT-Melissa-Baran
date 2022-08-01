from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Familiares
from django.template import loader
# Create your views here.

def hermano(self):
    hermano = Familiares(nombre='Ariel', apellido= 'Baran', tipo= 'hermano', edad='20', cumpleanos='2002-03-09')
    diccionario = {'hermano': hermano}
    template = loader.get_template('hermano.html')
    doc = template.render(diccionario)
    
    
    return HttpResponse(doc)

def hermana(self):
    hermana = Familiares(nombre='Vanesa', apellido= 'Baran', tipo= 'hermana', edad='30', cumpleanos='1992-06-10')    
    diccionario = {'hermana': hermana}
    template = loader.get_template('hermana.html')
    doc = template.render(diccionario)
    
    return HttpResponse(doc)
    
def sobrina(self):
    
    padre = Familiares(nombre='Pascual', apellido= 'Baran', tipo= 'padre', edad='62', cumpleanos='1960-09-12')
    diccionario = {'padre': padre}
    template = loader.get_template('padre.html')
    doc = template.render(diccionario)
    
    return HttpResponse(doc)    
    