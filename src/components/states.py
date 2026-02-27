import dataclasses

import src.import_functions as import_functions
import src.entities as entities


@dataclasses.dataclass
class State:

	state: bool = False
	is_available: bool = True
	last_availability_time: int = 0
	availability_delay: int = 0


STATES: dict[int, State] = dict()

yaml_file = import_functions.extract_yaml_data("data/components/states.yaml")


for entitiy_id, values in yaml_file.items():
	STATES[entities.IDS[entitiy_id]] = State(
		values["state"],
		values["is_available"],
		values["last_availability_time"],
		values["availability_delay"]
	)
