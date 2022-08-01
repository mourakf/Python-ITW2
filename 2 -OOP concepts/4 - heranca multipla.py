class Login:
    def __init__(self):
        self.nome_da_classe = ''

    def log_in(self, message):
        print(f'mensagem da classe {self.nome_da_classe}')


class Connection:
    def __init__(self):
        self.service = ''

    def connect(self):
        print(f'Conectando ao servico {self.service}')

    # logica de conexão com o banco de dados


class MySqlDatabase(Connection, Login):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySQLDB'
        self.service = 'localhost'


def framework(item):
    if isinstance(item, Connection) and isinstance(item, Login):
        item.connect()
        item.log_in()
    else:
        print("Not connected")


conexao_sql = MySqlDatabase()
framework(conexao_sql)
