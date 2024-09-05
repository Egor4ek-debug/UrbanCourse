class WordsFinder:
    def __init__(self, *files_name):
        self.files_name = tuple(files_name)

    def get_all_words(self):
        all_words = {}
        punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.files_name:
            words_list = []
            with open(file_name, encoding='utf=8') as file:
                for line in file:
                    line = line.lower()
                    for p in punctuation_marks:
                        if p in line:
                            line = line.replace(p, '')
                    words_list.extend(line.split())
            all_words[file_name] = words_list
        return all_words

    def find(self, word):
        all_word = self.get_all_words()
        word = word.lower()
        find_word = {}
        for file_name, words in all_word.items():
            if word in words:
                find_word[file_name] = words.index(word) + 1
        if not find_word:
            return 'Такого слова в файлах нет'
        return find_word

    def count(self, word):
        all_word = self.get_all_words()
        word = word.lower()
        find_word_counter = {}
        flag = 0
        for file_name, words in all_word.items():
            counter = 0
            for split_words in words:
                if word == split_words:
                    counter += 1
                find_word_counter[file_name] = counter

            if find_word_counter[file_name] == 0:
                flag += 1
        if len(find_word_counter) == flag:
            return 'Такого слова в файлах нет'
        return find_word_counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
