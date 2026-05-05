def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list = get_user_input()
 calc_average(num_list)
 find_min_max(num_list)
 sort_temperature(num_list)
 calc_median_temperature(num_list)


def display_main_menu():
 print( "Enter some numbers separated by commas (e.g. 5, 67,32)")

def calc_average(num_list):
 
 total = sum(num_list)
 average = total / len(num_list)

 print(f"Average temperature = {average}") 
 return average


def get_user_input():
 user_input = input()
 str_list = user_input.split(",") 
 floatlist = []
 for x in str_list:
  floatlist.append(float(x))

 return floatlist

def find_min_max(num_list):
 minimum = min(num_list)
 maximum = max(num_list)
 print(f"Minimum temperature = {minimum}")
 print(f"Maximum temperature = {maximum}")
 return [minimum , maximum]
 

def sort_temperature(num_list):
 sortlist = sorted(num_list)
 print(f"Sorted list = {sortlist}")
 return sortlist



def calc_median_temperature(num_list):
 sortlist = sorted(num_list)
 length = len(sortlist)
 if length % 2 == 0:
  mid1 = length // 2 - 1
  mid2 = length // 2 
  median = (sortlist[mid1] + sortlist[mid2]) / 2
 else:
  mid = length // 2
  median = sortlist[mid]
 print (f"Median temperature = {median}")
 return median
if __name__ == "__main__":
    main()