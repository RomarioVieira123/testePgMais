import json
from django.test import TestCase, Client

from broker.models import Broker
from shareds.facades import ValidationFacade
from shareds.models import Stat
from telephone_operator.models import TelephoneOperator


class Request():

    def __init__(self, data):
        self.data = data

    def setData(self, data):
        self.data = data


class ValidateMessageTestCase(TestCase):

    client = Client()
    validated = ValidationFacade()
    url = '/api/message/'

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

    def test_rules_validated(self):
        data = [{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "34", "celular": "996958849", "operadora": "vivo", "horario_envio": "17:24:03", "mensagem": "ola mundo"}]
        request = Request(data=data)
        response = self.validated.validate(request)
        self.assertEqual(json.dumps(response), json.dumps([{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 1}}]))

    def test_rules_invalid(self):
        data = [{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "00", "celular": "996958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem": "ola mundo"}]
        request = Request(data=data)
        response = self.validated.validate(request)
        self.assertEqual(json.dumps(response), json.dumps([]))
