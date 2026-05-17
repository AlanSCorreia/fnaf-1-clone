import os

import pygame

from src.userInterface.static_element import StaticElement
from src.userInterface.text_element   import TextElement

import src.setup            as setup
import src.import_functions as import_functions


ELEMENTS_TYPE = {
    "static": dict(),
    "text"  : dict()
}
UI_GROUPS = {
    "intro"     : pygame.sprite.Group(),
    "off_camera": pygame.sprite.Group(),
    "on_camera" : pygame.sprite.Group()
}


def build_static_element(
    element_name: str,
    image_path: str,
    position: tuple[int, int],
    groups: list[str]
) -> None:

    ELEMENTS_TYPE["static"][element_name] = StaticElement(
        image_path,
        position,
        [UI_GROUPS[group] for group in groups]
    )


def build_text_element(
    element_name: str,
    text_font: pygame.Font,
    text_content: str,
    text_color: str,
    position: tuple[int, int],
    groups: list[str]
) -> None:

    ELEMENTS_TYPE["text"][element_name] = TextElement(
        text_font,
        text_content,
        text_color,
        position,
        [UI_GROUPS[group] for group in groups]
    )

 
directory_path = "data/userInterface"

for path_name, _, filenames in os.walk(directory_path):
    for filename in filenames:
        for key, value in import_functions.extract_yaml_data(f"{path_name}/{filename}").items():
            match value["type"]:
                case "static":
                    build_static_element(
                        key,
                        value["image_path"],
                        (value["position"]["x"], value["position"]["y"]),
                        value["groups"]
                    )

                case "text":
                    build_text_element(
                        key,
                        setup.FONT,
                        value["message"],
                        value["color"],
                        (value["position"]["x"], value["position"]["y"]),
                        value["groups"]
                    )
