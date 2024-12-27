from random import randint
import random
import sys

"""
Cyril Mathé
Arthur Boutry
"""

class mob :
    def __init__(self,name,health,level,attack,defense,strenght,loot):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.strenght = strenght
        self.loot = loot

mob1 = mob("Koala",20,1,["coup de patte",60,20,4],2,2,"")
mob2 = mob("Paresseux",30,2,["griffes",80,20,6],2,2,"")
mob3 = mob("Macaque",45,3,["morsure",55,50,12],5,5,"")
mob4 = mob("BOSS ! - Serpent géant",160,5,["crachat de venin",60,70,15],8,8,"")

my_list = [mob1, mob2, mob3]
aléatoire = random.choice(my_list)
instance = aléatoire.name

class object :
    def __init__(self,name,power,type):
        self.name = name
        self.power = power
        self.type = type

    def use(self,player):
        if type == "health":
            player.health += self.power
        if type == "defense":
            player.defense += self.power                  # fonction pour utiliser un objet, vérifie le type de l'objet et effectue l'action en fonction du type
        if type == "strenght":
            player.strenght += self.power

class weapon :
    def __init__(self,name,power,attack):
        self.name = name
        self.power = power
        self.attack = attack
    
    def use (self,player):
        player.attack_list.append(self.attack)            # fonction ajoutant une attaque à la liste du personnage

class attack :
    def __init__(self,name,hit_chance,damage,crit_chance,use_number):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage
        self.crit_chance = crit_chance
        self.use_number = use_number

    def calculate_damage(self):
        percent = randint(1,100)
        crit = randint(1,100)
        if percent > self.hit_chance or self.use_number == 0:                   # fonction calculant si une attaque atteint sa cible et si cette attaque est un coup critique puis renvoie les dégâts infligés
            return 0
        else:
            if crit > self.hit_chance:
                return self.damage * 1.5
            else:
                return self.damage
            
    def attack_description(self):
        pass
      
class player :
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.inventory = [object("potion de soin","health",25),object("bandage","health",15),object("taseur à utilisation unique","strenght",50)]
        self.attack_list = [attack("coup de couteau",80,15,10,15),attack("saignement",70,25,45,10)]
        self.strength = 15
        self.defense = 15
        self.experience = 0
        self.level = 1
        self.position = 'c3'

    def choose_attack(self):
        for attack in self.attack_list:
            print(attack.name)
        choice = input()
        for attack in self.attack_list:                          # fonction permettant de choisir une attaque dans la liste d'attaques du joueur
            if attack.name == choice:
                damage = attack.calculate_damage()
                print("Dégats : " + str(damage))
                global current_mob_health
                current_mob_health = (current_mob_health - damage)
                if current_mob_health <= 0:
                    current_mob_health = 0
                    print(str(aléatoire.name) + " Vie : " + str(current_mob_health))
                    return current_mob_health
                else:
                    print(str(aléatoire.name) + " Vie : " + str(current_mob_health))
                    return current_mob_health
    
    def mob_attack(self):
        global current_player_health
        current_player_health = (current_player_health - aléatoire.strenght)
        print(aléatoire.name + " utilise " + str(aléatoire.attack))
        print(player1.name + " Vie : " + str(current_player_health))
        return current_player_health

    def open_inventory(self):
        print("\nTu as " + str(self.health) + " point de vie !\n")
        for object in self.inventory:                         # fonction permettant d'afficher l'inventaire et d'utiliser un objet
            print(object.name)
        print("\nRetouner au menu\n")
        print("Quel object voulez vous utiliser ?")
        choice = input()
        selected_object = None
        for object in self.inventory:
            if object.name.lower() == choice.lower():
                selected_object = object
            break
        if choice == "potion de soin" or choice == "bandage" or choice == "taseur a utilisation unique":
            object.use(self)
            self.inventory.remove(selected_object)
            print(choice + " a été utilisé(e)")
            print(current_player_health)
            prompt()
        else:
            prompt()

    def use_object(self):                          # fonction permettant d'utiliser un objet qui se situe dans l'inventaire puis le supprime de l'inventaire
        object.use()
        player1.inventory.remove(object)
        print(object.name + " a été utilisé")
        print(current_player_health)
        prompt()

    def death(self):
        print("Vous êtes mort !")                               # fonction qui mets un terme à la partie si on meurt
        print("Merci d'avoir jouer")

    def roll(self):
        print("Vous effectuez une roulade et esquivez l'attaque de " + aléatoire.name)         # fonction pour esquiver une attaque

    def run_away(self):
        print("Vous essayez de fuir")
        percent = randint(1,100)
        if percent > 75:                                         # fonction pour tenter de prendre la fuite
            print("Vous vous êtes enfui")
            prompt()
        else:
            print("Vous n'avez pas réussi a vous enfuir")
            self.mob_attack()

    def reset(self):
        global current_mob_health
        current_mob_health = aléatoire.health
    
    def reset_mob(self):
        global my_list
        global aléatoire
        aléatoire = random.choice(my_list)

    def experience_gained(self):
        global current_xp
        xp_from_mob = randint(1,60)
        current_xp += xp_from_mob
        if current_xp >= 50:
            print("Experience : +" + str(current_xp))				# fonction qui gére l'éxpérience gagner
            current_xp -= 50
            player1.level += 1
            player1.health += 10
            return current_xp
        else:
            print("Experience : +" + str(current_xp))
            return current_xp

    def combat(self):
        print(aléatoire.name + " vous attaque !")
        while player1.health > 0 and current_mob_health > 0:
            self.combat_interface()
            choice = input("=> ")
            if choice != "2" and choice !="4": self.mob_attack()
            match choice:
                case "1" | "Attaques" | "attaques": self.choose_attack()                 # fonction qui gére le combat
                case "2" | "Roulade" | "roulade": self.roll()
                case "3" | "Inventaire" | "inventaire": self.use_object()
                case "4" | "Fuir" | "fuir": self.run_away()
        if player1.health <= 0:
            self.death()
        else:
            print("Vous avez vaincu " + aléatoire.name)
            player1.reset()
            player1.reset_mob()
            player1.experience_gained()
            prompt()

    def combat_interface(self):
        print(player1.name + " Vie : " + str(current_player_health) + " Level : " + str(player1.level) + " Experience : " + str(current_xp) + " / 50 " + " VS " + aléatoire.name + " Vie : " + str(current_mob_health))
        print("Que voulez vous faire ?")
        print("1 - Attaques")
        print("2 - Roulade")                                # fonction qui affiche le menu interactif pendant le combat
        print("3 - Inventaire")
        print("4 - Fuir")

