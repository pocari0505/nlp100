def generate_n_gram(n, s):
    '''最後の要素がn単語orn文字あることを必須とするならば
    それぞれのforはrange(len - (n-1))'''
    l = s.split(' ')
    n_gram = [''.join(l[i:i + n]) for i in range(len(l))]
    if len(n_gram) == 1:
        n_gram = [l[0][i:i + n] for i in range(len(l[0]))]
    return n_gram


def main():
    s = 'I am an NLPer'

    word_bi_gram = generate_n_gram(2, s)
    print('word bi-bram:', end='')
    print(word_bi_gram)

    l = ''.join(s.split(' '))
    str_bi_gram = generate_n_gram(2, l)
    print('string bi-bram:', end='')
    print(str_bi_gram)


if __name__ == '__main__':
    main()
