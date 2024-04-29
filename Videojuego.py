import random

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza  = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre,":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".inteligencia:", self.inteligencia)
        print(".Defensa", self.defensa)
        print(".Vida", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
            
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.espada_especial = False
        
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valkyrio, daño 8. (2) Matadragones, daño 10. (3) Sable oscuro daño 8: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        elif opcion == 3:
            self.espada = 8
            self.espada_especial = True
        else:
            print("Número de arma incorrecto o no existe")
 
    def atributos(self):
        super().atributos()
        print(".Espada:", self.espada)
        
    def daño (self, enemigo):
       # return self.fuerza*self.espada - enemigo.defensa
        daño_base = self.fuerza * self.espada
        if self.espada_especial:
            daño_base += 3
        return daño_base - enemigo.defensa
 
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    def atributos(self):
        super().atributos()
        print(".Libro", self.libro)
        
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
class Witch(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, magia):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.magia = magia
        
    def atributos(self):
        super().atributos()
        print(".magia", self.magia)
        
    def daño(self, enemigo):
        return self.inteligencia*self.magia - enemigo.defensa
    
    def recuperar_vida(self):
        if self.vida <= 100:
            self.vida += self.vida_plus
            print(f"{self.nombre} ha recuperado {self.vida_plus} puntos de vida.")
    
            
class Oni(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, coraza):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.coraza = coraza
        
    def atributos(self):
        super().atributos()
        print(".coraza", self.coraza)
        
    def defensa_ex(self, Personaje):
        return self.defensa*self.coraza + Personaje.defensa
    
    def recuperar_vida(self):
        if self.vida <= 100:
            self.vida += self.vida_plus
            print(f"{self.nombre} ha recuperado {self.vida_plus} puntos de vida.")
    
class Zombie(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, vida_plus):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.vida_plus = vida_plus
        
    def atributos(self):
        super().atributos()
        
    def recuperar_vida(self):
        if self.vida <= 100:
            self.vida += self.vida_plus
            print(f"{self.nombre} ha recuperado {self.vida_plus} puntos de vida.")
      
      
per_1 = Guerrero("Guts", 20, 50, 4, 200, 3)
per_1.cambiar_arma()

oni_1 = Oni("Oni", 30, 5, 5, 450, 5)
zombie = Zombie("Zombi", 6, 5, 7, 1000, 100)
zombie_2 = Zombie("Zombi jefe", 6, 5, 7, 1000, 200)

witch_1 = Witch("Witch", 20, 9, 5, 500, 10)
witch_2 = Witch("Witch jefa", 20, 12, 6, 550, 11)

#enemigos secundarios
rat = Personaje("rata", 5, 1, 3, 50)
murc = Personaje("rata", 7, 1, 6, 70)
cuervo = Personaje("rata", 5, 1, 5, 70)

enemigos = [rat, murc, cuervo, oni_1, zombie, zombie_2, witch_2, witch_1] 

def combate(jug_1, enemigos):
    turno = 0
    enemigo = random.choice(enemigos)
    print("combatiras contra: ", enemigo.nombre)
    while jug_1.esta_vivo() and enemigo.esta_vivo():
        print("\n Turno", turno)
        if not jug_1.esta_vivo() or not enemigo.esta_vivo():
            break
        print(">>> Acción de ", jug_1.nombre, ":", sep="")
        jug_1.atacar(enemigo)
        if not jug_1.esta_vivo() or not enemigo.esta_vivo():
            break
        print(">>> Acción de ", enemigo.nombre, ":", sep="")
        enemigo.atacar(jug_1)
        enemigo.recuperar_vida()
        turno +=1
        
    if jug_1.esta_vivo():
        print("\n Ha ganado", jug_1.nombre)
    elif enemigo.esta_vivo():
        print("\n Ha ganado", enemigo.nombre)
    else:
        print("\n Empate")
        
def Seguir():
  
        
    while True:
        desicion = input("¿Quieres seguir combatiendo? (s/n): ").lower()
        if desicion == "s":
            combate(per_1, enemigos)
        elif desicion == "n":
            print("Gracias por jugar.")
            break
        else:
           print("Por favoir, introduce 's' para sí o 'n' para no")


combate(per_1, enemigos)
Seguir()

        
#goku = Personaje ("Goku", 20, 15, 10, 100)
#guts = Guerrero ("Guts", 20, 15, 10, 100, 5)
#vanessa = Mago ("Vanessa", 20, 15, 10, 100, 5)
#goku.atacar(guts)
#guts.atacar(vanessa)
#vanessa.atacar(goku)
#goku.atributos()
#guts.atributos()
#vanessa.atributos()

