import unittest


def offset_list(sub_str):
    un_chars = set() #  - значения, которые уже встречались
    s = {} #  - символы ии их кол-во

    if len(sub_str) != 0:
        last_char = (len(sub_str) - 1)

        s['*'] = len(sub_str)
        s[sub_str[last_char]] = 0

        for i in range(1, len(sub_str)):
            str_i = (len(sub_str) - 1) - i
            if sub_str[str_i] not in un_chars:
                un_chars.add(sub_str[str_i])
                s[sub_str[str_i]] = i


        if sub_str[last_char] not in un_chars:
            s[sub_str[last_char]] = len(sub_str)
    else:
        s['*'] = 0

    return s

# РЕШИТЬ ВОПРОС ДЛЯ ПУСТОЙ СТРОКИ
def find_substr(main_str, sub_str):
    obraz = offset_list(sub_str)

    m = len(sub_str) # длина образа
    i = m - 1 if m != 0 else len(main_str) # - индекс  строки (если длина образа 0, то не даем зайти в цикл (пустая строка не будет найдена в строке))
    j = m - 1 # - образа

    found = False

    while i < len(main_str) and not(found):
        if j == m - 1: # сравнение с последним символом образа
            if main_str[i] == sub_str[j]:
                if j == 0: # на случай, когда символ один (j == 1 - 1 = 0)
                    found = True
                i -= 1
                j -= 1
            else:
                if main_str[i] in sub_str:
                    i += obraz[main_str[i]]
                    j = m - 1
                else:
                    i += obraz['*']
                    j = m - 1
        else: # сравнение с НЕ последним символом образа
            if main_str[i] == sub_str[j]:
                if j == 0: # это последний проверенный символ образа
                    found = True
                i -= 1
                j -= 1
            else:
                i += obraz[sub_str[j]] + (m - j) # на какой символ мы хотим сдвинуться + те, которые уже не свопали
                j = m - 1


    return found


def boyer_moore_horspool(main_str, sub_str):
    result = find_substr(main_str, sub_str)
    if result:
        return 'Подстрока найдена!'
    
    return 'Подстрока НЕ найдена!'


class TestBoyerMooreHorspool(unittest.TestCase):
    def test_basic_found(self):
        self.assertEqual(boyer_moore_horspool("большие_метеоданные", "метео"), 'Подстрока найдена!')

    def test_basic_not_found(self):
        self.assertEqual(boyer_moore_horspool("большие_метеоданные", "климат"), 'Подстрока НЕ найдена!')

    def test_at_the_start(self):
        self.assertEqual(boyer_moore_horspool("метео_данные", "метео"), 'Подстрока найдена!')

    def test_at_the_end(self):
        self.assertEqual(boyer_moore_horspool("большие_метео", "метео"), 'Подстрока найдена!')

    def test_exact_match(self):
        self.assertEqual(boyer_moore_horspool("метео", "метео"), 'Подстрока найдена!')

 
    def test_single_char_found(self):
        self.assertEqual(boyer_moore_horspool("привет", "е"), 'Подстрока найдена!')

    def test_single_char_not_found(self):
        self.assertEqual(boyer_moore_horspool("привет", "х"), 'Подстрока НЕ найдена!')


    def test_empty_substring(self):
        self.assertEqual(boyer_moore_horspool("привет", ""), 'Подстрока НЕ найдена!')

    def test_empty_main_string(self):
        self.assertEqual(boyer_moore_horspool("", "метео"), 'Подстрока НЕ найдена!')

    def test_both_empty(self):
        self.assertEqual(boyer_moore_horspool("", ""), 'Подстрока НЕ найдена!')

    def test_substring_longer_than_main(self):
        self.assertEqual(boyer_moore_horspool("мет", "метео"), 'Подстрока НЕ найдена!')


    def test_repeating_found(self):
        self.assertEqual(boyer_moore_horspool("аааааа", "ааа"), 'Подстрока найдена!')

    def test_repeating_not_found(self):
        self.assertEqual(boyer_moore_horspool("ааааа", "аааааа"), 'Подстрока НЕ найдена!')
        
    def test_overlapping_pattern(self):
        self.assertEqual(boyer_moore_horspool("abababab", "abab"), 'Подстрока найдена!')

  
    def test_latin_found(self):
        self.assertEqual(boyer_moore_horspool("hello world", "world"), 'Подстрока найдена!')

    def test_digits(self):
        self.assertEqual(boyer_moore_horspool("abc123def", "123"), 'Подстрока найдена!')

    def test_spaces(self):
        self.assertEqual(boyer_moore_horspool("hello   world", "   "), 'Подстрока найдена!')


    def test_multiple_occurrences(self):
        self.assertEqual(boyer_moore_horspool("abcabcabc", "abc"), 'Подстрока найдена!')


if __name__ == '__main__':
    unittest.main()
