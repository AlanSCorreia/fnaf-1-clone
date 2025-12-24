import random


def movement_opportunity(animatronic_id,
						 night_id,
						 difficult_level) -> bool:
	
	return random.randint(0, 20) <= difficult_level[night_id][animatronic_id]


def increase_difficult(animatronic_id,
					   difficult_level,
					   amount) -> None:
	
	difficult_level[animatronic_id] += amount


def foxy_camera_stalling(animatronic_id,
						 camera_id,
						 states):
	
	# serve apenas para foxy enquanto no pirate cove e para freddy
	# no caso do foxy:
	# se a camera for utilizada ele falhará na sua próxima oportunidade de movimento
	# e continuará falhando por um tempo que vai de aleatório 0.83 à 17.48 segundos

	pass


def freddy_camera_stalling(animatronic_id,
						   camera_id,
						   states):

	# no caso do freddy:
	# contanto que a câmera tenha sido desativada observando ele,
	# ele irá falhar a próxima oportunidade de movimento
	# 
	# e quando estiver no west hall corner ele irá tentar entrar
	# no escritorio se a camera for ativada e, quando estiver sendo desativada,
	# não ter a câmera que ele se encontra como última visualizada
	# foxy e freddy não precisam de oportunidade de movimento para avançar assim que
	# chegarem nas suas respectivas portas, eles avançam direto para o Office
	pass


def office_stalling(animatronic_id,
					camera_id,
					states):

	# uma vez no escritorio, caso o player não use a camera, o animatronico fica 
	# incapaz de atacar, porém uma vez que o mesmo utiliza-lá, quando ele a fechar
	# vai ser atacado ou, se passado certo tempo com a camera ativa,
	# o animatronico irá desativa-lá e ataca-lo
	pass


def attack(animatronic_id,
		   camera_id,
		   states):

	#	se o animatronico conseguir entrar no escritorio, com excessão do Foxy
	# ele precisa esperar o player ativar a câmera
	# uma vez que ele faz isso, assim que a câmera for desativada 
	# ele irá atacar
	# execute o jumpscare
	# mude o estado do game para game over
	pass


def route_progression(animatronic_id,
					  door_id,
					  states,
					  routes,
					  current_room_index) -> None:
		
	next_room_index = current_room_index[animatronic_id]+1
	
	# 	se o indice atual for igual ao tamanho do dicionário de indices
	# significa que o animatronico já está na sua última sala (porta esquerda ou direita)
	if len(routes[animatronic_id]) == current_room_index[animatronic_id]:

		# caso ele cumpra os requisitos para poder entrar no office
		if not states[door_id].state:

			# -1 = office
			current_room_index[animatronic_id] = -1

		# caso ele não consiga entrar para o escritorio
		else:
			current_room_index[animatronic_id] = routes[animatronic_id]["fail_attempt"]
			# 	mude o indice do animatronico para uma das salas anteriores
			# (teoricamente, cada animatronico tem uma ou duas sala de retorno especifica)
			# para que ele continue avançando e mantendo esse loop
	else:
		
		current_room_index[animatronic_id] = next_room_index

		if type(routes[next_room_index]) is list:
		
			list_index = random.randint(0,
										len( routes[next_room_index] )-1)
			current_room_index[animatronic_id] = current_room_index[animatronic_id][list_index]
