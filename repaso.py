from objetos import Casa
personas = ["Deya","Leidy","Edward","Nata","Samantha"]
tuples = (1,2,3,6)

def saludar(persona):
    print(f"Hola querido {persona}")    
    for letras in persona:
        if(["a","e","i","o","u"].__contains__(letras)):
            print(letras)
    return len(persona)

longitud = saludar("un nombre muy largo")

print(longitud)
print("una nueva linea")

casa3 = Casa()