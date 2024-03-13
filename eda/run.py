import sys
import subprocess

def install_packages():
    try:
        dependencies = ['numpy', 'pandas', 'regex', 'langdetect', 'matplotlib',
                        'seaborn', 'OpenAI', 'langchain']
        for package in dependencies:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("Packages installed successfully.")
    except Exception as e:
        print(f"Error: {e}")

install_packages()

import pandas as pd 
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import openai
from langchain.llms import OpenAI
import random
import regex as re
from langdetect import detect
import seaborn as sns
import matplotlib.pyplot as plt
from json import load

filenames = ["demo.ipynb",
            "exploratory_visualizations.ipynb",
            "agent_responses.ipynb", 
            "agent_response_visualizations.ipynb", 
            "final_bias_visualizations.ipynb"]

    
if __name__ == '__main__':
    args = sys.argv[1:]
    if 'data' in args:
        for filename in filenames:
            with open(filename) as fp:
                nb = load(fp)

            for cell in nb['cells']:
                if cell['cell_type'] == 'code':
                    source = ''.join(line for line in cell['source'] if not line.startswith('%'))
                    exec(source, globals(), locals())
