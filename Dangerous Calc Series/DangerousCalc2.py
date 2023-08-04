import pickle

print('''
      Dangerous Calc's eval() function had terrible consequences, 
      since eval() can execute any code, not just math expressions. 
      Infuriating, but nevermind, we'll just have to write another, 
      safer calculator that can only do math without bothering with
      multiple conditions.
      eASY pEASY, rIGHT?
      ''')

input_str = str(input("Enter a calculation expression such as '1+1' : "))

# Pickle the input expression
with open('expression.pkl', 'wb') as file:
    pickle.dump(input_str, file)

# Unpickle the expression
with open('expression.pkl', 'rb') as file:
    expression = pickle.load(file)

    # Use exec() for evaluation (still vulnerable)
    result = None
    exec(f'result = {expression}')

    print(expression, "=", result)
