from textwrap import dedent

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
    """
    Opens and reads the file and returns in as a string

    arg() = pass in a document with .txt extension
    """
    with open(fle, 'r') as f:
        contents = f.read()
        return contents


def find_curly(string_file):
    """
    finds the values that need to be changed and replace them

    arg() = a file that has been read and in string format
    """
    key_list = list()
    end = 0
    rep = string_file.count('{')
    # with open('assets/madlib.new.txt', 'w') as f:
    for i in range(rep):
        start = string_file.find('{', end) + 1
        end = string_file.find('}', start)
        key = string_file[start: end]
        prompt = input(f'Enter a {key}: ')

        key_list.append(prompt)
        # f.write(string_file)
    repl(key_list)


def repl(lst):
    """
    Prints values that were inputted on final product.
    """
    print(f"""

  I the {lst[0]} and {lst[1]} {lst[2]} have {lst[3]}{lst[4]}'s {lst[5]} sister and plan to steal her {lst[6]} {lst[7]}!

  What are a {lst[8]} and backpacking {lst[9]} to do? Before you can help {lst[10]}, you'll have to collect the {lst[11]} {lst[12]} and {lst[13]} {lst[14]} that open up the {lst[15]} worlds connected to A {lst[16]} Lair. There are {lst[17]} {lst[18]} and {lst[19]} {lst[20]} in the game, along with hundreds of other goodies for you to find.
  """)


def start_game():
    """
    starts the game
    """
    welcome()
    find_curly(reading('assets/madlib.txt'))


start_game()
