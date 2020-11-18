import re

def get_extension(expression):
  expression = (expression)
  expression_list = []
  for char in expression:
    expression_list.append(char)
  # kolvo = expression_list[0]
  # expression_list.pop(0)
  sign = []
  value = []
  for i in expression_list:
    if i != '.':
      if i == 1:
        sign.append("+")
        expression_list.pop(0)
      if i == 2:
        sign.append("-")
        expression_list.pop(0)
      if i == 3:
        sign.append("*")
        expression_list.pop(0)
    elif i == '.':
      expression_list.pop(0)
      break

  for i in expression_list:
    value.append(i)

  result = 0
  for znak in sign:
    try:
      if znak == '*':
        index = sign.index('*')
        result = float(value[index]) * float(value[index + 1])
        del value[index]
        del value[index]
        value.insert(index, result)
        # del sign[index]
    except BaseException:
      pass
  for znak in sign:
    try:
      if znak == '+':
        some_result = float(value[0]) + float(value[1])
        value.pop(0)
        value.pop(0)
        value.insert(0, some_result)
        result += some_result
      if znak == '-':
        some_result = float(value[0]) - float(value[1])
        value.pop(0)
        value.pop(0)
        value.insert(0, some_result)
        result += some_result
    except BaseException:
      pass
  result = value[0]


  return result