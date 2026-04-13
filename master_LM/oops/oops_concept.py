
class Phone:
    def __init__(self):
        # Class attributes
        self.model_name = "NOKIA"
        self.display = "OLeD"
        self.RAM = "12 GB"
        self.ROM = "225 GB"
        self.camera = {"front_camera": "12 mp",
                       "Back_camera": ["50 mp", "50 mp", "12 mp"]}
        self.processor = "MediaTech"
        # self.PowerOn()
        # self.call()

    # Class functions
    def PowerOn(self):
        print(f"BootUp Your Phone my {self.model_name}")

    def PowerOff(self):
        print("Switching off your phone")

    def call(self):
        phone_number = input("Give me your 10 digit phone number")
        if len(phone_number) == 10:
            print("You can make a call")
        else:
            print("Invalid Number")

    # def camera(self):

    #     pass

    
phone_1 = Phone()

phone_1.model_name = "Oppo"
print(phone_1.PowerOn())