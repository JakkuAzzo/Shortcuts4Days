import subprocess

print('''
      Welcome to DangerousCalc3!
      The last Dangerous Calc was vulnerable to code injection, in two ways:
      Through eval() and through pickle.
      Enter a math expression, 
      we'll evaluate it without eval(), exec(), conditionals, or pickle.
      Still refuse to use multiple conditions, so we'll use subprocess.run() instead.
      Try enter an expression like '1 + 1' :
      ''')

input_str = input("Enter a calculation expression such as '1+1' or '2*3-4' : ")

try:
    process = subprocess.run(["python3", "-c", f"print({input_str})"], capture_output=True, text=True, check=True)
    result = process.stdout.strip()
    print(f"Result: {result}")
except subprocess.CalledProcessError as e:
    print("Error occurred while evaluating the expression.")
    print(e)