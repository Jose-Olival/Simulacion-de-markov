from tkinter import *
import tkinter as tk
import markov  as sim
import random

#Funciones de los botones 

def generar(textarea1, textarea2):
    ruta_archivo = 'corpus.txt'
    palabras = sim.leer_corpus(ruta_archivo)
    
    # Mostrar estadísticas del corpus
    sim.estadisticas_corpus(palabras)
    
    # Construir el modelo de Markov
    modelo_markov = sim.construir_modelo_markov(palabras)
    
    # Generar y mostrar el texto
    palabra_inicial = random.choice(palabras)
    texto_generado = sim.generar_texto(modelo_markov, palabra_inicial, 100)  # Generar 100 palabras
    
    textarea1.insert(tk.END, texto_generado)
    
    # Mostrar frecuencias de las palabras
    texto = sim.frecuencias_palabras(palabras)

    textarea2.insert(tk.END, texto)

def limpiar(textarea1, textarea2):
    textarea1.delete("1.0", tk.END)
    textarea2.delete("1.0", tk.END)
    

Ventana_principal = Tk()
Ventana_principal.title("MODELO MARKOV")
Ventana_principal.resizable(False, False)

# Panel principal de la ventana
panel_principal = Frame(Ventana_principal)
panel_principal.configure(width=1200, height=540,background="snow")
panel_principal.pack(fill="both", expand="True")

frame1 = Frame(panel_principal)
frame1.configure(width=1200, height=80, background="steel blue")
frame1.place(x=0, y=0)

titulo = Label(frame1)
titulo.configure(text="MODELO MARKOV DE SIMULACIÓN", font=("Arial", 25, "bold"), foreground="cyan", background="steel blue")
titulo.place(x=300, y=18)

frame2 = Frame(panel_principal)
frame2.configure(width=400, height=460, background="lavender")
frame2.place(x=0, y=80)

texto_palabras = Label(frame2)
texto_palabras.configure(text="Total de palabras: 123", font=("Arial", 15, "bold"), foreground="black", background="lavender")
texto_palabras.place(x=20, y=120)

texto_palabras_unicas = Label(frame2)
texto_palabras_unicas.configure(text="Total de palabras únicas: 79", font=("Arial", 15, "bold"), foreground="black", background="lavender")
texto_palabras_unicas.place(x=20, y=180)

texto_palabras_ejemplo = Label(frame2)
texto_palabras_ejemplo.configure(text="Ejemplo de palabras en el vocabulario", font=("Arial", 15, "bold"), foreground="black", background="lavender")
texto_palabras_ejemplo.place(x=20, y=240)

area_palabras_ejemplo = Text(Ventana_principal)
area_palabras_ejemplo.configure(height=5, width=32, font=("Arial", 15), foreground="black", border=1, relief="solid")
area_palabras_ejemplo.place(x=20, y=360)

texto_area_palabras = Label(Ventana_principal)
texto_area_palabras.configure(text="Texto Generado por el modelo de Markov", font=("Arial", 15, "bold"), foreground="black", background="snow")
texto_area_palabras.place(x=420, y=120)

area_parrafo = Text(Ventana_principal)
area_parrafo.configure(height=16, width=67, font=("Arial", 14), foreground="black", border=2, relief="solid")
area_parrafo.place(x=430, y=150)

boton_iniciar = Button(frame2)
boton_iniciar.configure(text="Iniciar", cursor="hand2", font=("Arial", 16), width=10, background="deep sky blue", command=lambda: generar(area_parrafo, area_palabras_ejemplo))
boton_iniciar.place(x=50, y=50)

boton_borrar = Button(frame2)
boton_borrar.configure(text="Borrar", cursor="hand2", font=("Arial", 16), width=10, background="deep sky blue", command=lambda: limpiar(area_parrafo, area_palabras_ejemplo))
boton_borrar.place(x=210, y=50)

texto_integrantes = Label(Ventana_principal)
texto_integrantes.configure(text="Integrantes \n Jose Olival 30281014  Stalin Salazar 25107117 \n Samir Abder 30334483  Flavio Franchich 30020789 \n Neil Rangel 30638786", font=("Arial", 12), foreground="black", background="lavender")
texto_integrantes.place(x=0, y=480)

Ventana_principal.mainloop()
