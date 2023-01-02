from flask import Flask, request
from flask_restx import Api, Resource, _http
from src.server.instance import server
from src.database.database import db_connection
from src.models.books import Books
# from pymysql import cursor

app, api = server.app, server.api
db = db_connection()

books_db = []


@api.route('/api/books/')
class BookList(Resource):
    def get(self):
        with db.cursor() as cursor:
            query = "SELECT * FROM `tb_livros`"
            cursor.execute(query)
            query_result = cursor.fetchall()

            books_db.clear()

            for result in query_result:
                books_db.append(result)

            return books_db, 302

    def post(self):
        response = api.payload

        book = Books(response['nome'], response['autor'], response['sinopse'], response['genero'])

        with db.cursor() as cursor:
            query = "INSERT INTO `tb_livros` (`nome`, `autor`, `sinopse`, `genero`) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (book._nome, book._autor, book._sinopse, book._genero))
            db.commit()
            return {'msg': 'Livro registrado com sucesso'}, 201

    def put(self):
        response = api.payload

        # book = Books(response['nome'], response['autor'], response['sinopse'], response['genero'])

        with db.cursor() as cursor:
            if response['autor'] == '' and response['sinopse'] == '' and response['genero'] == '':
                query = "UPDATE `tb_livros` SET `nome`=%s WHERE `id`=%s"
                cursor.execute(query, (response['nome'], response['id']))
                db.commit()
                return {"msg": "Livro atualizado com sucesso"}, 200
            elif response['nome'] == '' and response['sinopse'] == '' and response['genero'] == '':
                query = "UPDATE `tb_livros` SET `autor`=%s WHERE `id`=%s"
                cursor.execute(query, (response['autor'], response['id']))
                db.commit()
                return {"msg": "Livro atualizado com sucesso"}, 200
            elif response['nome'] == '' and response['autor'] == '' and response['genero'] == '':
                query = "UPDATE `tb_livros` SET `sinopse`=%s WHERE `id`=%s"
                cursor.execute(query, (response['sinopse'], response['id']))
                db.commit()
                return {"msg": "Livro atualizado com sucesso"}, 200
            elif response['nome'] == '' and response['autor'] == '' and response['sinopse'] == '':
                query = "UPDATE `tb_livros` SET `genero`=%s WHERE `id`=%s"
                cursor.execute(query, (response['genero'], response['id']))
                db.commit()
                return {"msg": "Livro atualizado com sucesso"}, 200
        
    def delete(self):
        response = api.payload

        with db.cursor() as cursor:
            query = "DELETE FROM `tb_livros` WHERE `id`=%s"
            cursor.execute(query, response['id'])
            db.commit()
            return {"msg": "Livro excluido com sucesso"}, 200
