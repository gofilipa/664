# what is web scraping?
Web scraping is a programmatic method for extracting data from webpages. It is the process of going into the website's source code, which is in the form of HTML code, pulling out information from the HTML, and manipulating that information into a desired format, like a spreadsheet. It is distinguished from web crawling (an even more automated form of scraping that "crawls" over several websites) and APIs (requesting data directly from the source), both of which are described below.

Before deciding what method of getting data is right for you, consider whether the data holder (the publisher or owner of the data) might be able to give it to you directly. Because web scraping can be considered invasive, especially if done repeatedly, data holders are often more than happy to package up the data for you. This is especially true of the data holder is an academic or cultural institution, such as a library, or an archive. If you want access to something in the Princeton University Library, including the online catalog, for example, you should email the librarians directly.

## vs APIs
The most common way to get data these days is via an API. API stands
for "application programming interface." It is a bit of software that
allows you to interface, or "talk," with an application. For example,
your weather application on your phone uses an API to request data
about the current temperature from a computer server that contains
this information.

The difference between web scraping and APIs is that APIs are created by the data holders themselves, so they are always more efficient. An API will return a nicely packed data in the form of JSON or XML, which are popular data formats, to the requester. Many large websites have APIs, for example Reddit, Twitter, the New York Public Library, SkyScanner, and more. Generally, if there is an API, use that before scraping. 

## the anatomy of a URL
My favorite API is the [Met API](https://metmuseum.github.io/), from the Metropolitan Museum of Art in New York City. I like this API because it is free, open, and requires no sign-up or authentication codes. 

To give more of a sense of how an API gets data from a server, I will explain the "anatomy" of a URL. APIs use URL *endpoints* to get data from servers. You can think of a URL as a series of folders that each contain data. The folder which contains the data you want is the endpoint. Here's how the Met uses URLs in its API:
- the *root* consists of the base URL. 
   - https://collectionapi.metmuseum.org/
- the *path* which consists of a directory structure (file structure) where the data is held: 
   - /public/collection/v1/objects
   - /public/collection/v1/departments 
   - /public/collection/v1/search
- the *query parameter* or the *endpoint* which is the specific request.
   - ?q=SearchTerm
   - ?q=Berthe+Morisot

So, to search for objects that match the name of the painter "Berthe Morisot," one would use the following request URL:
`https://collectionapi.metmuseum.org/public/collection/v1/search?q=Berthe+Morisot`

The results would appear as a list of object IDs in a JSON format. Then, one would use the objects path to search for a specific object. The result is the catalog information for that item in JSON format. Put the above URL in the browser to see it for yourself!

`https://collectionapi.metmuseum.org/public/collection/v1/objects/438009`

At the end of the workshop, we will look more deeply at the [Legiscan API](https://legiscan.com/legiscan). 

## tools for scraping
If you find yourself in a scenario where there's no API to access the data you want, or the access to the API might be restricted in some way, web scraping might be your best route. Just be aware that web scraping requires more work from the individual, who needs to figure out how to get and save data from the source, mostly without support from the source. 

In Python, there are three major "libraries," or collections of code, for web scraping. They each have different advantages, working best with specific use cases. Here is a brief overview of their differences.

### BeautifulSoup4, or bs4
More than a web scraper, [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is technically an HTML parser, which uses the `requests` library to make http requests using URLs.

Why it's useful:
- powerful for manipulating and transforming HTML data. 
- beginner-friendly, get started with just a few lines of code.

### Scrapy
[Scrapy](https://scrapy.org/) is a web crawling framework. It requires installation, and comes with many pre-made files for web scraping. 

Why it's useful:
- it has its own interactive mode, the "scrapy shell," for exploring web pages. 
- it enables one to "crawl," or navigate through, websites, pagination, clicking on links, etc. 
- more appropriate for larger scale crawling projects.

### Selenium
Like Scrapy, [Selenium](https://www.selenium.dev/) can also crawl web pages. The difference is that it uses a "web driver," that is, a simulated browser to scrape websites. 

Why it's useful:
- it enables the scraping of dynamic elements. Information served through JavaScript or APIs, for example, can be accessed via the simulated driver.