current_mob_health = aléatoire.health


################### MAP #####################

"""
Début en c3
a1  a2 a3 a4 a5
----------------
|  |  |  |  |  | a
----------------
|  |  |  |  |  | b
----------------
|  |  | c3 |  |  | c
----------------
|  |  |  |  |  | d
----------------
|  |  |  |  |  |  e
----------------
"""

ZONENAME = ""
DESCRIPTION = 'description'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

zonemap = {
    'a1': {
        ZONENAME: "Le Gouffre de l’Oubli",
        DESCRIPTION: 'Une faille béante au centre de l’île, remplie de brume scintillante. On dit que les murmures des disparus s’élèvent des profondeurs.',
        UP: "",
        DOWN: 'b1',
        LEFT: "",
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "La Forêt des Murmures",
        DESCRIPTION: 'Une jungle dense où les arbres semblent chuchoter aux visiteurs, leurs feuilles bruissant de secrets anciens.',
        UP: "",
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "La Plage des Os Blanchis",
        DESCRIPTION: 'Une étendue de sable où reposent les carcasses de créatures marines titanesques.',
        UP: "",
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "L’Œil du Cyclone",
        DESCRIPTION: 'Un lac circulaire aux eaux étrangement calmes, entouré par des vents violents.',
        UP: "",
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: 'a5',
    },
    'a5': {
        ZONENAME: "Le Pic des Cendres",
        DESCRIPTION: 'Un volcan éteint, dont les flancs noirs et craquelés suintent une chaleur surnaturelle.',
        UP: "",
        DOWN: 'b5',
        LEFT: 'a4',
        RIGHT: "",
    },
    'b1': {
        ZONENAME: "Les Rochers Chantants",
        DESCRIPTION: 'Des formations rocheuses au bord de l’eau qui produisent des sons mélodieux quand le vent souffle.',
        UP: 'a1',
        DOWN: 'c1',
        LEFT: "",
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "La Lagune des Étoiles",
        DESCRIPTION: 'Une lagune phosphorescente qui s’illumine comme un ciel étoilé lorsque la nuit tombe.',
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'Le Labyrinthe de l’Épine',
        DESCRIPTION: 'Un réseau de ronces géantes formant un dédale inextricable, protégé par des créatures venimeuses.',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "La Grotte des Échos Perdus",
        DESCRIPTION: 'Une caverne où chaque son se réverbère éternellement, rendant toute conversation dangereuse.',
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: 'b5',
    },
    'b5': {
        ZONENAME: "Le Rivage des Larmes Salées",
        DESCRIPTION: 'Une baie tranquille où l’eau a une étrange couleur argentée, chargée de légendes tragiques.',
        UP: 'a5',
        DOWN: 'c5',
        LEFT: 'b4',
        RIGHT: "",
    },
    'c1': {
        ZONENAME: "La Tour des Nuées",
        DESCRIPTION: 'Un piton rocheux si haut qu’il disparaît dans les nuages, habité par des oiseaux géants.',
        UP: 'b1',
        DOWN: 'd1',
        LEFT: "",
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "Le Jardin des Lunes",
        DESCRIPTION: 'Un champ d’herbes et de fleurs luminescentes, parfait pour se perdre dans une lumière surnaturelle.',
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: 'Home',
        DESCRIPTION: 'You are at your home',
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "Le Cimetière des Géants",
        DESCRIPTION: 'Un endroit où reposent les ossements de créatures colossales, vestiges d’une époque oubliée.',
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c5',
    },
    'c5': {
        ZONENAME: "Le Roc du Désespoir",
        DESCRIPTION: 'Un promontoire solitaire où des marins désespérés laissaient des offrandes pour calmer les dieux de la mer.',
        UP: 'b5',
        DOWN: 'd5',
        LEFT: 'c4',
        RIGHT: "",
    },
    'd1': {
        ZONENAME: "Les Ruines de l’Aube Éternelle",
        DESCRIPTION: 'Les vestiges d’une cité antique, éternellement baignés d’une lumière dorée.',
        UP: 'c1',
        DOWN: 'e1',
        LEFT: "",
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "Le Marais des Souvenirs",
        DESCRIPTION: 'Une étendue boueuse où des visions du passé se reflètent sur la surface des eaux troubles.',
        UP: 'c2',
        DOWN: 'e2',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "La Faille d’Obsidienne",
        DESCRIPTION: 'Une crevasse noire et luisante, réputée pour abriter des trésors et des créatures mythiques.',
        UP: 'c3',
        DOWN: 'e3',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "Le Sanctuaire des Vents Hurleurs",
        DESCRIPTION: 'Un plateau balayé par des vents si puissants qu’ils forment des mélodies surnaturelles.',
        UP: 'c4',
        DOWN: 'e4',
        LEFT: 'd3',
        RIGHT: 'd5',
    },
    'd5': {
        ZONENAME: "Les Dunes Sifflantes",
        DESCRIPTION: 'Un désert où chaque pas déclenche un sifflement étrange, comme si le sable était vivant.',
        UP: 'c5',
        DOWN: 'e5',
        LEFT: 'd4',
        RIGHT: "",
    },
    'e1': {
        ZONENAME: "L’Arbre des Âmes ",
        DESCRIPTION: 'Un arbre gigantesque dont les racines s’enroulent autour de crânes anciens, dégageant une aura mystique.',
        UP: 'd1',
        DOWN: "",
        LEFT: "",
        RIGHT: 'e2',
    },
    'e2': {
        ZONENAME: 'Les Falaises du Vide',
        DESCRIPTION: 'Des parois abruptes qui semblent plonger dans un abîme infini, hantées par des ombres mouvantes.',
        UP: 'd2',
        DOWN: '',
        LEFT: 'e1',
        RIGHT: 'e3',
    },
    'e3': {
        ZONENAME: "Le Temple Submergé",
        DESCRIPTION: 'Un édifice ancien enfoui sous les eaux, accessible uniquement à marée basse.',
        UP: 'd3',
        DOWN: "",
        LEFT: 'e2',
        RIGHT: 'e4',
    },
    'e4': {
        ZONENAME: "La Baie de l’Inconnu",
        DESCRIPTION: 'Un port naturel où des épaves d’origines variées s’entassent, vestiges de marins perdus.',
        UP: 'd4',
        DOWN: "",
        LEFT: 'e3',
        RIGHT: 'e5',
    },
    'e5': {
        ZONENAME: "Le Pont Suspendu",
        DESCRIPTION: 'Un ancien pont de lianes traversant un gouffre, semblant tenir grâce à une magie oubliée.',
        UP: 'd5',
        DOWN: "",
        LEFT: 'e4',
        RIGHT: "",
    }
}

