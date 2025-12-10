def has_component(entity_mask,
				  components):
	
    return (entity_mask & components) == components


def has_all_components(entities_mask,
					   bit_masks):
	
	return all(has_component(entities_mask, bit_mask)
			   for bit_mask in bit_masks)


def has_any_components(entities_mask,
					   bit_masks):
	
    return any(has_component(entities_mask, bit_mask)
			   for bit_mask in bit_masks)


def filter_entities_components(entities_id,
							   accept_bit_masks,#: list[str],
							   rejected_bit_masks,# : list[str] | None,
							   entities_mask):# : dict
	
	result = []

	for entity_id in entities_id:
		if accept_bit_masks:
			if rejected_bit_masks:
				if has_all_components(entities_mask[entity_id], accept_bit_masks)\
				and not has_any_components(entities_mask[entity_id], rejected_bit_masks):
					result.append(entity_id)

			else:
				if has_all_components(entities_mask[entity_id], accept_bit_masks):
					result.append(entity_id)
	
	return result
