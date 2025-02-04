class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(self.root, key)

    def _add(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._add(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._add(root.right, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self._remove(root.left, key)
        elif key > root.value:
            root.right = self._remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.value = min_larger_node.value
            root.right = self._remove(root.right, min_larger_node.value)
        return root

    def _get_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def display(self):
        elements = []
        self._in_order_traversal(self.root, elements)
        return elements

    def _in_order_traversal(self, root, elements):
        if root:
            self._in_order_traversal(root.left, elements)
            elements.append(root.value)
            self._in_order_traversal(root.right, elements)

    def search(self, key):
        return self._search(self.root, key, [])

    def _search(self, root, key, path):
        if root is None:
            return []
        if root.value == key:
            path.append(root.value)
        if key < root.value:
            path.extend(self._search(root.left, key, path))
        if key > root.value:
            path.extend(self._search(root.right, key, path))
        return path


def menu():
    bst = BinarySearchTree()
    while True:
        print("\nMenu:")
        print("1. Dodaj element")
        print("2. Usuń element")
        print("3. Wyświetl elementy")
        print("4. Wyszukaj element")
        print("5. Wyjście")
        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            key = int(input("Podaj wartość do dodania: "))
            bst.add(key)
            print("Element dodany.")
        elif choice == '2':
            key = int(input("Podaj wartość do usunięcia: "))
            bst.remove(key)
            print("Element usunięty.")
        elif choice == '3':
            elements = bst.display()
            print("Elementy w drzewie:", elements)
        elif choice == '4':
            key = int(input("Podaj wartość do wyszukania: "))
            results = bst.search(key)
            if results:
                print(f"Element {key} znaleziony w drzewie.")
            else:
                print(f"Element {key} nie występuje w drzewie.")
        elif choice == '5':
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

        print("\nAktualna zawartość drzewa:", bst.display())


if __name__ == "__main__":
    menu()
