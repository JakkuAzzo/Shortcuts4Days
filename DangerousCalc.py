
print('''
      I'm tired of seeing long if-else statements in my code. 
      And seeing exercises that ask for hard coded explanations for the program.
      My aim is from now on to make programs that are more dynamic, don't have hard coded values, and don't follow the norm.
      Wby? Because I can. And because I want to.
      Let's try to make a calculator that can take in a string and evaluate it. using the eval() function.
      For example, if I enter '1+1', the program should print '1+1 = 2'.
      ''')

input_str = str(input("Enter a calculation expression such as '1+1' : "))
print(input_str, "=", eval(input_str))



  