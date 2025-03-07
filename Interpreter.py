import re

LINE_NUMBER: str
TOKENS = [
    (r'\d+', 'NUMBER'),
    (r'[a-zA-Z_]\w*', 'ID'),
    (r'[+]', 'PLUS'),
    (r'[=]', 'EQUAL'),
    (r'[-]', 'MINUS'),
    (r'[*]', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'[ \t\n]+', None),
]
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


def recognizing_line_elements(string: str) -> list[list | list[str]]:
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

    string_buffer = []
    processed_string: list[str]

    processed_string = pre_processing(string)
    checking_for_end_of_line_semicolon()

    for index in range(len(processed_string)):
        # TODO len(): надо будет добавить проверку на длину symbol (например len() > 3 значит ключевое слово)

        if index == 0:
            checking_the_correctness_of_the_input(processed_string[index])\

        match = None
        for pattern, token_type in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(processed_string[index])

            if match:
                value = match.group(0)
                string_buffer.append([token_type, value])
                break

        if not match:
            raise SyntaxError(f"Неожиданный символ: {processed_string[index]}")

    return string_buffer


def check_for_input_completion(string_input: str) -> bool:
    return True if string_input == ";;" else False


def read_input():
    global LINE_NUMBER

    transformed_string = list[list | list[str]]
    string: str

    LINE_NUMBER = 0
    while True:
        try:
            string = input()

            if check_for_input_completion(string):
                break

            transformed_string = recognizing_line_elements(string)
            print(transformed_string)

            LINE_NUMBER += 1

        except EOFError:
            print("Обнаружен конец ввода (Ctrl + D).")
            break


def main() -> None:
    read_input()


if __name__ == "__main__":
    main()
