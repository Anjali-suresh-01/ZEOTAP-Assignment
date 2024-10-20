import json

# Define a simple AST Node structure
class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # "operator" or "operand"
        self.value = value          # For operand, it's the condition; for operator, it's AND/OR
        self.left = left            # Left child (another ASTNode)
        self.right = right          # Right child (another ASTNode)

    def __repr__(self):
        return f"ASTNode(type={self.node_type}, value={self.value}, left={self.left}, right={self.right})"

# 1. Function to create a rule (AST)
def create_rule(rule_string):
    # Split the rule into parts (e.g., "age > 18" -> ["age", ">", "18"])
    parts = rule_string.split()
    if len(parts) != 3:
        raise ValueError(f"Invalid rule format: {rule_string}")

    # Extract the operand and comparison operator
    operand, operator, value = parts[0], parts[1], parts[2]

    # Create an ASTNode for the rule (operand)
    return ASTNode(node_type="operand", value=f"{operand} {operator} {value}")

# 2. Function to combine multiple rules into a single AST
def combine_rules(rules, operator="AND"):
    # Create AST nodes for individual rules
    if not rules:
        raise ValueError("Rule list cannot be empty.")
    
    root = create_rule(rules[0])  # Start with the first rule

    for rule in rules[1:]:
        # Combine the current rule with the existing AST using the given operator
        new_node = create_rule(rule)
        root = ASTNode(node_type="operator", value=operator, left=root, right=new_node)
    
    return root

# 3. Function to evaluate the rule against user data
def evaluate_rule(ast_node, user_data):
    if ast_node.node_type == "operand":
        # Parse the condition string (e.g., "age > 18")
        operand, operator, value = ast_node.value.split()

        # Get the user attribute value
        user_value = user_data.get(operand)
        if user_value is None:
            raise ValueError(f"Attribute {operand} not found in user data")

        # Convert value to the appropriate type
        if value.isdigit():
            value = int(value)
        elif value.replace(".", "", 1).isdigit():  # Handle float
            value = float(value)

        # Evaluate the condition based on the operator
        if operator == ">":
            return user_value > value
        elif operator == "<":
            return user_value < value
        elif operator == "==":
            return user_value == value
        elif operator == "!=":
            return user_value != value
        else:
            raise ValueError(f"Invalid operator: {operator}")

    elif ast_node.node_type == "operator":
        # Evaluate the left and right children recursively
        left_result = evaluate_rule(ast_node.left, user_data)
        right_result = evaluate_rule(ast_node.right, user_data)

        # Apply the AND/OR operator
        if ast_node.value == "AND":
            return left_result and right_result
        elif ast_node.value == "OR":
            return left_result or right_result
        else:
            raise ValueError(f"Invalid operator: {ast_node.value}")

    return False

# Example test case implementation
def run_tests():
    print("=== Test Case 1: Create Individual Rules ===")
    rule1 = create_rule("age > 18")
    rule2 = create_rule("salary > 50000")
    print("Rule 1 AST:", rule1)
    print("Rule 2 AST:", rule2)
    
    print("\n=== Test Case 2: Combine Rules ===")
    combined_ast = combine_rules(["age > 18", "salary > 50000", "experience > 2"], operator="AND")
    print("Combined AST:", combined_ast)
    
    print("\n=== Test Case 3: Evaluate Rule ===")
    user_data = {"age": 35, "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_ast, user_data)
    print(f"Evaluation result for user data {user_data}: {result}")
    
    print("\n=== Test Case 4: Evaluate with another user data ===")
    user_data2 = {"age": 16, "salary": 30000, "experience": 1}
    result2 = evaluate_rule(combined_ast, user_data2)
    print(f"Evaluation result for user data {user_data2}: {result2}")

# Run the tests
run_tests()

