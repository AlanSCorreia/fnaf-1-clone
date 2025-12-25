from ..entities import flags
from .current_room_index import current_room_index
from .routes import routes


current_room = {
	flags.Flags.FREDDY: routes[flags.Flags.FREDDY][current_room_index[flags.Flags.FREDDY]],
	flags.Flags.BONNIE: routes[flags.Flags.BONNIE][current_room_index[flags.Flags.BONNIE]],
	flags.Flags.CHICA : routes[flags.Flags.CHICA ][current_room_index[flags.Flags.CHICA ]],
	flags.Flags.FOXY  : routes[flags.Flags.FOXY  ][current_room_index[flags.Flags.FOXY  ]]
}