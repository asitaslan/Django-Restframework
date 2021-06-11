from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haber.models import Makale
from haber.api.serializers import MakaleSerializer

@api_view('GET')
def makale_list_create_api_view(request):
    
    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif= True)
        serializer = MakaleSerializer(makaleler)

        return Response(serializer.data)