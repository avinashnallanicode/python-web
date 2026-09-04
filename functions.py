def readfile():
    """
    This is doc strings, gives insights about function in future
    Reads todos from file
    """
    # Doc strings doubles downs as multi line string, where we can avoid use of break line and other stuffs
    with open("todos.txt", "r") as refile:
        tasks = refile.readlines()
    return tasks

def writefile(tasks):
    with open("todos.txt", "w") as file:
        file.writelines(tasks)