import random
choice = random.choice

#丈夫回复老婆：

husband = """
husband = 自己 意愿 标点
自己 = 我 | 俺 | 杂家 
意愿 = 想 | 不想 
标点 = ！ | 。
"""

#老婆询问老公：

wife = """
wife = 寒暄 标点 询问 业务相关 结尾 
标点 = ，
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = Dear | Darling | Honey 
打招呼 = hi | hello | 喂 | 孩他爹 | 老头子
询问 = 你想吃 | 你吃
业务相关 = 具体业务
玩玩 = null
具体业务 = 早餐 | 午餐 | 晚餐 
结尾 = 吗？
"""

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


for i in range(2):
     print(generate(gram=create_grammar(wife, split='='), target='wife'))
     print(generate(gram=create_grammar(husband, split='='), target='husband'))