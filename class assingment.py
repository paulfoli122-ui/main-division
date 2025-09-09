# a = str("are you young")
# for b in
import math
import sys
import time
#from imaplib import Flags
from statistics import median
from token import NUMBER

#from PyQt5.QtNfc import removeTitle
from tabulate import tabulate

# def add_numbers(numbers):
#     total=0
#     for n in numbers:
#         total+=n
#     return total
# def divide_numbers(x,y):
#     ans=x/y
#     return ans
from colorama import Fore, Style
null='\n'
choice_mean=[]
choice_median=[]
choice_mode=[]
sum=0
running=True
while running:
    print(null)
    print("Chose option you are using")
    print("A.Raw data")
    print("B.Ungrouped data")
    print("C.Grouped data")
    print("E.Quit")
    user_first_choice=input(">>>>>>>>: ").upper()
    match user_first_choice:
        case "A":
            while True:
                print(Style.RESET_ALL+"Choose an option")
                print("A.Mean")
                print("B.Median")
                print("C.Mode")
                print("D.Mean deviation")
                print("E.Standard Deviation")
                print("Press q to quit")
                choice=input(">>>>>>>>: ").upper()



                print(null)
                if choice =='A':
                    print("FOR MEAN")
                    # num_choice=0
                    # mean_choice=0
                    mean_numbers_list=[]
                    #THIS IS TO CHECK IF THE USER ENTERS A NUMBER AND NOTHING ELSE
                    while True:
                        mean_num_of_numbers=input(Style.RESET_ALL+"Enter the number of numbers: ")
                        if not mean_num_of_numbers.isdigit():
                            print(Fore.RED+"INCORRECT ANSWER")
                            print(Fore.RED+"Enter a number")
                            continue
                        else:
                            break
                    mean_num_of_numbers = int(mean_num_of_numbers)
                    print(f"Enter {mean_num_of_numbers} numbers")
                    for i in range(mean_num_of_numbers):
                        # THIS IS TO CHECK IF THE USER ENTERS A NUMBER AND NOTHING ELSE
                        while True:
                            mean_number=input(Style.RESET_ALL+f"Enter number {i+1}: ")
                            if not mean_number.isdigit():
                                print(Fore.RED+"INVALID OPTION")
                                print(Fore.RED+"Enter a number")
                                continue
                            else:
                                break
                        mean_number=int(mean_number)
                        mean_numbers_list.append(mean_number)
                    for number in mean_numbers_list:
                        sum+=number
                    average=sum/mean_num_of_numbers
                    print(null)
                    print(Fore.YELLOW+f"The average of your numbers is {average:.2f}")


                elif choice=='B':
                    print("FOR MEDIAN")
                    # num_choice=0
                    # median_choice=0
                    median_numbers_list=[]

                    while True:
                        median_num_of_numbers=input(Style.RESET_ALL+"Enter number of numbers: ")
                        if not median_num_of_numbers.isdigit():
                            print(Fore.RED+"INCORRECT ANSWER")
                            print(Fore.RED+"ENTER A NUMBER")
                            continue
                        else:
                            break
                    median_num_of_numbers=int(median_num_of_numbers)
                    print(f"Enter {median_num_of_numbers} numbers: ")
                    for number in range(median_num_of_numbers):
                        while True:
                            median_number=input(Style.RESET_ALL+f"Enter number {number+1}: ")
                            if not median_number.isdigit():
                                print(Fore.RED + "INCORRECT ANSWER")
                                print(Fore.RED + "ENTER A NUMBER")
                                continue
                            else:
                                break
                        median_number=int(median_number)
                        median_numbers_list.append(median_number)
                    median_numbers_list.sort()
                    print()
                    print("SORTED NUMBERS")
                    for i in median_numbers_list:
                        print(i, end=" ")
                    print()
                    import statistics
                    ans=statistics.median(median_numbers_list)
                    print(Fore.YELLOW+f"The median of your numbers are: {ans}")


                elif choice=="C":
                    print("FOR MODE")
                    # num_choice=0
                    mode_number_list=[]
                    while True:
                        mode_num_of_numbers=input(Style.RESET_ALL+"Enter number of numbers: ")
                        if not mode_num_of_numbers.isdigit():
                            print(Fore.RED+"INCORRECT ANSWER")
                            print(Fore.RED+"ENTER A NUMBER")
                            continue
                        else:
                           break
                    mode_num_of_numbers=int(mode_num_of_numbers)
                    print(f"Enter {mode_num_of_numbers} numbers")
                    for number in range(mode_num_of_numbers):
                        while True:
                            mode_number=input(Style.RESET_ALL+f"Enter number {number+1}: ")
                            if not mode_number.isdigit():
                                print(Fore.RED + "INCORRECT ANSWER")
                                print(Fore.RED + "ENTER A NUMBER")
                                continue
                            else:
                                break
                        mode_number_list.append(mode_number)
                    from collections import Counter
                    counter=Counter(mode_number_list)
                    most_common_num, count=counter.most_common(1)[0]
                    print(most_common_num)
                    if most_common_num==mode_number_list[0]:
                        print(Fore.CYAN+"There is no number that occurs more than once")
                    #print(most_common_num)
                    print(Fore.YELLOW+f"The mode of your numbers is {most_common_num} it appears {count} times")

                                    #from collections import Counter
                                    # numbers = [1, 2, 2, 3, 3, 4]
                                    #
                                    # counts = Counter(numbers)
                                    # max_count = max(counts.values())
                                    # most_common = [num for num, freq in counts.items() if freq == max_count]
                                    #
                                    # print(most_common)
                                    # print("Frequency:", max_count)
                elif choice=='D':
                    print("For Mean Deviation you have find the mean")
                    mean_numbers=0
                    total=0
                    mean_numbers_list=[]
                    sum_of_absolute_values = []
                    while True:
                        mean_num_of_numbers=input("Enter the number of numbers: ")
                        if not mean_num_of_numbers.isdigit():
                            print(Fore.RED+f"Enter a number{mean_numbers} is not a valid number")
                            continue
                        else:
                            break
                    mean_num_of_numbers=int(mean_num_of_numbers)
                    print(f"Enter {mean_num_of_numbers} numbers")
                    for number in range(mean_num_of_numbers):
                        while True:
                            mean_deviation_choice=input(Style.RESET_ALL+f"Enter number {number+1}: ")
                            if not mean_deviation_choice.isdigit():
                                print(Fore.RED + f"Enter a number! {mean_numbers} is not a valid number")
                                continue
                            else:
                                break
                        mean_deviation_choice=int(mean_deviation_choice)
                        mean_numbers_list.append(mean_deviation_choice)
                    for number in mean_numbers_list:
                        total+=number
                    average=total/mean_num_of_numbers
                    print(mean_numbers_list)
                    absolute_values=0
                    for number in mean_numbers_list:
                        absolute_values+=abs((number-average))
                    print(sum_of_absolute_values)

                    mean_deviation=absolute_values/mean_num_of_numbers

                    print(Fore.CYAN+f"The mean deviation of the numbers is {mean_deviation}")

                elif choice=="E":
                    print("For Standard Deviation you have find the mean")
                    mean_numbers = 0
                    total = 0
                    mean_numbers_list = []
                    while True:
                        mean_num_of_numbers = input(Style.RESET_ALL+"Enter the number of numbers: ")
                        if not mean_num_of_numbers.isdigit():
                            print(Fore.RED + f"Enter a number {mean_num_of_numbers} is not a valid number")
                            continue
                        else:
                            break
                    mean_num_of_numbers = int(mean_num_of_numbers)
                    print(f"Enter {mean_num_of_numbers} numbers")
                    for number in range(mean_num_of_numbers):
                        while True:
                            mean_deviation_choice = input(Style.RESET_ALL + f"Enter number {number + 1}: ")
                            if not mean_deviation_choice.isdigit():
                                print(Fore.RED + f"Enter a number! {mean_deviation_choice} is not a valid number")
                                continue
                            else:
                                break
                        mean_deviation_choice = int(mean_deviation_choice)
                        mean_numbers_list.append(mean_deviation_choice)
                    for number in mean_numbers_list:
                        total += number
                    average = total / mean_num_of_numbers
                    #print(mean_numbers_list)
                    absolute_values = 0
                    for number in mean_numbers_list:
                        absolute_values += abs((number - average)**2)
                    mean_deviation = absolute_values / mean_num_of_numbers
                    population_or_sample = input(
                    Style.RESET_ALL + "Are you calculating the standard deviation for population or sample(press P or S): ").upper()
                    # while True:
                    #     population_or_sample=input(Style.RESET_ALL+"Are you calculating the standard deviation for population or sample(press P or S): ").upper()
                    #     if population_or_sample!='P' or population_or_sample!='S' or population_or_sample!='s' or population_or_sample!='p':
                    #         print(Fore.RED+"INVALID RESPONSE")
                    #         continue
                    #     else:
                    #         break
                    print()
                    if population_or_sample=="P":
                        standard_devaiation = math.sqrt(absolute_values / mean_num_of_numbers)
                        print(Fore.CYAN+f"The standard deviation of your numbers is {standard_devaiation:.2f}")
                    elif population_or_sample=="S":
                        standard_devaiation = math.sqrt(absolute_values / (mean_num_of_numbers-1))
                        print(Fore.CYAN+f"The standard deviation of your numbers is {standard_devaiation:.3f}")
                    else:
                        print(Fore.RED+"INCORRECT RESPONSE!")
                    #print(absolute_values, mean_num_of_numbers)
                elif not choice.isalpha():
                    print(Fore.RED+"Enter valid option(A,B or C)"+Style.RESET_ALL)
                    continue
                elif choice=='Q' or choice=='QUIT':
                    print("Bye"+Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED+f"{choice} not valid"+Style.RESET_ALL)
                    continue

        case "B":
                frequency_list=[]
                value_list=[]
                fx_list=[]
                cumulative_freq_list=[]
                absolute_values_list=[]
                absolute_values__squared_list=[]
                total_of_absolute_values__squared=0
                total_of_frequency=0
                total_of_fx=0
                total=0
                median_value=0
                mode_freq=0
                total_of_abolute_values=0
                while True:
                    mean_num_of_numbers=input(Style.RESET_ALL+"Enter number of numbers: ")
                    if not mean_num_of_numbers.isdigit():
                        print(Fore.RED+"INVALID RESPONSE")
                        continue
                    else:
                        break
                mean_num_of_numbers=int(mean_num_of_numbers)
                print("Enter the values(x) of the digits")
                for i in range(mean_num_of_numbers):
                    while True:
                        values_num=input(Style.RESET_ALL+f"Enter the value(x) of number {i+1}: ")
                        if not values_num.isdigit():
                            print(Fore.RED + "INVALID RESPONSE")
                            continue
                        else:
                            break
                    values_num = int(values_num)
                    value_list.append(values_num)
                print()
                for i in range(mean_num_of_numbers):
                    while True:
                        frequencies_num=input(Style.RESET_ALL+f"Enter the frequency of number {i+1}: ")
                        if not frequencies_num.isdigit():
                            print(Fore.RED + "INVALID RESPONSE")
                            continue
                        else:
                            break
                    frequencies_num = int(frequencies_num)
                    frequency_list.append(frequencies_num)
                print()
                #THIS FOR THE THE VISUAL REPRESENTARION OF THE TABLE WITH THE VALUES


                for frequency, value in zip(frequency_list,value_list):
                    fx_num=frequency*value
                    fx_list.append(fx_num)

                for number in frequency_list:
                    total_of_frequency+=number
                for number in fx_list:
                    total_of_fx+=number
                for number in frequency_list:
                    total+=number
                    cumulative_freq_list.append(total)
                # MEAN CALCULATION
                average = total_of_fx / total_of_frequency

                # MEAN DEVIATION
                for value,frequency in zip(value_list, frequency_list):
                    absolute_values = frequency* abs(value - average)
                    absolute_values_list.append(absolute_values)
                for value in absolute_values_list:
                    total_of_abolute_values += value
                mean_deviation_answer=total_of_abolute_values/total_of_frequency

                # STANDARD DEVIATION
                for value, frequency in zip(value_list, frequency_list):
                    absolute_values = frequency * (abs(value - average)**2)
                    absolute_values__squared_list.append(absolute_values)
                for value in absolute_values__squared_list:
                    total_of_absolute_values__squared += value
                standard_deviation_answer = math.sqrt(total_of_absolute_values__squared / total_of_frequency)
                table_data = [[xi, fi, fx,xabs,xabssq, cf] for xi, fi, fx,xabs,xabssq, cf  in zip(value_list, frequency_list, fx_list, absolute_values_list, absolute_values__squared_list, cumulative_freq_list) ]
                #print(cumulative_freq_list)
                table_data.append([Fore.LIGHTMAGENTA_EX+"Total", total_of_frequency, total_of_fx, total_of_abolute_values,total_of_absolute_values__squared,Style.RESET_ALL])
                print(tabulate(table_data, headers=[Fore.GREEN+"Values", "Frequency", "FX", "F(X-mean)","F(X-mean)²", "CF"+Style.RESET_ALL], tablefmt="grid"))



                #MEDIAN CALCULATION
                cf_x_dict=dict(zip(value_list, cumulative_freq_list))
                #print(cf_x_dict)
                median_number=total_of_frequency/mean_num_of_numbers
                for value in sorted(cf_x_dict.keys()):
                    if cf_x_dict[value]>= median_number:
                        median_value=value
                        break

                #MODE CALCULATION
                f_x_dict=dict(zip(value_list, frequency_list))
                max_freq = max(f_x_dict.values())
                for key, value in f_x_dict.items():
                    if value==max_freq:
                        mode_freq=key


                print()
                while True:
                    print(Style.RESET_ALL + "What do you want to find")
                    print("A.Mean")
                    print("B.Median")
                    print("C.Mode")
                    print("D.Mean deviation")
                    print("E.Standard Deviation")
                    print("Press q to quit")
                    choice = input(">>>>>>>>: ").upper()
                    if choice=="A":
                        print()
                        print("***************************")
                        print(Fore.YELLOW+f"Your mean is {average:.3f}"+Style.RESET_ALL)
                        print("***************************")
                        print()
                    elif choice=="B":
                        print()
                        print("***************************")
                        print(Fore.YELLOW+f"Your median is {median_value}"+Style.RESET_ALL)
                        print("***************************")
                        print()
                    elif choice=="C":
                        print()
                        print("***************************")
                        print(Fore.YELLOW + f"Your mode is {mode_freq}" + Style.RESET_ALL)
                        print("***************************")
                        print()
                    elif choice=="D":
                        print()
                        print("***************************")
                        print(Fore.YELLOW + f"Your mean deviation is {mean_deviation_answer:.3f}" + Style.RESET_ALL)
                        print("***************************")
                        print()
                    elif choice=="E":
                        print()
                        print()
                        question_running=True
                        while question_running:
                            population_or_sample = input(
                                Style.RESET_ALL + "Are you calculating the standard deviation for population or sample(press P or S): ").upper()
                            if population_or_sample == "P":
                                standard_deviation_answer = math.sqrt(total_of_absolute_values__squared / mean_num_of_numbers)
                                print(Fore.CYAN + f"The standard deviation of your numbers is {standard_deviation_answer:.2f}")
                                question_running=False
                            elif population_or_sample == "S":
                                standard_deviation_answer = math.sqrt(total_of_absolute_values__squared / (mean_num_of_numbers - 1))
                                print(Fore.CYAN + f"The standard deviation of your numbers is {standard_deviation_answer:.3f}")
                                question_running = False
                            else:
                                print(Fore.RED + "INCORRECT RESPONSE!")
                                continue
                    elif choice=="Q" or choice=="QUIT":
                        break
                    elif not choice.isalpha():
                        print("Enter valid option(A,B or C)")
                        print()
                        continue
                    elif choice == 'Q' or choice == 'QUIT':
                        print("Bye")
                        break
                            # for frequency,value in zip(frequency_list, value_list):
                            #     print("")
                    else:
                        print(f"{choice} not valid")
                        print()
                        continue

        case "C":
            upper_intervals=[]
            lower_intervals=[]
            class_intervals=[]
            frequency_list=[]
            FX_lists=[]
            X_lists=[]
            cumulative_freq_list=[]
            absolute_values_list=[]
            frequency_absolute_value_list=[]
            frequency_absolute_value_squared_list=[]
            total_of_frequency=0
            total_of_FX=0
            cumulative_total=0
            median_value=0
            raa=0
            CF_BEFORE=0
            cf_before=0
            median_frequency=0
            CF_BEFORE_MEDIAN_FREQUENCY=0
            median_Lower_interval_value=0
            absolute_values_total=0
            frequency_absolute_values_total=0
            highest_frequency=0
            position=None
            D1=0
            D2=0
            frequency_absolute_value_squared=0
            mode_Lower_interval_value=0
            frequency_absolute_value_squared_total=0
            standard_deviation=0
            while True:
                num_of_numbers = input(Style.RESET_ALL + "Enter number of numbers: ")
                if not num_of_numbers.isdigit():
                    print(Fore.RED + "INVALID RESPONSE")
                    continue
                else:
                    break
            num_of_numbers=int(num_of_numbers)
            while True:
                class_size=input(Style.RESET_ALL + "Enter the class size: ")
                if not class_size.isdigit():
                    print(Fore.RED + "INVALID RESPONSE")
                    continue
                else:
                    break
            class_size=int(class_size)
            while True:
                class_interval_first_num=input(Style.RESET_ALL + "Enter the number of the first class boundary: ")
                if not class_interval_first_num.isdigit():
                    print(Fore.RED + "INVALID RESPONSE")
                    continue
                else:
                    break
            class_interval_first_num=int(class_interval_first_num)

            print(f"Enter {num_of_numbers}")
            for i in range(num_of_numbers):
                while True:
                    frequencies_num = input(Style.RESET_ALL + f"Enter the frequency of number {i + 1}: ")
                    if not frequencies_num.isdigit():
                        print(Fore.RED + "INVALID RESPONSE")
                        continue
                    else:
                        break
                frequencies_num = int(frequencies_num)
                frequency_list.append(frequencies_num)
            print()

            # THIS CREATES THE UPPER CLASS BOUNDARY PF THE CLASS INTERVALS
            current_value=class_interval_first_num
            for i in range(num_of_numbers):
                upper_intervals.append(current_value)
                current_value=current_value+class_size
            # upper_interval = [class_interval_first_num+ class_size*i for i in range(num_of_numbers)]

            # THIS CREATES THE LOWER CLASS BOUNDARY OF THE CLASS INTERVALS
            new_class_size=class_size-1
            for upper_interval in upper_intervals:
                Total=upper_interval+new_class_size
                lower_intervals.append(Total)

            #THIS CREATES A STRING FORM OF THE CLASS INTERVALS
            for upper_interval, lower_interval in zip(upper_intervals, lower_intervals):
                classes=str(upper_interval)+"-"+ str(lower_interval)
                class_intervals.append(classes)

            # CREATING THE X
            for upper_interval, lower_interval in zip(upper_intervals, lower_intervals):
                individual_midpoints=(upper_interval+lower_interval)/2
                X_lists.append(individual_midpoints)

            #THIS CREATES THE FX VALUES LIST
            for frequency, x in zip(frequency_list, X_lists):
                Total = frequency*x
                FX_lists.append(Total)

            #THIS IS THE TOTAL FREQUENCY
            for frequency in frequency_list:
                total_of_frequency+=frequency

            # THIS IS THE TOTAL FX
            for i in FX_lists:
                total_of_FX+=i
            #print(lower_intervals)

            # CALCULATION OF THE CUMULATIVE FREQUENCY
            for number in frequency_list:
                cumulative_total += number
                cumulative_freq_list.append(cumulative_total)

            # MEDIAN CALCULATION
            median_number=total_of_frequency/2
            cf_x_dict = dict(zip(upper_intervals, cumulative_freq_list))
            f_dict = dict(zip(frequency_list, upper_intervals))
            for value in sorted(cf_x_dict.keys()):
                if cf_x_dict[value] >= median_number:
                    median_Lower_interval_value = value
                    break
            for num in sorted(f_dict.keys()):
                if f_dict[num]==median_Lower_interval_value:
                    median_frequency=num
                    break
            for i in cumulative_freq_list:
                if i <= median_number:
                    CF_BEFORE_MEDIAN_FREQUENCY=i
                    break
            # print(CF_BEFORE_MEDIAN_FREQUENCY)
            # print(median_frequency)
            median=median_Lower_interval_value+((median_number-CF_BEFORE_MEDIAN_FREQUENCY)/median_frequency)*class_size


            #CALCULATION OF THE MODE
            index=0
            for index, num in enumerate(frequency_list):
                if num == max(frequency_list):
                    highest_frequency=num
                    position=index
                    break
            #print(index)
            if position>0 and position <len(frequency_list)-1:
                D1 = highest_frequency - (frequency_list[position - 1])
                D2=highest_frequency- (frequency_list[position+1])
            # print(D1, D2)
            # print(highest_frequency)
            f_dict = dict(zip(upper_intervals, frequency_list))
            for key, value in f_dict.items():
                if value == highest_frequency:
                    mode_Lower_interval_value = key
            # print(mode_Lower_interval_value)
            # print(class_size)
            mode=mode_Lower_interval_value+(D1/(D1+D2))*class_size



            # THIS IS CALCULATION OF THE MEAN
            average=total_of_FX/total_of_frequency

            # THIS THE CALCULATION OF THE ABSOLUTES VALUES
            for x in X_lists:
                absolute_values=abs(x-average)
                absolute_values_list.append(absolute_values)
            for frequency, absolute_value, in zip(frequency_list, absolute_values_list):
                frequency_absolute_values=frequency*absolute_value
                frequency_absolute_value_list.append(frequency_absolute_values)
            for frequency_absolute_value in frequency_absolute_value_list:
                frequency_absolute_values_total+=frequency_absolute_value

            #THIS THE CALCULATION OF THE MEAN DEVIATION
            mean_deviation=frequency_absolute_values_total/total_of_frequency

            #THIS IS THE CALCULATION OF THE STANDARD DEVIATION
            for frequency, absolute_value in zip(frequency_list, absolute_values_list):
                frequency_absolute_value_squared=frequency*(absolute_value**2)
                frequency_absolute_value_squared_list.append(frequency_absolute_value_squared)
            for frequency_absolute_value_squared in frequency_absolute_value_squared_list:
                frequency_absolute_value_squared_total+=frequency_absolute_value_squared

            # THIS CREATES THE TABLE
            table_data = [[class_interval, frequency, X, FX, CF, absv, absvsq] for class_interval, frequency, X, FX, CF, absv , absvsq in zip(class_intervals, frequency_list, X_lists, FX_lists, cumulative_freq_list, frequency_absolute_value_list, frequency_absolute_value_squared_list)]
            table_data.append([Fore.LIGHTMAGENTA_EX+ "Total", total_of_frequency, "", total_of_FX, "", frequency_absolute_values_total, frequency_absolute_value_squared_total, Style.RESET_ALL])
            print(tabulate(table_data, headers=[Fore.GREEN+ "ClassIntervals", "Frequency", "Midpoints(X)", "FX", "CF", "|X-average|", "|X-average|²"+Style.RESET_ALL], tablefmt="grid"))
            # time.sleep(1)

            while True:
                print(Style.RESET_ALL + "What do you want to find")
                print("A.Mean")
                print("B.Median")
                print("C.Mode")
                print("D.Mean deviation")
                print("E.Standard Deviation")
                print("Press q to quit")
                choice = input(">>>>>>>>: ").upper()
                if choice == "A":
                    print()
                    print("***************************")
                    print(Fore.YELLOW + f"Your mean is {average:.3f}" + Style.RESET_ALL)
                    print("***************************")
                    print()
                elif choice == "B":
                    print()
                    print("***************************")
                    print(Fore.YELLOW + f"Your median is {median:.3f}" + Style.RESET_ALL)
                    print("***************************")
                    print()
                elif choice == "C":
                    print()
                    print("***************************")
                    print(Fore.YELLOW + f"Your mode is {mode:.3f}" + Style.RESET_ALL)
                    print("***************************")
                    print()
                elif choice == "D":
                    print()
                    print("***************************")
                    print(Fore.YELLOW + f"Your mean deviation is {mean_deviation:.3f}" + Style.RESET_ALL)
                    print("***************************")
                    print()
                elif choice == "E":
                    print()
                    question_running=True
                    while question_running:
                        population_or_sample = input(Style.RESET_ALL + "Are you calculating the standard deviation for population or sample(press P or S): ").upper()
                        if population_or_sample == "P":
                            standard_deviation = math.sqrt(frequency_absolute_value_squared_total / num_of_numbers)
                            print()
                            print(Fore.CYAN +"***************************")
                            print(Fore.CYAN + f"The standard deviation of your numbers is {standard_deviation:.2f}")
                            print("***************************")
                            question_running=False
                        elif population_or_sample == "S":
                            standard_deviation = math.sqrt(frequency_absolute_value_squared_total / (num_of_numbers - 1))
                            print()
                            print(Fore.CYAN +"***************************")
                            print(Fore.CYAN + f"The standard deviation of your numbers is {standard_deviation:.3f}")
                            print()
                            print("***************************")
                            question_running=False
                        else:
                            print(Fore.RED + "INCORRECT RESPONSE!")
                            continue
                elif choice=="Q" or choice=="QUIT":
                    break
                else:
                    print(Fore.RED+"INVALID CHOICE")

        case "E":
            break
        case _ :
            pass
# for number in frequency_list:
#     total += number
#     cumulative_freq_list.append(total)



# table_data = [[xi, fi, fx,xabs,xabssq, cf] for xi, fi, fx,xabs,xabssq, cf  in zip(value_list, frequency_list, fx_list, absolute_values_list, absolute_values__squared_list, cumulative_freq_list) ]
#                 #print(cumulative_freq_list)
#                 table_data.append([Fore.LIGHTMAGENTA_EX+"Total", total_of_frequency, total_of_fx, total_of_abolute_values,total_of_absolute_values__squared,Style.RESET_ALL])
#                 print(tabulate(table_data, headers=[Fore.GREEN+"Values", "Frequency", "FX", "F(X-mean)","F(X-mean)²", "CF"+Style.RESET_ALL], tablefmt="grid"))


























