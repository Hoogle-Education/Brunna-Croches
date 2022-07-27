def isMultipleOfTwo(number):
  if number%2 == 0 : 
    return True

  return False

def isMultipleOfFive(number):
  if number%5 == 0 : 
    return True

  raise Exception('Desculpe, este valor não permitido')

def test(number) :
  if isMultipleOfTwo(number):
    return 'deu errado'
  
  if isMultipleOfFive(number):
    return 'deu errado'

  return 'deu certo'