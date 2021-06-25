# python-mailgun
Script enviar mails con python y mailgun desde su APi RESTful.

Pre-requisitos:
* Ver requirements.txt.
* Tener acceso a la APi de Mailgun y su respectiva Key. 
* La versión de python utilizada es la 3 o superior. 

Instrucciones:

El script corre por linea de comandos, consta de nueve argumentos, algunos de ellos opcionales. 
python mailgun.py --help para ver los argumentos disponibles.

Ejemplo de uso:

Enviar mail con asunto y texto plano en el cuerpo. 
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'"
Enviar mail con asunto, texto plano y archivo adjunto.
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'" -a "nombrearchivoadjunto"
Enviar mail con asunto, texto plano y archivo adjunto.
python mailgun.py -d example.com -f frommail@example.com -t examplemail@gmail.com -s 'subject' -m 'text body'" -a "nombrearchivoadjunto" 

Documentación:
https://documentation.mailgun.com/en/latest/
https://docs.python.org/3/library/argparse.html




