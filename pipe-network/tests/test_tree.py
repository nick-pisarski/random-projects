from unittest import TestCase

from lib.networks.tree import Tree


class TestTreeNoParent(TestCase):
    def setUp(self) -> None:
        self.tree = Tree()


class TestTreeWithParent(TestCase):
    def setUp(self) -> None:
        parent_tree = Tree()
        parent_tree.children.append(Tree(value="parent_child"))

        self.tree = Tree(parent=parent_tree)


class TestInitNoParent(TestTreeNoParent):
    def test_birth_order(self):
        self.assertEqual(self.tree.birth_order, 0)
        self.assertEqual(len(self.tree.children), 0)


class TestInitWithParent(TestTreeWithParent):
    def test_birth_order(self):
        self.assertEqual(1, self.tree.birth_order)
        self.assertEqual(2, len(self.tree.parent.children))
        self.assertIsNotNone(self.tree.parent)


class TestNumChildren(TestTreeNoParent):
    def test_no_children(self):
        result = self.tree.num_children()
        self.assertEqual(0, result)

    def test_with_children(self):
        Tree(parent=self.tree, value="child")
        result = self.tree.num_children()
        self.assertEqual(1, result)


class TestGetChildByPosition(TestTreeNoParent):
    def test_with_children(self):
        self.tree.children.append(Tree(parent=self.tree, value="child"))
        result = self.tree.get_child_by_position(0)
        self.assertIsNotNone(result)


class TestAddChildren(TestTreeNoParent):
    def test_add_children(self):
        children = [Tree(value=f"child-{i}") for i in range(2)]
        self.tree.add_children(children)
        self.assertEqual(2, len(self.tree.children))
