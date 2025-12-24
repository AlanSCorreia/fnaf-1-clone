import random

from ..entities import flags
from . import nights


difficult_levels = {
	nights.Nights.FIRST : {
		flags.Flags.FREDDY: 20,
		flags.Flags.BONNIE: 20,
		flags.Flags.CHICA : 20,
		flags.Flags.FOXY  : 20
	},
	nights.Nights.SECOND: {
		flags.Flags.FREDDY: 0,
		flags.Flags.BONNIE: 3,
		flags.Flags.CHICA : 1,
		flags.Flags.FOXY  : 1
	},
	nights.Nights.THIRD : {
		flags.Flags.FREDDY: 1,
		flags.Flags.BONNIE: 0,
		flags.Flags.CHICA : 5,
		flags.Flags.FOXY  : 2
	},
	nights.Nights.FOURTH: {
		flags.Flags.FREDDY: random.randint(1, 2),
		flags.Flags.BONNIE: 2,
		flags.Flags.CHICA : 4,
		flags.Flags.FOXY  : 6
	},
	nights.Nights.FIFTH : {
		flags.Flags.FREDDY: 3,
		flags.Flags.BONNIE: 5,
		flags.Flags.CHICA : 7,
		flags.Flags.FOXY  : 5
	},
	nights.Nights.SIXTH : {
		flags.Flags.FREDDY: 4,
		flags.Flags.BONNIE: 10,
		flags.Flags.CHICA : 12,
		flags.Flags.FOXY  : 6
	},
	nights.Nights.CUSTOM: {
		flags.Flags.FREDDY: 0,
		flags.Flags.BONNIE: 0,
		flags.Flags.CHICA : 0,
		flags.Flags.FOXY  : 0
	}
}
