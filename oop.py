class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # Initialize attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # battery percentage (0-100)

    def check_battery(self):
        return f"{self.model} has {self.battery}% battery remaining."

    def charge_battery(self):
        self.battery = 100
        return f"{self.model} is fully charged."

    def use_battery(self, usage):
        if usage > self.battery:
            return f"Not enough battery! Only {self.battery}% left."
        self.battery -= usage
        return f"Used {usage}%. Battery is now at {self.battery}%."

class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, has_5g, has_face_unlock):
        super().__init__(brand, model, storage, battery)
        self.has_5g = has_5g
        self.has_face_unlock = has_face_unlock

    def check_features(self):
        features = []
        if self.has_5g:
            features.append("5G")
        if self.has_face_unlock:
            features.append("Face Unlock")
        return f"{self.model} supports: {', '.join(features)}."


# Create objects
basic_phone = Smartphone("Nokia", "3310", "32MB", 80)
advanced_phone = AdvancedSmartphone("Apple", "iPhone 15", "256GB", 60, True, True)

# Use methods
print(basic_phone.check_battery())
print(basic_phone.use_battery(20))
print(advanced_phone.check_battery())
print(advanced_phone.check_features())
print(advanced_phone.charge_battery())
