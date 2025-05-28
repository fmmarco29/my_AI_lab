from .base_agent import BaseAgent

class MLAgent(BaseAgent):
    def train(self, data):
        super().train(data)
        print("MLAgent specific training logic")

    def predict(self, data):
        print("MLAgent prediction logic")
        return [0] * len(data)