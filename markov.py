import random
import re
from collections import defaultdict, Counter
#import networkx as nx
#import matplotlib.pyplot as plt

# Paso 1: Leer y procesar el corpus
def leer_corpus(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        texto = file.read().lower()
    texto = re.sub(r'[^\w\sáéíóúüñ]', '', texto)  # Incluye acentos y ñ, excluye otros caracteres
    palabras = texto.split()
    return palabras

# Paso 2: Construir el modelo de Markov
def construir_modelo_markov(palabras):
    transiciones = defaultdict(list)
    for i in range(len(palabras) - 1):
        transiciones[palabras[i]].append(palabras[i + 1])
    return transiciones

# Generar texto usando el modelo de Markov
def generar_texto(modelo, palabra_inicial, longitud_texto):
    palabra_actual = palabra_inicial
    resultado = [palabra_actual]
    
    for _ in range(longitud_texto - 1):
        if palabra_actual not in modelo or not modelo[palabra_actual]:
            # Si no hay transiciones disponibles, elige una nueva palabra inicial aleatoria
            palabra_actual = random.choice(list(modelo.keys()))
        
        siguiente_palabra = random.choice(modelo[palabra_actual])
        resultado.append(siguiente_palabra)
        palabra_actual = siguiente_palabra
    
    return ' '.join(resultado)


# Mostrar probabilidades de transición
def mostrar_probabilidades(modelo):
    for palabra, transiciones in modelo.items():
        print(f"Palabra: '{palabra}'")
        conteos = {transicion: transiciones.count(transicion) for transicion in set(transiciones)}
        total = sum(conteos.values())
        probabilidades = {transicion: conteo / total for transicion, conteo in conteos.items()}
        texto = ""
        for siguiente_palabra, probabilidad in probabilidades.items():
            texto += f"  -> '{siguiente_palabra}': {probabilidad:.2f}\n"
        texto += "\n"
        return texto

# Mostrar estadísticas del corpus
def estadisticas_corpus(palabras):
    num_palabras = len(palabras)
    vocabulario = set(palabras)
    num_palabras_unicas = len(vocabulario)
    
    print("Estadísticas del Corpus:")
    print(f"Total de palabras: {num_palabras}")
    print(f"Total de palabras únicas: {num_palabras_unicas}")
    print(f"Ejemplo de palabras en el vocabulario: {list(vocabulario)[:10]}")

# Calcular y mostrar las frecuencias de las palabras
def frecuencias_palabras(palabras):
    conteo_palabras = Counter(palabras)
    palabras_comunes = conteo_palabras.most_common(10)  # Las 10 palabras más comunes
    
    texto = ""
    for palabra, frecuencia in palabras_comunes:
        texto += f"'{palabra}': {frecuencia} veces"
    
    return texto
'''
# Visualizar la cadena de Markov
def visualizar_markov(modelo):
    G = nx.DiGraph()
    for palabra, transiciones in modelo.items():
        conteos = {transicion: transiciones.count(transicion) for transicion in set(transiciones)}
        for siguiente_palabra, conteo in conteos.items():
            G.add_edge(palabra, siguiente_palabra, weight=conteo)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Visualización de la Cadena de Markov")
    plt.show()
'''
# Ejemplo de uso
if __name__ == "__main__":
    ruta_archivo = 'corpus.txt'  # Reemplaza con la ruta de tu archivo de texto
    
    # Leer el corpus
    palabras = leer_corpus(ruta_archivo)
    
    # Mostrar estadísticas del corpus
    estadisticas_corpus(palabras)
    
    # Construir el modelo de Markov
    modelo_markov = construir_modelo_markov(palabras)
    
    # Mostrar probabilidades de transición
    mostrar_probabilidades(modelo_markov)
    
    # Generar y mostrar el texto
    palabra_inicial = random.choice(palabras)
    texto_generado = generar_texto(modelo_markov, palabra_inicial, 100)  # Generar 100 palabras
    print("Texto generado por el modelo de Markov:")
    print(texto_generado)
    
    # Mostrar frecuencias de las palabras
    frecuencias_palabras(palabras)
    
    # Visualizar la cadena de Markov
    #visualizar_markov(modelo_markov)
