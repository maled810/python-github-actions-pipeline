from setuptools import setup, find_packages # type: ignore

setup(
    name="gui_calculator",
    version="0.0.1",
    author="Dejan Malesevic",
    author_email="",
    url="",
    description="An application is a simple gui calculator.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy"],
    entry_points={"console_scripts": ["gui_calculator = calculator.calculator:GUICalculator"]},
)
