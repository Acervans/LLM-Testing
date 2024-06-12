from typing import Callable

class Tool:
    definition: dict
    function: Callable

    def __init__(self, definition, function) -> None:
        self.definition = definition
        self.function = function

    def call(self, **kwargs):
        return self.function(**kwargs)
