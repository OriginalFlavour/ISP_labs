import statistics
import re


class TextHandler:

    @classmethod
    def get_words(cls, text):
        return re.findall(r'\b[a-zA-Z]{1,}\b', text)


    @staticmethod
    def get_frequency(frequency, text):
        words = TextHandler.get_words(text)

        for word in words:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        return frequency


    @staticmethod
    def get_amount_of_repetitions(frequency, text):
        frequency = TextHandler.get_frequency(frequency, text)
        return frequency.keys()


    @classmethod
    def get_all_sentences(cls, text):
        return re.split("\. |\.\.\. |\! |\? ", text)

    @classmethod
    def count_words_per_sentense(cls, text):
        words_amount = []

        for sentence in TextHandler.get_all_sentences(text):
            words_amount.append(len(sentence.split()))

        return words_amount


    @staticmethod
    def get_average_number_words(text):
        average_number = statistics.mean(TextHandler.count_words_per_sentense(text))

        return average_number


    @staticmethod
    def get_median_number_words(text):
        return statistics.median(TextHandler.count_words_per_sentense(text))


    @staticmethod
    def ngram(text, n):
        words = TextHandler.get_words(text)

        for word in words:
            if len(word) < n:
                words[words.index(word)] = ''

        words = ' '.join(words)
        words = words.split()

        for i in words:
            words[words.index(i)] = i[:n]

        out_dict = {i: 1 for i in words}
        
        for word in words:
            if word not in out_dict:
                out_dict.append(i)
            if out_dict.get(word, None):
                out_dict[word] += 1
        
        return out_dict
    

    @staticmethod
    def print_amount_of_repetitions(frequency, text):
        for key in TextHandler.get_amount_of_repetitions(frequency, text):
            print(key, frequency[key])


    @staticmethod
    def print_average_number_words(text):
        print(TextHandler.get_average_number_words(text))


    @staticmethod
    def print_median_number_words(text):
        print(TextHandler.get_median_number_words(text))