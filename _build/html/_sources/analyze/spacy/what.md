# what is text analysis?
Text analysis involves asking questions about text and using different computational methods, like Natural Language Processing (NLP) or visualization methods, to answer them. It can be as simple as generating a list of the most frequent terms in a text, or as complicated as a machine learning model that extracts words related to a particular topic. 

What distinguishes text analysis from other kinds analysis, even those that use similar visualization methods (such as word clouds or network graphs), is the focus on *text* as the object of study. Text analysis asks questions like:
  - What ideas are in the text? What are the central concepts?
  - What are some of the nuances around a specific concept?
  - What are some perspectives contained within the text?
 
 To answer these questions, text analysis involves close study of textual features and patterns. 
  - What do certain words mean in their context, how are they being used?
  - What word or phrase patterns appear across the text?
  - What are the similarities and differences between textual features or patterns? 
  - What contextual nuances appear across features and patterns?

## tasks and questions for NLP
NLP is a type of text analysis based on certain tasks. Text analysis can, but does not necessarily have to, involve NLP tasks. Due to their focus on linguistic elements in text, NLP tasks like "Text Summarization," "Named Entity Recognition," and "Sentiment Analysis" are very useful for finding and analyzing patterns in text. While these tasks, which use "[rules-based](https://www.geeksforgeeks.org/rule-based-approach-in-nlp/)" or pattern matching approaches, have been around for decades, some of them have more recently adoped "probablistic" methods. These more advanced methods use Machine Learning algorithms to "train" programs to automate NLP tasks. 

For example, let's look at a Sentiment Analysis task, a popular NLP task that scores text based on whether it is positive or negative. A rules-based approach would hard-code the criteria for scoring, including specific and explicit examples of negative and positive words, directly into the algorithm's instructions. By contrast, a program trained to do Sentiment Analysis will process a pre-existing dataset made of texts and their sentiment scores, which is called "training data," so that it can learn (so to speak) which kinds of texts tend to have certain scores. 

Today we will be exploring a library, or a collection of code, for doing NLP in Python, which combines rules based and probablistic methods for doing NLP. This library, called `spaCy`, uses a [statistical model](https://spacy.io/usage/spacy-101#training) to categorize and label linguistic features (like parts of speech), and enables researchers to build on these write their own rules for text extraction. In other words, users leverage the results from `spaCy`'s predictions to write code that can search for specific patterns in text. 

Our work today will be about searching and extracting textual patterns. This kind of analysis can be part of a larger process that also includes visualization in a graph or chart, such as with [Voyant-Tools](https://voyant-tools.org/) (my favorite graphical tool). Or, the process can be part of a preparing a dataset for Machine Learning tasks. Here, we would use the results from our extraction to help train a new statistical model, to process even more text. This gives just an idea of how cyclical text analysis methods can be, where one kind of task feeds into another, and then circles back. 

Before jumping into analysis, it is important to discuss briefly how we gather and prepare data in the first place. 