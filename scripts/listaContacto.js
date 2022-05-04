let redes = ["Whatsapp", "Telegram", "Twitter", "Instagram", "Facebook", "Tiktok", "Otra"];

Whatsapp = "+56 9 xxxx xxxx o https://wa.me/"
Telegram = "@usuario o https://web.telegram.org/"
Twitter = "@usuario o https://www.twitter.com/"
Instagram = "@usuario o https://www.instagram.com/"
Facebook = "@usuario o https://www.facebook.com/"
Tiktok = "@usuario o https://www.tiktok.com/"
Otra = "Ingrese un URL al perfil"

let placeholders = [Whatsapp, Telegram, Twitter, Instagram, Facebook, Tiktok, Otra];
k = 0
for (let i in redes) {
    Red = redes[i];
    red = Red.toLowerCase();
    document.write('<label class="checkbox-container">' + Red +
                    '<input type="checkbox" onclick="mostrarContacto(\'check-' + red + '\',\'contacto-' + red + '\')"' +
                           'id="check-' + red +'" name="check-' + red +'">'+
                    '<span class="checkmark"></span>'+
                    '</label>'+
                    '<div class="div-' + red +'">'+
                    '<input type="text" id="contacto-' + red +
                    '" name="contactar-por" size="30" minlength="4"'+
                           'maxlength="50" placeholder="'+placeholders[k]+'" style="display: none">'+
                    '</div>');
    k = k + 1
}
