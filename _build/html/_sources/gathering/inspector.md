# the HTML Inspector

## intro to HTML
For those of you who have never seen HTML before, I'm going to examine a sample HTML file. An HTML file (short for HyperText Markup Language) tells the computer how to layout the web page. 

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

## the Inspector
Before playing around with the web scraper, we will first inspect a web page "under the hood" to get a sense of what the website code looks like. This will be helpful later on, when we want to isolate elements from a webpage for scraping. 

To see the website code, you can use the "inspector" tool. Follow these steps:
1. Open up a web browser, go to the *The New York Times* at `https://nytimes.com`
2. Right click on the first heading.
3. On the dropdown menu, select "Inspect" or "Inspector." (If you do not see this option, try opening the "Tools" or "Development" menu at the top of the application, and then selecting "Web Development Tools" or "Inspector" from the menu).
4. A new window will pop up within your browser window. This window may appear overwhelming, and it contains a lot more information that we will need. For now, just focus on the part that shows the HTML code.

## anti-trans legislation
The past couple of years have seen an explosion in anti-trans legislation that restricts basic rights and recognition for trans people. The number of bills introduced in 2025, like in the year 2024, 2023, and 2022 before it, marks new records. These bills prevent trans people from using bathrooms, playing in sports, accessing healthcare, and more in ways that accord with their gender identity. See the [Trans Legislation Tracker](https://translegislation.com/) for more information.

## inspecting our page
Remember that we must inspect pages with our browser's "Inspector" tool, so we know what elements to scrape with bs4.

First, navigate to the target website, at [`https://translegislation.com/`](https://translegislation.com/). Scroll down until you see the "National Anti-Trans Bills" heading. Click on the blue button that says "View 2025 National Bills". (Alternatively, just navigate directly to the page [here](https://translegislation.com/bills/2025/US)).

Once you're on the page, *right click* on a bill title, any bill title, and select the **inspect element** option (or whatever option is closest to that phrase in your menu). The inspector should pop up.

![To open the inspector](./img/inspector0.jpg)

Then, look for that element in the HTML code. The inspector contains everything you need to know about that element, including it's HTML tag `h3`, which contains the `a` and any attributes, like `class` or `href`.

![Examine the inspector](./img/inspector1.jpg)

## individual challenge
Spend some time exploring the HTML of the bill cards. Make a note of elements and their classes for the bill number (which starts with US) and the bill title (in bold text). Also be aware of parent and child elements for each of those components. 