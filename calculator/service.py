from .views import UserForm
import re
import _sqlite3




class Calculator:

    def get_extension(self,expression_and_values):
       expression = expression_and_values["expression"]
       print(expression)
       values = expression_and_values["variables"]
       print(values)
       value = []
       sign = []
       for key in values:
           value.append(values[key])
       value_of_expression = re.split('[^*,+,-]', expression)
       for val in value_of_expression:
           if val == '':
               pass
           else:
            sign.append(val)
       result = 0
       for znak in sign:
           try:
                if znak == '*':
                    index = sign.index('*')
                    result = float(value[index]) * float(value[index+1])
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
       # print(result)
       conn = _sqlite3.connect("db.sqlite3")  # или :memory: чтобы сохранить в RAM
       cursor = conn.cursor()
       cursor.execute("INSERT INTO CALCULATOR VALUES('hello', '123', '5')")
       conn.commit()
