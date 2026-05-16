class SlidingWindowMemory:
    def __init__(self, k: int = 2):

        self.chat_history = []
        self.k = k

    def add_interactions(self, user_msgs: str, ai_msgs: str):

        self.chat_history.append({"User": user_msgs, "AI": ai_msgs})

        if len(self.chat_history) > self.k:
            self.chat_history.pop(0)

    def get_formated_history(self):

        formated_string = ""
        for turn in self.chat_history:
            formated_string += f"User: {turn["User"]}\nAI: {turn["AI"]}\n"

        return formated_string
    

memory = SlidingWindowMemory()

memory.add_interactions("Hi model, how are you ?", "I'm good , what about you ?")
memory.add_interactions("I'm good model, Can you explain little about ML system design", "Sure, ML system design is a very crucial topic these days...")

memory.add_interactions("Hi model, how are you ?", "I'm good , what about you ?")
memory.add_interactions("I'm good model, Can you explain little about ML system design", "Sure, ML system design is a very crucial topic these days...")

memory.add_interactions("Hi model, how are you ?", "I'm good , what about you ?")
memory.add_interactions("I'm good model, Can you explain little about ML system design", "Sure, ML system design is a very crucial topic these days...")

print(memory.get_formated_history())