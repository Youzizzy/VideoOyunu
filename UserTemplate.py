class User :
    def __init__(self , uN , role , pW):
        self.uN = uN
        self.role = role
        self.pW = pW

    def check_password(self , input_password):
        return self.pW == input_password
