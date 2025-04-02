# chapter overview

## learning objectives

This section builds on the previous ones to clean and analyze
data, using data from current anti-trans legisation as an example. 
First, participants will clean and transform raw data using string methods into an analyzable, structured format in a spreadsheet. 
Then, they will analyze and visualize this data using the `pandas` library. Finally, they will explore different methods
for text generation using the `transformers` library for machine learning.

This section introduces
- string methods for working with text data
- how to write custom functions for automating tasks
- the `pandas` libary for working with tabular data
- the `transformers` library for generating text

## anti-trans legislation
The past couple of years have seen an explosion in anti-trans
legislation that restricts basic rights and recognition for trans
people. In 2023, more than 500 bills were proposed that prevent trans
people from using bathrooms, playing in sports, accessing healthcare,
and more in ways that accord with their gender identity. Of those 500
proposals across state legislatures, 87 passed. Compare that number
with last year, 2022, 174 bills were proposed, and 26 passed. See the
[Trans Legislation Tracker](https://translegislation.com/) for more
information.

## Python environments

There are many ways to use Python. For this workshop, we will be using
[Jupyter-Notebooks](https://jupyter.org/), installed through the
[Python Anaconda](https://www.anaconda.com/download/success)
distrubtion. This option is convenient because it creates a "local"
version of Python directly on your computer, which means you can use
it in mutiple ways and without an internet connection.

For those of you who cannot download Python, you can use [Google
Colab](https://colab.research.google.com), a browser-based tool for
running Python code. Like Google Docs, Google Colab creates a
collaborative environment hosted on the Google cloud for authoring
content. Whereas most Python environments require installations (some
of which can be really complicated), Google Colab offers Python
software pre-installed on the cloud environment. It enables new users
to jump right into programming.

