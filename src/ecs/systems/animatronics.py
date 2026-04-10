import random

import src.ecs.components as components


def movement_opportunity(
	animatronic_id,
	night_id,
	difficult_level
) -> bool:

	return random.randint(0, 20) <= difficult_level[night_id][animatronic_id]


def increase_difficult(
	animatronic_id: int,
	night_id: components.nights.Nights,
	amount: int
) -> None:
	
	components.animatronics.ANIMATRONICS[animatronic_id].difficult_levels[night_id] += amount


def foxy_camera_stalling(
	animatronic_id,
	camera_id
) -> None:
	
	# serve apenas para foxy enquanto no pirate cove e para freddy
	# no caso do foxy:
	# se a camera for utilizada ele falhará na sua próxima oportunidade de movimento
	# e continuará falhando por um tempo que vai de aleatório 0.83 à 17.48 segundos

	pass


def freddy_camera_stalling(
	animatronic_id,
	camera_id
) -> None:

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


def office_stalling(
	animatronic_id,
	camera_id,
) -> None:

	# uma vez no escritorio, caso o player não use a camera, o animatronico fica 
	# incapaz de atacar, porém uma vez que o mesmo utiliza-lá, quando ele a fechar
	# vai ser atacado ou, se passado certo tempo com a camera ativa,
	# o animatronico irá desativa-lá e ataca-lo
	pass


def attack(
	animatronic_id,
	camera_id
):

	#	se o animatronico conseguir entrar no escritorio, com excessão do Foxy
	# ele precisa esperar o player ativar a câmera
	# uma vez que ele faz isso, assim que a câmera for desativada 
	# ele irá atacar
	# execute o jumpscare
	# mude o estado do game para game over
	pass


def waiting_at_the_door(
	animatronic_id: int,
	night_id: components.nights.Nights
) -> bool:
	
	return components.animatronics.ANIMATRONICS[animatronic_id].current_room_name.startswith(
		("left_door", "right_door")
	)


def try_enter_the_office(
	animatronic_id: int,
	door_id: int,
	office_id: int,
	night_id: components.nights.Nights
) -> None:

	# caso ele cumpra os requisitos para poder entrar no office
	if waiting_at_the_door(animatronic_id, night_id) and not components.states.STATES[door_id].state:

		# -1 = office
		route_progress(animatronic_id)

	# caso ele não consiga entrar para o escritorio
	else:

		components.animatronics.ANIMATRONICS[animatronic_id].current_room_index = components.animatronics.ANIMATRONICS[animatronic_id].routes["fail_attempt"]
		components.animatronics.ANIMATRONICS[animatronic_id].current_room_name = components.animatronics.ANIMATRONICS[animatronic_id].routes[current_room_index[animatronic_id]]

		print(f"{animatronic_id} is back to: {current_room[animatronic_id]}")
		# 	mude o indice do animatronico para uma das salas anteriores
		# (teoricamente, cada animatronico tem uma ou duas sala de retorno especifica)
		# para que ele continue avançando e mantendo esse loop
	
	

# Refatorar
def route_progress(animatronic_id) -> None:

	components.animatronics.ANIMATRONICS[animatronic_id].current_room_index += 1
	next_room_name = components.animatronics.ANIMATRONICS[animatronic_id].routes.get(
			components.animatronics.ANIMATRONICS[animatronic_id].current_room_index
		)

	if isinstance(next_room_name, list):
		next_room_name = random.choice(next_room_name)

	components.animatronics.ANIMATRONICS[animatronic_id].current_room_name = next_room_name
	
	print(f"{components.animatronics.ANIMATRONICS[animatronic_id]} advanced to: {components.animatronics.ANIMATRONICS[animatronic_id].current_room_name}")
