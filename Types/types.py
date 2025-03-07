from enum import Enum, auto


class VariableType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    SET = auto()
    TUPLE = auto()
    LIST = auto()


# Data Types
TYPES = [
    ("T_INTEGER", VariableType.INTEGER),
    ("T_FLOAT", VariableType.FLOAT),
    ("T_STRING", VariableType.STRING),
    ("T_BOOLEAN", VariableType.BOOLEAN),
    ("T_SET", VariableType.SET),
    ("T_TUPLE", VariableType.TUPLE),
    ("T_LIST", VariableType.LIST),
]
