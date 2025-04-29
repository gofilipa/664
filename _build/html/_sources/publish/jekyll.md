# publishing a static site

For this session, we will combine [Jekyll](https://jekyllrb.com/) and
[Github Pages](https://pages.github.com/) to deploy your project into
a website that others can access on the internet.

## what is Github Pages?

A hosting service by Github that lets you create static sites on the web. It takes HTML, CSS, and JavaScript files from a GitHub repository, and publishes them as a website.

What are static sites? Websites that are generated once (usually by a program like Python or Ruby), then pushed to the server to be hosted in its already-generated or "static" state.

## what is Jekyll?

Jekyll is a static site generator. A program that allows you to convert plain text documents (like markdown files) into HTML and CSS. With Jekyll you can author documents in a relatively easy format like Markdown, and have it transform into HTML.

There are two ways to use Jekyll for Github pages. The easy way and the hard way. I'm going to review both of them here, and provide detailed instructions below.

The easy way: Github pages has built-in support for some kinds of Jekyll sites, which means that you can create one completely through Github.com. This is a massive benefit, because virtually all open source web authoring platforms require you to download and install software via the command line.

The hard way: For those of you more familiar with the command line, you'd have a lot more options of different Jekyll themes to choose from, and a lot more control generally over the way your site is created. That being said, it is a higher barrier to entry and requires you to install software like git, ruby, and jekyll over the command line.

## how to set up Jekyll on Github Pages
### 1) choose a theme and fork it!

Choose a theme you like from this page: https://pages.github.com/themes/

Fork the theme by going to the github page, and on the top right, press "fork".

When you are prompted, be sure to change the name of the respository to something relevant to your project.

### 2) open the web editor, edit your index.md file

Open the code editor by pressing the period button on your keyboard. You'll see a new interface appear which lets you edit the files in your repo.

First, move all of the files (except README) in the root folder to nest permanently under the "docs" folder. You can leave the README.md file in the root (later on, you can add your own information here).

The "docs" folder is where Github looks for the HTML files to display on your site, so by moving the files there, you're making it easier for Github to generate your site later on.

Second, open the index.md file, which should now be in the "docs" folder. This file is written in markdown, and offers a handy key for markdown formatting. The top section (sandwiched by hyphens) is layout information for the page. Do not change these first three lines).

The rest you can delete to get rid of it, or keep it around for convenience, as it offers useful information on how to format markdown. I've simply "commented" it out using markdown comments, which look like this:

```
<!-- -->
```

You can comment out most of that text by wrapping it with these symbols. For example, I'm commenting out the first line from the file below:

```
<!-- Text can be bold, italic, ~strikethrough~ or `keyword`. -->
```

You can read a whole lot more about markdown formatting here: https://www.markdownguide.org/cheat-sheet/

Want to create new page? Create a new file for your page called PAGE-NAME.md, replacing PAGE-NAME with a meaningful filename for the page.

Add the following frontmatter to the top of the file, replacing PAGE-TITLE with the page's title and URL-PATH with a path you want for the page's URL. For example, if the base URL of your site is https://octocat.github.io and your URL-PATH is about/contact, your page will be located at https://octocat.github.io/about/contact.

```
layout: page
title: "PAGE-TITLE"
permalink: /URL-PATH
```

Below the frontmatter, add content for your page.

### 3) commit and push your changes

Once you're done editing the markdown file, go to the little "source" tab on the left. It looks like three dots connected by lines. Here, on the lefthand sidebar, you'll see a list of all the changes you've made, and a blank text box above them. In that blank box, write a short message summarizing your changes, like "edited the index.md file". Then, press the "commit & push" button.

### 4) configure Github pages on your repo settings

Back on your regular repository page (you will need to open up a new tab and navigate to your repo on github), go to the "Settings" tab at the top. Then, scroll down to the "Pages" tab on the left sidebar.

Then, on the main section of the page, go to the Branch heading. From the first dropdown, select "Master" or "Main," and on the second dropdown, select "docs". Finally, click save.

Congratulations!

Your website will be visible in a few minutes at the URL:

`your_username.github.io/your_repo_name`
