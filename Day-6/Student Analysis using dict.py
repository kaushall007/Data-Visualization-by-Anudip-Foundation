from tabulate import tabulate
data_dict = {
    "std101": {
        "stdname": "Ashish Kumar",
        "standard": "10th",
        "Age": 15,
        "Hindi": 67,
        "English": 89,
        "Maths": 87,
        "Science": 89,
        "Computer": 90,
        "Total": 422
    },
    "std102": {
        "stdname": "Abhishek Kumar",
        "standard": "10th",
        "Age": 14,
        "Hindi": 85,
        "English": 45,
        "Maths": 48,
        "Science": 90,
        "Computer": 45,
        "Total": 313
    },
    "std103": {
        "stdname": "Aman",
        "standard": "10th",
        "Age": 15,
        "Hindi": 23,
        "English": 56,
        "Maths": 78,
        "Science": 78,
        "Computer": 67,
        "Total": 302
    },
    "std104": {
        "stdname": "Rahul",
        "standard": "10th",
        "Age": 14,
        "Hindi": 45,
        "English": 67,
        "Maths": 45,
        "Science": 45,
        "Computer": 56,
        "Total": 258
    },
    "std105": {
        "stdname": "Ruby",
        "standard": "10th",
        "Age": 13,
        "Hindi": 89,
        "English": 67,
        "Maths": 89,
        "Science": 93,
        "Computer": 65,
        "Total": 403
    },
    "std106": {
        "stdname": "Suman",
        "standard": "10th",
        "Age": 13,
        "Hindi": 90,
        "English": 46,
        "Maths": 67,
        "Science": 67,
        "Computer": 67,
        "Total": 337
    },
    "std107": {
        "stdname": "Saurabh",
        "standard": "10th",
        "Age": 15,
        "Hindi": 45,
        "English": 23,
        "Maths": 34,
        "Science": 45,
        "Computer": 34,
        "Total": 181
    },
    "std108": {
        "stdname": "Sumit",
        "standard": "10th",
        "Age": 14,
        "Hindi": 23,
        "English": 45,
        "Maths": 67,
        "Science": 78,
        "Computer": 90,
        "Total": 303
    },
    "std109": {
        "stdname": "Kamlesh",
        "standard": "10th",
        "Age": 15,
        "Hindi": 45,
        "English": 56,
        "Maths": 78,
        "Science": 99,
        "Computer": 67,
        "Total": 345
    },
    "std110": {
        "stdname": "Rohan",
        "standard": "10th",
        "Age": 15,
        "Hindi": 34,
        "English": 12,
        "Maths": 24,
        "Science": 45,
        "Computer": 56,
        "Total": 171
    }
}

keys = list(data_dict.keys())
values = list(data_dict.values())

# Create a list of lists, where each inner list represents a row in the table
table_data = []
for value in values:
    row = [value["stdname"], value["standard"], value["Age"], value["Hindi"], value["English"], value["Maths"], value["Science"], value["Computer"], value["Total"]]
    table_data.append(row)

# Print the table
print(tabulate(table_data, headers=["Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]))
