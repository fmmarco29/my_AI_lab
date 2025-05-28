class BaseAgent:
    def __init__(self):
        self.name = "BaseAgent"

    def train(self, data):
        print(f"Training with data: {data}")

    def predict(self, data):
        print(f"Predicting with data: {data}")