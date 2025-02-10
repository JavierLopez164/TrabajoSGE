# TrabajoSGE

# Pasos a seguir
Crear un Pull Request (PR):

La persona debe crear un Pull Request desde su rama hacia la rama main.
Para crear un Pull Request, puede ir a la página del repositorio en GitHub, seleccionar la pestaña "Pull requests" y luego hacer clic en "New pull request".
Seleccionar la rama de origen (la rama de la persona) y la rama de destino (main).
Revisión del Pull Request:

Otros miembros del equipo pueden revisar el código propuesto en el Pull Request.
Se pueden agregar comentarios, solicitar cambios o aprobar el Pull Request.
Merge del Pull Request:

Una vez que el Pull Request ha sido revisado y aprobado, se puede fusionar (merge) en la rama main.
Para fusionar el Pull Request, hacer clic en el botón "Merge pull request" en la página del Pull Request.
Eliminar la rama (opcional):

Después de fusionar, se puede eliminar la rama de la persona si ya no es necesaria. Esto se puede hacer directamente en la página del Pull Request.

Para traer cambios de la rama main a tu rama de trabajo, puedes seguir estos pasos:

Cambiar a tu rama de trabajo:
    git checkout tu-rama

Actualizar la rama main:
    git checkout main
    git pull origin main

Fusionar main en tu rama de trabajo:
    git checkout tu-rama
    git merge main

Esto traerá los cambios de la rama main a tu rama de trabajo. Si hay conflictos, Git te notificará y tendrás que resolverlos antes de completar la fusión.

# Ideas
El proyecto se basa en hacer gestiones de productos en un almacen y ver las ventas que se han realizado.
Una base de datos local, cada uno en su equipo, en la que tenemos la tabla producto y la tabal venta.
De cada producto tenemos: 
- Nombre
- Precio
- Stock
- Nº articulo
- Descripcion

De cada venta:
- Nº articulo
- Cantidad
- Nombre cliente

La gráfica estaría relaccionada con las ventas de los productos y el stock que queda de ellos.

El correo podría ser de que el usuario pone el nombre o nº articulo y le envia por correo toda la información de dicho producto.

# Paleta de colores
[text](https://paletadecolores.com.mx/paleta/9c9c9c/adadad/bfbfbf/d0d0d0/e2e2e2/)