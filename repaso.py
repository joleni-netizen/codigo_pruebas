from objetos import Casa
personas = ["Deya","Leidy","Edward","Nata","Samantha"]
tuples = (1,2,3,6)

def saludar(persona):
    print(f"Hola querido {persona}")    
    for letras in persona:
        if(["a","e","i","o","u"].__contains__(letras)):
            print(letras)
    return len(persona)

# for persona in personas:
#     print(saludar(persona))

longitud = saludar("un nombre muy largo")
print(longitud)

casa3 = Casa()