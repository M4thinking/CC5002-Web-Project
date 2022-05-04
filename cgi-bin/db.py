import mysql.connector
import hashlib
import sys


class DB:
    def __init__(self, host, user, password, database, charset):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cursor = self.db.cursor()

    def save_data(self, data):
        """ 
        Este método guarda un archivo y un médico en la base de datos.
        La tabla de archivo tiene un atributo path, el cual contiene el nombre
        hasheado del archivo, concatenado con su id en la base de datos.

        """
        # Procesar archivo
        fileobj = data[5]
        filename = fileobj.filename

        sql = "SELECT COUNT(actividad_id) FROM foto"  # Cuenta los archivos que hay en la base de datos
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1
        filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30]  # aplica función de hash
        filename_hash += f"_{total}"  # concatena la función de hash con el número total de archivos, nombre único
        # OJO:lo anterior puede ser peligroso en el caso en que se tenga un servidor que ejecute peticiones en paralelo.
        #      Lo que se conoce como un datarace. Nuestro servidor ejecuta sus procesos de forma secuencial, no worries.

        # Guardar archivo
        try:
            open(f"media/{filename_hash}", "wb").write(fileobj.file.read())  # guarda el archivo localmente
            sql_file = '''
                INSERT INTO foto (nombre, path) 
                VALUES (%s, %s)
                '''
            self.cursor.execute(sql_file,
                                (filename, filename_hash))  # ejecuta la query que guarda el archivo en base de datos

            # Guardar medico
            id_imagen = self.cursor.getlastrowid()  # recupera el último id procesado, tb propenso a datarace
            sql = '''
                INSERT INTO medico (nombre, experiencia, especialidad, email,celular,foto) 
                VALUES (%s, %s, %s, %s, %s,%s)
                '''
            self.cursor.execute(sql, data[:5] + (id_imagen,))  # ejecuta la consulta
            self.db.commit()  # modifico la base de datos
        except:
            print(data[:5] + (id_imagen,))
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def get_data(self):
        """ 
        Este método realiza una consulta que hace un left join
        entre la tabla de medicos y archivos.
        
        Retorna una lista de tuplas, cada tupla contiene
            (nombre, experiencia, especialidad, email,celular,path) 

        """
        sql = '''
            SELECT A.nombre, A.experiencia, A.especialidad, A.email, A.celular, B.path FROM medico A
            LEFT JOIN archivos B
            ON A.foto = B.id
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_region_comuna(self):
        sql = '''SELECT A.id, B.region_id, FROM region A
                    LEFT JOIN comuna B
                    ON A.foto = B.id
                    '''

        # OJOS
    def search(self, name):
        sql = f"select nombre from medico where nombre LIKE '{name}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
