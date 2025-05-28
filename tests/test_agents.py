from my_ai_lib.agents.ml_agent import MLAgent
from my_ai_lib.agents.rl_agent import RLAgent
from my_ai_lib.agents.custom_agent import CustomAgent

def test_ml_agent_train():
    agent = MLAgent()
    agent.train([1, 2, 3])
    assert agent.name == "BaseAgent"

def test_rl_agent_predict():
    agent = RLAgent()
    result = agent.predict([1, 2, 3])
    assert result == [1, 1, 1]

def test_custom_agent_predict():
    agent = CustomAgent()
    result = agent.predict([1, 2, 3])
    assert result == [2, 2, 2]