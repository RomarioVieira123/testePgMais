import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from message.models import Message
from message.serializers import MessageSerializer
from shareds.facades import ValidationFacade, GenerateFacade


class MessageView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({'Page': 'Not found'}, status=status.HTTP_400_OK)

    def post(self, request):
        validation = ValidationFacade()
        generate = GenerateFacade()

        #Envia a request com as mensagens para serem validadas.
        messages = validation.validate(request)
        #Ao receber o retorno das mensagens validadas, é enviada as mensagens para geração da estrutura de acordo com a solicitação do TESTE.
        retorno = generate.generate_json_return(messages)

        return Response({"retorno": retorno})

