from ..entities import flags


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

movement_opportunity_delay = {
	flags.Flags.FREDDY: 3020,
	flags.Flags.BONNIE: 4970,
	flags.Flags.CHICA : 4980,
	flags.Flags.FOXY  : 5010
}

routes = {

	flags.Flags.FREDDY: {
		"fail_attempt": 5,
		1: flags.Flags.SHOW_STAGE,
		2: flags.Flags.DINING_AREA,
		3: flags.Flags.RESTROOMS,
		4: flags.Flags.KITCHEN,
		5: flags.Flags.EAST_HALL,
		6: flags.Flags.EAST_HALL_CORNER,
		7: flags.Flags.RIGHT_DOOR
	},

	flags.Flags.BONNIE: {
		"fail_attempt": 3,
		1: flags.Flags.SHOW_STAGE,
		2: [flags.Flags.BACKSTAGE,
	  		flags.Flags.DINING_AREA],
		3: flags.Flags.WEST_HALL,
		4: [flags.Flags.SUPPLY_CLOSET,
	  		flags.Flags.WEST_HALL_CORNER],
		5: flags.Flags.LEFT_DOOR
	},

	flags.Flags.CHICA : {
		"fail_attempt": 4,
		1: flags.Flags.SHOW_STAGE,
		2: flags.Flags.DINING_AREA,
		3: [flags.Flags.RESTROOMS,
			flags.Flags.KITCHEN],
		4: flags.Flags.EAST_HALL,
		5: [flags.Flags.DINING_AREA,
			flags.Flags.EAST_HALL_CORNER],
		6: [flags.Flags.EAST_HALL,
			flags.Flags.RIGHT_DOOR]
	},

	flags.Flags.FOXY  : {
		"fail_attempt": 2,
		1: (flags.Flags.PIRATE_COVE, "stage1"),
		2: (flags.Flags.PIRATE_COVE, "stage2"),
		3: (flags.Flags.PIRATE_COVE, "stage3"),
		4: (flags.Flags.PIRATE_COVE, ["stage4_a", "stage4_b"]),
		5: flags.Flags.EAST_HALL,
		6: flags.Flags.LEFT_DOOR
	}
	
}

current_room_index = {
	flags.Flags.FREDDY: 1,
	flags.Flags.BONNIE: 3,
	flags.Flags.CHICA : 4,
	flags.Flags.FOXY  : 1
}

current_room = {
	flags.Flags.FREDDY: routes[flags.Flags.FREDDY][current_room_index[flags.Flags.FREDDY]],
	flags.Flags.BONNIE: routes[flags.Flags.BONNIE][current_room_index[flags.Flags.BONNIE]],
	flags.Flags.CHICA : routes[flags.Flags.CHICA ][current_room_index[flags.Flags.CHICA ]],
	flags.Flags.FOXY  : routes[flags.Flags.FOXY  ][current_room_index[flags.Flags.FOXY  ]]
}