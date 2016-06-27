from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.db import connection




def index(request):

    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    row = cursor.fetchone()
  
 # palabra= "El usuario es: "+row.get

    return HttpResponse(row)


    #return HttpResponse("Index del proyecto. Juli sos el rey.")

    #return render(request, 'home/index.html', {})
