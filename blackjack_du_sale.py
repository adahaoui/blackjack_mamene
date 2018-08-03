"""
black jack du sale
"""

print("bienvenue mamene au jeu du blackjack du sale")
def regle():
	print(" mon poto rico va vous z'expliké les regles")
	print("les regles sont simple mamene. \n 1# Tu dois battre la banque a pilon pour gagner un max de pilon mamene; \n 2# Tu ne peux pas dépasser 21 pts sinon tu saute et tu perd tes pilons misé sale babos de merde; \n 3# l'AS vaut 1 ou 11 points c'est toi qui choisis c kdo ca tqt c moi qui offre <3 ; \n #4 les cartes de 2 à 10 valent leurs valeur facial si t'as pas kompris achete un dico sale analpha teubé ; #5 le valet, la dame et le roi valent tous 10 pts; \n #6 en cas d'égalité tu recupere tes pilons et tu ne gagne rien c comme sa; \n # un 21 obtenu avec 2 cartes (sa s'appelle un blackjack) l'emporte sur un 21 avec 3 cartes ou plus. \n c'est tout pour les regles mamène.")
	print('\n \n ')
from random import randint
banque= 5000
player= 250


	
def game():
	print(" C'est bien sa, j'adooore sa! ")

	print("tout d'abord sache que t'as ", player, "pilons dans ton go fast")
	
	cartes={ 1:4 , 2:4 , 3:4 , 4:4 , 5:4 , 6:4 , 7:4 , 8:4 ,9:4 , 10:4 ,11:4 , 12:4 , 13:4 }
	valeur={1:11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:11}
	g=[1,11]
	h=[1,10,11,12,13]
	score_joueur=0
	score_ordi=0
	max_score=21
	job=16
	mise=int(input(" mtn dis moi combien de pilon(s) tu veux miser? "))
	mise_ordi= mise
	jeu=1
	
	def test():

		if player_carte in cartes:
			cartes[player_carte]-=1
		for elem in range(1,len(cartes)):
			if cartes[elem] :
				del cartes[elem]
	while jeu == 1:
		#premier tour
		player_carte=randint(1,len(cartes))
		
		if player_carte ==1 or player_carte ==13:
			value= int(input(" tu veux que ton cart ai quel valeur 1 ou 11? "))
			if value not in g:
				value= int(input("gros met une valeur valide fait pas le mec, c'est soit 1 ou 11 mamène :"))
			score_joueur+=value
		if player_carte == 12:
			score_joueur+=valeur[player_carte]
			print("vous avez piochez le roi ca te fait",score_joueur)
		if player_carte == 11:
			score_joueur+=valeur[player_carte]
			print("vous avez piochez la reine ca te fait",score_joueur)
		if player_carte == 10:
			score_joueur+=valeur[player_carte]
			print("vous avez piochez le valet ca te fait",score_joueur)
		if player_carte not in h:
			print("tu a pioché le ",player_carte)
			score_joueur+= valeur[player_carte]
		test()
		print("ton score est pour l'instant ",score_joueur)
		jeu=int(input("tu veux continuer a jouer? (1 pour oui et 0 pour non"))
		if jeu==1:
			player_carte=randint(1,len(cartes))

		ordi_carte=randint(1,len(cartes))
		if ordi_carte == 12:
			score_ordi+=valeur[ordi_carte]
			print("Janine a pioché le roi ca lui fait",score_ordi)
		if ordi_carte == 11:
			score_ordi+=valeur[ordi_carte]
			print("Janine a pioché la reine ca lui fait",score_ordi)
		if ordi_carte == 10:
			score_ordi+=valeur[ordi_carte]
			print("Janine a pioché le valet ca lui fait",score_ordi)
		if ordi_carte not in h:
			print("Janine a pioché le ",ordi_carte)
			score_ordi+= valeur[ordi_carte]
		if ordi_carte == 1 or ordi_carte ==1:
			if score_ordi<=10:
				score_ordi+=11
			else:
				score_ordi+=1
		print("le score de Janine est de ",score_ordi, " pts pour l'instant mamène")
	

























p=[1,3]
start=int(input("Mamène si tu veux jouer tape 1 si tu veux pas jouer tape 0 si tu veux connaitre les régles parce que t trop con tape 3 : "))
while start not in p :
	if start == 3:
		regle()
		start=int(input("Mamène si tu veux jouer tape 1 si tu veux pas jouer tape 0 si tu veux connaitre les régles parce que t trop con tape 3 : "))
	if start ==1:
		jeu=1
game()
