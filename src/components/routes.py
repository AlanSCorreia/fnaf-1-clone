from ..entities import flags


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
		1: flags.Flags.PIRATE_COVE,
		2: "stage1",
		3: "stage2",
		4: "stage3",
		5: ["stage4_a", "stage4_b"],
		6: flags.Flags.EAST_HALL,
		7: flags.Flags.LEFT_DOOR
	}
}