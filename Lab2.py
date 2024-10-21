def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    user_input = input("Please enter a sequence of numbers separated by commas: ")
    input_split = user_input.split(",")
    input_float = [float(num.strip()) for num in input_split]
    return input_float

def find_min_max_average(numbers):
    if not numbers:
        print("The list is empty. No calculation will be performed.")
        return
    average = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print(f"Average = {average:.2f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

def sort_temperature(numbers):
    if not numbers:
        print("The list is empty. No sorting will be performed.")
        return
    sorted_temps = sorted(numbers)  # Corrected the use of sorted()
    print(f"Sorted Temperature: {sorted_temps}")

def calc_median_temperature(numbers):
    sorted_temps = sorted(numbers)
    length = len(sorted_temps)

    # Calculate median
    if length % 2 == 1:
        median = sorted_temps[length // 2]
    else:
        mid1 = sorted_temps[length // 2 - 1]
        mid2 = sorted_temps[length // 2]
        median = (mid1 + mid2) / 2

    print(f"Median Temperature: {median}")

# Main Program Flow
display_main_menu()
my_num = get_user_input()
find_min_max_average(my_num)
sort_temperature(my_num)
calc_median_temperature(my_num)
