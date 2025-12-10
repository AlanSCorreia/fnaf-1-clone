from random import randint


def movement_opportunity(animatronic_id,
						 difficult_level) -> bool:
	return randint(0, 20) <= difficult_level[animatronic_id]