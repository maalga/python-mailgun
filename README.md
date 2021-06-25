# python-mailgun
Script enviar mails con python y mailgun desde su APi RESTful.

Pre-requisitos:
* Ver requirements.txt.
* Tener acceso a la APi de Mailgun y su respectiva Key. 
* La versión de python utilizada es la 3 o superior. 

Instrucciones:

El script corre por linea de comandos, consta de nueve argumentos, algunos de ellos opcionales. <br />
python mailgun.py --help para ver los argumentos disponibles.

Ejemplo de uso:

Enviar mail con asunto y texto plano en el cuerpo. <br />
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'"<br />
Enviar mail con asunto, texto plano y archivo adjunto.<br />
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'" -a "nombre_archivoa_djunto"<br />
Enviar mail con asunto, texto plano y contenido en html.<br />
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'" -o "archivo_html" <br />

Documentación:<br />
https://documentation.mailgun.com/en/latest/<br />
https://docs.python.org/3/library/argparse.html<br />




