import re
from string import punctuation


class CityInformation:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_information(self) -> str:
        """
        Read information from file
        """
        with open(self.file_name, mode='r', encoding='UTF-8') as read_file:
            file_information = read_file.read()
            return file_information

    def count_words(self) -> list[str]:
        """
        Counting Words
        """
        words_count = {}
        words = self.read_information().split()
        # words_count = {word: words.count(word) for word in words}
        for word in words:
            if any(symbol in punctuation for symbol in word):
                word = word.rstrip(punctuation)
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1
        return sorted(words_count.items(), key=lambda value: value[1], reverse=True)

    def count_symbols(self) -> list[str]:
        """
        Counting Symbols
        """
        symbol_count = {}
        for line in self.read_information():
            words = line.split()
            for word in words:
                if word in punctuation:
                    symbol_count[word] = symbol_count.get(word, 0) + 1
                else:
                    symbol_count[word] = 1
        return sorted(symbol_count.items(), key=lambda item: item[1], reverse=True)

    def words_with_symbol(self, characters: str) -> list:
        """
        Find words with certain symbols
        """
        characters = re.escape(characters)
        pattern = r'\b(?=\w*[' + characters + r'])\w+\b'
        matches = re.findall(pattern, self.read_information())
        return matches
