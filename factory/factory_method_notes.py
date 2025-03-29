# Without Factory Method
class User:
  def __init__(self, type):
    if type == 'admin':
      # admin-specific setup
      ...
    elif type == 'regular':
      # regular user setup
      ...
# Client directly creates objects, knowing internal logic
user = User('admin')

class User:
  def __init__(self, type):
    if type == 'admin':
      # admin-specific setup
      ...
    elif type == 'regular':
      # regular user setup
      ...
# Client directly creates objects, knowing internal logic
user = User('admin')