###############################################

def start_game():
    print(('-' * 50) + '\n')
    print(' ' *7 +"Bienvenu dans notre RPG textuel \n")
    print('-' * 50 + '\n')
    print(' '* 12 + ("    - Play -    ") + ' ' * 5)
    print(' '* 12 + ("    - About -    ") + ' ' * 5)
    print(' '* 12 + ("    - Quit -    ") + ' ' * 5 + '\n')
    print(('-' * 50) + '\n')
    game_select()
	
def game_select():
	answer = input('>>>   ')
	if answer == "play" or answer == "Play" :
		setup()
	elif answer == "About" or answer == "about":
		about()
	elif answer == "Quit" or answer == "quit" :
		sys.exit()

def about():
    print('\n' + '='*19 + "  A propos  " + '='*19 + '\n'+ '\n')
    print('   Pojet réalisé par Cyril Mathé et Arthur Boutry ' + '\n')
    print("Projet RPG python réalisé dans le cadre d'un projet\nd'école HETIC" + '\n')
    print('\n'+ '\n')
    start_game() 

def print_location():
    print('\n' + (' #' * (11 + len(player1.position))))
    print('# ' + (zonemap[player1.position][ZONENAME]) + ' #')                          # fonction de d'affichage de map qui boucle 
    print(' #' * (11 + len(player1.position)))
    print('\n' + (zonemap[player1.position][DESCRIPTION]))
    prompt()
    
