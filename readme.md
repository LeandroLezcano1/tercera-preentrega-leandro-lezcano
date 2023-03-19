Estructura de la aplicación


=========================================================================================



La aplicación consta de tres modelos: TrabajadorReciente, TrabajadorAntiguo y TrabajadorPrueba. Cada modelo tiene un formulario que pide el nombre y apellido, la fecha de nacimiento y la antigüedad.

Además, la aplicación tiene una vista buscar_trabajador que muestra un formulario para buscar trabajadores por nombre y apellido.

La base de la aplicación es la plantilla base.html, que contiene el encabezado y pie de página comunes a todas las vistas. Las demás plantillas heredan de base.html.

Funcionalidades de la aplicación


==========================================================================================



Para probar la aplicación, sigue los siguientes pasos:

Crea una base de datos y migra los modelos con el comando python manage.py migrate.

Crea un superusuario con el comando python manage.py createsuperuser para acceder al panel de administración.

Inicia el servidor de desarrollo con el comando python manage.py runserver.

Abre el navegador y ve a la URL http://localhost:8000/admin. Inicia sesión con las credenciales del superusuario.

Agrega algunos trabajadores a la base de datos desde el panel de administración.

