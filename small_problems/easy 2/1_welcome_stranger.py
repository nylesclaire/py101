# expected inputs: a list, a dictionary
# expected output: a string greeting

def greetings(name_list, title_dict):
    name = ""
    for item in name_list:
        name += f" {item}"
    title = f"{title_dict["title"]} {title_dict["occupation"]}"
    return(f"Hello,{name}! Nice to have a {title} around.")

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.