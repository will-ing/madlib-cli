

"""
welcome variable - explain process and commands
read file madlib
find keywords - find? > input? > replace?
create dict
user input
make copy
read file and print on screen

"""


def welcome():
    """
    This function prints a message when the game starts
    """

    welcome_message = """
  //////////////////
  Welcome to madlibs!
  //////////////////
  
  You will get prompted with inputs for each section of the game we are going to make!

  Ready to get started!

  """

    print(welcome_message)


def reading(fle):
    with open(fle, 'r') as f:
        contents = f.read()
        return contents


def find_curly(string_file):

    keyList = list()
    end = 0
    rep = string_file.count('{')

    for i in range(rep):
        start = string_file.find('{', end) + 1
        end = string_file.find('}', start)
        key = string_file[start: end]
        keyList.append(key)

    return(keyList)


def ask_user():

    number_of_prompts = find_curly(reading('assets/madlib.txt'))
    for i in number_of_prompts:
        print(i)
        prompt = input(f'Enter a {i}: ')
        i.replace(prompt)
        print(i)


ask_user()
