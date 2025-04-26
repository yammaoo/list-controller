array = [1,2,3,4,5,"hi","hi","hi"]

answered1 = False
counter = 0
counter2 = 0

print("there is an array of numbers")
print(array)
print("press 1 if you want to add an element to the array")
print("press 2 if you want to delete an element from the array")
print("press 3 if you want to check if an element exists in the array")

choice = int(input("press a number"))

while answered1 == False:
    if choice == 1:
      print("press 4 if you want to add text data to the array")
      print("press 5 if you want to add numerical data to the array")
      numtxt = int(input("press a number"))
      if numtxt == 4:
        txt = input("what text data do you want to add to the array?")
        array.append(txt)
        print("your text has been added to the array")
        print(array)
        answered1 = True
      elif numtxt == 5:
        number = int(input("what number do you want to add to the array?"))
        array.append(number)
        print("your number has been added to the array")
        print(array)
        answered1 = True
      else:
        print("answer the question appropriately please.")
        answered1 = False
    elif choice == 2:
        print(array)
        print("which element in the array do you want to delete?")
        print("starting from 0 on the left and increasing the number till the end")
        delete = int(input("press a number"))
        if delete < len(array):
            array.remove(array[delete])
            print(array)
            answered1 = True
        else:
            print("incorrect number, try again")
            answered1 = False
    elif choice == 3:
      print("press 6 if you want to search text data in the array")
      print("press 7 if you want to search numerical data in the array")
      searchnumtxt = int(input("press a number"))
      if searchnumtxt == 6:
        txtdata = input("type the text data you want to search in the array(CASE SENSITIVE)")
        for x in range(len(array)):
          if array[x] == txtdata:
            counter = counter + 1
        if counter >= 1:
          print("your text data, " + txtdata + ", has been found in the array")
          print("it has been found " + str(counter) + " time(s) in the array")
      
        else:
          print("your text " + txtdata + "has NOT been found in the array")
      answered1 = True
      if searchnumtxt == 7:
        numdata = int(input("type the numerical data you want to search in the array"))
        for x in range(len(array)):
          if array[x] == numdata:
            counter2 = counter2 + 1
        if counter2 >= 1:
          print("your number, " + str(numdata) + " ,has been found in the array")
          print("it has been found " + str(counter2) + " time(s) in the array")
        else:
          print("your number " + str(numbdata) + " has NOT been found in the array")
      answered1 = True
      else:
        print("answer the question appropriately please")
      answered1 = False
    else:
      print("answer the question appropriately please")
      answered1 = False  
          
      

