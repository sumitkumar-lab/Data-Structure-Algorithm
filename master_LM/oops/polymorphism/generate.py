class GroqClient:
    def generate(self, prompt: str) -> str:
        return f"Groq response: {prompt[:20]}..."
    

class AnthropicClient:
    def generate(self, prompt: str) -> str:
        return f"Anthropic response: {prompt[:20]}..."
    

class OllamaClient:
    def generate(self, prompt: str) -> str:
        return f"Local Ollama response: {prompt[:20]}"
    

# polymorphism in action: same loop different objects
def run_test(clients: list, test_prompt: str):
    for client in clients:
        result = client.generate(test_prompt)
        print(result)


clients = [GroqClient(), AnthropicClient(), OllamaClient()]
run_test(clients, "Tell me what is ML ?")

"""
Instead of creating lots of different model class again an again
must implement inherritance concept...
"""
class LargeModel:
    def __init__(self, name: str, lr_rate: float):
        self.name = name
        self.lr_rate = lr_rate


class LanguageModel(LargeModel):
    def __init__(self, name, lr_rate):
        super().__init__(name, lr_rate)



class VisionModel(LargeModel):
    def __init__(self, name, lr_rate):
        super().__init__(name, lr_rate)


v_model = VisionModel("GPT-4V", 0.05)
l_model = LanguageModel("GPT", 0.02)

print(v_model.name)
print(l_model.name)