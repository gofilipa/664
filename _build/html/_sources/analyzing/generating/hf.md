# Huggingface🤗 platform
🤗 is an AI research and development company based in Brooklyn, New York City. The company hosts and develops a *platform* for Machine Learning, which contains compute & collaborative spaces for AI models, datasets, and more. 

It is like a github for ML, if github had additional "hubs" for things besides just code (like datasets, papers, apps, etc).

## "models hub"
We will start with the "models hub," which contains AI models created
by 🤗 users. Users train and/or fine-tune models, then publish them on
the hub for others to use.

The navigation goes from left to right: on left side, there are tasks, like text classification; on right side, there are models. 

**Filter results by "most downloaded"**, and try to guess what the model
does just by looking at the name.
  - Wav2Vec - audio to vector, speech to text.
  - RoBERTa - one of the many permutations of BERT, you'll see. First
    model to put into practice the Transformer architecture.

Then, **filter results by "most liked"**:
  - click on [stable-diffusion-3.5-medium ](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
    - on each model, you can see the model details at the top of the
      page (keywords, size, papers)
    - the inference on the right. "Inference" means you give it a prompt, and it generates a response.
        - you used to do this without limits and on all the models, now it's hard to find one that will allow you. 
    - the model card in the main section.
      - explanation of model, code to use it, attributions, licensing,
        instructions for ethical use, "limitations and biases"
	- things like "Training" and "Environmental Impact" are super
          rare.

Now, **filter by task and by size**. Then, filter by *inference available*. Choose one of the results that looks interesting to you, and practice running inference here for a few minutes. Anything that you notice about the results?
- it's repetitive. A problem caused by the traits of our
            language itself.
- it generates words that have the highest likelihood. The words that
            have this likelihood tend to be the same ones, over and
            over again.

Go back to the search, and **type `gpt-neo-125`.** Click on the
[gpt-125m](https://huggingface.co/EleutherAI/gpt-neo-125m) result. This is a model developed by EleutherAI, a non-profit research lab. It is part of a larger family of models named "gpt-neo" with the size at the end.

Here, we can see the *model card*, which contains important information about the model. There are a couple of things to note here: 

On the header, and the right hand panel:
- notice "*model size*". How big is it?
 - 125m parameters. That's how many inputs goes into
      inference. Includes things like word vectors, but also different
      kinds of inputs.
 - size is an indication of complexity. The larger the size, the more
        likely that the model will preform well.
- notice the "*license*":
  - MIT license. Very permissive, part of the "Open Source"
    licenses.
    - the model is totally open to download and modify as you wish,
      even for commercial purposes.
- notice the dataset, in this case, [the Pile](https://en.wikipedia.org/wiki/The_Pile_(dataset)). This was the dataset used to train the model, and it's a relatively well curated dataset for LLM training.

Now, look at the main text on the page. Here you will find context and information for the model, including training and inference information.

## "datasets hub"
Besides models, 🤗 offers Datasets. These datasets are used to fine-tune (and also train and evaluate) models. We are going to take a little peak into this part of the platform.

Where do we get most of the data used to train these models? From scraping the internet. Look at the [c4](https://huggingface.co/datasets/allenai/c4) dataset, for example. This dataset is based on [the Common Crawl](https://commoncrawl.org/), the largest web crawling initiative. The c4 dataset is a "colossal, cleaned" version of the common crawl (hence the *4*c). It cleans the Common Crawl dataset using the "badwords filter", aka the [List of Dirty Naughty Obscene and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words).

It is very difficult to clean this amount of data at scale, which is a major issue for ML model training --- and a major opportunity for anyone who wants to get into the field. 

In the next section, we will look at how to use these models by running "inference" directly in Python. 

