# research questions: defining gender
There is no objective or neutral way of doing text analysis. It is a speculative and creative endeavor, which requires researchers to imagine what kinds of patterns they might find in the data. *Research questions by design imply some assumptions or expectations about results*. Additionally, the process of analysis itself will likely bring researchers to re-frame their perspectives and re-write their questions. Though it often feels like a step backward, this recursive process actually means that they are making progress toward finding an answer (by finding the right question!). 

Being cognizant of the implications and assumptions contained within research questions is a crucial part of critical analysis. It is also an opportunity to draw from domain-specific expertise, allowing you to build from your own knowledge as you imagine the kinds of patterns that might emerge in the analysis.

## anti-trans legislation
Over the past several years, there has been a dramatic increase in "anti-trans legislation," that is, legislation that limits trans peoples' rights. According to the [Trans Legislation Tracker](https://translegislation.com/), in just one month in 2023 (the year of this writing), "the U.S. doubled the number of anti-trans bills being considered across the country from the previous year." 

Many of these bills block access to healthcare that is gender-affirming and to public places and activities, like the "bathroom bans," the bans in sports, and the bans on expressing gender identity in school. The explosion of bills across the country not only codifies discrimination, but also reflects a worrying trend about how the general public views trans peoples' existence and rights. 

I am interested in examining the language of the bills themselves for the assumptions they might make about sex and gender. *How are these terms being defined? Are they being defined as biological fact, cultural phenomena, or a mixture of both? What assumptions are being made in these definitions? How do certain perspectives exacerbate the current discrimination against trans people?*

## domain-specific knowledge
For my dataset, a collection of legislative bills from congress that feature the term "transgender," I want to know how each bill is defining terms related to gender. My goal is to get a list of definitions for these terms, so I can start to explore any possible conflations between gender as a cultural and expressive phenomenon and sex as a biological one. This conflation is something I am anticipating from the results. 

Informing these questions is an understanding of gender drawn from a linked vocabulary of LGBTQ+ terms, the "[Homosaurus Vocabulary](https://homosaurus.org/)," which offers definitions of various LGBTQ+ related terms. 

For example, this vocabulary defines "Gender" as a cultural phenomenon, "A socially constructed system that gives meaning to masculinity and femininity," which is "developed through the interaction of social roles and expectations, one’s response to those expectations, one’s physiology, and one’s internal sense of self" ("Gender," Homosaurus). This definition contrasts with "Sex," which is "The category assigned to an individual to describe their body and its role in sexual reproduction, usually based on external anatomy, but also including chromosomes, gene expression, hormones, and internal and external reproductive/sexual organs" ("Sex," Homosaurus).

## close-reading the dataset
To write effective research questions, I also ought to also spend some time close-reading part of the dataset, the collection of congress bills. Close-reading the dataset will give me contextual information for writing code that pulls out patterns that I want from the data. Here, I will examine the first few bills for how they are defining the terms that I'm interested in.

For example, below are some definitions for the terms "biological sex", "gender", "sex", "gender identity", and "sexual orientation":

```
Biological sex.--The term `biological sex\' means the biological indication 
of male or female in the context of reproductive potential or capacity, 
such as sex chromosomes, naturally occurring sex hormones, gonads, and 
non-ambiguous internal and external genitalia present at birth, without 
regard to an individual\'s psychological, chosen, or subjective experience 
of gender.

Gender.--The term `gender\' means the psychological, behavioral, social, 
and cultural aspects of being male or female.

Sex.--The term ``sex\'\' includes--(A) a sex stereotype;(B) pregnancy,
childbirth, or a related medical condition;(C) sexual orientation or
gender identity; and(D) sex characteristics, including intersex
traits.

Gender identity.--The term `gender identity' means the gender-related 
identity, appearance, mannerisms, or other gender-related 
characteristics of an individual, regardless of the individual's 
designated sex at birth.

Sexual orientation.--The term `sexual orientation' means homosexuality, 
heterosexuality, or bisexuality.
```

Later in the workshop, we will examine this language even more closely in order to code our patterns.