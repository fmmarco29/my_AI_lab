from .base_agent import BaseAgent

class CustomAgent(BaseAgent):
    def train(self, data):
        super().train(data)
        print("CustomAgent specific training logic")

    def predict(self, data):
        print("CustomAgent prediction logic")
        return [2] * len(data)