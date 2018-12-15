
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
from math import ceil, floor

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)

    # Use every row as an OrderedDict
    # Their properties can be accessed via name
    # and since they are ordered, their properties can be accessed using indexes when converted to lists
    data_list = [row for row in csv.DictReader(file_read, skipinitialspace=True)]

print("Ok!")


# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

for i in range(20):
    print('{0}th row: {1}'.format(i+1, data_list[i]))

# Let's change the data_list to remove the header from it.
# Line commented since when using DictReader to read the file, the header no longer gets in
# data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for i in range(20):
    print('{0}th row gender: {1}'.format(i+1, data_list[i]['Gender']))


# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
"""
Given a list of OrderedDict and the index of a column/feature, returns a list of values related to that column (one item for every row)
Args:
    param1: The list of OrderedDict objects that represents the dataset (where every OrderedDict represents a row)
    param2: The index of the column/feature to be selected (as if you were slicing a list)
Returns:
    List of values for the index specified column

"""
def column_to_list(data, index):
    column_list = []
    for row in data:
        column_list.append(list(value for key, value in row.items())[index])
        
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
for row in data_list:
    if row['Gender'] == 'Male':
        male += 1
    elif row['Gender'] == 'Female':
        female += 1


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
"""
Given a list of OrderedDict and the index of a column/feature, returns a list containing how many males and females resides on the dataset
Args:
    param1: The list of OrderedDict objects that represents the dataset (where every OrderedDict represents a row)
Returns:
    The list where the first item (position 0) is the number of males and the second item (position 1) the number of females

"""
def count_gender(data_list):
    male = 0
    female = 0
    for row in data_list:
        if row['Gender'] == 'Male':
            male += 1
        elif row['Gender'] == 'Female':
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
"""
Given a list of OrderedDict and the index of a column/feature, returns a string that tells the most popular gender
Args:
    param1: The list of OrderedDict objects that represents the dataset (where every OrderedDict represents a row)
Returns:
    A string that says which gender is the most popular. Possible answers: "Male", "Female" or "Equal".

"""
def most_popular_gender(data_list):
    count = count_gender(data_list)
    male = count[0]
    female = count[1]
    answer = ""

    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"
    
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
"""
Given a list of OrderedDict and the index of a column/feature, returns a list containing the amount of subscribers and customers
Args:
    param1: The list of OrderedDict objects that represents the dataset (where every OrderedDict represents a row)
Returns:
    The list where the first item (position 0) is the number of subscribers and the second item (position 1) the number of customers

"""
def count_user_type(data_list):
    subscriber = 0
    customer = 0
    for row in data_list:
        if row['User Type'] == 'Subscriber':
            subscriber += 1
        elif row['User Type'] == 'Customer':
            customer += 1
    return [subscriber, customer]

user_type_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.xlabel('User type')
plt.ylabel('Quantity')
plt.xticks(y_pos, types)
plt.title('Quantity by type of user')
plt.show(block=True)

print("\nTASK 7: Check the chart!")


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because some items in the sample don't have the gender specified (probably because this information was no colleted for that user)"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = [int(duration) for duration in column_to_list(data_list, 2)]
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[0]
mean_trip = trip_duration_list[0]
median_trip = 0.

for duration in trip_duration_list[1:]:
    mean_trip += duration
    if duration > max_trip:
        max_trip = duration
    if duration < min_trip:
        min_trip = duration

list_size = len(trip_duration_list)
mean_trip = mean_trip/list_size

sorted_list = sorted(trip_duration_list)

if list_size % 2 == 0:
    median_trip = (sorted_list[floor(list_size/2)]-1 + sorted_list[floor(list_size/2)]) / 2
else:
    median_trip = sorted_list[floor(list_size/2)-1]



print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
    List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

# Are the instructions correct? They talk about the "user types" as if they were the gender.
# The asserts use gender.


def count_items(column_list):
    item_types = []
    count_items = []
    temp_list = column_list.copy()
    unique_set = set(temp_list)
    print("unique set: " + str(unique_set))

    for i, gender in enumerate(unique_set):
        count = 0
        for item in temp_list:
            if item == gender:
                count += 1

        count_items.append(count)

    item_types = list(unique_set)
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------