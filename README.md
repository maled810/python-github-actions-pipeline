# Python Github Actions Pipeline

This is a repository containing a minimal Python Github Actions pipeline.

# Python Github Actions Pipeline

A Python Github Actions Pipeline which pushes a package to a Test Pypi Server.

## Usage

After successful upload install the package

```bash
pip install -i https://test.pypi.org/simple/ gui_calculator
```
Run it with 
```py
from calculator import calculator as calc
calc.GUICalculator()
```

## Important

Do not forget to add the credentials for the Test Pypi server in Github.
