def inserir_recordes(nome_db='app/storage.db', nome_tabela='marciano'):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {nome_tabela}(
                id integer primary key autoincrement not null,
                nome varchar(30) not null,
                vitorias integer,
                empates integer,
                derrotas integer, 
                total integer,
                media integer)""")
            cursor.execute(f"""
                insert into {nome_tabela}(nome, vitorias, empates, derrotas, total, media)
                values(?, ?, ?, ?, ?, ?)""",
                            ('fdsa', '2', '1', '0', '0', '0'))
        conexao.commit()


def consulta_dados(nome_db='app/storage.db', nome_tabela='marciano'):
    import sqlite3
    from contextlib import closing

    with sqlite3.connect(nome_db) as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(f"select * from {nome_tabela}")
            resultado = cursor.fetchall()
            return resultado

inserir_recordes()
print(consulta_dados())
