from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from collections import Counter
import heapq

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

class HuffmanTree:
    def __init__(self):
        self.raiz = None
        self.tabla_codigos = {}

    def construir_arbol_huffman(self, tabla_frecuencias):
        cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in tabla_frecuencias.items()]
        heapq.heapify(cola_prioridad)

        while len(cola_prioridad) > 1:
            nodo_izq = heapq.heappop(cola_prioridad)
            nodo_der = heapq.heappop(cola_prioridad)
            nuevo_nodo = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
            nuevo_nodo.izquierda = nodo_izq
            nuevo_nodo.derecha = nodo_der
            heapq.heappush(cola_prioridad, nuevo_nodo)

        self.raiz = cola_prioridad[0]
        return self.generar_codigos_huffman(self.raiz)

    def generar_codigos_huffman(self, nodo_actual, codigo_actual=''):
        if nodo_actual.caracter is not None:
            self.tabla_codigos[nodo_actual.caracter] = codigo_actual
        else:
            self.generar_codigos_huffman(nodo_actual.izquierda, codigo_actual + '0')
            self.generar_codigos_huffman(nodo_actual.derecha, codigo_actual + '1')

    def comprimir(self, contenido):
        tabla_frecuencias = Counter(contenido)
        self.construir_arbol_huffman(tabla_frecuencias)
        bits = ''.join([self.tabla_codigos[caracter] for caracter in contenido])
        bits = '0' * (8 - len(bits) % 8) + bits + '0' * 8
        bytes_comprimidos = bytes([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)])
        return bytes_comprimidos, self.tabla_codigos

    def descomprimir(self, bytes_comprimidos):
        bits = ''.join(format(byte, '08b') for byte in bytes_comprimidos)
        codigo_actual = ''
        contenido_descomprimido = ''
        nodo_actual = self.raiz

        for bit in bits:
            if bit == '0':
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
            
            if nodo_actual.caracter is not None:
                contenido_descomprimido += nodo_actual.caracter
                nodo_actual = self.raiz

        return contenido_descomprimido

class InterfazHuffman:
    def __init__(self):
        self.arbol_huffman = HuffmanTree()
        self.ventana_principal()

    def ventana_principal(self):
        root = Tk()
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        ttk.Label(frm, text="Ventana principal").grid(column=0, row=0)
        ttk.Button(frm, text="Abrir archivo", command=self.mostrar_info_archivo).grid(column=0, row=1)
        ttk.Button(frm, text="Comprimir archivo", command=self.comprimir_archivo).grid(column=0, row=2)
        ttk.Button(frm, text="Descomprimir archivo", command=self.descomprimir_archivo).grid(column=0, row=3)
        root.mainloop()

    def mostrar_info_archivo(self):
        nombre_archivo = filedialog.askopenfilename()
        if nombre_archivo:
            contenido = ""
            caracteres = 0
            contar_caracteres = {}  # Inicializar un diccionario vacío para el conteo de caracteres
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                caracteres = len(contenido)
                # Calcular el conteo de caracteres utilizando Counter de collections
                contar_caracteres = Counter(contenido)
            
            ventana_info = Toplevel()
            ventana_info.title("Información del archivo")
            etiqueta_contenido = Label(ventana_info, text="Contenido del archivo:")
            etiqueta_contenido.pack()
            texto_contenido = Text(ventana_info, height=10, width=50)
            texto_contenido.insert(END, contenido)
            texto_contenido.pack()
            etiqueta_caracteres = Label(ventana_info, text=f"Número de caracteres: {caracteres}")
            etiqueta_caracteres.pack()
            etiqueta_conteo = Label(ventana_info, text="Conteo de caracteres:")
            etiqueta_conteo.pack()
            for letra, cantidad in contar_caracteres.items():
                etiqueta = Label(ventana_info, text=f"'{letra}': {cantidad}")
                etiqueta.pack()

    def comprimir_archivo(self):
        nombre_archivo = filedialog.askopenfilename()
        if nombre_archivo:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            bytes_comprimidos, tabla_codigos = self.arbol_huffman.comprimir(contenido)
            # Guardar el archivo comprimido
            ruta_comprimido = filedialog.asksaveasfilename(defaultextension=".bin")
            if ruta_comprimido:
                with open(ruta_comprimido, 'wb') as archivo_comprimido:
                    archivo_comprimido.write(bytes_comprimidos)
                    print("Archivo comprimido guardado:", ruta_comprimido)
                    print("Tabla de códigos Huffman:", tabla_codigos)

    def descomprimir_archivo(self):
        nombre_archivo = filedialog.askopenfilename()
        if nombre_archivo:
            with open(nombre_archivo, 'rb') as archivo:
                bytes_comprimidos = archivo.read()
            contenido_descomprimido = self.arbol_huffman.descomprimir(bytes_comprimidos)
            # Guardar el archivo descomprimido
            ruta_descomprimido = filedialog.asksaveasfilename(defaultextension=".txt")
            if ruta_descomprimido:
                with open(ruta_descomprimido, 'w', encoding='utf-8') as archivo_descomprimido:
                    archivo_descomprimido.write(contenido_descomprimido)
                    print("Archivo descomprimido guardado:", ruta_descomprimido)
                    print("Contenido descomprimido:", contenido_descomprimido)

InterfazHuffman()
