#Codigo hecho por Josué Avendaño Galarza
import tkinter as tk
from tkinter import filedialog
from collections import Counter

#Esta funcion es la que utilice la anterior clase para contar los caracteres
def contar_caracteres_lineas(archivo_entrada, archivo_salida):
    try: 
        with open(archivo_entrada, 'r', encoding='utf-8') as f_in: 
            contenido = f_in.readlines()  
            num_lineas = len(contenido)  
            contenido = ''.join(contenido)  
            frecuencia_caracteres = Counter(contenido)
            caracteres_ordenados = sorted(frecuencia_caracteres.items(), key=lambda x: x[1], reverse=True)  
            with open(archivo_salida, 'w', encoding='utf-8') as f_out:
                f_out.write("Caracteres ordenados por frecuencia:\n")
                print("Caracteres ordenados por frecuencia: ")
                for caracter, frecuencia in caracteres_ordenados:
                    print(f"{caracter}: {frecuencia}")
                    f_out.write(f"{caracter}: {frecuencia}\n")
                f_out.write(f"Número total de líneas: {num_lineas}\n")
                print(f"Numero total de lineas: {num_lineas}")  
            print(f"Resultados guardados en '{archivo_salida}'")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#Aqui esta funcion la cree para que pueda yo seleccionar el archivo txt que quiero que leea el codigo
def seleccionar_archivo(entrada=True):
    filename = filedialog.askopenfilename() if entrada else filedialog.asksaveasfilename()
    if filename:
        if entrada:
            archivo_entrada_entry.delete(0, tk.END)
            archivo_entrada_entry.insert(0, filename)
            # Mostrar contenido del archivo en el widget Text
            with open(filename, 'r', encoding='utf-8') as f:
                contenido = f.read()
                contenido_text.delete(1.0, tk.END)
                contenido_text.insert(tk.END, contenido)
        else:
            archivo_salida_entry.delete(0, tk.END)
            archivo_salida_entry.insert(0, filename)

def mostrar_resultados():
    archivo_entrada = archivo_entrada_entry.get()
    archivo_salida = archivo_salida_entry.get()
    contar_caracteres_lineas(archivo_entrada, archivo_salida)
    with open(archivo_salida, 'r', encoding='utf-8') as f:
        resultados = f.read()
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resultados)

#Aqui cree la ventana principal
root = tk.Tk()
root.title("Contador de Caracteres y Líneas")

#Cree el widget
tk.Label(root, text="Archivo de Entrada:").pack()
archivo_entrada_entry = tk.Entry(root, width=50)
archivo_entrada_entry.pack()
tk.Button(root, text="Seleccionar Archivo de Entrada", command=lambda: seleccionar_archivo(entrada=True)).pack()

#botones de Comprimir y Descomprimir (sin funciones por ahora)
tk.Button(root, text="Comprimir").pack()
tk.Button(root, text="Descomprimir").pack()

tk.Label(root, text="Contenido del Archivo de Entrada:").pack()
contenido_text = tk.Text(root, height=10, width=80)
contenido_text.pack()

tk.Label(root, text="Archivo de Salida:").pack()
archivo_salida_entry = tk.Entry(root, width=50)
archivo_salida_entry.pack()
tk.Button(root, text="Seleccionar Archivo de Salida", command=lambda: seleccionar_archivo(entrada=False)).pack()

tk.Button(root, text="Mostrar Resultados", command=mostrar_resultados).pack()
resultado_text = tk.Text(root, height=10, width=80)
resultado_text.pack()

root.mainloop()