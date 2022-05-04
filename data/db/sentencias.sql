-- insertar actividad:
INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
-- ejemplo: 
-- INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id) VALUES (130606, 'Estadio Comunal', 'Dante Torobolino', 'dante@juegostorobolino.cl', '+56955555555', '2022-04-13 13:00', '2022-04-13 19:00', 'juegos de ayer y hoy', 7);

-- insertar contactar por:
INSERT INTO contactar_por (nombre, identificador, actividad_id) VALUES (?, ?, ?);
-- ejemplo:
-- INSERT INTO contactar_por (nombre, identificador, actividad_id) VALUES ('instagram', 'https://www.instagram.com/dantetorobolino/', 1);

-- insertar foto:
INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id) VALUES (?, ?, ?);
-- ejemplo:
-- INSERT INTO foto (ruta_archivo, nombre_archivo, actividad_id ) VALUES ('/Users/jourzua/personal/DCC/51t/python/archivos/', 'foto-juego.jpg', 1);

-- seleccionar actividades:
SELECT id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id FROM actividad
-- seleccionar ultimas 5 actividades agregadas:
SELECT id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id FROM actividad ORDER BY id DESC LIMIT 5
-- seleccionar ultimas 5 actividades agregadas, con nombre de comuna y nombre de tema
SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT 5

-- seleccionar contactar_por de una actividad
SELECT id, nombre, identificador, actividad_id FROM contactar_por WHERE actividad_id=?

-- seleccionar información de la fotos de una actividad:
SELECT id, ruta_archivo, nombre_archivo, actividad_id FROM foto WHERE actividad_id=?

