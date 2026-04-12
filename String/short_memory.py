class MemoryBuffer:
    def __init__(self):
        self.chat_history = []

    def add_user_message(self, message: str):
        return self.chat_history.append({"role": "user", "content": message})
    
    def add_ai_message(self, message: str):
        return self.chat_history.append({"role": "AI", "content": message})
    
    def get_formated_history(self):

        formated_string = ""
        for turn in self.chat_history:
            formated_string += f"{turn["role"]}: {turn["content"]}\n"
        
        return formated_string
    

memory = MemoryBuffer()

memory.add_user_message("Hi LLM, how are you ?")
memory.add_ai_message("I'm good, how about you")

memory.add_user_message("Tell me how AI is booming right now ?")
memory.add_ai_message("Well, Today AI is in everywhere, AI is shapping businesses, improving education quality, ai is making people smarter in some instance as per the awarness is concerns")

print(memory.get_formated_history())

"""
The Production Problem: Context Limits -->
If you use the basic array above, the list grows infinitely. Eventually, 
get_formatted_history() will generate a string so massive that it exceeds gemma3:1b's context window, 
causing the model to crash or hallucinate.

Solution: Sliding Window using Queue concept.
"""