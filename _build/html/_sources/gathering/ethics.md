# what is ethical? what is legal?
What follows is a brief overview of ethical and legal considerations for web scraping. Then, I offer my own process  in navigating these considerations as I determine how to scrape data on anti-trans legislation (explained further below). 

Though I consider both legality and ethics, my emphasis throughout the process will be on ethics. The legality of web scraping is already well covered in many places, including the University of Michigan's excellent [guidebook](https://docs.google.com/document/d/11LZweIYD9MmjiZgY-VW1IXUPOP1k-SwXNiOdJDVC7Vw/edit#heading=h.ut4ttuudwb6i) on the subject, so I will not attempt to reproduce it here.

## ethical: 
I begin with a list of ethical questions that researchers should ask themselves at the outset of any project. Here, I encourage you to think carefully about *who* your data pertains to (who is the data about?) and how gathering, doing analysis, and/or publishing that dataset will affect the groups involved. You especially want to do this work if your project involves communinities that are marginalized in any way. 

Here are some initial questions you want to ask yourself:
- Who is the data about? Who owns the data? (often times, the data's owner is not the same as the person/group it describes)
- Does the data contain any personally identifying characteristics? If so, what are the potential effects of these details being shared or published?
- What do I intend to do with the data? (gather it, analyze it, publish it online, all of the above, etc.)
- How will publishing the data affect the persons/group(s) that the data describes?

The most important thing is to **assess any vulnerabilities about the people directly associated with the data**. And this can only be answered on a case by case basis. There is no standard that applies to all groups.

As you deliberate, you'll want to consider how the data can be repurposed for monetary value or surveillance. How could that data be used for monitoring or value extraction? In what ways could that data be used to exploit human subjects? Could it make a particular group vulnerable? If the answer is yes, that doesn't mean you have to forgo the project. But it does mean that you should think about how you use and share that data, to commit to protecting the dataset. 

Protocols for handling data will vary according to group of people your data is about. For example, indigenous populations across the United States are understandably protective of their information and may not want it to be made public. In that case, you could reach out to the groups directly and ask permission, or you can commit to keeping the data private (doing analysis on your own) and only sharing the results of the analysis. Another example, anti-trans legislation, is a different case. Collecting and publishing data about anti-trans laws brings scrutiny to the issue of trans discrimination, which benefits the group that the data describes. And additionally, the research goal of this project--to do a text analysis of terms like "gender" and "sex" defined within the bills--creates an opportunity to examine the ways that language is being used to oppress and limit this particular group.

The most important consideration is how copying, analyzing, and/or publishing that data affects the groups to whom that data pertains. Be thoughtful about the potential effects of collecting that data and making it available. 

## legal:
If after assessing the communities involved, you've determined how to handle the data in an ethical way, then you can move on to legality.

What is legal? Basically, there are two questions here:
- First, is the data publically accessible? This is distinct from "open" or "free" data, each containing their own complexities. Just because something is publically accessible on the internet doesn’t mean it is open data, in the "public domain". It may be protected by data holder's IP rights or copyright law. Which leads to the second question.
- Second, does the data publisher permit scraping or mining their data? For this, you'd need to check the `robots.txt` file (more on this below) and the "Privacy" or "Terms of Service" pages on the website. Make sure to check the website thoroughly. On the Princeton University Library website, for example, scraping is clearly prohibited in a "Copyright and Access" section on the sidebar. 
  
If the answer is yes to both of these questions, then scraping (and perhaps even publishing, but you'd want to check that too) the data should be legal. If the answer is no to any of them, then your project *may* run the risk of violating the law.

Finally, it is important to remember that copyright law protects making copies of information for the purpose of academic research. This means that, provided you do not distribute, publish, or sell the data, you can scrape information for your own private study. See more under the "[Fair Use](https://www.copyright.gov/fair-use/)" description at the US Copyright Office.

## not everything legal is ethical: exhibit A(I)
It's worth re-iterating the importance of ethics. Just because something legally can be scraped, analyzed and/or published doesn't mean it should be scraped, analyzed, and/or published.

For example, the web scraping processes being used to train the very popular generative AI tools like *ChatGPT*. The companies like OpenAI that make these tools take data from every corner of the web, use it to train their language and vision models, and then sell that technology back to the user. They do this without any compensation to their data sources, not even when the sources include [works of literature](https://authorsguild.org/news/ag-and-authors-file-class-action-suit-against-openai/) or [openly licensed software](https://githubcopilotlitigation.com/), which is often stipulated for non-commercial use.

Perhaps the worst offenders of scraping are those who use that data for surveillance and policing purposes, like in the creation of facial recognition software. For example, Clearview AI infamously [scraped images from social media to sell to law enforcement](https://www.technologyreview.com/2021/04/09/1022240/clearview-ai-nypd-emails/), who has been using the images in ways that violate privacy and [exacerbate racial profiling](https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212). 

## anti-trans legislation
Taking ethics and legality is only the begining, and other hurdles can arise when logistically trying to scrape a website. I'm going to demonstrate one path of negotiating this complicated process, using trans legislation websites as an example.

After making the assessment that this dataset (anti-trans legislation) wouldn't harm any marginalized groups, I sought out some websites that were legally scrapable. By checking the `robots.txt` file for each site, I was able to see which ones prohibited scraping. To check this file, just append `robots.txt` to the root of the URL (the "root" is the part of the URL that ends with `.com` or `.org`, etc.).

First, I came across a website that totally prohibits web scraping. Here, the [Bill Track 50](https://www.billtrack50.com/) website, which aggregates legislative data from across the United States, has its `robots.txt` at `https://www.billtrack50.com/robots.txt`. It contains the following declaration:

```
User-agent: *
Disallow: /
```

The "user-agent" refers to the entity looking at the website, whether that be a person or a bot. The asterisk is a "wild card," which means that it applies to *all* user-agents. 

The "disallow" line indicates which parts of the websites are off limits. The `/` in "disallow" means that all possible paths--that means, all possible sites contained under the root `billtrack50.com`, are off limits. Together, the user-agent and disallow declarations definitively shut the door to all scrapers: it means that all users,no matter who they are, cannot access any possible page created from the root URL, including the root itself. This is fairly understandable, as the organization's financial model depends on its user-friendly API for accessing this data, which it sells to users. 

Here's an example from another contender for scraping, *Track Trans Legislation*, which mostly allows scraping. It does have some limits, but only on the `admin` and `bill-logs` paths. Everything else on the site is fair game:

```
User-agent: *
Disallow: /admin/
Disallow: /bill-logs
```

<!-- add the connection to BillTrack50-->
However, even if the website is legally scrapable, it may not be *technically* scrapable, which I quickly discovered when I tried to scrape the *Track Trans Legislation* site. The reason has to do with its so-called "dynamic" web interface. Because many scrapers work with static HTML (HTML that is rendered all at once), it cannot capture shifting, dynamic elements like those contained in JavaScript code. You can quickly tell if a site has dynamic elements if it has scrollable boxes, buttons, search bars, or something else that changes or updates in place without reloading the whole page. Those elements include their own processes, like APIs, that are not present in the static version of the website code (interestingly, one of the APIs contained in this site is the BillTrack50 API! which explains why this company wants to lock down scraping). So, although scraping *Track Trans Legislation* is legally permissable (for the most part), the information contained in its dynamic interface cannot be captured with typical web scrapers. To work with dynamic websites, use another tools like [Selenium](https://www.selenium.dev/) (which simulates a browser where elements can then be "clicked" or "scrolled", etc).

Dynamic websites are popular, and unfortunately for me, there were a couple more of them which, while legally permissible, I couldn't scrape. While these websites show the source code in the "page course" or "inspector" views (discussed in the next section), the dynamic elements do not appear in the code that is scraped by tools like bs4. 

Here's a list of the sites that contain the data I want within dynamic elements, in this case, within scrollable boxes: 
- ACLU's "[Mapping Attacking on LGBTQ Rights in US State Legislatures](https://www.aclu.org/legislative-attacks-on-lgbtq-rights)"
- Equality Federation's "[Anti-Transgender Legislation](https://www.equalityfederation.org/tracker/cumulative-anti-transgender)"

Besides dynamic websites, another obstacle is the use of "bot blockers," which guards against web scrapers by feeding the wrong information (usually a blank webpage) to the scraper. For example, the [Congress.gov](https://www.congress.gov/) website uses bot blockers (even though the federal legislation is technically in the public domain). A bot blocker will usually give a web scraper a blank page with the following title embedded in the HTML:

```html
<title>Just a moment...</title>
```

To its credit, Congress.gov does offer an API, the [Congress.gov API](https://blogs.loc.gov/law/2022/09/introducing-the-congress-gov-api/), which is a good option for those who want legislative data. If you encounter bot blockers, remember to check for an API, and also consider reaching out directly to the data holders/curators, to get your data.

At the end of my search, I was left with the following two sites that contained the data I want in a static format: 
- National Center for Transgender Equality's "[State Action Center](https://transequality.org/state-action-center)" 
- Trans Leglislation Tracker's "[2023 anti-trans bills tracker](https://translegislation.com/)"
  
I selected the second site, *Trans Legislation Tracker*, due to its wonderfully open declaration in its `robots.txt` file:

```
User-agent: *
Allow: /
```

Nothing could be more permissive than that.
