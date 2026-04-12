"""
A context manager is an object that defines what happens before and after a block of code runs.

You use it with the **with** statement.

__enter__() → runs at the start of with
__exit__() → runs at the end (even if error occurs)

with something as resource:
    # use resource
"""
# with open("data.txt", "r") as file:
#     data = file.read()
# # file is automatically closed ✔


"""
Using a class
"""
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with MyContext() as obj:
    print("Inside block")


"""
Using contextlib
"""
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")

with my_context():
    print("Inside block")