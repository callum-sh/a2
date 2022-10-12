from datetime import date, datetime
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def front(request):
    context = {}

    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def example(request):

    if request.method == 'GET':
        ret = "Hello Joshua, how are you?"
        return Response({"data": ret, 'time': datetime.now()})
    
    elif request.method == 'POST':
        print(f"POST request data: {request.data}.")
        return Response(status=status.HTTP_200_OK, data={"data": f"received: {request.data}", "time": datetime.now()})