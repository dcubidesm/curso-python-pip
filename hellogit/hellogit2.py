"""
wappalizer- mira las tecnologias usadas en una app web

1.Ingresar a Activar o desactivar las caracteristicas de Windows:
2.Tener seleccionado: WindowsPowerShell 2.0, Virtual Machine Platform y Subsistema de Windows para Linux- Reiniciar.
3.Ir a la tienda de Windows y descargar Ubuntu, cuando el equipo ya haya reiniciado se abre una vebta de Ubuntu para que le configures un user y pass (dcubidesm, root)
-----------------------------------------------------

Herramientas para desarrolladores:
Extensiones: Cómo se denomina la extensión que permite conectar y desconectar rápidamente el JavaScript en tu página web
Toggle JavaScript
Qué hace la herramienta Google Lighthouse? Automaticamente comprueba la calidad de las paginas web.
-----------------------------------------------------
https://www.dongee.com/tutoriales/comandos-basicos-de-linux/?utm_source=google&utm_medium=cpc&utm_campaign=tutoriales&utm_id=tutoriales&utm_term=comandos-linux&tm=tt&ap=gads&aaid=adaFnZvkSdpvp&gclid=Cj0KCQiApOyqBhDlARIsAGfnyMpLGd685y_O9u5fvNRcDF3sXydobqTJtvSsRUCtmGpHPoP5aIs4rgwaAvDlEALw_wcB

---
permisos:
https://www.hostinger.mx/tutoriales/cambiar-permisos-y-propietarios-linux-linea-de-comandos/#:~:text=Usar%20opciones%20con%20los%20comandos%20chmod%20y%20chown,-Una%20opci%C3%B3n%20es&text=Esta%20opci%C3%B3n%20te%20permite%20cambiar,despu%C3%A9s%20del%20comando%20chmod%2Fchown.
---

C O M A N D O S  E N  W S L   T E R M I N A L->
pwd: muestra en que directorio actual.
cd .. : para cambiar de directorio, se puede llegar hasta la raiz (/)
	(para devolverse o salir desde la carpeta en la que estás posicionado)
	cd nom_carpeta

	(para ingresar a un folder)
	cd /home/usuario/public_html

touch: para crear un archivo nuevo
ls: lista los archivos y directorios en el directorio actual.
ll: Muestra  los permisos del propietario, grupo y otros clientes, fecha y los archivos creados y carpetas
cd: cambia el directorio actual.
mkdir: crea un nuevo directorio.
rm: elimina archivos y directorios.
cp: copia archivos y directorios.
mv: mueve o renombra archivos y directorios.
cat: muestra el contenido de un archivo en la pantalla.
grep: busca texto en archivos.
ps: muestra los procesos en ejecución.
kill: detiene un proceso en ejecución.
chmod: cambia los permisos de acceso a archivos y directorios.
sudo: permite al usuario realizar tareas con permisos de superusuario.
tar: crea y extrae archivos comprimidos.
ssh: inicia una sesión segura de shell remota en otro sistema.
ping: comprueba la conectividad de red.



----------------------
https://i-bsd.com/chmod-operation-not-permitted/#google_vignette

nom_error: chmod: changing permissions of '/proyectoPersonal/web.html': Operation not permitted
Error cuando no deja cambiar los permisos de un archivo o una carpeta, se debe instalar: sudo apt install acl

getfacl /proyectoPersonal

getfacl: Removing leading '/' from absolute path names
# file: proyectoPersonal
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

https://i-bsd.com/chmod-operation-not-permitted/#:~:text=You're%20not%20doing%20it%20as%20root%20user&text=If%20that%20directory%20doesn't,or%20doas%20when%20chmod'ing.

Se hizo: Para eliminar acl(lista de control de acceso) permisos, utilice:

setfacl -b /directory/
luego: 
Solucion: sudo chmod -R 777 /proyectoPersonal/web.html

nuevos permisos:  ls -l web.html
-rwxrwxrwx 1 root root 186 Nov 20 21:22 web.html

--------------------------------------------------
Instalacion de Node: Es un entorno de ejecucion para javascript.
es un entorno en tiempo de ejecución multiplataforma para la capa del servidor (en el lado del servidor) basado en JavaScript que es un entorno controlado por eventos diseñado para crear aplicaciones escalables, permitiéndote establecer y gestionar múltiples conexiones al mismo tiempo.

sudo apt update: Se conecta con los servidores del archivo de Ubuntu , como un repositorio de software.

comando: sudo apt install nodejs
versin: node -v
v12.22.9


-----
npm: Node package management: son librerias o paquetes que puedes utilizar para javascript 

Instalacion:
sudo apt install npm

Instalar una versión específica de node 🔎
Se instala el paquete n que permite administrar las versiones de Node:

sudo npm install -g n

Para instalar la versión más actualizada disponible, se ejecuta:

sudo n latest

node -v 
v 21.2.0

-----------------------------

Instalacion de python:

Comando para mantenernos actualizados

sudo apt update

Software que requerimos para instalar Python en su versión actual.

sudo apt install software-properties-common

Actualizar a los lanzamientos de repositorios más recientes

sudo add-apt-repository ppa:deadsnakes/ppa


Volvemos a actualizar porque instalamos anteriormente un nuevo repositorio.

sudo apt update


Instalamos Python

sudo apt install python3.8

Verificamos la versión que instalamos

python3 --version ó python3 -V



---------------------------
¿Qué se usa para instalar Ubuntu sin problemas? Windows Subsystem for Linux
¿Qué hace el comando dism.exe /online /enable-feature -- featurename: virtual machine platform con la opción all no-restart? Habilita la plataforma de windows para maquinas virtuales
---------------------------

Instalacion de GIT:

sudo apt update
sudo apt-get git-all

git --version

LLAVE SSH: Permite acceder a git con una llave propia, sin necesidad de siempre ingresar las credenciales, utiliza encriptacion

Llave generator: shh-keygeb
. Vamos a utilizar el SSH Keygen. Sustituímos nuestro correo en el comando.
ed25519: Algoritmo de encriptacion:
~$ ssh-keygen -t ed25519 -C "tucorreo@mail.com"

. Inicializar Agente de SSH:
eval "$(ssh-agent -s)"

. Agregar nuestra Llave a nuestro Agente de SSH:
ssh-add ~/.ssh/id_ed25519

. Comando para imprimir nuestra llave:
cat ~/.ssh/id_ed25519.pub

----
passphrase: diana0808

The key fingerprint is:
Your identification has been saved in /home/dcubidesm/.ssh/id_ed25519
Your public key has been saved in /home/dcubidesm/.ssh/id_ed25519.pub

SHA256:Nleb93cJ5eFnSbJWYhKpCUOe0EirwmhEqL115rwWhkw repo0806@hotmail.com
The key's randomart image is:
+--[ED25519 256]--+
|..  .o+.   ..    |
|o    .++.  ..    |
|.o   . oo o..+ = |
|= . E o  o .ooX o|
|.+ * *  S . o+.+o|
|. o o =. o  ...oo|
|     . o       .+|
|      o         o|
|     .           |
+----[SHA256]-----+

----

GIT:
Comandos: 
git init: Sirve para iniciar un repositorio.
git branch -m master
git status: 
Untracket files: Significa que habian archivos desde antes de crear el repositorio y el Git no se han añadido porque no lo hace automaticamente.

git add nom_archivo.extension : Sirve para agregar un archivo.
git add . : Especifica que puede agregar todo lo que exista alli.
git add * : Especifica que puede agregar todo lo que exista alli.
git commit -m "Mi primer commit" : Sirve para hacer un commit directo a Git con un mensaje. 

Si te sale error debes hacer esto: 
	git config --global user.name "dcubidesm"
	git config --global user.email "repo0806@hotmail.com"

git push orogin master: Sirve para darle push a la raiz principal que se llama master

RAMAS:
Tiene una rama principal (master) y puede influir en varios conceptos.

PARA ENVIAR UN PUSH AL REPO WEB:
1.confirmar si estas inicializando con el git al que vas a subir los archivos:
	git init
2.Ingresas a la carpeta que vas a subir y pones el nombre(s) de los archivos actualizar.
	git add -f "data.csv"
3.Envias un commit con el mensaje a mostrar
	git commit -m "Se cargo archivo de muestra de datos"
4.Enviar el push a git web
	git push orogin master
5.Revisar en Git web si quedo el cambio


CHECKOUT AND RESET: Revertir los cambios 
git checkout







GIT REMOTE:
Esto permite conectar git para poder enviar commits, pero aun no se ha enviado al git de la red para poder visualizarlo, se ejecuta el siguietne comando:
Nota: Para sacar la URL desde git, debes buscar <> Code -> Local -> SHH -< Copiar la ruta.
git remote add origin git@github.com:dcubidesm/my_web.git
git remote -v : para visualizar si ya estamos conectados en el repositorio
origin  git@github.com:dcubidesm/my_web.git (fetch)
origin  git@github.com:dcubidesm/my_web.git (push)
got
git config --global user.name "dcubidesm": Sirve para configurar que solo sea con mi usurio. Se crea en usuarios > archivo .gitconfig 





--------------------------------------------------------

Descargar e Instalar -> PowerToys x64 de Microsoft para GitHub.
Es una administrador de ventanas que facilita la creacion de diseños de ventanas complejos y la colocacion rapida de ventanas en los diseños.

-----QUE DEBE TENER UN PROYECTO PROFESIONAL DE PYTHON-----------
.gitignore: Este archivo permite que algunos archivos en nuestro proyecto sean ignorados ya que no son necesarios.
Para que el repositorio se vea mas profesional de python, debemos configurar un archivo gitignore (en la web buscar gitignore.io)
https://www.toptal.com/developers/gitignore > se busca los 3 SO y luego el lenguaje y te arroja un archivo el cual debemos copiar

README.md: Este archivo se especificas las instrucciones para los compañeros que empiecen a trabajar en el proyecto.

..........

pip: gestor de paquetes de python, tiene librerias y frameworks que podemos usar para desarrollar los proyectos.

Instalaciones: 
pip:
sudo apt install python3-pip 
pip3 -V
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

librerias:
matplotlib: Esta libreria sirve para crear graficas y cabe resaltar que algunas librerias utiliza dependencias de otras librerias o paquetes, por ejemplo esta utiliza numpy.

Para ver las librerias instaladas de manera global,es decir, de toda mi pc, utilizamos:
pip3 freeze


-----------------------------------------------------------------------------------------------------------------------------------
Creacion de repositorio en github directamente y copias el enlace del origen del repositorio:
git@github.com:dcubidesm/curso-python-pip.git

En la terminal de Ubuntu:
dcubidesm@DESKTOP-DIANA:~/py-project$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /home/dcubidesm/py-project/.git/
dcubidesm@DESKTOP-DIANA:~/py-project$ ll
total 16
drwxr-xr-x 3 dcubidesm dcubidesm 4096 Nov 21 20:05 ./
drwxr-x--- 7 dcubidesm dcubidesm 4096 Nov 21 17:31 ../
drwxr-xr-x 7 dcubidesm dcubidesm 4096 Nov 21 20:05 .git/ --muestra la carpeta de creacion de git.
-rw-r--r-- 1 dcubidesm dcubidesm   26 Nov 21 17:35 Hello.py




"""