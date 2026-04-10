import os

import pygame

from src.userInterface.declaration import UIStaticElement, UITextElement
import src.setup            as setup
import src.import_functions as import_functions


ELEMENTS = {
    "static": dict(),
    "text"  : dict()
}
GROUPS = {
    "off_camera": pygame.sprite.Group(),
    "on_camera" : pygame.sprite.Group()
}


def build_static_element(
    element_name: str,
    image_path: str,
    position: tuple[int, int],
    groups: list[str]
) -> None:

    ELEMENTS["static"][element_name] = UIStaticElement(
        image_path,
        position,
        [GROUPS[group] for group in groups]
    )


def build_text_element(
    element_name: str,
    text: str,
    text_font: pygame.Font,
    text_color: str,
    position: tuple[int, int],
    groups: list[str]
) -> None:

    ELEMENTS["text"][element_name] = UITextElement(
        text,
        text_font,
        text_color,
        position,
        [GROUPS[group] for group in groups]
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
                        value["message"],
                        setup.FONT,
                        value["color"],
                        (value["position"]["x"], value["position"]["y"]),
                        value["groups"]
                    )
