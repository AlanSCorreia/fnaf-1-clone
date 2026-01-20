import os

import pygame
import yaml

from custom_types import str_ID, surfaces_dict
from entities import entities_ids


all_imports: dict[str_ID, surfaces_dict] = {
    "backgrounds": dict(),
    "camera_rooms_buttons": dict(),
    "inanimated_props": dict(),
    "animated_props": dict(),
    "jumpscares": dict()
}


def import_data_from_yaml(path: str):
    
    with open(path) as stream:
        file = yaml.safe_load(stream)

    return file


def convert_dict_values_into_surfaces(id,
                                      _dict,
                                      target_dict):

    for key, surface_path in _dict:
        target_dict[entities_ids[id]][key] = pygame.image.load(surface_path).convert_alpha()


def convert_list_values_into_surfaces_frames(id,
                                             _list,
                                             target_dict) -> None:

    frames_dict = dict()

    # _list = [path, frames_count]
    for frame in range(1, _list[1]+1):
        frames_dict[frame] = pygame.image.load(_list[0].format(frame=frame)).convert_alpha()
    
    target_dict[entities_ids[id]] = frames_dict


def update_target_dict(target_dict: dict,
                       surfaces_paths_dict: dict[str_ID, str]) -> None:

    for id, value in surfaces_paths_dict.items():

        if type(value) is dict:
            convert_dict_values_into_surfaces(id,
                                              value,
                                              target_dict)
            
        if type(value) is list:
            convert_list_values_into_surfaces_frames(id,
                                                     value,
                                                     target_dict)

        else:
            target_dict[entities_ids[id]] = pygame.image.load(value).convert_alpha()


def dump_surfaces_into_target_dict(target_dict: dict,
                                   surfaces_paths_path: str) -> None:
    
    surfaces_paths_dict: dict[str_ID, str] = import_data_from_yaml(surfaces_paths_path)

    update_target_dict(target_dict,
                        surfaces_paths_dict)


def import_all_assets():

    root_path = "data/assets_paths_normalization"

    for _, _, directories_names in os.walk(root_path):
        for directory_name, dict_name in zip(sorted(directories_names), sorted(all_imports.keys())):
            dump_surfaces_into_target_dict(all_imports[dict_name],
                                           f"{root_path}/{directory_name}")
