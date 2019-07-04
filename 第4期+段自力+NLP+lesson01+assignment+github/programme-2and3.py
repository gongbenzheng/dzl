import random
import pandas as pd
import re
from collections import Counter
import jieba

# 功能：用条件概率，计算一个句子的正确的概率，把自动生成的句子最可能的找出来
#在西部世界里，一个”人类“的语言可以定义为：

human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们 
寻找 = 找找 | 想找点 
活动 = 乐子 | 玩的
"""


#一个“接待员”的语言可以定义为

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = null
具体业务 = 什么 | 帮助 
结尾 = 吗？
"""

choice = random.choice
# filename = 'sqlResult_1558435.csv'
filename = 'movie_comments.csv'
content = pd.read_csv(filename, encoding='gb18030')
# articles = content['content'].tolist()
articles = content['comment'].tolist()

def token(string):
    # we will learn the regular expression next course.
    return re.findall('\w+', string)

with_jieba_cut = Counter(jieba.cut(articles[110]))
articles_clean = [''.join(token(str(a)))for a in articles]
with open('article_9k.txt', 'w') as f:
    for a in articles_clean:
        f.write(a + '\n')

def cut(string): return list(jieba.cut(string))

TOKEN = []

for i, line in enumerate((open('article_9k.txt'))):
    if i % 100 == 0:
        print(i)
    # replace 10000 with a big number when you do your homework.
    if i > 10000: break
    TOKEN += cut(line)

words_count = Counter(TOKEN)

def prob_1(word):
    return words_count[word] / len(TOKEN)

TOKEN = [str(t) for t in TOKEN]
TOKEN_2_GRAM = [''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
words_count_2 = Counter(TOKEN_2_GRAM)
def prob_2(word1, word2):
    if word1 + word2 in words_count_2: return words_count_2[word1+word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)

# 在上一个事件发生的情况下事件的发生概率（请指点一下这个思路是否正确）
def get_probablity(sentence):
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        if i==0:
            probability = prob_1(word)
        else:
            previous_ = words[i - 1]
            probability = prob_2(word, previous_)
        sentence_pro *= probability
    return sentence_pro


def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

def generate(gram, target):
    if target not in gram: return target  # means target is a terminal expression

    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

# 根据语法树随机生成20个句子
need_compared = []
sent = ''
for i in range(20):
    sent1 = generate(gram=create_grammar(host, split='='), target='host')
    print(sent1)
    sent +=' '+sent1

need_compared.append(sent)

# 找出生成的句子中概率最大的一个
for s in need_compared:
    sentList = []
    sentArray = s.split()
    num = sentArray.__len__()

    # pythonic
    [sentList.append((sentArray[i], get_probablity(sentArray[i]))) for i in range(num)]
    better = sorted(sentList, key=lambda x: x[1], reverse=True).pop(0)
    print('**************************RESULT************************')
    print('{} is more possible'.format(better))

    # j = 0
    # for i in range(num):
    #     if get_probablity(sentArray[i])>get_probablity(sentArray[j]):
    #         j=i
    #     s1 = sentArray[i]
    #     p1 = get_probablity(sentArray[i])
    #     print('-' * 4 + ' {} with probility {}'.format(s1, p1))
    #
    # better = sentArray[j]
    # print('{} is more possible'.format(better))


    # for i in range(num):
    #     sentList.append((sentArray[i],get_probablity(sentArray[i])))
    #
    # print(sorted(sentList, key=lambda x: x[1], reverse=True))
    # print(sorted(sentList, key=lambda x: x[1], reverse=True).pop(0))




















