# Teste Celero 

O projeto fornece uma api REST para interagir com alguns dados das olimpíadas de 1986 a 2016;

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