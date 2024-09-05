# "Intro to Python for Working with Text" workshop series

## Workshop Overview
As one of the most popular, versatile, and beginner-friendly
programming langauges, Python can be used for a variety of tasks from
gathering data to publishing websites.

This 5-part workshop series introduces participants to the Python
programming language for working with text-based data. Participants
will gain Python skills by gathering, cleaning, and exploring data
about the current [anti-trans
legislation](https://translegislation.com/) that is sweeping the
United States. At the end of the series, participants will use the
datasets that they create to train a small AI model to generate text.

The first workshop begins with core concepts in programming to
understand digital forms of data and basic manipulations. The second
and third workshops move to data gathering and processing with web
scraping, APIs, and text cleaning methods. Participants will then
spend the fourth and fifth workhops exploring their datasets with text
analysis and deep learning tools. See a more detailed description of
each workshop below.

The workshop website is built using [Jupyter
Book](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://jupyterbook.org/&ved=2ahUKEwi7h8TotvSGAxXTk4kEHTBTCUEQFnoECAYQAQ&usg=AOvVaw2U9BjlgotCJej2DEcDbtcp)
and [Github Pages](https://pages.github.com/). To make changes to the
workshop, please read the [technical
specifications](./readme.md#technical-specifications) section below.

### Individual workshop overviews
#### Workshop 1: “Introduction to Python Fundamentals”
Basic introduction to core concepts in Python programming. Grounds
instruction in critical awareness of data and what happens to data at
various levels of transformation and abstraction.

#### Workshop 2: “Python for Web Scraping and APIs
Teaches programmatic methods for extracting data from webpages using
web scraping and APIs within an ethical approach. Advances core
concepts of looping and conditional statements from introductory
session and introduces object-oriented programming and working with
code libraries. Participants will apply skills to gather data about
current [anti-trans legislation](https://translegislation.com/) in the
USA.
- libraries: `requests`, `bs4`, and `pandas`

#### Workshop 3: “Python for Text Cleaning”
Explores preparing text data for analysis, with emphasis on removing
  unwanted elements that may skew analysis. Participants will continue
  to build skills in algorithmic thinking while learning to
  write functions and  scripts for customizing and automating text cleaning processes.  
- libraries: `pandas`, `spacy`

#### Workshop 4: “Python for Text Analysis” 
Explores methods for finding and analyzing textual patterns through popular tasks in Natural
  Language Processing. Participants practice writing code to annotate
  and extract text according to specific features from current
  “anti-trans” bills in the USA.
- libraries: `spaCy`
  
#### Workshop 5: “Python for Text Generation (with Machine Learning)”
With the anti-trans bills data that they prepared in previous workshops, participants practice fine-tuning a small Text Generation model and learn about how to use Machine Learning for research.
- libraries: `transformers`

## Digital Scholarship at PUL
See more workshop offerings (including on Python) at the [Princeton University library](https://libcal.princeton.edu/calendar/). We have upcoming workshops on working with data, digital publishing, and more.

Want to talk Python or another digital project or tool? Sign up for a [consultation with Digital Scholarship](https://bit.ly/ds-consults) at Princeton. 

## Technical Specifications
The front-facing website that hosts the workshops is built using
[Jupyter
Book](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://jupyterbook.org/&ved=2ahUKEwi7h8TotvSGAxXTk4kEHTBTCUEQFnoECAYQAQ&usg=AOvVaw2U9BjlgotCJej2DEcDbtcp)
and displayed on Github servers via [Github
Pages](https://pages.github.com/). 

Making changes to the website is much like making changes to any
Github repository, but with the added step of pushing the changes to a
new Github Pages branch. Below are the steps necessary to make changes
and update the website accordingly. Please follow the steps below. 

Before starting, you'll need to install a few pieces of software:
- Python (I use the [Anaconda](https://www.anaconda.com/download)
  distribution, but any kind of Python works as long as it is a
  version of Python 3+.
- [Jupyter-Book](https://jupyterbook.org/en/stable/start/overview.html)
  for building the website.
- [Git](https://git-scm.com/downloads) versioning software for sending
  files to a [Github](https://github.com/) server, where they will be
  hosted. An account on Github will also be necessary.

1. First, clone the repository onto your computer by typing the
   following into your command line. After that, you'll have your
   "book" (the Jupyter-Book repository) on your local machine.
   
   ```console
   git clone https://github.com/PULdischo/python-for-text.git
   ```
2. Second, make changes to the files as needed. Maybe you want to add
   a new page or a new workshop. Jupyter-book files can be in markdown
   or python notebooks (`.ipynb` files). If you are adding a new file
   or section to the workshop, make sure to indicate the new material
   in the `_toc.yml` (the table of contents) files, so it will appear
   in the sidebar. To learn more about how to create and modify files,
   check the excellent [documentation on
   Jupyter-Book](https://jupyterbook.org/en/stable/basics/organize.html).
   
3. Third, you will "build" the book by running the following in your
   command line, making sure you are one directory *above* your book.
   For example, if you cloned the book into your Desktop folder, make
   sure you are in the Desktop folder (rather than the book's folder),
   when you run the code below.  
   
   The build process will create a `_build` folder in your book, which
   contains all of the html files necessary to display your content in
   a web browser. 
   
   ```console
   jupyter-book build [book's name]
      
   ```

4. After building the book, you can push your changes to Github. Here
   you can add, commit, and push changes like you would do for a
   normal repository.
   
   ```console
   cd bookname
   git add .
   git commit -m "updating files"
   git push
   ```
   
5. The final step will be another Github push, but this time to a new
   branch called `gh-pages`. Pushing to the `gh-pages` branch allows
   us to upload the html files so viewers can see them rendered nicely
   on the browser.
   
   To push to `gh-pages`, you will need to install a software package
   called `ghp-import`. To install that package, run the code below.
   (Note: you will only need to install the package once; every time
   after that, you can simply push your changes.)
      
   ```console
   pip install ghp-import
   ```
   
   Finally, back on your command line, you can push your changes to
   `gh-pages` using the `ghp-import` command:
   
   ```console
   ghp-import -n -p -f _build/html
   ```

6. Note: only follow this step if you are setting up a completely new
   repository, such as on your own account. In this case, you need to
   tell Github explicitly to create a Github pages based off the
   `gh-pages` branch that you just pushed. Go to your Github
   repository's settings (check the toolbar at the top of your repo),
   select "Pages" from the tabs on the left, and configure your repo
   to build from the `gh-pages` branch. Select this option from the
   dropdown under "Build and Deployment."
   
In a few minutes, your site should be visible at
`https://PULdischo.github.io/bookname`, for this repo, the link is
https://PULdischo.github.io/python-for-text. If you're experienceing
problems, read more about [pushing to Github
pages](https://jupyterbook.org/en/stable/start/publish.html#publish-your-book-online-with-github-pages)

## Credits
Created by Filipa Calado, Digital Scholarship Specialist, Princeton
University Library.

The first workshop, "Intro to Python," is adapted from the [Graduate
Center Digital Initiatives](https://gcdi.commons.gc.cuny.edu/) Digital
Humanities Research Institute [Python
workshop](https://github.com/DHRI-Curriculum/python). The opening
challenge from this workshop takes text from the [Feminist Data
Manifest-No](https://www.manifestno.com/) by M. Cifor, P. Garcia, et
al.

For more instruction with Python, please see these books:
- WJB Mattingly's [Introduction to Python for
Humanists](https://python-textbook.pythonhumanities.com/intro.html)
- Melanie Walsh's [Introduction to Cultural Analytics &
Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html)

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

