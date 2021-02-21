def get_result(pass_credits, defer_credits, fail_credits):
    global progress_count
    global module_trailer_count
    global module_retriever_count
    global exclude_count
    
    if pass_credits == 120 :
        if defer_credits == 0 and fail_credits == 0 :
            progress_count += 1
            print('Progress\n')
            
    elif pass_credits == 100 :
      if defer_credits == 20 and fail_credits == 0 :
          module_trailer_count += 1
          print('Progress - module trailer\n')
      elif defer_credits == 0 and fail_credits == 20 :
          module_trailer_count += 1
          print('Progress - module trailer\n')
          
    elif pass_credits == 80 :
      if defer_credits == 40 and fail_credits == 0 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 20 and fail_credits == 20 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 0 and fail_credits == 40 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
          
    elif pass_credits == 60 :
      if defer_credits == 60 and fail_credits == 0 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 40 and fail_credits == 20 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 20 and fail_credits == 40 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 0 and fail_credits == 60 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
          
    elif pass_credits == 40 :
      if defer_credits == 80 and fail_credits == 0 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 60 and fail_credits == 20 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 40 and fail_credits == 40 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 20 and fail_credits == 60 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 0 and fail_credits == 80 :
          exclude_count += 1
          print('Exclude\n')
           
    elif pass_credits == 20 :
      if defer_credits == 100 and fail_credits == 0 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 80 and fail_credits == 20 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 60 and fail_credits == 40 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 40 and fail_credits == 60 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 20 and fail_credits == 80 :
          exclude_count += 1
          print('Exclude\n')
      elif defer_credits == 0 and fail_credits == 100 :
          exclude_count += 1
          print('Exclude\n')
          
    elif pass_credits == 0 :
      if defer_credits == 120 and fail_credits == 0 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 100 and fail_credits == 20 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 80 and fail_credits == 40 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 60 and fail_credits == 60 :
          module_retriever_count += 1
          print('Do not Progress - module retriever\n')
      elif defer_credits == 40 and fail_credits == 80 :
          exclude_count += 1
          print('Exclude\n')
      elif defer_credits == 20 and fail_credits == 100 :
          exclude_count += 1
          print('Exclude\n')
      elif defer_credits == 0 and fail_credits == 120 :
          exclude_count += 1
          print('Exclude\n')

def print_histogram():
    print("Progress\t", progress_count, "\t:", "*"*progress_count)
    print("Trailing\t", module_trailer_count, "\t:", "*"*module_trailer_count)
    print("Retriever\t",module_retriever_count, "\t:", "*"*module_retriever_count)
    print("Excluded\t", exclude_count, "\t:", "*"*exclude_count)
    total_outcomes= progress_count + module_trailer_count + module_retriever_count + exclude_count
    print(total_outcomes, "outcomes in total.")
    
def vertical_histogram():
    print("Progress\tTrailing\tRetriever\tExcluded")

    for i in range(max(progress_count,module_trailer_count,exclude_count,module_retriever_count)):
        if(progress_count >= i+1):
            print("*", end="\t\t")
        else:
            print("\t\t", end="")
        if(module_trailer_count >= i+1):
            print("*", end="\t\t")
        else:
            print("\t\t", end="")
        if(module_retriever_count >= i+1):
            print("*", end="\t\t")
        else:
            print("\t\t", end="")
        if(exclude_count >= i+1):
            print("*")
        else:
            print()


print('Welcome to University progression outcomes prediction system !\n')

while True:
        progress_count = 0
        module_trailer_count = 0
        module_retriever_count = 0
        exclude_count=0
        while True:
            try:
                print('Enter your credits or press "q" to quit the program and print the histograms !\n')
                first_input=input('Enter your credits at Pass: ')
                if first_input == 'q':
                    print_histogram()
                    vertical_histogram()
                    break
                elif int(first_input) in range (0,140,20):
                    pass_credits = int(first_input)
                    while True:
                        try:
                            defer_credits=int(input('Enter your credits at Defer: '))
                            if defer_credits in range (0,140,20):
                                while True:
                                    try:
                                        fail_credits=int(input('Enter your credits at Fail: '))
                                        if fail_credits in range (0,140,20):
                                            if pass_credits + defer_credits + fail_credits != 120 :
                                                print('Total incorrect\n')
                                                break
                                            else:
                                                get_result(pass_credits,defer_credits,fail_credits)
                                                
                                                break
                                        else:
                                            print('Range Error\n')
                                    except ValueError:
                                        print('Integers required\n')                                     
                            else:
                                print('Range Error\n')
                            if defer_credits in range (0,140,20):
                                break
                        except ValueError:
                            print('Integers required\n')
                else:
                   print('Range Error\n')
            except ValueError:
                print('Integers required\n')

        break
        

