let redes = ["Whatsapp", "Telegram", "Twitter", "Instagram", "Facebook", "Tiktok", "Otra"];

for (let i in redes) {
    Red = redes[i];
    red = Red.toLowerCase();
    document.write('<label class="checkbox-container">' + Red +
                    '<input type="checkbox" onclick="mostrarContacto(\'check-' + red + '\',\'contacto-' + red + '\')"' +
                           'id="check-' + red +'" value="1" name="contactar-por">'+
                    '<span class="checkmark"></span>'+
                    '</label>'+
                    '<div class="div-' + red +'">'+
                    '<input type="text" id="contacto-' + red +
                    '" name="contactar-por" size="30" minlength="4"'+
                           'maxlength="50" placeholder="ID de contacto / URL de red social" style="display: none">'+
                    '</div>');
}
