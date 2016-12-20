import functools


def swap_a_b():
    """First test exercise"""
    a = 5
    b = 12
    (a, b) = (b, a)
    return (a, b)


def upcase_reverse(text):
    """Second test exercise"""
    if not isinstance(text, str):
        raise TypeError('Text must be string')

    return text.upper()[::-1]


def count_word_and_sentence(text):
    """Third test exercise"""
    if not isinstance(text, str):
        raise TypeError('Text must be string')

    sentence_count = text.count('.')
    word_count = len(text.strip().split(' '))
    return sentence_count, word_count


def sum_and_multi(number):
    """Fourth test exervise"""
    if not isinstance(number, int):
        raise TypeError('Text must be string')

    number_as_list = [int(s) for s in str(number)]
    sum_of_numerals = sum(number_as_list)
    product_of_numerals = functools.reduce(lambda x, y: x * y, number_as_list)
    return sum_of_numerals, product_of_numerals


def main():
    print('swap a and b: {}'.format(swap_a_b()))
    print('upcase reverse: {}'.format(upcase_reverse("hello world!")))
    text = "Написать функцию, которая во входных параметрах принимает строку с текстом.\
            Функция должна возвращать количество слов и предложений в строке. "
    print('number of word: {1} \nand sentence: {0}'.format(*count_word_and_sentence(text)))
    print('sum of numerals: {}\nproduct of numerals: {}'.format(*sum_and_multi(5869)))


if __name__ == "__main__":
    main()
