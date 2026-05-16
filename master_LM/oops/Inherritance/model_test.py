"""
imagine you are expanding your personal AI research lab. You've built a solid 
foundation for evaluating standard language models, but you want to start testing 
multimodal systems—specifically, Vision-Language Models (VLMs) like GPT-4V or Claude 3 Opus.

If you want to create a VisionModel class, it still needs a name, 
a lr_rate, and the ability to update_lr(). Without Inheritance, 
you would have to copy and paste the entire LanguageModel code block to build VisionModel. 
If you later find a bug in update_lr(), you now have to fix it in two different places.
"""
from oops.Encapsulation.config import LanguageModel

class VisionModel(LanguageModel):
    def __init__(self, name, lr_rate, image_resolution):
        super().__init__(name, lr_rate)
        self.image_resolution = image_resolution
    

v_model = VisionModel("GPT-4V", 0.08, 1024)

print(v_model.name)