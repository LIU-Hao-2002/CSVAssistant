# Introduction
CSVAssistant is an agent that can help you automatically analyze the csv file, which is developed within 3 hours so everything is still simple and naive.
All you need to do is input the file path and your requirements in natural language, and then wait for the agent to finish the whole analysis.

# Structure

```
|-- README.md
|-- config.py
|-- demo.py
|-- outcome
|   |-- code_0.py
|   |-- code_1.py
|   |-- code_2.py
|   |-- explanation_0.txt
|   |-- explanation_1.txt
|   |-- explanation_2.txt
|   |-- plot_0.png
|   |-- plot_1.png
|   |-- result_0.pkl
|   |-- result_1.pkl
|   `-- result_2.pkl
|-- requirements.txt
|-- utils.py
`-- test.csv
```

## config.py
It defines all the prompts (to generate code, to dubug code and to genearte answers in natural language). Please enter your api key for LLM here.

## demo.py
It defines class DataAnalyzer, which is an end to end agent to assist in data analysis.

## outcome
This directory stores all the outcomes (codes, answers, plots and results).

## utils.py
It defines the function to get response from LLM.

## test.csv 
The test csv file for demo.

## requirements.txt
The required packages.

# Quick Start
## Install the necessary packages in requirements.txt
## Change your api key and base in config.py
## Prepare your csv file for analysis
## Run demo.py and follow the instructions to input through your keyboard