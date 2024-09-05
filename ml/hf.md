# Huggingface🤗 platform
Now let's move to the platform we will be using, HuggingFace🤗. 

🤗 is an AI research and development company based in Brooklyn, New
    York City. The company hosts and develops platform for Machine
    Learning, which contains compute & collaborative spaces for AI
    models, datasets, and more. It is like a github for ML, if github
    had additional "hubs" for things besides just code (like datasets,
    papers, apps, etc).

## "models hub"
We will start with the "models hub," which contains AI models created
by 🤗 users. Users train and/or fine-tune models, then publish them on
the hub for others to use.

The navigation goes from left to right. On left side, there are tasks,
    like text classification. On right side, there are models. We are
    going to narrow down the models.

Filter results by "most downloaded", and try to guess what the model
does just by looking at the name.
  - Wav2Vec - audio to vector, speech to text.
  - RoBERTa - one of the many permutations of BERT, you'll see. First
    model to put into practice the Transformer architecture.

Then, filter results by "most liked":
  - click on [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)
    - on each model, you can see the model details at the top of the
      page (keywords, size, papers)
    - the inference on the right. Because this is a large model, we
      will enter a prompt now.
      - You can run these models (what we call "inference") directly
        on the HF website. Which is amazing.
    - the model card in the main section.
      - explanation of model, code to use it, attributions, licensing,
        instructions for ethical use, "limitations and biases"
	- things like "Training" and "Environmental Impact" are super
          rare.

Go back to the search, and type `gpt-neo-125`.
- click on the
  [gpt-125m](https://huggingface.co/EleutherAI/gpt-neo-125m) result.
  - a model developed by EleutherAI, a non-profit research lab.
  - part of a larger family of models named "gpt-neo" with the size
      at the end.
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

practice running inference here for a few mintues. Anything that you
notice about the results?
- it's repetitive. A problem caused by the traits of our
            language itself.
- it generates words that have the highest likelihood. The words that
            have this likelihood tend to be the same ones, over and
            over again.

### models hub activity: 5-10 minutes
Go back to the models page, and choose a task that interests you.

Filter by "most likes" or "most downloads".

Explore some of the top results, clicking on the links to the model
pages.

Run inference on a few of the models that you find, taking note of the
model size.

What differences do you notice between the models?

## "datasets hub"
Besides models, 🤗 offers Datasets. These datasets are used to
  fine-tune (and also train and evaluate) models. We are going to take
  a little peak into this part of the platform.

Before diving in, important to consider how these datasets were
created. There are a lot of *ethical issues* with the ways that
datasets for training are created and cleaned (or not cleaned).

Where do we get most of the data used to train these models? 
- scraped from the internet, most of them. 
  - What kind of data does the internet contain?
- how do you remove bias and discrimination? 
  - attempts to automate this have failed: "[List of Dirty Obscene...](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words)"
- RLHF - "reinforcement learning from human feedback", which creates a
  labor exploitation issue.

TLDR: There's a race to get these products out there, so people aren't
    taking the time needed to adequately clean the data and make sure
    it's safe. 
