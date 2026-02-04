# Proyecto-_Algoritmos-CRUD

Sistema de Caja Registradora con CRUD y Autenticación en Tkinter
<img width="301" height="167" alt="image" src="https://github.com/user-attachments/assets/197e06db-66ac-47af-baf6-b167d58267e1" />


Este proyecto consiste en el desarrollo de una aplicación de escritorio implementada en Python, utilizando la biblioteca gráfica Tkinter, cuyo propósito principal es simular un sistema de caja registradora con funcionalidades completas de administración de pedidos, integrando además un módulo básico de autenticación de usuarios.

La aplicación está diseñada bajo un enfoque estructurado que combina un sistema de acceso mediante registro e inicio de sesión, con un módulo CRUD (Create, Read, Update, Delete) que permite gestionar pedidos comerciales de manera dinámica e interactiva.

🔐 Módulo de Autenticación y Control de Acceso

El sistema incorpora una interfaz inicial de login, donde los usuarios pueden:

Registrar nuevas credenciales (usuario y contraseña).

Validar el acceso mediante verificación de datos almacenados en estructuras internas.

Controlar el ingreso al sistema principal únicamente si las credenciales son correctas.

Este mecanismo permite simular un entorno real de control de usuarios, restringiendo el acceso al módulo de pedidos hasta que exista una sesión válida.

🛒 Gestión de Pedidos mediante CRUD

Una vez iniciada la sesión, el usuario accede a la interfaz principal de la caja registradora, la cual permite:

Registrar pedidos, ingresando datos como nombre, apellido, teléfono y dirección.

Seleccionar un paquete tecnológico mediante un menú desplegable.

Calcular automáticamente valores económicos asociados:

Precio base del producto.

Precio total con IVA aplicado.

Generar un código identificador aleatorio para cada pedido.

Asimismo, el sistema permite:

Visualizar todos los pedidos registrados en tiempo real.

Actualizar información de pedidos existentes mediante índices internos.

Eliminar pedidos previa confirmación del usuario.

📂 Estructuras de Datos y Almacenamiento Temporal

El almacenamiento de información se realiza a través de listas organizadas en una estructura tipo matriz, donde cada sublista representa un atributo específico del pedido. Esto permite mantener sincronizados los registros de manera ordenada:

Nombres

Apellidos

Teléfonos

Direcciones

Precio sin IVA

Precio con IVA

Código aleatorio único

De igual manera, las credenciales de usuarios se almacenan en listas paralelas para facilitar la validación durante el inicio de sesión.

🖥️ Interfaz Gráfica Interactiva

La interfaz se compone de múltiples componentes visuales como:

Campos de entrada (Entry)

Etiquetas informativas (Label)

Botones de acción (Button)

Menús desplegables (OptionMenu)

Ventanas emergentes (messagebox)

Además, el sistema implementa el uso de frames dinámicos, alternando entre la pantalla de login y la pantalla principal del CRUD, lo cual mejora la organización y experiencia del usuario.

🎯 Objetivo General del Proyecto

El objetivo principal de este sistema es demostrar el uso práctico de:

Programación orientada a eventos en Python

Construcción de interfaces gráficas con Tkinter

Manejo de estructuras de datos dinámicas

Implementación de operaciones CRUD

Control de acceso mediante autenticación básica

Este proyecto representa una base sólida para futuras mejoras como integración con bases de datos, cifrado de contraseñas o expansión hacia sistemas de facturación más avanzados.

🚀 Tecnologías Utilizadas

Python 3

Tkinter

Messagebox

Random (generación de códigos)
