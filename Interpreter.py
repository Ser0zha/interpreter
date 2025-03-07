from Tokens.tokens import TokenType


class Interpreter:
    def __init__(self):
        self.var = {}

    def evaluate(self, node):
        """Recursively computes the AST"""
        node_type = node[0]

        if node_type == TokenType.NUMBER:
            return int(node[1])

        elif node_type == TokenType.ID:  # Вместо "VAR" теперь TokenType.ID
            var_name = node[1]
            if var_name not in self.var:
                raise NameError(f"Variable {var_name} not defined")
            return self.var[var_name]

        elif node_type == TokenType.EQUAL:  # Присваивание
            var_name = node[1]
            value = self.evaluate(node[2])
            self.var[var_name] = value
            return value

        elif node_type in (TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE):
            left = self.evaluate(node[1])
            right = self.evaluate(node[2])

            if node_type == TokenType.PLUS:
                return left + right

            elif node_type == TokenType.MINUS:
                return left - right

            elif node_type == TokenType.MULTIPLY:
                return left * right

            elif node_type == TokenType.DIVIDE:
                return left / right if right != 0 else float("inf")

        raise ValueError(f"Unknown node type: {node_type}")
