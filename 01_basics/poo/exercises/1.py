import random

class Mago:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 100
        self.turno = False
        self.defensa = False
        self.parry = False
        
    def get_vida(self):
        return self.vida
    
    def get_mana(self):
        return self.mana
    
    def get_name(self):
        return self.nombre
    
    def set_vida(self, nueva_vida):
        self.vida = nueva_vida

    def ataque_basico(self, enemigo):
        if self.get_mana() >= 10:
            if random.random() > 0.03:
                enemigo.vida -= 16
                self.mana -= 10
            else:
                enemigo.vida -= 10
                self.mana -= 10
                
            if enemigo.get_vida() <= 0:
                return f"El mago {self.get_name()} ha derrotado a {enemigo.get_name()}"
            else:
                return f"Ataque exitoso, vida restante del enemigo: {enemigo.get_vida()}"
        else:
            return f"Mago {self.get_name()}: Insuficiente maná para atacar"
    
    def turno(mago1,mago2):
        if (random.random() > 0.5):
            mago1.turno = True
        else:
            mago2.turno = True
            
            
mago1 = Mago("Bayron")
mago2 = Mago("Kevin")

while mago1.get_vida() > 0 and mago2.get_vida() > 0:
    print(mago1.get_vida())
    print(mago1.ataque_basico(mago2))
    print(f"Mana restante: {mago1.get_mana()}")
    if mago2.get_vida() <= 0:
        break
    print(mago2.get_vida())
    print(mago2.ataque_basico(mago1))
    print(f"Mana restante: {mago2.get_mana()}")
    if mago1.get_vida() <= 0:
        break
