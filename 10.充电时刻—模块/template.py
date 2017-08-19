#创建一个模板系统：
import fileinput,re
#创建模式匹配中括号里的字段
field_pat=re.compile(r'\[(.+?)\]')

#收集变量
scope={}

#定义函数，用于re.sub中：
def replacement(match):
    code=match.group(1)
    try:
        #如果字段可以求值，返回它：
        return str(eval(code,scope))
    except SyntaxError:
        # 否则执行相同作用域内的赋值语句
        exec code in scope
        #返回空字符串
        return ''

#将所有文本以一个字符串的形式获取：
lines=[]
for line in fileinput.input():
     lines.append(line)
text=''.join(lines)
#将field模式的所有匹配项都替换掉：
print field_pat.sub(replacement,text)
#说明：上述案列：
#定义了用于匹配字段的模式。
#创建充当模板作用域的字典。
#定义具有下列功能的替换函数。
  #.将组1从匹配中取出，放人code中;
  #.通过将作用域字典作为命名空间来对code进行求值，将结果转换为字符串返回。如果
  # 成功的话，字段就是个表达式，一切正常。否则(也就是引发了SyntaxError异常)，跳
  #  到下一步;
  #.执行在相同命名空间(作用域字典)内的字段来对表达式求值，返回空字符串(因为
  #  赋值语句没有对任何内容进行求值)。
#使用fileinput读取所有可用的行，将其放入列表，组合成一个大字符串。
#将所有field pat的匹配项用re.sub中的替换函数进行替换，并且打印结果。