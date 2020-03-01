
def print_list(mylist, title=""):

    if len(title) > 0:
        print("TITLE: " + title)

    for a in mylist:
        print(a)

    
colour_list = ["red", "green", "blue"]

print_list(colour_list, "List of colours")