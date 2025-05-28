from my_ai_lib.agents.ml_agent import MLAgent
from my_ai_lib.data.dataset import load_data

def main():
    agent = MLAgent()
    data = load_data()
    agent.train(data)

if __name__ == "__main__":
    main()