#  Default arguments:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
print() #for new line

# Keyword arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
print()

# Required arguments:
"""
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
"""
# Example 2: when number of arguments passed matches to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
print()

# Variable-length arguments:
# There are two ways to achieve this:
# Arbitrary Arguments:
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
print()

# Keyword Arbitrary Arguments:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

