# Proyecto Flask
Proyecto de creación de una web dinámica que obtiene información de un fichero json usando flask

## Enunciado del proyecto
El proyecto consiste en crear una aplicación web a partir de un fichero json con las siguientes características:
- La aplicación debe tener una hoja de estilo. Para ello lo mejor es que busques una plantilla HTML/CSS.
- Las plantillas se heredarán de la plantilla base.html.
- La plantilla base tendrá al menos dos bloques: uno para indicar el título y otro para poner el contenido.
- La página principal tendrá una imagen con el logotipo al pulsar sobre está imagen nos llevará a una página /xxxx.
- La página /xxxx nos mostrara un buscador, para ello pon un formulario con un cuadro de texto donde puedas poner el nombre de un xxxx que quieres buscar. Cuando pulséis el botón de buscar enviará la información a la página /listaxxxx. El formulario enviará los datos con el método POST.
- En la página /listaxxxx (qué sólo se puede acceder por el método POST) aparecerán los xxxx cuyo nombre empiezan por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna cadena mostrará todos los xxxx.
- La página /listaxxxx mostrará una tabla generada dinámicamente a partir de los datos de vuestro fichero json y la búsqueda que se haya realizado.
- La tabla tendrá al menos tres columnas: en la primera aparecerá el nombre, en la segunda otra información relevante y en la tercera habrá un enlace con la palabra “Detalle” que me llevará a la página del xxx con la ruta /xxx/<identificador> o /xxx?id=xxxxxxxxxx.
- La lista está en la página /listaxxx y el detalle está en la página /xxx/<identificador> o /xxx?id=xxxxxxx donde aparecerán todos los datos del xxx que tenga ese identificador. Si el identificador no existe devolverá un 404. Tendrá un enlace que me devuelve a la página /xxxx.
- Buscar una Plataforma como Servicio (PaaS) basada en la nube que sea gratuita (Railway, Dokku,,..).y desplegar la aplicación en ella.

### Mejoras
1. Realizar la búsqueda utilizando una sola ruta: Es decir que en la página /xxxx este el formulario de búsqueda y la lista de xxxx seleccionado. La información del formulario se enviará a la misma página. No existirá la página /listaxxxx.
2. Como el protocolo HTTP no tiene estado, no es capaz de acordarse de los datos anteriores, por lo tanto cada vez que se haga una búsqueda aparecerá la lista de xxxx pero el formulario estará vacío, no recuerda lo que pusimos. Modifica el programa para que aparezca en el formulario la cadena que habías introducido en la búsqueda (Pista: tendrá que utilizar el atributo value del elemento input).
3. Añade otro criterio de búsqueda. Para ello hay que generar dinámicamente una lista desplegable (elemento select) en el formulario con las valores de los xxx). 
4. De la misma forma que en el apartado 1, programar la lista desplegable para que recuerde la opción elegida en la búsqueda. (Pista: Usar el atributo selected del elemento option del elemento select).
