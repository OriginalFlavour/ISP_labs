import argparse
from text_handler import TextHandler


class Main:

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', nargs='?', default=10)
    parser.add_argument('-n', nargs='?', default=4)
    args = parser.parse_args()

    def print_ngram(out_dict: dict, k=int(args.k)):
        list_d = list(out_dict.items())
        list_d.sort(key=lambda l: l[1])
        list_d.reverse()

        print(*[f'{i} {j}' for i, j in enumerate(list_d[:k])], sep='\n')

    @staticmethod
    def main():
        f = open('text.txt', 'r')
        text = f.read()
        f.close()

        frequency = {}

        TextHandler.print_amount_of_repetitions(frequency, text)
        TextHandler.print_average_number_words(text)
        TextHandler.print_median_number_words(text)

        Main.print_ngram(TextHandler.ngram((text), int(Main.args.n)))


Main.main()
