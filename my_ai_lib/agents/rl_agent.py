from .base_agent import BaseAgent

class RLAgent(BaseAgent):
    def train(self, data):
        super().train(data)
        print("RLAgent specific training logic")

    def predict(self, data):
        print("RLAgent prediction logic")
        return [1] * len(data)