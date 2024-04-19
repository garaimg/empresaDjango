Instalar Django
1. (comprobarlo con “python --version”)
2. Instalar el
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
3. Instalar (provee un entorno virtual dedicado a
cada proyecto desarrollado con Django):
pip install virtualenvwrapper-win
Instalar Django
4. Establecer el directorio de trabajo en donde los entornos virtuales
serán almacenados. Para ello añadir la variable del sistema
 (en Linux: export WORKON_HOME = .virtualenvs ).
5. Establecer el directorio de trabajo en donde se crearán los proyectos.
Para ello añadir la variable del sistema (en Linux:
export PROJECT_HOME=./projects ).
6. para tu primer proyecto: mkvirtualenv env1
a. Es posible crear el proyecto y el entorno al mismo tiempo con mkproject
7. : pip install django

SOLO TRABAJA CON BASES DE DATOS RELACIONALES

MVT
ORM propio de Django

Crean env-> estando en entornos, en venvx -> .\Scripts\activate
django-admin startproject nombre_del_proyecto
Crear app -> python manage.py startapp appEmpresaDjango
Hacer migraciones-> Crea los modelos
python manage.py makemigrations appEmpresaDjango
python manage.py migrate
python manage.py runserver -> Iniciar servidor
python manage.py shell
-> Una vez hecho eso:
>>> from appEmpresaDjango.models import Departamento, Habilidad, Empleado
>>> Empleado.objects.all()
<QuerySet [<Empleado: Empleado object (1)>, <Empleado: Empleado object (2)>]>
>>> Habilidad.objects.all()
<QuerySet [<Habilidad: Habilidad object (1)>, <Habilidad: Habilidad object (2)>]>
>>> habilidad = Habilidad(nombre="git")
>>> habilidad.save()
>>> Habilidad.objects.all()
<QuerySet [<Habilidad: Habilidad object (1)>, <Habilidad: Habilidad object (2)>, <Habilidad: Habilidad object (3)>]>
>>> Habilidad.objects.filter(nombre__contains="git")
<QuerySet [<Habilidad: Habilidad object (3)>]>
>>> Habilidad.objects.filter(nombre__contains="git").count()
1
>>> Habilidad.objects.get(id=2)      #Id para poder sacar el detalle de ese departamento
<Habilidad: Habilidad object (2)>

https://docs.djangoproject.com/en/5.0/topics/db/queries/
-> Toda la info de querys ORM
Un fichero URL-s por cada aplicación
Por cada app un fichero urls.py, appEmpresaDjango, appVentasDjango...
http://127.0.0.1:8000/appEmpresaDjango/empleados/ -> Listar -> Index (GET)
http://127.0.0.1:8000/appEmpresaDjango/departamentos/ -> Listar -> Index (GET)
http://127.0.0.1:8000/appEmpresaDjango/departamentos/<id>/ -> Ver detalle del departamento con un id específico -> show/view
http://127.0.0.1:8000/appEmpresaDjango/departamentos/ (POST) -> Crear departamento -> Create
http://127.0.0.1:8000/appEmpresaDjango/departamentos/<id> (DELETE) -> Eliminar -> Delete
http://127.0.0.1:8000/appEmpresaDjango/departamentos/<id> (PUT)  -> modificar/actualizar -> update
