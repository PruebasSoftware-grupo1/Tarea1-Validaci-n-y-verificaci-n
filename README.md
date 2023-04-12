# Tarea1-Validacion-y-verificacion
## Chat Empresarial

## **Descripción:** 
Sistema compuesto de dos codigos, el servidor que es el que inicia el sistema de mensajes y los clientes que se conectan a este sistema. Los mensajes se codificarán y decodificarán por parte del cliente para que el servidor no los pueda leer.

## **Instalación:** 
Se requiere de Python 3.6 o mayor, se debe clonar el repositorio en una carpeta y dejar los dos archivos en la misma carpeta para no tener problemas con los códigos.

## **Cómo usar:**
1.  Primero se debe iniciar el servidor mediante el comando ```python3 server.py``` (en caso de tener instalado python con anaconda, usar ```python server.py```)
2.  Para conectar un cliente al chat, se pueden usar dos comandos: ```python3 client.py``` donde se pedirá un nickname por consola. El otro comando es: ```python3 client.py [nickname]``` donde se iniciara el chat automaticamente con el nombre escrito en el [nickname].
3.  En caso de querer agregar mas de un cliente, simplemente usar otra consola con las mismas intrucciones del paso 2 (con nicknames distintos).
4.  Ahora se pueden mandar mensajes libremente, para salir del chat simplemente mande un mensaje vacío (presione enter sin escribir nada).

## **Como contribuir:**
Simplemente hacer un ```git pull``` para obtener el repositorio y agregar la feature mediante el comando ```git flow start feature```. Posteriormente esta feature será revisada por los propietarios del repositorio para corroborar que cumpla los estandares de calidad definidos por el grupo, en caso de pasar esta revisión, será aprobada esta pull request y probablemente sea enviada a producción (cuando se verifique que tampoco tiene errores).

## **Licencia:**
Copyright <YEAR> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
