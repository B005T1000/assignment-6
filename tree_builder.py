class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name: str):
        """
        Initialize an EmployeeNode.
        """
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"EmployeeNode({self.name!r})"

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name: str, employee_name: str, side: str) -> None:
        """
        Insert `employee_name` under the manager with `manager_name` on `side` ('left' or 'right').
        This uses a simple breadth-first search to find the manager.
        """
        if not self.root:
            print("⚠️  No team lead set. Add a team lead before inserting employees.")
            return

        side_norm = (side or "").strip().lower()
        if side_norm not in ("left", "right", "l", "r"):
            print("❌ Invalid side. Use 'left' or 'right'.")
            return

        # Simple BFS to find the manager node
        queue = [self.root]
        manager_node = None
        while queue:
            node = queue.pop(0)
            if node.name.lower() == manager_name.lower():
                manager_node = node
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if manager_node is None:
            print(f"❌ Manager named '{manager_name}' not found.")
            return

        # perform insertion
        if side_norm in ("left", "l"):
            if manager_node.left is None:
                manager_node.left = EmployeeNode(employee_name)
                print(f"✅ {employee_name} added as LEFT report to {manager_node.name}.")
            else:
                print(f"⚠️  {manager_node.name} already has a LEFT report ({manager_node.left.name}).")
        else:
            if manager_node.right is None:
                manager_node.right = EmployeeNode(employee_name)
                print(f"✅ {employee_name} added as RIGHT report to {manager_node.name}.")
            else:
                print(f"⚠️  {manager_node.name} already has a RIGHT report ({manager_node.right.name}).")

    def print_tree(self, node: EmployeeNode = None, level: int = 0) -> None:
        """
        Print the tree starting at `node` (defaults to root). Keeps formatting minimal.
        """
        if node is None:
            node = self.root

        if node is None:
            print("No team structure available.")
            return

        print("    " * level + f"- {node.name}")
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

# A: Since the tree begins at the start, you go down the roots to find the manager. So you start at the top and go down.
# B: Challenges could arise from duplicate names, unbalanced trees, and ensuring valid input for sides.
# C: Trees are preferred to be used for a hierarchy or structure type data, since it runs down the lists.