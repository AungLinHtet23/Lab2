def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    user_input = input("Please enter a sequence of numbers separated by commas: ")
    input_split = user_input.split(",")
    input_float = [float(num.strip()) for num in input_split]
    return input_float

def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

def calc_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def sort_temperature(numbers):
    if not numbers:
        print("The list is empty. No sorting will be performed.")
        return
    sorted_temps = sorted(numbers)
    print(f"Sorted Temperature: {sorted_temps}")

def calc_median_temperature(numbers):
    if not numbers:
        return None
    sorted_temps = sorted(numbers)
    length = len(sorted_temps)

    if length % 2 == 1:
        return sorted_temps[length // 2]
    else:
        mid1 = sorted_temps[length // 2 - 1]
        mid2 = sorted_temps[length // 2]
        return (mid1 + mid2) / 2

# Only execute this code if running as the main script
if __name__ == "__main__":
    display_main_menu()
    my_num = get_user_input()
    min_val, max_val = find_min_max(my_num)
    if min_val is not None and max_val is not None:
        print(f"Minimum: {min_val}, Maximum: {max_val}")

    average = calc_average(my_num)
    if average is not None:
        print(f"Average = {average:.2f}")

    sort_temperature(my_num)
    median = calc_median_temperature(my_num)
    if median is not None:
        print(f"Median Temperature: {median}")
