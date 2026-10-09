"""
====================================================================
  EJERCICIOS DE FUNCIONES EN PYTHON
  #Jesus Arriaga 
  # NC = 0019
  Asignación : Número 5 de lista
  Contenido  : 6 Ejemplos de El Pythonista + 5 Ejemplos de Pythones
====================================================================
"""

import sys

# ==================================================================
# FUNCIONES AUXILIARES PARA FORMATO DE CONSOLA
# ==================================================================

def imprimir_titulo(numero, titulo, fuente):
    """Genera una cabecera limpia para separar visualmente cada ejemplo."""
    print("\n" + "=" * 65)
    print(f" EJEMPLO {numero:02d} | [{fuente.upper()}] {titulo}")
    print("=" * 65)


# ==================================================================
# BLOQUE 1: EJEMPLOS DE EL PYTHONISTA (Ejemplos 01 al 06)
# ==================================================================

# --- Ejemplo 01: Sintaxis básica ---
def saludar():
    """Imprime un saludo simple en consola."""
    print("  ▶ ¡Hola, mundo desde una función básica!")

def ejec_ejemplo_01():
    imprimir_titulo(1, "Sintaxis básica de una función", "El Pythonista")
    saludar()


# --- Ejemplo 02: Parámetros posicionales y keyword ---
def crear_usuario(nombre, edad, ciudad):
    """Devuelve una cadena formateada con los datos del usuario."""
    return f"  • Usuario: {nombre:<10} | Edad: {edad:<3} | Ciudad: {ciudad}"

def ejec_ejemplo_02():
    imprimir_titulo(2, "Parámetros posicionales y Keyword Arguments", "El Pythonista")
    print(crear_usuario("Ana", 25, "Madrid"))
    print(crear_usuario(nombre="Carlos", edad=30, ciudad="Barcelona"))
    print(crear_usuario(ciudad="Valencia", nombre="Laura", edad=28))


