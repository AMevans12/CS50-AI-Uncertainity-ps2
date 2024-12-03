# CS50 AI Week 2: Uncertaininty

## Overview

This repository contains solutions for the CS50 AI Week 2 problems focusing on **Heridity** and **PageRank**. The two main problems are:

1. **Heridity:** Building a Bayesian network to predict the inheritance of genetic traits.
2. **PageRank:** Implementing the PageRank algorithm to rank web pages based on their link structure.

## Problems
 
### 1. Heridity

The Heridity problem involves creating a model to simulate the inheritance of genetic traits in a family. Using a Bayesian network, the model predicts the probability of a trait appearing in offspring based on genetic information from parents and grandparents.

**Key Concepts:**
- Bayesian Networks
- Probabilistic Reasoning
- Genetic Inheritance

**Files:**
- `heridity.py`: Contains the implementation of the Bayesian network model for predicting genetic traits.

**Example Usage:**
```python
from heridity import trait_probability
trait_probability('A', 'B', 'c')
```

### 2. PageRank

The PageRank problem focuses on ranking web pages based on their importance using the PageRank algorithm. This problem involves calculating the relative importance of web pages by analyzing the link structure of a set of pages.

**Key Concepts:**
- PageRank Algorithm
- Graph Theory
- Link Analysis

**Files:**
- `pagerank.py`: Contains the implementation of the PageRank algorithm.

**Example Usage:**

from pagerank import compute_pagerank
compute_pagerank(links)


## Installation

To use the code in this repository, you need to have Python installed. You can then clone the repository and install the required dependencies.


git clone https://github.com/AMevans12/CS50-AI-Uncertainity-ps2.git
cd cs50ai-week2


# MIT License

Copyright (c) 2024 AMevans12

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Running Tests

To run the test cases for both problems, use the following commands:


python heridity_test.py
python pagerank_test.py


## Contributing

Feel free to fork this repository and submit pull requests for improvements or fixes. Contributions are welcome!


## Contact

For any questions or feedback, please reach out to me via [GitHub](https://github.com/AMevans12).


**Enjoy exploring uncertainty with AI!**
