class Expression_Validator:
  def __init__(self, expression):
    stack = Stack()

    for char in expression:
      if char == '(' or char == '[' or char == '{':
        stack.stack(char)

      if char == ')':
        if stack.see_top() != '(':
          return print('Invalid expression')
        else:
          stack.unstack()

      if char == ']':
        if stack.see_top() != '[':
          return print('Invalid expression')
        else:
          stack.unstack()

      if char == '}':
        if stack.see_top() != '{':
          return print('Invalid expression')
        else:
          stack.unstack()
    
    if stack.is_empty():
      return print('Valid expression')
    else:
      return print('Invalid expression')