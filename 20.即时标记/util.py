# -*- coding:utf-8 -*-
# 文本快生成器
def lines(file_txt):
    for line in file_txt:
        yield line
        yield '\n'
def blocks(file_txt):
    block=[]
    for line in lines(file_txt):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]