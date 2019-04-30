---
permalink: resources/
title: Resources
---

{% include toc %}

This page lists web sites, PDF documents, Jupyter notebooks, and
Python packages that have been mentioned during the course.

It's not an attempt to list everything related to each of those topics; just
to collect those resources that have already been mentioned into one place.

It is a companion to the [Recipes]({% link pages/recipes.md %}) page.

## General

[Stack Overflow](http://stackoverflow.com) is a community of programmers, and a knowledge base of programming questions and answers. You can search it directly from its site; it also shows up in Google search.

## Python

### Python References

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) – the class text
* [Python 3.6 Documentation](https://docs.python.org/3.6/)
* [Python 3.6 Standard Library](https://docs.python.org/3.6/library/index.html)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/), especially [Writing Great Python Code](http://docs.python-guide.org/en/latest/#writing-great-python-code)
* [Python Tutor](http://www.pythontutor.com) interactive visualization

### Learn Python

* [HackerRank Python Introduction](https://www.hackerrank.com/domains/python/py-introduction)
* [How to Think Like a Computer Scientist](https://runestone.academy/runestone/static/thinkcspy/index.html) interactive course. Register [here](https://runestone.academy/runestone/default/user/register#) and enter "thinkcspy" as the course name.
* [Google's Python Class](https://developers.google.com/edu/python/)
* [Automate the Boring Stuff with Python](http://automatetheboringstuff.com) (includes video tutorials)
* [Practice Python](http://www.practicepython.org) exercises
* [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Spring 2014 NINJA tutorial: Python exercises](https://docs.google.com/document/d/1k-JU9cPokJ58ur4ubpbhLAxC26aAx9bCUcianobBLFE/edit)

### Python Style Guides

* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
* [GeneFinder in Google Style](https://github.com/sd17fall/GeneFinder/blob/formatted/gene_finder.py) (see how it compares to master [here](https://github.com/sd17fall/GeneFinder/pull/2/files#diff-3941f5c15920a6b919f1db7864a6d2c7))

### Python Packages

* [PyPI Python Package Index](https://pypi.python.org/pypi)
* [Awesome Python](https://github.com/vinta/awesome-python) list of curated Python packages.
* [tqdm](https://pypi.python.org/pypi/tqdm) progress meter

## Atom

### Atom Reference

* [Atom Flight Manual](http://flight-manual.atom.io)
* [Atom Keyboard Shortcuts](https://github.com/nwinkler/atom-keyboard-shortcuts)

### Atom Tips

These have moved to [Atom recipes]({% link pages/recipes.md %}#atom-recipes).

### Atom Packages

[https://teletype.atom.io](Teletype) is like Google Docs for Atom. It enables real-time collaborative editing of a single Python file from two or more computers.

## Command Line

### Bash

* [Linux at Olin](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzZDE1c3ByaW5nfGd4OmMyNzcyOTBjYThlMTM1Mg)

## Git

Also see [Git recipes]({% link pages/recipes.md %}#git-recipes) and [Reading Journal instructions]({% link pages/reading-journal.md %}).

### Git Reference

* [Pro Git](https://git-scm.com/book/en/v2)
* [Great visualization](http://www.ndpsoftware.com/git-cheatsheet.html#loc=workspace;) of basic Git commands for moving source around
* [A Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html)
* GitHub's [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) (PDF)

### Learn Git

* A [fantastic visual introduction](http://pcottle.github.io/learnGitBranching/) to the high-level concepts around Git and branching. If you are at all interested in using branches, this is one is not to be missed.
* [Why is Git so hard?](http://merrigrove.blogspot.com/2014/02/why-heck-is-git-so-hard-places-model-ok.html) (it's not just you!)
* [Try Git](https://try.github.io/)
* [Learn Git Branching](http://learngitbranching.js.org)

#### Git Tutorials From Past Semesters

* [Spring 2014 NINJA tutorial: GitHub Help](https://docs.google.com/document/d/12mYDk2Bto-8a4LEq3tL9gvNO_8uehsyaV5WMg2-WNj4/edit)
* [Spring 2014 NINJA tutorial: Introduction to Version Control](https://docs.google.com/presentation/d/15UsxsUBIDA78iplWfKsX0yZAoYIf5ofpEr7PRUE2Y28/edit#slide=id.p)
* [Spring 2014 NINJA tutorial: Pushing to your GitHub repository](https://docs.google.com/document/d/1faRvcK33bIetPkgBH5Vw3Vlz8vl6jdPFKvtowT6Q1xw/edit)

[Git &amp; GitHub presentation](https://docs.google.com/presentation/d/1NpeHiQKs-y2PKp_XrUgzhSSXXBrhTv5DHU4vjQoF99Y/edit?usp=sharing)
(thanks: Chris)

[One-page cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf) (PDF, thanks: Celine)

### Digging Deeper

* [Git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out)
* [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/)

## Markdown

* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* GitHub's [Markdown Cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf) (PDF)

## Media

### Screen Capture

One of the most impactful ways to show your work in action is to... show your work in action!

For **still images**, there is a Ubuntu built-in tool called [Screenshot](https://help.ubuntu.com/lts/ubuntu-help/screen-shot-record.html) that will allow you to capture the entire screen, one window, or a region you select.

There are many options to **record video of your screen**, but for Ubuntu we recommend you start by trying [Peek](https://github.com/phw/peek). To install:

```
sudo add-apt-repository ppa:peek-developers/stable
sudo apt update
sudo apt install peek
```

Used sparingly this can be a powerful way to quickly show what you've created, but too much can be overwhelming.

![]({% link images/notes/resources/Peek_usage.gif %})

You have two options for recording format:
 - **GIF** - good for short interactions, can be embedded directly in a webpage
 - **MP4** - good for editing together into a longer video, can be uploaded to video sharing services and linked from your webpage

If you saved as a GIF and you need an MP4 to work with video editors like Pitivi, you can use an
[online converter](https://ezgif.com/video-to-gif)
or convert it using ```ffmpeg```:

```bash
ffmpeg -i foo.gif foo.mp4
```


_Troubleshooting:_ If you get the following error message, there is a problem with peek trying to utilize ffmpeg from inside Anaconda (as opposed to the one installed in the system path).

```
Using screen recorder backend ffmpeg
Error: Child process exited with code 1
Recording canceled: Command "ffmpeg -f x11grab -show_region 0 -framerate 10 -video_size 498x256 -i :0+941,643 -filter:v scale=iw/1:-1 -codec:v libvpx-vp9 -lossless 1 -r 10 -y /home/pruvolo/.cache/peek/peek7WRLIZ.webm" failed with status 256 (received signal 0).

Output:
ffmpeg version 3.4 Copyright (c) 2000-2017 the FFmpeg developers  built with gcc 7.2.0 (crosstool-NG 8a21ab48)  configuration: --prefix=/home/pruvolo/anaconda3 --disable-doc --enable-shared --extra-cflags='-fPIC -I/home/pruvolo/anaconda3/include' --extra-cxxflags='=-fPIC' --extra-libs='-L/home/pruvolo/anaconda3/lib -lz' --enable-pic --disable-static --disable-gpl --disable-nonfree --disable-openssl --enable-libvpx --cc=/home/pruvolo/anaconda3/bin/x86_64-conda_cos6-linux-gnu-cc --cxx=/home/pruvolo/anaconda3/bin/x86_64-conda_cos6-linux-gnu-c++ --enable-libopus  libavutil      55. 78.100 / 55. 78.100  libavcodec     57.107.100 / 57.107.100  libavformat    57. 83.100 / 57. 83.100  libavdevice    57. 10.100 / 57. 10.100  libavfilter     6.107.100 /  6.107.100  libswscale      4.  8.100 /  4.  8.100  libswresample   2.  9.100 /  2.  9.100Unrecognized option 'show_region'.Error splitting the argument list: Option not found
```

To fix this, simply run this command from your terminal.
``` bash
PATH=/usr/bin:$PATH peek
```

### Demo Videos

As part of your final project, your team will create a short demo video.
There are two main routes you can take to create this presentation:
 - video with audio narration
 - "silent film" with title cards and/or text overlay explanations

#### Silent film option

From your storyboard, combine a series of still images and/or short GIF clips into a longer animated GIF. There are many tools you can use to do the stitching, but we recommend [EZGIF](https://ezgif.com/maker), which can both create and edit GIFs including overlaying text. 

Note that your "silent film" doesn't need to remain silent. You can create an animation using this method, then convert to MP4 video and overlay an audio track following the directions below.


#### Video option

There are also a huge variety of options for video production, but for this class we recommend the instructions for creating an [Ubuntu screen cast](https://wiki.ubuntu.com/ScreencastTeam/RecordingScreencasts) (you can ignore the part about creating a virtual machine) using [Pitivi](http://www.pitivi.org/). Note that you can also use this flow to create a "silent film" with a bit more control.

#### Recording audio

Since it's difficult to get a demo and your narration right at the same time, we recommend that you first create your video, then record an audio voiceover using [Audacity](https://www.audacityteam.org/), and finally compose the two using Pitivi.

Find a quiet place to record your audio. We also have quality studio microphones you can check out rather than using your laptop's microphone.

If you'd like to include a "talking head" video clip of your team members, you can record it using the built-in Ubuntu webcam app called Cheese.

If you choose to use background music (by no means necessary), make sure you select options which are [licensed appropriately](http://freemusicarchive.org/curator/Video/).


#### Generating title slides and text overlays

Regardless of what implementation technology you use, you will likely want title cards, transitions, and credits (don't forget to add your names and give credit to resources you use). There are many options to generate these still images, including:

 - Use a photo editor to add text overlays to screenshots
 - Use presentation software (e.g. Google Slides) and download the slide as an image
 - Screenshot from a presentation
 - Use magic markers and scan it in
 - For GIFs, you can [add subtitles with EZGIF](https://ezgif.com/add-text)



## Jupyter

* [How to use Jupyter Notebooks](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook##UseJupyter)
* [Jupyter Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/) (compact)
* [Jupyter Keyboard Shortcuts](https://gist.github.com/kidpixo/f4318f8c8143adee5b40) (longer)
* [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

## UML Diagrams

### Diagram Types

There are a number of types of UML diagrams. For this class, the most useful are:

*  A [Class Diagram](https://en.wikipedia.org/wiki/Class_diagram) describes the responsibilities of and relationships between the classes in a system.
*  An [Object Diagram](https://www.tutorialspoint.com/uml/uml_object_diagram.htm) shows the relationship between objects (instances of classes). (The relationship between a class diagram and an object diagram is the “noun” version of the relationship between a static call graph and a dynamic call graph.)
*  A [Sequence Diagram](https://en.wikipedia.org/wiki/Sequence_diagram) shows how objects operate with each other. You can use it to show function (including method) calls and returns between two or more objects. You can also use it to show the flow of actions and responses between a user and the system.

Depending on your project, these may also be helpful:

* A [State Diagram](https://en.wikipedia.org/wiki/UML_state_machine) depicts the different states that a system can be in. In this class, it is most useful to describe interactive programs, where a game might be displaying one of several screens. Sometimes it is useful to create state diagrams for individual objects within a program, rather than one diagram for the entire program state.
* A [Use Case diagram](https://en.wikipedia.org/wiki/Use_case_diagram) represents the relationship between the user and the system. In a complex system that is defined UOCD-style, starting from use cases, this kind of diagram can be helpful in collecting use cases and starting to translate them into system structure and behavior.

### Diagram Type Directories

These online references variously include examples, text descriptions, and discussions of when to use each one.

* [Wikipedia page on UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language#Diagrams)
* [TutorialsPoint UML Tutorial](https://www.tutorialspoint.com/uml/uml_standard_diagrams.htm)
* [Lucidchart “What is UML”](https://www.lucidchart.com/pages/what-is-UML-unified-modeling-language )
* [ConceptDraw Guide](http://www.conceptdraw.com/How-To-Guide/uml-diagrams)

*UML Distilled*, by Martin Fowler, is more involved reference that also has a lot of good material for how to think about programming in general. It's [available at the Olin Library](https://olin.tind.io/record/133644?ln=en).

### Making Diagrams

#### Drawing by Hand

Any of the Olin printer/scanners can mail a scan to you. For a diagram, taking a photo from a recent phone will probably work just as well.

#### Slide Tools

For simple diagrams, you can get by with the draw tools in PowerPoint, Keynote, or Google Slides.

#### Diagramming Software

 * Gliffy and LucidChart are cloud-based collaborative diagram editors. Gliffy is free for students. (I don’t know whether the collaborative features are free.)
 * There’s a variety of free / open source draw programs, and also UML-specific drawing programs, mostly written in Java; I’m not familiar with that world.

#### Text-based diagram tools.

[PlantUML](http://plantuml.com) produces an image from a text description. It can create a variety of different kinds of diagrams, shown on its home page.

[Mermaid](https://mermaidjs.github.io) is (IMO) easier to install and use, and produces several useful diagram types, but *not* class diagrams.

There are Atom plugins for PlantUML and Mermaid, that display the image in one pane while you edit the text in another. I’ve used the Mermaid plugin.

[GraphViz](http://graphviz.org) is a general-purpose text-to-graph program. It’s not specific to, and doesn’t know about, class diagrams or UML, but can be used for this. It’s a useful tool to have in your toolbox.

#### “Reverse-Engineering” Tools

These are tools that create UML diagrams from Python sources.

The [PyCharm](http://jetbrains.com/pycharm) Python IDE (Integrated Development Environment) has this feature. I’ve heard that quite a few students in the Olin community use PyCharm; I don’t know that any use this feature.

Standalone tools include [Epydoc](http://epydoc.sourceforge.net), [Pyreverse](https://www.logilab.org/blogentry/6883), and Allen's own [Lumpy](http://www.greenteapress.com/thinkpython/swampy/lumpy.html). A longer list is [here](https://modeling-languages.com/uml-tools/#UML_tools_for_Python).

These appealing, but I’ve found it more helpfully for understanding a pile of code that has been left, without adequate docs, or your doorstep, than for designing of documenting your own code. Done properly, a diagram is expressive and reflects intent: how you position elements, what you leave out, focus on and emphasize different elements in your design. Just as writing prose documentation for your code can lead you to realize how you *should* have written it (and cause you to go back and revise it, if you’ve got time), the process of creating a diagrams can help you design your system. Tools that run on code that’s already written, and make diagrams mechanically, don’t come out as well, and deprive you of those benefits.
