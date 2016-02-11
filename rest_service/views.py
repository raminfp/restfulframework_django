from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_service.serializers import SaminSerializer
from rest_service.models import Samin


@api_view(['GET', 'POST'])
def api_select(request):

    """
    List all model, or create a new list.
    """

    if request.method == 'GET':
        tasks = Samin.objects.all()
        serializer = SaminSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SaminSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def api_del(request, pk):

    try:
        task = Samin.objects.get(pk=pk)
    except Samin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def api_up(request, pk):

    try:
        getdata = Samin.objects.get(pk=pk)
    except Samin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = SaminSerializer(getdata, data=request.POST.dict())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

