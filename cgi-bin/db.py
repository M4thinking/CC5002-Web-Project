import mysql.connector
import hashlib
import sys
import os
import cgitb

cgitb.enable()


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

    def save_data(self, data, contacts, files):
        """ 
        Este método guarda las fotos, la actividad en la base de datos y actualiza los temas.
        La tabla de fotos tiene un atributo path, el cual contiene el nombre
        hasheado del archivo, concatenado con su id en la base de datos.

        """
        # try:
        # Verificar si existe el tema
        id_tema = data[8]
        otro_tema = data[9]
        sql = "SELECT COUNT(*) FROM tema TM WHERE TM.id = '%s'"
        self.cursor.execute(sql, (id_tema,))
        if self.cursor.fetchall()[0][0] == 0:  # Si no existe, se crea un nuevo tema
            sql = "INSERT INTO tema (nombre) VALUES (%s)"
            self.cursor.execute(sql, (otro_tema,))
            id_tema = self.cursor.getlastrowid()  # recalculamos él id del tema en función del incremental
            self.db.commit()

        # Guardar actividad
        sql = '''INSERT INTO 
                actividad (comuna_id, sector, nombre, email, celular,
                dia_hora_inicio, dia_hora_termino, descripcion, tema_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            '''
        self.cursor.execute(sql, (*data[:-2], id_tema))
        self.db.commit()
        # Guardamos los contactos
        conns = ["whatsapp", "telegram", "twitter", "instagram", "facebook", "tiktok", "otra"]
        id_actividad = self.cursor.getlastrowid()  # recupera el último id procesado, tb propenso a datarace
        k = 0
        while k < len(contacts):
            if contacts[k].value != '':
                sql_contact = "INSERT INTO contactar_por (nombre, identificador, actividad_id) VALUES (%s, %s, %s);"
                self.cursor.execute(sql_contact, (conns[k], contacts[k].value, id_actividad))
                self.db.commit()
            k = k + 1
        # Procesar fotos
        if not isinstance(files, list):
            files = [files]
        for file_obj in files:
            filename = file_obj.filename
            sql = "SELECT COUNT(id) FROM foto"  # Cuenta las fotos que hay en la base de datos
            self.cursor.execute(sql)
            total = self.cursor.fetchall()[0][0] + 1

            # Guarda la foto con hash en la ruta
            fn = os.path.basename(filename)  # nombre original
            filename_hash = hashlib.sha256(filename.encode()).hexdigest()[0:30]  # aplica función de hash
            filename_hash += f"_{total}"  # Función de hash + el número total de fotos, nombre único (datarace)
            route = f"data/media/{filename_hash}"
            open(route, "wb").write(file_obj.file.read())

            # Guardar las fotos
            sql_file = "INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES (%s, %s, %s)"

            # ejecuta la query que guarda el archivo en base de datos
            self.cursor.execute(sql_file, (route, fn, id_actividad))

            # modifico la base de datos
            self.db.commit()

        # except mysql.connector.Error as err:
        #     print("Error en la base de datos: {}".format(err))
        #     print("Info general:\n", data, "\nInfo de contacto:\n", contacts)
        #     print("ERROR AL GUARDAR FOTO")
        #     sys.exit()

    def get_data(self):
        """ 
        Este método realiza una consulta que hace un left join
        entre la tabla de medicos y archivos.
        
        Retorna una lista de tuplas, cada tupla contiene
            (nombre, experiencia, especialidad, email,celular,path) 

        """
        sql = '''
                SELECT  DATE_FORMAT(AC.dia_hora_inicio, "%Y-%m-%d %H:%i"), DATE_FORMAT(AC.dia_hora_termino, "%Y-%m-%d %H:%i"), CO.nombre, AC.sector, TE.nombre, AC.nombre, AC.email, AC.celular, AC.descripcion, AC.id 
                FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC;
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_temas(self, id_tema=-1):
        if id_tema == -1:
            sql = '''SELECT * FROM tema FT'''
        else:
            sql = f"""SELECT nombre FROM tema TE WHERE id = '{id_tema}%'"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_activities(self):
        # seleccionamos todos los datos de la tabla
        self.cursor.execute(f'SELECT * FROM actividad ORDER BY comuna_id, dia_hora_inicio ASC')  # Agregamos el input a la consulta con un f-string
        return self.cursor.fetchall()  # retornamos los datos de la tabla

    def get_activity(self, id_actividad):
        """
        Este método realiza una consulta que hace un left join
        entre la tabla de medicos y archivos.

        Retorna una lista de tuplas, cada tupla contiene
            (nombre, experiencia, especialidad, email,celular,path)

        """
        sql = f'''
                SELECT  DATE_FORMAT(AC.dia_hora_inicio, "%Y-%m-%d %H:%i"), DATE_FORMAT(AC.dia_hora_termino, "%Y-%m-%d %H:%i"), CO.nombre, AC.sector, TE.nombre, AC.nombre, AC.email, AC.celular, AC.descripcion, AC.id 
                FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id AND AC.id = '{id_actividad}%'  ORDER BY id DESC;
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_region_comuna(self):
        sql = '''SELECT R.nombre, C.nombre FROM region R, comuna C WHERE R.id = C.region_id '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comuna(self, id_comuna):
        sql = f"SELECT C.nombre FROM comuna C WHERE C.id = '{id_comuna}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def search(self, name):
        sql = f"select nombre from medico where nombre LIKE '{name}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_last_5(self):
        sql = '''
        SELECT  DATE_FORMAT(AC.dia_hora_inicio, "%Y-%m-%d %H:%i"), DATE_FORMAT(AC.dia_hora_termino, "%Y-%m-%d %H:%i"), CO.nombre, AC.sector, TE.nombre, AC.nombre, AC.email, AC.celular, AC.descripcion, AC.id 
        FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT 5;
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_images(self, id_actividad, get_all=True):
        if get_all:
            sql = f"SELECT id, ruta_archivo, nombre_archivo FROM foto WHERE actividad_id='{id_actividad}%'"
        else:
            sql = f"SELECT ruta_archivo FROM foto WHERE actividad_id='{id_actividad}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def events_per_day(self):
        sql = '''SELECT DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d') as fecha,
         count(*) as total from actividad group by DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d')
          order by DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d') asc;'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count_type(self):
        sql = """SELECT TE.nombre as temas, count(*) AS total 
                FROM actividad AC, tema TE 
                WHERE AC.tema_id = TE.id 
                GROUP BY AC.tema_id 
                ORDER BY total ASC;"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def events_per_hour(self):
        sql1 = '''SELECT DATE_FORMAT(dia_hora_inicio, '%Y-%m') as fecha,
        COUNT(CASE WHEN time(dia_hora_inicio) >= '00:00:00' and time(dia_hora_inicio) <= '10:59:59' THEN 1 ELSE NULL END),
        COUNT(CASE WHEN time(dia_hora_inicio) >= '11:00:00' and time(dia_hora_inicio) <= '14:59:59' THEN 1 ELSE NULL END), 
        COUNT(CASE WHEN time(dia_hora_inicio) >= '15:00:00' and time(dia_hora_inicio) <= '23:59:59' THEN 1 ELSE NULL END)
        FROM actividad group by DATE_FORMAT(dia_hora_inicio, '%Y-%m');
        '''
        self.cursor.execute(sql1)
        return self.cursor.fetchall()
