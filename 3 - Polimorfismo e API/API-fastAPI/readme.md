Criar uma virtual env
1 - Criar o ambiente virtual: python -m venv api_fastAPI
2 - Ativar o ambiente virtual: .\api_fastAPI\Scripts\activate
4 - rodar o servidor: uvicorn main:app --reload
5 - desligar o servidor: deactivate

- Gerar requisitos ```pip freeze > requirements.txt```
- Executar o projeto em outra máquina ```pip install -r  requirements.txt```