import re

from Interpreter import Interpreter
from Parser import Parser
from Tokens.tokens import TOKENS

# Line of code counter
LINE_NUMBER: str

# Counter of variables and other data
VARIABLE_COUNTER = 0

# Required keywords
KEYWORDS = [
    ("loopfor", "KW_FOR"),
    ("loopwhile", "KW_WHILE"),
]


def checking_the_correctness_of_the_input(line_to_check: str) -> None:
    """
    Проверка на то, что строка не начинается с числа
    :param line_to_check:
    :return:
    """
    try:
        int(line_to_check)
        raise ValueError("Числу не может быть присвоена переменная")
    except ValueError:
        pass


def pre_processing(raw_string: str) -> list[str]:
    return raw_string.strip().split()


def tokenization(processed_string: list[str]) -> list[tuple | tuple[str]]:
    result = []

    for index, item in enumerate(processed_string):
        # TODO len(): надо будет добавить проверку на длину symbol (например len() > 3 значит ключевое слово)
        if index == 0:
            checking_the_correctness_of_the_input(item)

        match = None

        for pattern, token_type in TOKENS:

            regex = re.compile(pattern)
            match = regex.match(item)

            if match:
                value = match.group(0)
                result.append((token_type, value))
                break

        if not match:
            raise SyntaxError(f"Неожиданный символ: {item}")

    return result


def recognizing_line_elements(string: str) -> list[tuple | tuple[str]]:
    def checking_for_end_of_line_semicolon() -> None:
        """
        Проверка окончание строка символом ';'
        :return:
        """
        global LINE_NUMBER
        nonlocal processed_string

        last = processed_string[-1]

        if last[-1] != ';':
            raise Exception(f"Ошибка компиляции в строке {LINE_NUMBER}")
        else:
            processed_string[-1] = processed_string[-1][0]

    processed_string: list[str]

    processed_string = pre_processing(string)
    checking_for_end_of_line_semicolon()

    return tokenization(processed_string)


def check_for_input_completion(string_input: str) -> bool:
    return True if string_input == ";;" else False


def read_input() -> None:
    global LINE_NUMBER

    string: str

    LINE_NUMBER = 0
    while True:
        try:
            string = input()

            if check_for_input_completion(string):
                break

            transformed_string = recognizing_line_elements(string)

            parser = Parser(transformed_string)
            ast = parser.parse()

            interpreter = Interpreter()
            res = interpreter.evaluate(ast)

            print(res)
            LINE_NUMBER += 1

        except EOFError:
            print("Обнаружен конец ввода (Ctrl + D)")
            break


def main() -> None:
    read_input()


if __name__ == "__main__":
    main()
