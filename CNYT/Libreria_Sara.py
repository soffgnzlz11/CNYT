#Librería computación Cuántica: Números complejos
#Sara Spfia Gonzalez Mora

#Operaciones entre números complejos que contiene la libreria:

#Suma, Producto, Resta, División, Módulo, Conjugado, 
#Conversión entre representaciones polar y cartesiano, en los dos sentidos, Retornar la fase de un número complejo.

import math

def sumar(x, y):  
    "Suma números complejos."
    real1, imag1 = x     
    real2, imag2 = y     
    parte_rea = real1 + real2
    parte_imag = imag1 + imag2
    return (parte_rea, parte_imag)

def modulo(z):
    "Retorna el módulo"
    real, imag = z
    return math.sqrt(real**2 + imag**2)

def producto(x, y):
    "Realiza el producto"
    real1, imag1 = x     
    real2, imag2 = y  
    real_parte = (real1 * real2) - (imag1 * imag2)
    immag_parte = (real1 * imag2) + (real2 * imag1)
    return (real_parte, immag_parte)

def division(x, y):
    "Realiza la division de los complejos."
    real1, imag1 = x
    real2, imag2 = y
    
    denom = real2**2 + imag2**2  
    
    parte_real = (real1 * real2 + imag1 * imag2) / denom
    parte_imagi = (imag1 * real2 - real1 * imag2) / denom 
    
    return (parte_real, parte_imagi)

def restar(x, y):
    "Resta complejos."
    real1, imag1 = x
    real2, imag2 = y
    return (real1 - real2, imag1 - imag2)

def conjugado(z):
    "Conjugado: cambia signo de imaginaria."
    real, imag = z
    return (real, -imag)

def cartesiano_a_polar(z):
    "(real, imag) -> (modulo, fase)."
    real, imag = z
    modulo_z = math.sqrt(real**2 + imag**2)
    fase_z = math.atan2(imag, real)
    return (modulo_z, fase_z)

def fase(z):
    "Retorna solo la fase."
    return cartesiano_a_polar(z)[1]

def polar_a_cartesiano(p):
    "(modulo, fase) -> (real, imag)."
    mod, fase = p
    real = mod * math.cos(fase)
    imag = mod * math.sin(fase)
    return (real, imag)



