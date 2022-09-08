
## Tecnologias
* Python 3.9.0
* [Fast API](https://fastapi.tiangolo.com/)
* [uvicorn[standard]](https://www.uvicorn.org/)

### Criar uma virtual env
1. Criar o ambiente virtual: ```python -m venv api_fastAPI```

2. Ativar o ambiente virtual: ```.\api_fastAPI\Scripts\activate```

3. Instalar o uvicorn: ```pip install "uvicorn[standard]"```

4. Executar o servidor: ```uvicorn main:app --reload```
5. Desligar o servidor: ```deactivate```

### Executar o projeto em outra máquina

Dentro da virtual env, executar o comando: ```pip install -r  requirements.txt```