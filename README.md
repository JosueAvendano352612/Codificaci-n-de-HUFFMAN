# Codificacion-de-HUFFMAN
Se trabajara en este repositoria una actividad haciendo Codificacion de HUFFMAN
El dia 11/04/2024, se trabajo en la participacion 07 de codificacion de huffman en el cual se hizo un script que lee un archivo de txt, el script cuenta los carácteres y líneas del archivo y los acomoda de manera acendente a decendente y crea un nuevo archivo txt el cual se guardan todos los resultados obtenidos

#Desarrollo de la actividad
#29/04/2024

Selección de Archivo y Mostrar Contenido

Se creó la función seleccionar_archivo para que el usuario pueda elegir archivos de texto (.txt) tanto para la entrada como para la salida, utilizando filedialog.askopenfilename y filedialog.asksaveasfilename para manejar la selección de archivos.
Se implementó el widget Text llamado contenido_text para mostrar de manera interactiva el contenido del archivo seleccionado, ofreciendo una vista previa al usuario.
Conteo de Caracteres y Líneas

Se desarrolló la función contar_caracteres_lineas para contar los caracteres y líneas en el archivo de entrada, utilizando la biblioteca estándar de Python y la clase Counter para realizar el conteo de frecuencia de caracteres. Los resultados se guardan tanto en un archivo de salida como se muestran en la consola y en el widget resultado_text.
Interfaz de Usuario (GUI)

Se diseñó una interfaz intuitiva utilizando varios widgets (Label, Entry, Button, Text) en la ventana principal (root), con un título significativo para una mejor experiencia de usuario.
Se implementaron botones con funciones asociadas que permiten al usuario realizar acciones como seleccionar archivos, mostrar resultados, etc.
Funcionalidad de Comprimir y Descomprimir (sin implementación actual)

Se añadieron botones para las funciones de Comprimir y Descomprimir, aunque actualmente no tienen ninguna funcionalidad asociada, dejando la puerta abierta para futuras expansiones del código.
Manejo de Excepciones

Se implementó el manejo de excepciones para capturar errores como archivos no encontrados (FileNotFoundError) u otros errores genéricos (Exception), mejorando así la robustez del programa.
Desarrollo del Back-End
Implementación del Algoritmo de Huffman

Se definió la clase NodoHuffman para representar un nodo en el árbol de Huffman, y la clase HuffmanTree para construir el árbol de Huffman a partir de las frecuencias de caracteres utilizando una cola de prioridad (heapq).
Se desarrollaron las funciones construir_arbol_huffman y generar_codigos_huffman para la construcción del árbol de Huffman y la asignación de códigos binarios a cada carácter en el árbol.
Comprimir y Descomprimir Archivos

Se implementaron los métodos comprimir y descomprimir para realizar la compresión y descompresión de archivos utilizando el algoritmo de Huffman, respectivamente.
Interfaz de Usuario y Funcionalidades

Se creó la clase InterfazHuffman para manejar la interfaz de usuario utilizando Tkinter, incluyendo botones para abrir un archivo, comprimir y descomprimir archivos.
Se desarrollaron las funcionalidades principales como mostrar_info_archivo, comprimir_archivo y descomprimir_archivo para realizar las acciones correspondientes según la selección del usuario.
Manejo de Excepciones y Guardado de Resultados

Se implementó el manejo de excepciones para mejorar la robustez del programa y se estableció el guardado de archivos comprimidos y descomprimidos utilizando las funciones de filedialog.
