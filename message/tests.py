import json

from django.test import TestCase

from broker.models import Broker
from message.facade import MessageFacade
from shareds.models import Stat
from telephone_operator.models import TelephoneOperator


class CreateMessagesCase(TestCase):

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

    #Testar gravação da mensagem no banco de dados e o retorno do respectivo broker de acordo com a operadora.
    def test_create_message_vivo(self):
        messagefacade = MessageFacade()
        serializer = messagefacade.create(json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "996958849", "operadora": "vivo", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}'))
        self.assertEqual(json.dumps(serializer), '{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 1}}')

    def test_create_message_tim(self):
        messagefacade = MessageFacade()
        serializer = messagefacade.create(json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "996958849", "operadora": "tim", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}'))
        self.assertEqual(json.dumps(serializer), '{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 1}}')

    def test_create_message_claro(self):
        messagefacade = MessageFacade()
        serializer = messagefacade.create(json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "996958849", "operadora": "claro", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}'))
        self.assertEqual(json.dumps(serializer), '{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 2}}')

    def test_create_message_oi(self):
        messagefacade = MessageFacade()
        serializer = messagefacade.create(json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "996958849", "operadora": "oi", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}'))
        self.assertEqual(json.dumps(serializer), '{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 2}}')

    def test_create_message_nextel(self):
        messagefacade = MessageFacade()
        serializer = messagefacade.create(json.loads('{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "ddd": "12", "celular": "996958849", "operadora": "nextel", "horario_envio": "17:24:03", "mensagem":  "ola mundo"}'))
        self.assertEqual(json.dumps(serializer), '{"idmensagem": "bff58d7b-8b4a-456a-b852-5a3e000c0e63", "operator": {"broker": 3}}')