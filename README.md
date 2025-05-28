
---

# my\_AI\_lab

[<img src="https://img.shields.io/badge/GitHub-my_AI_lab-181717?logo=github&logoColor=white" alt="GitHub" width="200"/>](https://github.com/fmmarco29)
[<img src="https://img.shields.io/badge/LinkedIn-Fernando%20Mart%C3%ADnez%20Marco-0A66C2?logo=linkedin&logoColor=blue" alt="LinkedIn" width="300"/>](https://www.linkedin.com/in/fernando-mart%C3%ADnez-marco-a8127328/)
[<img src="https://img.shields.io/badge/HuggingFace-Spaces-FCC624?logo=huggingface&logoColor=black" alt="Hugging Face" width="200"/>](https://huggingface.co/fmcsihe2929)



![ci_cd](https://github.com/fmmarco29/my_AI_lab/actions/workflows/ci_cd.yml/badge.svg)


## Overview

This repository hosts the My AI Lab project, an experimental AI/ML environment featuring modular architecture for agents, data pipelines, and model management. It is designed for rapid prototyping and testing new ideas in a clean, extendable setup.

## Features

* Modular AI agents for supervised learning, reinforcement learning, and custom workflows
* Dataset loaders and preprocessing modules
* Model factory and wrappers for flexible model creation
* Utilities for logging, callbacks, and decorators
* Comprehensive testing with pytest and coverage reporting
* Continuous integration via GitHub Actions

## Installation

1. Clone the repository:
   git clone [https://github.com/fmmarco29/my\_AI\_lab.git](https://github.com/fmmarco29/my_AI_lab.git)
   cd my\_AI\_lab
2. Create and activate a virtual environment:

   * **Linux/macOS**:
     python3 -m venv myenv
     source myenv/bin/activate
   * **Windows (PowerShell)**:
     python -m venv myenv
     .\myenv\Scripts\activate
3. Install dependencies and development tools:
   pip install -e .\[dev]

## Usage

Import core components and start building:

```python
from my_ai_lib.agents.ml_agent import MLAgent
from my_ai_lib.data.dataset import load_dataset
from my_ai_lib.models.model_factory import create_model

agent = MLAgent()
data = load_dataset("path/to/data.csv")
model = create_model("random_forest", params={"n_estimators": 100})
```

## Testing

Run tests with coverage:

```bash
pytest --cov=my_ai_lib tests/
```

## Continuous Integration

GitHub Actions workflows in `.github/workflows/ci_cd.yml` ensure automated testing and coverage reporting on each push and pull request.

## Troubleshooting

* Ensure `pytest-cov` is installed (`pip install pytest-cov`).
* If tests cannot import the package, set `PYTHONPATH`:

  * **Linux/macOS**:
    export PYTHONPATH=\$(pwd)
  * **Windows (PowerShell)**:
    \$env\:PYTHONPATH = (Get-Location)

## Contributing

Contributions are welcome. Please open issues or submit pull requests. Follow existing style and testing conventions.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact & Links

* GitHub: [https://github.com/fmmarco29/my\_AI\_lab](https://github.com/fmmarco29/my_AI_lab)
* LinkedIn: [https://www.linkedin.com/in/fernando-mart%C3%ADnez-marco-a8127328/](https://www.linkedin.com/in/fernando-mart%C3%ADnez-marco-a8127328/)
* Hugging Face Spaces: [https://huggingface.co/fmcsihe2929](https://huggingface.co/fmcsihe2929)
* Portfolio: [https://fmmarco29.github.io/AI/](https://fmmarco29.github.io/AI/)
* Email: [fmmarco29@hotmail.com](mailto:fmmarco29@hotmail.com)

---