def prompt():
    print("\nQue veux-tu faire ?\n")
    print("Vous avez le choix entre :\nAvancer, \nOuvrir l'inventaire, \nCombattre\n")
    action = input(">>>   ")
    acceptable_actions = ['avancer', 'partir', 'quitter', "ouvrir l'inv", 'inventaire', "ouvrir l'inventaire", "combattre"]

    while action.lower() not in acceptable_actions:
        print("Erreur réponse incorrecte\n")
        action = input(">>>   ")

    if action.lower() == 'quitter':                                                     # fonction de jeu qui boucle 
        sys.exit()
    elif action.lower() in ['avancer', 'partir']:
        move(action.lower())
    elif action.lower() in ["ouvrir l'inv", 'inventaire', "ouvrir l'inventaire"]:
        player1.open_inventory()
    elif action.lower() == "combattre":
        player1.combat()

def move(myAction):
	askString = "Où est ce que tu aimerais "+myAction+"?\n> "
	print("Direction possible : " + zonemap[player1.position][UP],zonemap[player1.position][DOWN],zonemap[player1.position][LEFT],zonemap[player1.position][RIGHT] )
	destination = input(askString)
	if destination == zonemap[player1.position][UP]:
		move_dest = zonemap[player1.position][UP]
		move_player(move_dest)
	elif destination == zonemap[player1.position][LEFT]:
		move_dest = zonemap[player1.position][LEFT]
		move_player(move_dest)
	elif destination == zonemap[player1.position][RIGHT]:
		move_dest = zonemap[player1.position][RIGHT]
		move_player(move_dest)
	elif destination == zonemap[player1.position][DOWN]:
		move_dest = zonemap[player1.position][DOWN]
		move_player(move_dest)
	else:
		print("Direction invalide choississez entre up, left, right, down\n")
		move(myAction)

def move_player(move_dest):
	player1.position = move_dest
	print_location()
	
def setup():
	print("\nBienvenu " + player_name + " !!\n\nPour un peu de contexte de vais t'expliquer le but de notre jeu")
	print("\nVous êtes le héros. Vous vous réveillez sur une île déserte suite à un crash d'avion avec pour seul objet un couteau. Vous devrez battre des monstres en tout genre pour accumuler de l'expérience et récuperer de nouvelles armes pour devenir plus puissant et battre le boss pour vous échappez de l'ile. \n")
	prompt()

player_name = input("Quel est votre nom ? ")
player1 = player(player_name)
current_player_health = player1.health
current_xp = player1.experience

start_game()
