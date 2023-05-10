"""A switch component."""
from typing import Dict

from pynecone.components.component import EVENT_ARG
from pynecone.components.libs.chakra import ChakraComponent
from pynecone.vars import Var


class Switch(ChakraComponent):
    """Toggleable switch component."""

    tag = "Switch"

    # If true, the switch will be checked. You'll need to pass onChange to update its value (since it is now controlled)
    is_checked: Var[bool]

    # If true, the switch will be disabled
    is_disabled: Var[bool]

    # If true and isDisabled is passed, the switch will remain tabbable but not interactive
    is_focusable: Var[bool]

    # If true, the switch is marked as invalid. Changes style of unchecked state.
    is_invalid: Var[bool]

    # If true, the switch will be readonly
    is_read_only: Var[bool]

    # If true, the switch will be required
    is_required: Var[bool]

    # The name of the input field in a switch (Useful for form submission).
    name: Var[str]

    # The spacing between the switch and its label text (0.5rem)
    spacing: Var[str]

    # The placeholder text.
    placeholder: Var[str]

    # The color scheme for the switch
    color_scheme: Var[str]

    def __init__(self, **kwargs):
        """
        Initialize the component with the provided kwargs.

        Args:
            **kwargs: Optional keyword arguments.
                color_scheme (str): The color scheme to use for the component.

        Returns:
            None
        """
        super().__init__(**kwargs)
        self.color_scheme = kwargs.get("color_scheme", "blue")

    def get_style_props(self) -> Dict:
        """
        Get the style properties for the component.

        Returns:
            A dictionary of style properties.
        """
        style_props = super().get_style_props()
        style_props["colorScheme"] = self.color_scheme
        return style_props

    @classmethod
    def get_controlled_triggers(cls) -> Dict[str, Var]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            "on_change": EVENT_ARG.target.checked,
        }
