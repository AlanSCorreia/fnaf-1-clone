import pygame
import src.states.components as states_components
import src.states.systems    as states_systems


def update_button(
	button_id: int,
    current_time: int
) -> None:

    states_systems.update(
        button_id,
        current_time
    )


def has_button_been_clicked(
    button_id: int,
    current_time: int
) -> bool:

    has_been_clicked = False

    if states_components.STATES[button_id].is_available:

        update_button(
            button_id,
            current_time
        )

        has_been_clicked = True

    return has_been_clicked


class Button:
    def __init__(
        self,
        id: int
    ) -> None:

        self.id: int = id

    def update_button(
        self,
        current_time: int
    ) -> None:

        states_systems.update(
            self.id,
            current_time
        )

    def has_button_been_clicked(
        self,
        current_time: int
    ) -> bool:

        has_been_clicked = False

        if states_components.STATES[self.id].is_available:

            update_button(
                self.id,
                current_time
            )

            has_been_clicked = True

        return has_been_clicked
    
    def update(
        self,
        event: pygame.Event
    ) -> None:

        pass
    