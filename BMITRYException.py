#Jonathan Tinoy
#3rd Year BS Stat

class BMI:

    def __init__(self, Inches, Pounds):
        self.height = Inches
        self.weight = Pounds
        
    def convert(self):
        self.get_weight = self.weight/2.20462262
        self.get_height = self.height*0.0254
        
    def getbmi(self):
        self.body_mass_index = round(self.get_weight /(self.get_height**2), 1)
        return(self.body_mass_index)

        if self.self.body_mass_index <= 18.5:
            self.self.body_mass_index_classification = "underweight"
            print(', It means you are underweight.')
        elif self.self.body_mass_index > 18.5 and self.self.body_mass_index < 25:
            self.self.body_mass_index_classification = "normal"
            print(', It means you are normal.')
        elif self.self.body_mass_index > 25 and self.self.body_mass_index < 30:
            self.self.body_mass_index_classification = "overweight"
            print(', It means you are an overweight.')
        elif self.self.body_mass_index > 30:
            self.self.body_mass_index_classification = "obese"
            print(', It means you are an obese.')
        else:
            self.self.body_mass_index_classification = "An error occured"
            print(', THERE IS AN ERROR OF YOUR INPUT.')

    def tryexception(self):
        try:
            self.body_mass_index = round(self.get_weight /(self.get_height**2), 1)
            if self.height <=0 or self.weight <=0:
                raise Exception
            elif type(self.height) == str or type(self.weight) == str:
                raise Exception
        except Exception:
            return "-"

    def lenght(self):
        try:
            if len(self.height)>=4 or len(self.weight)>=3:
                raise Exception
            else:
                self.get_weight = self.weight/2.20462262
                self.get_height = self.height*0.0254
        except Exception:
            return "-"
