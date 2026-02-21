📦 Sistema de Gestión de Inventarios Mejorado (Semana 10)
📌 Descripción

Este proyecto corresponde a la mejora del Sistema de Gestión de Inventarios desarrollado en la Semana 9 de la asignatura Programación Orientada a Objetos.

En esta versión se implementa:

Persistencia de datos mediante archivos de texto.

Carga automática del inventario al iniciar el programa.

Manejo robusto de excepciones en operaciones de lectura y escritura.

Notificación en consola sobre el éxito o fallo de las operaciones.

El sistema aplica principios de Programación Orientada a Objetos y buenas prácticas en el manejo de archivos en Python.

🎯 Objetivos Implementados

✔ Almacenamiento automático del inventario en inventario.txt
✔ Recuperación automática de productos al iniciar el sistema
✔ Manejo de excepciones como:

FileNotFoundError

PermissionError

ValueError

OSError

✔ Validación de datos ingresados por el usuario
✔ Código modular y documentado

🧠 Arquitectura del Proyecto
producto.py

Define la clase Producto, que representa una entidad del inventario.

Incluye:

Atributos privados

Getters y setters

Método __str__

Métodos auxiliares para convertir el objeto a línea de archivo y reconstruirlo

inventario.py

Define la clase Inventario, responsable de:

Añadir productos (ID único)

Eliminar productos por ID

Actualizar cantidad y precio

Buscar por nombre

Mostrar inventario completo

Guardar cambios en archivo automáticamente

Cargar datos desde archivo al iniciar

Incluye manejo de excepciones durante:

Creación de archivo

Lectura de datos

Escritura segura con archivo temporal

main.py

Contiene la interfaz de usuario en consola:

Menú interactivo

Validación de entrada

Mensajes de éxito o error

Comunicación clara con el usuario

💾 Formato del Archivo

El archivo inventario.txt almacena cada producto en una línea con el siguiente formato:

id|nombre|cantidad|precio

Ejemplo:

001|Laptop|5|1200.50
002|Mouse|20|15.99

Se utiliza el separador | para evitar problemas con nombres que contengan comas.

🔒 Manejo de Excepciones

El sistema maneja situaciones como:

Archivo inexistente (se crea automáticamente).

Archivo corrupto (líneas inválidas se ignoran).

Falta de permisos de escritura.

Errores del sistema operativo.

Esto garantiza que el programa sea resiliente y no se detenga inesperadamente.

▶ Cómo Ejecutar el Proyecto

Abrir la carpeta SEMANA10 en Visual Studio Code.

Asegurarse de tener Python instalado.

Ejecutar en la terminal:

python main.py
🧪 Pruebas Realizadas

Primera ejecución sin archivo previo.

Agregado de productos y verificación de persistencia.

Eliminación y actualización con comprobación en archivo.

Simulación de líneas corruptas en el archivo.

Pruebas de manejo de errores de escritura.

📈 Conclusión

La integración de manipulación de archivos y manejo de excepciones fortalece el sistema, permitiendo desarrollar una aplicación más robusta, segura y cercana a entornos reales de producción.

Este proyecto demuestra la aplicación práctica de conceptos fundamentales de Python como Programación Orientada a Objetos, persistencia de datos y control de errores.
