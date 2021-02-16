# Teste Celero 

O projeto fornece uma api REST para interagir com alguns dados das olimpíadas de 1986 a 2016;

## Projeto hospedado

https://testcelero.herokuapp.com/
## Executando o projeto localmente

1. Primeiro, certifique-se de ter o `PostgreSQL` instalado e executando, em seguida, crie um banco de dados com o nome `celero_db`, com o owner `celero`, e password `celero`, apenas para testar localmente.

Exemplo:
```
psql -d postgres 
postgres=# CREATE ROLE celero WITH SUPERUSER LOGIN PASSWORD 'celero';
postgres=# CREATE DATABASE celero_db OWNER celero;
```

2. Em seguida, execute os seguintes comandos para clonar o repositório e executar localmente (certifique-se de ter os pacotes `pip` e `pipenv` instalados e configurados corretamente): 
- `git clone https://github.com/flakesrc/test_django_csv.git`
- `cd test_django_csv`
- `pipenv shell`
- `pipenv install`
- `./manage.py migrate` ou `python3 manage.py migrate`

Agora, você pode servir o projeto para testar se está funcionando:
- `./manage.py runserver` ou `python3 manage.py runserver`

## Populando o banco de dados a partir do arquivo csv

Agora, vamos inserir os dados do arquivo csv baixado do Kaggle (https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv)

1. Certifique-se de que o ambiente virtual está ativo (ativado com o comando `pipenv shell`)
2. Execute o seguinte comando: `python3 populate.py`, você verá mensagens sobre o progresso de 
inserção dos dados no banco.
3. Quando terminar, você verá uma mensagem como: 
```
População concluída. Total de registros: 271116

Duração: 0:00:46
```
4. Você também pode confirmar o total de registros diretamente do banco de dados. Exemplo:
```
celero_db=# SELECT COUNT(*) FROM olympic_game;
 count  
--------
 271116
(1 row)
```

## Interagindo com a API 

Você pode simplesmente navegar pela API pelo navegador (não recomendado) após servir o projeto, mas
neste exemplo, irei mostrar como interagir utilizando a biblioteca CLI `httpie` 

1. Instale a biblioteca com o `pip`: `pip install httpie --user` ou globalmente: `sudo pip install httpie`
2. Execute o comando para executar o `httpie` e testar se está funcionando:
```https httpie.io/hello```, você verá uma mensagem contendo "Thank you for trying out HTTPie" no final do resultado
3. Utilizando o método get: `http http://localhost:8000/games/` (certifique-se de que o projeto está sendo servido localmente e está na porta `8000`), o resultado será algo como:
```
{
            "athlete": [
                {
                    "age": 28,
                    "height": 175,
                    "name": "Paavo Johannes Aaltonen",
                    "noc": "FIN",
                    "sex": "M",
                    "team": "Finland",
                    "url": "http://localhost:8000/athletes/17/",
                    "weight": 64.0
                }
            ],
            "city": "Helsinki",
            "event": "Gymnastics Men's Individual All-Around",
            "id": 51,
            "medal": null,
            "name": "1952 Summer",
            "season": "Summer",
            "sport": "Gymnastics",
            "url": "http://localhost:8000/games/51/",
            "year": 1952
        }
```
4. Criando uma instância dos modelos com o método `POST`:
- Criando um atleta:
```
http POST http://localhost:8000/athletes/ \
name="Marcos Souza" sex="M" age=24 height=167 weight=70 team=Brazil noc=BR >
```

Em seguida, você recebera algo como:
```
HTTP/1.1 201 Created
# ...
{
    "age": 24,
    "height": 167,
    "id": 271117,
    "name": "Marcos Souza",
    "noc": "BR",
    "sex": "M",
    "team": "Brazil",
    "url": "http://localhost:8000/athletes/271117/",
    "weight": 70.0
}
```

Vamos lembrar o `271117` e usa-lo para relacionar na instância de um jogo olímpico. 

- Criando uma instância de Game: 
```
http POST http://localhost:8000/games/ \
name="Gambi 2021" year=2021 season="Summer" city="Rio de Janeiro" sport="Gambi"  \
event="Gambi Maker and eXtreme Go Horse Master" medal="Gold" athlete:="[271117]"
```

5. Deletando uma instância
- Exemplo: `http DELETE http://localhost:8000/athletes/271117/`

Se deletado com sucesso, irá retornar:
```
HTTP/1.1 204 No Content
```

## Notas

Algumas notas e observações sobre o teste e o processo de criação do projeto

1. Depois de popular o banco de dados e tentar inserir algum novo registro, o Django poderá 
levantar um erro de integridade, e pelo que li no google até o momento, isso parece ser algum "BUG", pois nada no código
justifica esse erro. Quando ocorreu localmente, eu simplesmente deletei os arquivos de migrações do app olympic
(havia diversos) e criei
uma nova migração para gerar um único arquivo

2. O arquivo requirements.txt é para caso você deseje usar o pip diretamente, e não seguir o passo a passo do README

3. populate_sem_bulk.py foi o primeiro código que funcionava, depois dele pesquisei sobre como otimizar, o que 
me levou ao bulk

4. o campo athlete_id_ref tanto de Games como Athletes é para "sincronizar" uma mesma referência e 
saber qual instância de Game pertence a qual instância de Athlete, pois após o loop for que gera as instâncias
para o bulk, essa mesma referencia seria perdida, e não teria como saber o que pertence ao que. 
E eu precisei disso para gerar o último bulk de atualização dos campos relacionados, porque sem isso,
o código ficaria misto entre full bulk e uma query para cada instância, e estava levando cerca de 7 minutos para popular, 
e após deixar "full bulk", demorou cerca de 44 segundos a 1 minuto e 20 segundos para popular localmente.

5. Um erro meu: por falta de costume, acabei utilizando somente uma branch para todo o trabalho, a branch `dev`,
tenho conhecimentos em sepração de branches utilizando o git flow, mas acabei não usando. As mensagens de commits talvez
não soem muito claras em alguns commits, e por causa do formatador (que as vezes simplesmente adicionava um espaço
no final de um arquivo), as vezes a mensagem de alteração de um arquivo acabou indo para 2, já que o espaço em branco no final do arquivo modificava ele.

6. Como todos sabemos, SECRET_KEY não deve ser upada no repositório, mas deixei no código por praticidade,
e para caso de deploy, será utilizada uma nova SECRET_KEY