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
def bs():
	
	cartes={ 1:4 , 2:4 , 3:4 , 4:4 , 5:4 , 6:4 , 7:4 , 8:4 ,9:4 , 10:4 ,11:4 , 12:4 , 13:4 }
	print("les cartes ", cartes)
	player_carte= 4
	if player_carte in cartes:
		cartes[player_carte]-=1
	print("les cartes restantes ", cartes)
def game():
	print(" C'est bien sa, j'adooore sa! ")

	print("tout d'abord sahce que t'as ", player, "pilons en banque")
	

	mise=int(input(" mtn dis moi combien de pilon(s) tu veux miser? "))
	jeu=1
	while jeu != 0:
		jeu=0
bs()





























start=int(input("Mamène si tu veux jouer tape 1 si tu veux pas jouer tape 0 si tu veux connaitre les régles parce que t trop con tape 3 : "))
while start != 0:
	if start == 3:
		regle()
		start=int(input("Mamène si tu veux jouer tape 1 si tu veux pas jouer tape 0 si tu veux connaitre les régles parce que t trop con tape 3 : "))
	if start > 3 or start <1:
		start = 0
		if start ==1:
			start=0