import json

import requests
from django.test import TestCase, Client
from rest_framework import request

from broker.models import Broker
from shareds.models import Stat
from telephone_operator.models import TelephoneOperator
from shareds.facades import ValidationFacade


class ValidateMessageCase(TestCase):

    def setUp(self):
        TelephoneOperator.objects.create(operator="vivo", broker_id=1)
        TelephoneOperator.objects.create(operator="tim", broker_id=1)
        TelephoneOperator.objects.create(operator="claro", broker_id=2)
        TelephoneOperator.objects.create(operator="oi", broker_id=2)
        TelephoneOperator.objects.create(operator="nextel", broker_id=3)
        Stat.objects.create(name="São Paulo", uf="SP", ddd=11)
        Stat.objects.create(name="São Paulo", uf="SP", ddd=12)
        Stat.objects.create(name="Rondônia", uf="RO", ddd=69)
        Stat.objects.create(name="Minas Gerais", uf="MG", ddd=34)
        Stat.objects.create(name="Paraná", uf="PR", ddd=43)
        Stat.objects.create(name="Rio de Janeiro", uf="RJ", ddd=21)
        Stat.objects.create(name="Paraná", uf="PR", ddd=42)
        Broker.objects.create(name="romario")
        Broker.objects.create(name="tiago")
        Broker.objects.create(name="vanessa")

        #Mensagem válida.
        self.data = {"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "996958849", "operadora": "vivo", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}
        #Mensagem DDD inválido.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "00", "celular": "996958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        #Mensagem com qnt de caracteres inválido.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "996958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}')
        # Mensagem celular inválido(Primeiro dígito < 9).
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "896958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem celular inválido(Segundo dígito < 6).
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "992958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem DDD com mais de 2 dígitos.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "345", "celular": "996958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem DDD com menos de 2 dígitos
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "3", "celular": "999958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem com celular na blacklist.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "68904994120", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem com celular na blacklist.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "68904994120", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem com para o estado de SP.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "999958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem com agendamento após 20:00:00
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "999958849", "operadora": "tim", "horario_envio": "20:00:00", "mensagem":  "ola mundo"}')
        # Mensagem com celular acima de 9 dígitos.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "9999588490", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')
        # Mensagem com celular abaixo de 9 dígitos.
        #self.data = json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "99995884", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}')

    def test_validate_message(self):
        client = Client()
        url = '/api/message/'
        response = client.post(url, self.data)
        #retorno = validation.validate(self.messages)
        self.assertEqual(response.json(), {"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 1}})
