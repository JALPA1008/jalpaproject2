print('Welcome to the Pattern Generator and Number Analyzer!')

while True:

  print('select an option:')
  print("1. Generate a Pattern")
  print("2. Analyze a Range of Numbers")
  print("3. Exit")

  choice = input("Enter your choice (1-3): ")

  if choice == "1":

    a = int(input("Enter number of rows: "))
    if a <= 0:
        print("Invalid row count!")
        break
    else:
        print("Right-Angled Triangle using FOR LOOP:")
        for i in range(1, a + 1):
            for j in range(i):
                print("*", end=" ")
            print()
        i = a
        print("Right-Angled Triangle using WHILE LOOP:")
        while i >= 1:
            j = 1
            while j <= i:
                print("*", end=" ")
                j += 1
            print()
            i -= 1  

  elif choice == "2":

         start = int(input("Enter starting number: "))
         end = int(input("Enter ending number: "))
         total = 0
         print("===== NUMBER ANALYSIS =====")
         for num in range(start, end + 1):
            if num == 0:
                pass
            if num % 2 == 0:
               print(num, "is EVEN")
            else:
               print(num, "is ODD")
            total += num
         print("Sum of all numbers =", total)
    
  elif choice == "3":
         print("Program Exited Successfully!")
         break
else: 
         print("Invalid Choice! Please enter 1, 2, or 3.")