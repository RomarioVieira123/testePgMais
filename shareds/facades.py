import json
from django.utils.datetime_safe import datetime
from core.settings import DATE_FORMAT, LIMIT_HOUR, LIMIT_MESSAGE, LIMIT_CHAR_DDD, LIMIT_DIG_CELULAR
from shareds.blacklist import BlackList
from shareds.models import Stat
from telephone_operator.models import TelephoneOperator
from message.facade import MessageFacade


class ValidationFacade:

    def validate(self, request):
        blacklist = BlackList()

        # Carrega a BlackList(Todos os dados são carregados de uma só vez para evitar de quando existir uma lista grande, seja feitas várias requisiçoes perdendo desempenho a aplicação.)
        blacklistnumbers = blacklist.tochange()

        data_isnotvalid = []
        data_isvalid = []

        # Percorre a lista de mensagens validando cada mensagem de acordo com as regras especificadas no TESTE.
        for message in request.data:
            operator = TelephoneOperator.objects.filter(operator=message['operadora']).first()
            if operator is not None:
                isvalid = True

                # REGRAS
                # Números que estão na blacklist devem ser bloqueadas.
                for numberblacklist in blacklistnumbers:
                    if numberblacklist['phone'] == message['celular']:
                        if numberblacklist['active']:
                            data_isnotvalid.append(json.dumps(message))
                            isvalid = False
                            break

                # Mensagens para SP devem ser bloqueadas.
                if isvalid:
                    stat = Stat.objects.filter(ddd=message['ddd']).first()
                    if stat is not None:
                        if stat.uf == "SP":
                            data_isnotvalid.append(json.dumps(message))
                            isvalid = False

                # Mensagens com agendamento após as 19:59:59 devem ser bloqueadas.
                if isvalid:
                    if datetime.strptime(message['horario_envio'], DATE_FORMAT) > datetime.strptime(LIMIT_HOUR,
                                                                                                    DATE_FORMAT):
                        data_isnotvalid.append(json.dumps(message))
                        isvalid = False

                    # Mensagens com mais de 140 caracteres devem ser bloqueadas.
                    if len(message['mensagem']) > LIMIT_MESSAGE:
                        data_isnotvalid.append(json.dumps(message))
                        isvalid = False

                # DDD com mais de 2 dígitos ou menos de 2 dígitos ou DDD não for válido deve ser bloqueada.(Válido se estiver cadastrado no banco de dados.)
                if isvalid:
                    if len(message['ddd']) > LIMIT_CHAR_DDD or len(message['ddd']) < LIMIT_CHAR_DDD:
                        data_isnotvalid.append(json.dumps(message))
                        isvalid = False
                    else:
                        stat = Stat.objects.filter(ddd=message['ddd']).first()
                        if stat is None:
                            data_isnotvalid.append(json.dumps(message))
                            isvalid = False

                # Número de celular deve conter 9 dígitos.
                if isvalid:
                    if len(message['celular']) > LIMIT_DIG_CELULAR or len(message['celular']) < LIMIT_DIG_CELULAR:
                        data_isnotvalid.append(json.dumps(message))
                        isvalid = False

                # O 1º dígito do número do celular deve começar com 9 e o 2º dígito deve ser maior que 6.
                if isvalid:
                    indice = 0
                    for dig in message['celular']:
                        indice += 1
                        if indice == 1:
                            if int(dig) != 9:
                                data_isnotvalid.append(json.dumps(message))
                                isvalid = False
                                break
                        if indice == 2:
                            if int(dig) < 6:
                                data_isnotvalid.append(json.dumps(message))
                                isvalid = False
                                break
                            break

                if isvalid:
                    data_isvalid.append(json.dumps(message))

        # Caso mais de uma mensagem para o mesmo destino,a mensagem com maior horário deve ser bloqueada.
        # A verificação de mensagens para o mesmo destino, ocorre somente na lista de mensagens válidas, pois caso uma msg 1 com horário superior a msg 2 for bloqueada e a msg 2 ser classificada
        # como inválida pelas outras regras, as 2 mensagens serão bloqueadas ou seja, a msg 1 apesar de ser válida foi bloqueada por uma msg 2 com menor horário mas inválida pelas outras regras.
        for datavalid in data_isvalid:
            data = json.loads(datavalid)
            blocked_message = None
            for destiny in data_isvalid:
                data2 = json.loads(destiny)
                if data['ddd'] == data2['ddd'] and data['celular'] == data2['celular']:
                    if datetime.strptime(data['horario_envio'], DATE_FORMAT) > datetime.strptime(data2['horario_envio'],  DATE_FORMAT):
                        blocked_message = data

            if blocked_message is not None:
                data_isnotvalid.append(json.dumps(blocked_message))
                data_isvalid.remove(json.dumps(blocked_message))

        # Salvo as mensagens válidas no banco de dados retornando em json somente o id_broker e id_mensagem para a mensagem enviada e válida.
        message = MessageFacade()
        retorno = []
        for data in data_isvalid:
            data = json.loads(data)
            retorno.append(message.create(data))

        return retorno


class GenerateFacade:

    def generate_json_return(self, messages):
        retorno = []
        for data in messages:
            body = {
                'idmensagem': data['idmensagem'],
                'idbroker': data['operator']['broker']
            }

            retorno.append(body)

        return retorno