# --- Ejemplo 03: Retorno múltiple ---
def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo de una lista."""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo

def ejec_ejemplo_03():
    imprimir_titulo(3, "Retorno múltiple de valores (Tuplas)", "El Pythonista")
    datos = [10, 20, 30, 40, 50]
    suma, prom, max_val = calcular_estadisticas(datos)
    
    print(f"  • Datos evaluados : {datos}")
    print(f"  • Suma Total      : {suma}")
    print(f"  • Promedio        : {prom:.2f}")
    print(f"  • Valor Máximo    : {max_val}")


# --- Ejemplo 04: *args y **kwargs ---
def funcion_completa(param_obligatorio, param_opcional="Predeterminado", *args, **kwargs):
    """Demuestra el uso de *args y **kwargs."""
    print(f"  • Obligatorio          : {param_obligatorio}")
    print(f"  • Opcional             : {param_opcional}")
    print(f"  • Posicionales (*args) : {args}")
    print(f"  • Claves (**kwargs)    : {kwargs}")

def ejec_ejemplo_04():
    imprimir_titulo(4, "Uso de *args y **kwargs", "El Pythonista")
    funcion_completa(
        "Obligatorio1", 
        "Opcional2", 
        "Extra_1", "Extra_2", 
        rol="Admin", activo=True
    )


# --- Ejemplo 05: Funciones anidadas y Closures ---
def crear_multiplicador(factor):
    """Retorna una función que multiplica por un factor específico."""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

def ejec_ejemplo_05():
    imprimir_titulo(5, "Funciones anidadas y Closures", "El Pythonista")
    duplicar = crear_multiplicador(2)
    triplicar = crear_multiplicador(3)
    
    val = 10
    print(f"  • Valor base : {val}")
    print(f"  • Duplicar   : {duplicar(val)}")
    print(f"  • Triplicar  : {triplicar(val)}")


# --- Ejemplo 06: Casos prácticos de validación y filtrado ---
def validar_email(email):
    """Valida si un correo contiene '@' y un dominio válido."""
    return "@" in email and "." in email.split("@")[1]

def filtrar_pares(numeros):
    """Filtra y devuelve solo los números pares."""
    return [num for num in numeros if num % 2 == 0]

def ejec_ejemplo_06():
    imprimir_titulo(6, "Casos prácticos: Validación y Filtrado", "El Pythonista")
    
    correos = ["usuario@ejemplo.com", "correo_invalido.com"]
    for c in correos:
        estado = "VÁLIDO" if validar_email(c) else "INVÁLIDO"
        print(f"  • Email '{c}': {estado}")
        
    numeros = list(range(1, 11))
    print(f"  • Lista original : {numeros}")
    print(f"  • Filtro de pares: {filtrar_pares(numeros)}")


# ==================================================================
# BLOQUE 2: EJEMPLOS DE PYTHONES (Ejemplos 07 al 11)
# ==================================================================

# --- Ejemplo 07: Funciones Built-in ---
def ejec_ejemplo_07():
    imprimir_titulo(7, "Funciones incorporadas (Built-in)", "Pythones")
    texto = "Python"
    nums = [5, 10, 15, 20]
    
    print(f"  • Longitud de '{texto}' len() : {len(texto)}")
    print(f"  • Tipo de dato type()      : {type(texto).__name__}")
    print(f"  • Suma de lista sum()      : {sum(nums)}")


# --- Ejemplo 08: Definición y retorno explícito ---
def suma_basica(a, b):
    return a + b

def ejec_ejemplo_08():
    imprimir_titulo(8, "Definición y retorno con return", "Pythones")
    res = suma_basica(12, 8)
    print(f"  • Resultado de suma_basica(12, 8): {res}")


# --- Ejemplo 09: Diferencia entre print() y return ---
def funcion_imprime(a, b):
    print(f"    [Ejecutando print dentro de la función]: {a + b}")

def funcion_retorna(a, b):
    return a + b

def ejec_ejemplo_09():
    imprimir_titulo(9, "Diferencia entre print() y return", "Pythones")
    
    print("  1. Llamando a funcion_imprime(5, 5):")
    val_print = funcion_imprime(5, 5)
    print(f"     Valor capturado en la variable: {val_print} (None)")
    
    print("\n  2. Llamando a funcion_retorna(5, 5):")
    val_return = funcion_retorna(5, 5)
    print(f"     Valor capturado en la variable: {val_return}")


# --- Ejemplo 10: Inspección con dir() y help() ---
def ejec_ejemplo_10():
    imprimir_titulo(10, "Exploración de código (dir y help)", "Pythones")
    
    metodos_str = [m for m in dir(str) if not m.startswith("__")][:5]
    print(f"  • Primeros 5 métodos de 'str': {metodos_str}")
    print("  • Documentación abreviada de abs():")
    print("    " + repr(abs.__doc__))


# --- Ejemplo 11: Calculadora estructurada ---
def calc_sumar(a, b): return a + b
def calc_restar(a, b): return a - b
def calc_multiplicar(a, b): return a * b
def calc_dividir(a, b): return a / b if b != 0 else "Error (División por 0)"

def ejec_ejemplo_11():
    imprimir_titulo(11, "Calculadora modular con funciones", "Pythones")
    a, b = 15, 3
    
    print(f"  • Operando A: {a} | Operando B: {b}")
    print(f"    - Suma           : {calc_sumar(a, b)}")
    print(f"    - Resta          : {calc_restar(a, b)}")
    print(f"    - Multiplicación : {calc_multiplicar(a, b)}")
    print(f"    - División       : {calc_dividir(a, b)}")
    print(f"    - Div. por Cero  : {calc_dividir(a, 0)}")


# ==================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# ==================================================================

def ejecutar_todos():
    """Ejecuta todos los ejercicios en orden secuencial."""
    ejec_ejemplo_01()
    ejec_ejemplo_02()
    ejec_ejemplo_03()
    ejec_ejemplo_04()
    ejec_ejemplo_05()
    ejec_ejemplo_06()
    ejec_ejemplo_07()
    ejec_ejemplo_08()
    ejec_ejemplo_09()
    ejec_ejemplo_10()
    ejec_ejemplo_11()
    print("\n" + "=" * 65)
    print("  ✔ FIN DE LA EJECUCIÓN DE TODOS LOS EJERCICIOS")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    ejecutar_todos()
    print("programa realizado por Jesus Arriaga 0019")