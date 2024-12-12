class Node:
    def __init__(self, username, password, website):
        self.username = username
        self.password = password
        self.website = website
        self.next = None
        self.left = None
        self.right = None


class StackList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, username, password, website):
        if password == username:
            print("Error: Password cannot be the same as the username.")
            return
        username_exists = False
        password_exists = False
        # Check for duplicate username and password
        current = self.head
        while current:
            if current.username == username and current.website == website:
                username_exists = True
            if current.password == password and current.website == website:
                password_exists = True
            current = current.next

        if username_exists and password_exists:
            print("Error: This username and password already exists for this website.")
            return
        elif username_exists:
            print("Error: This username already exists for this website.")
            return
        elif password_exists:
            print("Error: This password already exists for this website.")
            return

        # If no duplicates, add the new node
        new_node = Node(username, password, website)
        new_node.next = self.head
        self.head = new_node
        print("details  added successfully.")

    def _pop(self):
        # Private method to remove the top element of the stack.
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node

    def peek(self):
        # Return the top element without removing it.
        if self.is_empty():
            return None
        return self.head

    def delete_by_element(self):
        # Public method to delete the top element if it matches user input.
        if self.is_empty():
            print("Stack is empty. Nothing to delete.")
            return

        top_node = self.peek()
        # print(
        #     f"Top element: Username: {top_node.username}, Password: {top_node.password}, Website: {top_node.website}")

        confirm = input(
            "Do you want to delete this element? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self._pop()
            print("Top element deleted.")
        else:
            print("Deletion canceled.")

    def view(self):
        current = self.head
        if self.is_empty():
            return
        while current:
            print(
                f"Username: {current.username}, Password: {current.password}, Website: {current.website}")
            current = current.next


class BinarySearchTree:

    def __init__(self):
        self.root: Node = None

    def Add_To_Bst(self, username, password, website):
        new_node = Node(username, password, website)

        if self.root is None:
            self.root = new_node
        else:
            self._add_to_bst(self.root, new_node)

    def _add_to_bst(self, current, new_node):
        if new_node.username < current.username:
            if current.left is None:
                current.left = new_node
            else:
                self._add_to_bst(current.left, new_node)
        elif new_node.username > current.username:
            if current.right is None:
                current.right = new_node
            else:
                self._add_to_bst(current.right, new_node)

    def search(self, username):
        return self._search(self.root, username)

    def _search(self, current, username):
        if current is None or current.username == username:
            return current

        if username < current.username:
            return self._search(current.left, username)

        return self._search(current.right, username)

    def delete(self, username):
        self.root = self._delete(self.root, username)

    def _delete(self, current, username):
        if current is None:
            return current

        if username < current.username:
            current.left = self._delete(current.left, username)
        elif username > current.username:
            current.right = self._delete(current.right, username)
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(current.right)
            current.username = successor.username
            current.password = successor.password
            current.website = successor.website
            current.right = self._delete(current.right, successor.username)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
