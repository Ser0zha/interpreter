from Tokens.tokens import TokenType


class Parser:
    def __init__(self, tokens: list[tuple | tuple[str]]):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_assignment()

    def parse_assignment(self):
        """Handles assignment expressions (e.g., x = 5 + y)"""
        if self.lookahead() == TokenType.ID and self.lookahead(1) == TokenType.EQUAL:
            var_name = self.consume(TokenType.ID)[1]
            self.consume(TokenType.EQUAL)
            expr = self.parse_expression()
            return TokenType.EQUAL, var_name, expr
        return self.parse_expression()

    def parse_expression(self):
        """Processes arithmetic expressions"""
        left = self.parse_term()

        while self.lookahead() in (TokenType.PLUS, TokenType.MINUS):
            op = self.consume()[0]
            right = self.parse_term()
            left = (op, left, right)

        return left

    def parse_term(self):
        """Handles multiplication and division"""
        left = self.parse_factor()

        while self.lookahead() in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.consume()[0]
            right = self.parse_factor()
            left = (op, left, right)

        return left

    def parse_factor(self):
        """Handles numbers and variables"""
        if self.lookahead() == TokenType.NUMBER:
            return TokenType.NUMBER, self.consume()[1]

        elif self.lookahead() == TokenType.ID:
            return TokenType.ID, self.consume()[1]

        raise SyntaxError("Expected a number or a variable")

    def lookahead(self, offset=0) -> str | None:
        """Peeks at the next token without consuming it"""
        if self.pos + offset < len(self.tokens):
            return self.tokens[self.pos + offset][0]
        return None

    def consume(self, expected: TokenType = None) -> tuple[tuple | tuple[str]]:
        """Consumes a token and advances the position"""
        if expected and self.tokens[self.pos][0] != expected:
            raise SyntaxError(f"Expected {expected}, but received {self.tokens[self.pos][0]}")
        token = self.tokens[self.pos]
        self.pos += 1
        return token
