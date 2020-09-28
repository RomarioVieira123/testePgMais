<h1>INTRODUÇÃO</h1>

<body>Projeto teste criado para validar uma entrada de mensagens em formato .json e retornar as mensagens
aptas para envio e seu respectivo broker, validadas de acordo com as regras propostas. 

<body>
<h2>Índice</h2>
<ul>
    <li><a href="#estruturaprojeto">Estrutura Projeto</a>
        <ul>
            <li><a href="#appbroker">App Broker</a></li>
            <li><a href="#appmessage">App Message</a></li>
            <li><a href="#appshared">App Shareds</a></li>
            <li><a href="#apptelephoneoperator">App Telephone Operator</a></li>
            <li><a href="#projetpcore">Project Core</a></li>
        </ul>
    </li>
    <li><a href="#regras">Regras</a></li>
    <li><a href="#testeunitarios">Testes Unitários</a>
        <ul>
             <li><a href="">Gravação da Mensagem e Retorno</a></li>
             <li><a href="">Validação blackList</a></li>
             <li><a href="">Validação celular</a></li>
             <li><a href="">Validação DDD</a></li>
             <li><a href="">Validação mensagem</a></li>
        </ul>
    </li>
    <li><a href="#instrucoesteste">Instruções de Teste</a></li>
    <li><a href="#instrucoesexecucao">Instruções de Execução</a></li>
    <li><a href="#tecnologiasusadas">Tecnologias para Desenvolvimento</a>
        <ul>
            <li><a href="">Sistema Operacional</a></li>
            <li><a href="">IDE</a></li>
            <li><a href="">Frameworks</a></li>
            <li><a href="">Teste API</a></li>
        </ul>
    </li>
</ul>
<h2 id="estruturaprojeto">Estrutura do Projeto</h2>
        A estrutura do projeto está organizado em 4 apps, sendo elas broker, message, shareds, telephone_operator e o projeto core.
        A organização do banco de dados obedece o diagrama abaixo:
        <img src="Diagrama%20API%20Broker_Message.png" alt="">
        <h4 id="appbroker">App Broker</h4>
            <ol>
                <li>App responsável pelos dados do broker, sendo o idbroker, name e create_at.</li>
                <li>Sua serialização é realizada apenas retornando o idbroker.</li>
                <li>Não possui urls ou views.</li>          
            </ol>         
        <h4 id="appmessage">App Message</h4>
            <ol>
                <li>App responsável pelos dados compartilhados.</li>
                <li>Possui 3 models sendo Country, Stat e City usando apenas Stat.</li>
                <li>Não possui serialização, urls ou views.</li>
                <li>Contém o arquivo BlackList.py responsável pela conexão com a API Black List</li>
                <li></li>
            </ol>  
        <h4 id="appshared">App Shareds</h4>
             <ol>
                <li>App responsável pelos dados de mensagens, sendo o idmensagem, operator, stat, message, destination_number, shipping_time e created_at.</li>
                <li>Sua serialização é realizada apenas retornando o idmensagem e operator.</li>
                <li>Posusi a url principal de acesso da API.</li>    
                <li>Sua view possui 2 métodos sendo GET e POST.</li>
                <li>O método GET retorna HTTP 400, enquanto o método POST retorna os dados solicitados de acordo com a regra do teste, sendo somente idmensagem e idbroker.</li>
                <li>Possui a pasta fixtures onde guarda um arquivo shared.json para inicialização e população com dados fictícios no banco de dados.</li>
            </ol>  
        <h4 id="apptelephoneoperator">App Telephone Operator</h4>
             <ol>
                <li>App responsável pelos dados da operadora sendo idoperator, broker, operator e created_at.</li>
                <li>Sua serialização é realizada apenas retornando o idmensagem e operator.</li>
                <li>Posusi 2 métodos de serialização onde um retorna todos os dados e o outro retorna apenas o idbroker.</li>    
                <li>Não possui urls ou views.</li>
            </ol>  
        <h4 id="projetpcore">Projeto Core</h4>
            <ol>
                <li>Projeto do django.</li>
                <li>Seu arquivo settings.py possui todas variáveis usadas como contantes no projeto. </li>
            </ol>  
<h2 id="regras">Regras</h2>
<h2 id="testeunitarios">Teste Unitários</h2>
<h2 id="instrucoesteste">Instruções de Teste</h2>
<h2 id="instrucoesexecucao">Instruções de Execução</h2>
<h2 id="tecnologiasusadas">Tecnologias para Desenvolvimento</h2>
</body>