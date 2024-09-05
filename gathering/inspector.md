# the HTML Inspector

## the Inspector
Before playing around with the web scraper, we will first inspect a web page "under the hood" to get a sense of what the website code looks like. This will be helpful later on, when we want to isolate elements from a webpage for scraping. 

To see the website code, you can use the "inspector" tool. Follow these steps:
1. Open up a web browser, go to the *Trans Legislation Tracker* at `https://translegislation.com`
2. Right click on the first heading, which should say "2024 anti-trans bills tracker"
3. On the dropdown menu, select "Inspect" or "Inspector." (If you do not see this option, try opening the "Tools" or "Development" menu at the top of the application, and then selecting "Web Development Tools" or "Inspector" from the menu).
4. A new window will pop up within your browser window. This window may appear overwhelming, and it contains a lot more information that we will need. For now, just focus on the part that shows the HTML code. 


## intro to HTML

For those of you who have never seen HTML before,m I'm going to examine a sample HTML file. An HTML file (short for HyperText Markup Language) tells the computer how to layout the web page. 

Note the different parts of the page indicated by "elements" or "tags." The **head** tag, for example, includes the **title**, **h1**, **h2** tags, and the **body** tag includes **a** and **p** tags. In addition to elements/tags there are also "attributes," which provide more information about the tag, like how to style it or where to insert a link. Below we see attributes for **class** and **href**. 


```html
<html>
    <head>
        <title>The Dormouse's story</title>
        <h1>This is a first level heading</h1>
        <h2>This is a second level heading</h2>
    </head>
    <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
    </body>
</html>
```

## scraping on Google Colab

On the next page, we will open a Google Colab document to start scraping. If you are unfamiliar with the Colab environment, please see the [Colab overview section](../intro/overview.md#google-colab-environment)

