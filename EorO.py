#definingAVarForInput

def name_ok():

  print('What is your Name' + "?")

name_ok()

name= input()

def n_o():

  print(f'\nHello @{name}')

n_o()

#WhileLoopForTakingUserInputMultipleTimes

while True:

  

  n = input('\nPlease Enter Number:- \n @oxyop-op ')

  try:

    if int(n)%2 == 0:

      print(f'{n} is An Even Number')

    elif int(n)%2 != 0:

      print(f'{n} is Odd Number')

    else:

      print("Invalid")

  except (TypeError, ValueError):

    print('Please Type Valid Value')

    

  

  

