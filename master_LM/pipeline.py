"""
*steps means “accept any number of arguments and pack them into a tuple”.
"""

def pipeline(*steps):
    def run(data):
        for step in steps:
            data = step(data)
        return data
    return run

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    stopwords = ["the", "a", "is"]
    return [t for t in tokens if t not in stopwords]

def to_uppercase(tokens):
    return [t.upper() for t in tokens]

process = pipeline(tokenize, remove_stopwords, to_uppercase)
print(process("the cat is happy"))

"""
LangChain does exactly this -->
chain = prompt_template | llm | output_parser

Which internally is just -->
process = pipeline(prompt_template, llm, output_parser)

That | operator in LangChain? It's the same pipeline pattern you just built — just with a 
custom __or__ dunder method on each component. we'll implement that yourself in Phase 3 when we cover OOP.

"""
def show(*args, **kwargs):
    print(type(args))    # tuple
    print(type(kwargs))  # dict
    print(args)
    print(kwargs)

show(1, 2, 3, name="Sumit", role="engineer")

print("======== Unpacking ========")

def build_prompt(context, question, tone):
    return f"Tone: {tone}\nContext: {context}\nQuestion: {question}"

config = {
    "context": "Paris is in France",
    "question": "Where is Paris?",
    "tone": "formal"
}
print(build_prompt(**config))  # unpacks dict into keyword arguments

print("==================")
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # unpacks list into positional arguments

print("===================")
"""
In AI engineering you constantly load configs from JSON files and unpack them directly into functions:

with open("model_config.json") as f:
    config = json.load(f)

model = initialize_model(**config)  # clean, flexible, no hardcoding
"""
print("========== Challenge ===========")

"""
Build a function called "run_experiment" that:

Accepts a model function as first argument
Accepts any number of datasets as positional arguments
Accepts any number of config options as keyword arguments
Runs the model on each dataset with the config and prints results
"""
def run_experiment(model_fn, *datasets, **config):
    results = []
    for i, dataset in enumerate(datasets, 1):
        result = model_fn(dataset, **config)
        print(f"Dataset {i}: {result}")
        results.append(result)
    return results

def dummy_model(data, learning_rate=0.01, epochs=10):
    return f"Trained on {len(data)} samples | lr={learning_rate} | epochs={epochs}"

run_experiment(
    dummy_model,
    [1,2,3], [4,5,6], [7,8,9],
    learning_rate=0.001,
    epochs=20
)
# Dataset 1: Trained on 3 samples | lr=0.001 | epochs=20