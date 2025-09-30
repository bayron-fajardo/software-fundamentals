class Mago:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 100
        
    
    def get_vida(self):
        return self.vida
    
    def get_mana(self):
        return self.mana
    
    def get_name(self):
        return self.nombre
    
    def set_vida(self,nueva_vida):
        self.vida = nueva_vida
        self.get_vida()

    def ataque_basico(self):
        self.vida = self.vida - 100
        if (self.get_vida()) == 0:
            print(f"{self.get_name()}")
        else:
            print(f"Ataque exitoso vida restante {self.get_vida()}")
        
mago = Mago("Bayron")
print(mago.get_vida())
print(mago.ataque_basico())
#print(mago.get_vida())