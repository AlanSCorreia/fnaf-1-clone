import dataclasses

import src.import_functions as import_functions
import src.ecs.entities as entities


@dataclasses.dataclass
class StateData:

	state: bool = False
	is_available: bool = True
	last_availability_time: int = 0
	availability_delay: int = 0


yaml_file = import_functions.extract_yaml_data("data/components/states.yaml")


STATES: dict[int, StateData] = {
	entities.IDS[entity_id]: StateData(**values)
	for entity_id, values in yaml_file.items()
}
