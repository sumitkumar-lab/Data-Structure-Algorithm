"""
Encapsulate config information of a language model...
"""
class LanguageModel:
    def __init__(self, name: str, lr_rate: float):
        
        self.name = name
        self.lr_rate = lr_rate

    def update_lr(self, new_lr):
         self.lr_rate = new_lr
        #  return new_lr  ->  this is echoes

    def generate(self, prompt: str):
        return f"Generating text for: {prompt}"
    

model_one = LanguageModel("Llama-3", 0.002)
model_two = LanguageModel("Mistral", 0.005)

# print(model_one.update_lr(0.0023))

model = LanguageModel("Llama-3", 0.001)

# You call your update method
result = model.update_lr(0.05)

# What happened?
print(result)         # This prints 0.05 (because you returned it)
print(model.lr_rate)  # This STILL prints 0.001!

"""
Inherritance
"""
class VisionModel(LanguageModel):
    def __init__(self, name, lr_rate, image_resolution):
        super().__init__(name, lr_rate)
        self.image_resolution = image_resolution

    def generate(self, prompt: str):
        return f"Processing image at {self.image_resolution}p and generating text for: {prompt}"
    

v_model = VisionModel("GPT-4V", 0.08, 1024)
l_model = LanguageModel("GPT", 0.01)

print(v_model.generate("generate me..."))
print(l_model.generate("generate now..."))