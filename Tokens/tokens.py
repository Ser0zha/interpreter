from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    ID = auto()
    PLUS = auto()
    EQUAL = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    LPAREN = auto()
    RPAREN = auto()
    WHITESPACE = auto()  # Пробелы, если нужно


# Required tokens
TOKENS = [
    (r'\d+', TokenType.NUMBER),
    (r'[a-zA-Z_]\w*', TokenType.ID),
    (r'\+', TokenType.PLUS),
    (r'=', TokenType.EQUAL),
    (r'-', TokenType.MINUS),
    (r'\*', TokenType.MULTIPLY),
    (r'/', TokenType.DIVIDE),
    (r'\(', TokenType.LPAREN),
    (r'\)', TokenType.RPAREN),
    (r'[ \t\n]+', TokenType.WHITESPACE),  # Можно оставить None, если не используешь
]
