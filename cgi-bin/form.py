# -*- coding: utf-8 -*-
import sys
from db import DB

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print()
sys.stdout.reconfigure(encoding='utf-8')

# db = DB('localhost', 'root', '', 'ejercicio4', 'utf8')
# data = db.get_data()  # retorna una lista de tuplas formato (nombre, experiencia, especialidad, email,celular,path)

form = """
<div id="contenido-formulario" class="contenido">
    <!-- Form -->
    <form id="main-form" method="post" action="envío-exitoso.html" onsubmit="return validar();" novalidate>
        <!-- Form title -->
        <div id="form-title">Informar actividad</div>
        <br>
        <!-- Apartado ¿Dónde? -->
        <div id="donde" class="sección-formulario">
            <label><b>Información del lugar</b></label><br>

            <!-- Obligatorio validado por JS -->

            <!-- Selección de la Región -->
            <label for="region">Región*</label><br>
            <!-- Obligatorio validado por JS -->
            <select id="region" name="region"></select><br>
            <!-- Selección de la Comuna -->
            <label for="comuna">Comuna*</label><br>
            <select id="comuna" name="comuna">
                <script src="scripts/lugarEvento.js"></script>
            </select>

            <!-- Sector del Evento -->
            <div class="input-group">
                <label for="sector">Sector</label><br>
                <input type="text" id="sector" name="sector" placeholder="Sector del evento."
                       size="100" maxlength="100">
            </div>
        </div>
        <!-- Apartado ¿Quién organiza? -->
        <div id="quien-organiza" class="sección-formulario">
            <label><b>Datos del organizador</b></label><br>
            <!--Nombre del usuario-->
            <div class="input-group">
                <label for="nombre">Nombre*</label><br>
                <input type="text" id="nombre" name="nombre" size="100" maxlength="200" placeholder="Juan Perez"
                       required>
            </div>
            <!-- Correo del usuario-->
            <div class="input-group">
                <label for="email">Email*</label><br>
                <input type="text" id="email" name="email" size="100" maxlength="100" placeholder="juan@perez.com"
                       required>
            </div>
            <!-- Número de celular -->
            <div class="input-group">
                <label for="celular">Número de celular</label><br>
                <input type="text" id="celular" name="celular" size="15" placeholder="+56 9 1234 5678">
            </div>

            <!-- Contacto -->
            <div class="input-group">
                <script>
                    function mostrarContacto(check_box_id, text_id) {
                        let checkBox = document.getElementById(check_box_id);
                        let text = document.getElementById(text_id);
                        if (checkBox.checked == true && $('input[type=checkbox]:checked').length <= 5) {
                            text.style.display = "block";
                        } else {
                            text.style.display = "none";
                        }
                    }
                </script>
                <label id="contactar">Contactar por</label><br><br>
                <div id="aviso"></div>
                <script src="scripts/listaContacto.js"></script>
                <script>
                    /* Evita marcado de más de 5 casillas, igualmente se valida */
                    $('input[type=checkbox]').on('change', function (e) {
                        if ($('input[type=checkbox]:checked').length > 5) {
                            $(this).prop('checked', false);
                            let paragraph = document.getElementById("aviso");
                            if (paragraph.childNodes.length === 0) {
                                paragraph.textContent += " (Máximo 5 medios de contacto)";
                            }
                        }
                    });
                </script>
            </div>
            <br>
        </div>

        <!-- Apartado ¿Cuándo y de qué trata? -->
        <div id="cuando-tema" class="sección-formulario">
            <label><b>Información de la actividad</b></label><br>
            <!-- Día hora inicio -->
            <div class="input-group">
                <label for="dia-hora-inicio">Día y hora de inicio*</label><br>
                <input type="text" id="dia-hora-inicio" name="dia-hora-inicio" size="20" placeholder="aaaa-mm-dd hh:mm"
                       required>
                <script src="scripts/listaActividades.js"
                        onload="fecha('dia-hora-inicio')"></script>
            </div>

            <!-- Día hora termino -->
            <div class="input-group">
                <label for="dia-hora-termino">Día y hora de término.</label><br>
                <input type="text" id="dia-hora-termino" name="dia-hora-termino" size="20"
                       placeholder="aaaa-mm-dd hh:mm">
                <script src="scripts/listaActividades.js"
                        onload="fecha('dia-hora-termino',3)"></script>
            </div>
            <!-- Descripción del Evento -->
            <div class="input-group">
                <label for="descripcion-evento">Descripción</label><br>
                <textarea id="descripcion-evento" name="descripcion-evento"
                          placeholder="Describe aquí como será el evento." maxlength="500"
                          rows="10"
                          cols="50"></textarea>
            </div>

            <!-- Seleccionar tema del evento-->
            <div class="input-group">
                <label for="tema">Tema*</label><br>
                <select name="tema" id="tema"
                        onchange="showfield(this.options[this.selectedIndex].value,this.options.length)" required>
                    <option value="">Selecciona una opción</option>
                    <script src="scripts/temas.js"></script>
                </select>
                <script>
                    function showfield(value, len) {
                        if (value == (len - 1)) { //"otro siempre está en la última categoría disponible"
                            document.getElementById('especificar-otro').innerHTML =
                                'Nuevo tema' + ': <input type="text" id="otro-tema" name="tema" minlength="3" maxlength="15"/>';
                        } else {
                            document.getElementById('especificar-otro').innerHTML = '';
                        }
                    }
                </script>
                <div id="especificar-otro"></div>
            </div>
            <!-- Subir de 1 a 5 fotos-->
            <div class="input-group">
                <label>Subir Foto*</label><br>
                <input type="file" accept="image/*" id="foto-actividad1" name="foto-actividad" required>
                <button type="button" id="agregar-otra-foto" class="boton-form" onclick="nuevaFoto()">Agregar otra
                    foto
                </button>
                <div id="div-foto-actividad2"></div>
                <div id="div-foto-actividad3"></div>
                <div id="div-foto-actividad4"></div>
                <div id="div-foto-actividad5"></div>

                <script>
                    /* Evita más de 5 imágenes, igualmente se valida */
                    let numeroArchivos = 1;

                    function nuevaFoto() {
                        if (numeroArchivos < 5) {
                            numeroArchivos++;
                            document.getElementById('div-foto-actividad' + numeroArchivos).innerHTML =
                                '<input type="file" accept="image/*" id="foto-actividad' +
                                numeroArchivos + '" ' + 'name="foto-actividad" maxlength="15" minlength="3" required>';
                        }
                    }
                </script>
            </div>
        </div>

        <!-- Submit button -->
        <div class="button">
            <button id="agregar-actividad" class="boton-form" type="button" onclick="showDiv()">Agregar esta actividad
            </button>
        </div>

        <script>
            function showDiv(id = 'myModal') {
                document.getElementById(id).style.display = "block";
            }

            function notShowDiv(id = 'myModal') {
                document.getElementById('myModal').style.display = "none";
            }


        </script>

        <div id="myModal" class="modal" hidden>
            <div class="modal-content">
                <div class="modal-header">
                    Enviar formulario
                    <span class="close" onclick="notShowDiv()">&times;</span>
                </div>
                <div class="modal-body">
                    <p>¿Está seguro que desea agregar esta actividad?</p>
                </div>
                <div class="modal-footer">
                    <button class="confirmar" type="submit" value="Submit" onclick="notShowDiv()">Sí, estoy seguro
                    </button>
                    <button class="rechazar" type="button" onclick="notShowDiv()">No, no estoy seguro, quiero volver al
                        formulario
                    </button>
                </div>
            </div>
        </div>
    </form>
</div>
"""

with open('templates/template.html', mode="r", encoding="utf-8") as template:
    file = template.read()
    print(file.format(form))
