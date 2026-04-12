"""
The Fourth Pillar: Abstraction
When building a comprehensive AI research dashboard for model evaluation 
and ablation studies, you are going to be plugging dozens of different 
models into your testing pipeline. You need an absolute guarantee that 
every model added to your system has specific methods, like evaluate(), 
ready to be called.

If a collaborator adds a new AudioModel to your lab but forgets to write 
an evaluate method for it, your entire testing pipeline will crash in the 
middle of a 10-hour run when it tries to call model.evaluate().


Abstraction solves this by enforcing a strict contract. 

In Python, we use Abstract Base Classes (ABCs) to define a blueprint. 
An ABC says: "I don't care how you implement this method, but if you want
to be considered a valid AI model in this system, you MUST have a method 
with this exact name."

Abstraction — Hiding Complexity Behind Simple Interfaces
Abstraction means exposing only what is necessary, hiding the complex 
details. Abstract Base Classes (ABCs) enforce that subclasses implement 
required methods — they're like contracts.

"""
from abc import ABC, abstractmethod

# 1. inherrit class from abc
class AbstractAIModel(ABC):

    def __init__(self, name: str):
        self.name = name

    # 2. Define the contract
    @abstractmethod
    def evaluate(self, dataset: str):
        # no code inside, just requirement
        pass

class TabularModel(AbstractAIModel):
    def __init__(self, name):
        super().__init__(name)

    # Forgot to built evaluate method, problem debugging...
    # Need bouncer: abc do the same -> gives TypeError so to fix it in given class
    # Now fix it:
    def evaluate(self, dataset: str):
        return f"Model is evaluating on: {dataset}"

# What happense when we try to do this ?
my_model = TabularModel("XGBoost")

print(my_model.evaluate("I'm a Tabular data..."))