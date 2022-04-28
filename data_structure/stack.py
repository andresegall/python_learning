class Stack:
  def __init__(self):
    self.__top = -1
    self.__content = ""

  def is_empty(self):
    if self.__top == -1:
      return True
    else:
      return False

  def stack(self, value):
    self.__top += 1
    self.__content += value

  def unstack(self):
    if not self.is_empty():
      self.__top -= 1
      self.__content = self.__content[:-1]

  def see_top(self):
    if not self.is_empty():
      return self.__content[self.__top]