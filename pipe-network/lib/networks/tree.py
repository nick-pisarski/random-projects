from __future__ import annotations

from typing import Any, Optional


class Tree:
    """A group of Nodes"""

    def __init__(self, parent: Optional[Tree] = None, value: Optional[Any] = None) -> None:
        self.parent = parent
        self.value = value
        self.children: list[Tree] = []

        if parent is None:
            self.birth_order = 0
        else:
            self.birth_order = len(parent.children)
            parent.children.append(self)

    def add_children(self, children: list[Tree]) -> None:
        for child in children:
            child.update_birth_order(len(self.children) + 1)
            self.children.append(child)

    def update_birth_order(self, value: int) -> None:
        self.birth_order = value

    def num_children(self) -> int:
        return len(self.children)

    def get_child_by_position(self, n: int) -> Tree:
        return self.children[n]
