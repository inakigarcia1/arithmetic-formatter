def arithmetic_arranger(problems, answers = False):
  results = {}
  i = 0
  if len(problems) >  5:
    return 'Error: Too many problems.'

  for operation in problems:
    if '*' in operation or '/' in operation:
      return "Error: Operator must be '+' or '-'."

    op = operation.split()

    if not op[0].isnumeric() or not op[- 1].isnumeric():
      return 'Error: Numbers must only contain digits.'

    if len(op[0]) > 4 or len(op[-1]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    num1 = int(op[0])
    num2 = int(op[-1])

    if op[1] == '+':
      result = num1 + num2
      sign = '+'
    else:
      result = num1 - num2
      sign = '-'

    results['op' + str(i)] = [num1, num2, result, sign]
    i = i + 1

  line1 = []
  line2 = []
  for i in range(len(results)):
    element = 'op' + str(i)
    subelement = results[element]
    number1 = subelement[0]
    number2 = subelement[1]
    line1.append(number1)
    line2.append(number2)

    
  spaces = {}
  for i in range(len(results)):
    if len(str(line1[i])) > len(str(line2[i])):
      spaces['op' + str(i)] = len(str(line1[i])) - len(str(line2[i]))
    else:
      spaces['op' + str(i)] = len(str(line2[i])) - len(str(line1[i]))

  
  arrange1 = ''
  for i in range(len(line1)):
    strNum1 = str(line1[i])
    strNum2 = str(line2[i])
    strSpaces = spaces['op' + str(i)]

    if len(strNum1) > len(strNum2):
      if i == 0:
        strNum1 = strNum1.rjust(len(strNum1) + 2, ' ')
        arrange1 += strNum1
      else:
        strNum1 = strNum1.rjust(len(strNum1) + 6, ' ')
        arrange1 += strNum1
    else:
      if i == 0:
        strNum1 = strNum1.rjust(len(strNum1) + 2 + strSpaces, ' ')
        arrange1 += strNum1
      else:
        strNum1 = strNum1.rjust(len(strNum1) + 6 + strSpaces, ' ')
        arrange1 += strNum1


  arrange2 = ''
  for i in range(len(line2)):
    strNum1 = str(line1[i])
    strNum2 = str(line2[i])
    extraction = results['op' + str(i)]
    sign = extraction[-1]
    strSpaces = spaces['op' + str(i)]

    if len(strNum1) > len(strNum2):
      if i == 0:
        arrange2 += sign
        strNum2 = strNum2.rjust(len(strNum2) + 1 + strSpaces, ' ')
        arrange2 += strNum2
      else:
        arrange2 += sign.rjust(5, ' ')
        strNum2 = strNum2.rjust(len(strNum2) + 1 + strSpaces, ' ')
        arrange2 += strNum2
    else:
      if i == 0:
        arrange2 += sign
        strNum2 = strNum2.rjust(len(strNum2) + 1, ' ')
        arrange2 += strNum2
      else:
        arrange2 += sign.rjust(5, ' ')
        strNum2 = strNum2.rjust(len(strNum2) + 1, ' ')
        arrange2 += strNum2

  arrange3 = ''
  for i in range (len(arrange2)):
    if arrange2[i] == '+' or arrange2[i] == '-':
      arrange3 += '-'
      continue
    if arrange2[i].isspace():
      if arrange2[i - 1] == '+' or arrange2[i - 1] == '-':
        arrange3 += '-'
        continue
    if arrange1[i].isnumeric() or arrange2[i].isnumeric():
      arrange3 += '-'
      continue
    else:
      arrange3 += ' '
  
  if answers:
    arrange4 = ''
    allResults = []

    for i in range(len(results)):
      values = results['op' + str(i)]
      allResults.append(str(values[2]))

    arrange4 = ''
    numResult = 0
    count = 0
    num = 0
    for i in range(len(arrange3)):
      if i == len(arrange3) - 1:
        num = allResults[numResult]
        num = num.rjust((count + 1) + 4, ' ')
        arrange4 += num
        numResult += 1
        count = 0
      
      if arrange3[i] == '-':
        count += 1
        continue

      if arrange3[i - 1] == '-':
        num = allResults[numResult]
  
        if numResult == 0:
          num = num.rjust(count, ' ')
          count = 0
          numResult += 1
          arrange4 += num
          continue

        num = num.rjust(count + 4, ' ')
        arrange4 += num
        numResult += 1
        count = 0
        
      else:
        count = 0 
    arranged_problems = f'{arrange1}\n{arrange2}\n{arrange3}\n{arrange4}'
  else:
    arranged_problems = f'{arrange1}\n{arrange2}\n{arrange3}'

  return arranged_problems
