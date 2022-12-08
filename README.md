# Outlier Monitor
Detecção de consumo atípico

Não foi implementado a detecção de outliers
Na linha 24 do client.py foi limitado aos 200 primeiros usuários
o calculo total de consumo devido a demora para se calcular todos
os usuários. 

# Como rodar o projeto

- Clone o repositório
- Faça o build dos container
- Inicie os containers

```
git clone https://github.com/AdrianoCasimiro/outlier_monitor.git
docker-compose build
docker-compose up
```


# Documentação da API

http://localhost:8000/swagger/
