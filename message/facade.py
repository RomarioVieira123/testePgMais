from message.models import Message
from message.serializers import MessageSerializer
from shareds.models import Stat
from telephone_operator.models import TelephoneOperator


class MessageFacade:

    def create(self, data):
        db = DataBase()
        serializer = MessageSerializer(db.save(data))

        return serializer.data


class DataBase:
    def save(self, data):
        operator = TelephoneOperator.objects.filter(operator=data['operadora']).first()
        stat = Stat.objects.filter(ddd=data['ddd']).first()
        message = Message.objects.create(
            idmensagem=data['idmensagem'],
            operator=operator,
            stat=stat,
            message=data['mensagem'],
            destination_number=data['celular'],
            shipping_time=data['horario_envio']
        )

        return message
