


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    print ("Raw Input = "+inputstr)

    # Split the input string into a segments of strings separated by commas as splitter
    splitlist = inputstr.split(",")
    print ("After splitting = ", splitlist)

    # Next step is to convert eaach short string in the list into float
    floatlist = [] # Define an empty list of float numbers
    for x in splitlist:
        floatnum = float(x)  # onvert the string into float
        floatlist.append(floatnum)  # Add the float number to the floatlist
    print("Float list = ", floatlist)
    return floatlist


def calc_average(input_list):
    print("calc_average")
    total = sum(input_list)
    average = total / len(input_list)
    print("Average = ", average)
    return average

def find_min_max(input_list):
    print("find_min_max")
    input_list.sort()
    resultlist = [input_list[0], input_list[-1]]
    print("Min and Max list = ", resultlist)
    return resultlist

def sort_temperature(input_list):
    print("sort_temperature")
    input_list.sort()


def calc_median_temperature(sortedlist):
    print("calc_median_temperature")
    sortedlist.sort
    cnt = len(sortedlist)
    print("cnt",cnt)
    if cnt % 2 is 1: #no.of elements in list is odd
        median = sortedlist[int((cnt-1)/2)] # // is integer division
    else:
        median = (sortedlist[cnt//2] + sortedlist[cnt//2-1])/2
    print("Median = ", median)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sort_temperature(floatlist)
    print ("After sorting = ", floatlist)
    calc_median_temperature(floatlist)


if __name__ == "__main__":
    main()