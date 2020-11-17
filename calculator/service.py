from .views import UserForm
import re
import psycopg2

con = psycopg2.connect(
  database="db",
  user="dbadmin",
  password="dbadmin",
  host="localhost",
  port="5432"
)

print("Database opened successfully")

class Calculator:

    def get_extension(self,expression_and_values):
       expression = expression_and_values["expression"]
       values = expression_and_values["variables"]
       new_values = values.values()
       result_values = ''
       for key in new_values:
           result_values += key + ','
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
       cur = con.cursor()
       cur.execute(
           f"INSERT INTO Expressions (Expression,Values,Result) VALUES ('{expression}','{result_values}',{result}) RETURNING id"
       )
       con.commit()
       id = str(cur.fetchone())
       id = id[0:-2]
       id = id[1:]
       itog = {'expression_id': id}

       return itog



    def get_result(self,expression_id):
        expression_id = expression_id['expression_id']
        cur = con.cursor()
        cur.execute(
            f"SELECT Result FROM Expressions WHERE Id = {expression_id}"
        )
        con.commit()
        result = str(cur.fetchone())
        result = result[1:-2]
        result = {'result': int(result)}
        return result