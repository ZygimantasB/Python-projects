class Sentence:
    def __init__(self, enter_txt):
        self.enter_txt = enter_txt

    def make_text_backwards(self):
        return print(self.enter_txt[::-1])

    def return_text_lower(self):
        return self.enter_txt.lower()

    def return_text_upper(self):
        return self.enter_txt.upper()

    def return_how_many_words(self):
        return len(self.enter_txt.split(' '))

    def return_how_many_digits(self):
        return sum([1 for x in self.enter_txt if x in '1234567890'])

    def return_how_many_symbols(self):
        return print(sum([1 for x in self.enter_txt if x in '/*-,./!;[]-=']))

    def __str__(self):
        sentence = Sentence()
        return print(f'My function do what: {sentence.return_text_lower()}')
