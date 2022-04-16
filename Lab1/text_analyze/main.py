from utils.utils import read_text_from_file, get_command_line_args, write_to_file
from constants.constants import DEFAULT_N, DEFAULT_K, SOURCE_FILE, OUTPUT_FILE
from text_analyzer.types import Query
from text_analyzer.analyzer import analyze_text


def main():
    command_line_arguments = get_command_line_args((DEFAULT_N, DEFAULT_K))
    text = read_text_from_file(SOURCE_FILE)
    query = Query(text, *command_line_arguments)

    response = analyze_text(query)

    print(response)

    write_to_file(OUTPUT_FILE, str(response))

    cort = (5, 6, 7)
    array = [5, 6, 7]
    set = {5, 6,7, 8, 8, 8, 8, 10}
    map = {'a': 5,
           'kirill': 6,
           'pc': [5, 6, 7],
           5: 9}


if __name__ == '__main__':
    main()