class Casa:
    def __init__(self):
        self.medida = "20mt2"
        self.color = "blanco"
        self.direccion = "cra 12 No 34 -56"
        self.propietario = "Edward Bustos"
        self.numero_ocupantes = 5
        self.photo = "c:/documentos/foto"

    def agregar_ocupantes(self, num_personas):
        self.numero_ocupantes = self.numero_ocupantes+num_personas
    
    def quitar_ocupantes(self, num_personas):
        self.numero_ocupantes = self.numero_ocupantes-num_personas

    def sonar_alarma(self):
        print("ui ui ui ui ui ui ui")
    