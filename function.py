"""
作者：ZYC
时间：2021年09月20日
"""
key_word = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']


def manage_txt(all_lines):
    chars = ['(', ')', '{', '}', ':', ',', '<', '>', '=', '+', '-', '#', ';']
    count = 0
    all_words = []
    for line in all_lines:
        # 删除单行注释
        if '//' in line:
            temp = line.index('//')
            line = line[:temp]
        # 删除多行注释
        if '/*' in line:
            first_line = all_lines.index(line)
            for new_line in all_lines[first_line:]:
                if '*/' not in new_line:
                    del all_lines[first_line]
                else:
                    del all_lines[first_line]
                    break
        # 删除双引号内内容
        while True:
            if '"' in line:
                first_subscript = line.index('"')
                last_subscript = line[first_subscript + 1:].index('"')
                line = line[:first_subscript] + line[first_subscript + last_subscript + 2:]
            else:
                break
        # 删除单引号内内容
        while True:
            if "'" in line:
                first_subscript = line.index("'")
                last_subscript = line[first_subscript + 1:].index("'")
                line = line[:first_subscript] + line[first_subscript + last_subscript + 2:]
            else:
                break
        # 将特殊字符转化为空格，分词
        for ch in chars:
            line = line.replace(ch, ' ')
        word_line = line.split()

        # 将else if看成整体
        if 'else' in word_line and 'if' in word_line:
            all_words.append('elif')
            count += 2
        else:
            for word in word_line:
                if word in key_word:
                    count += 1
                    all_words.append(word)
    return all_words, count


def switch_case_num(all_words):
    """统计switch-case个数"""
    case_num = []
    switch_num = 0

    while True:
        num = 0
        if 'default' in all_words:
            default_subscript = all_words.index('default')
            switch_num += 1
            for word in all_words[:default_subscript]:
                if word == 'case':
                    num += 1
            case_num.append(num)
            del all_words[:default_subscript + 1]
        else:
            break
    return case_num, switch_num


def if_else_elif_num(all_words):
    """统计if-else和if-else if语句个数"""
    if_num = 0
    new_list = []
    if_elif_num = 0
    for word in all_words:
        count = 0  # 标志位，1  则为if-else-if 语句 ，0 为if-else语句

        if word == 'if':
            if_num += 1

        if word == 'if' or word == 'elif':
            new_list.append(word)
        elif word == 'else':
            while True:
                temp = new_list.pop()
                if temp == 'elif':
                    count = 1
                elif temp == 'if':
                    break
        if count == 1:
            if_elif_num += 1
    for word in new_list:  # 删除出现if-elseif-elseif的情况
        if word == 'if':
            if_num -= 1

    return if_num, if_elif_num
