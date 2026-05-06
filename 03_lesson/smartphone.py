class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_number(self):
        return self.number

    def get_unit_info(self):
        return f"Smartphone: {self.brand},{self.model},{self.number}"
