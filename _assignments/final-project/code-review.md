---
title: Code Review
parent: final-project
---

{% include toc %}

For some motivation, please check out this quote:

> I believe that peer code reviews are the single biggest thing you can do to improve your code.
>
>         – Jeff Atwood, Co-Founder of Stack Overflow

_Source: [http://blog.codinghorror.com/code-reviews-just-do-it/](http://blog.codinghorror.com/code-reviews-just-do-it/)_

Code reviews are widely used in industry as a means to improve code quality.  Often, code reviews will be required before finalizing any contributions to a software repository.  For instance, a very common workflow for code reviews is to use Git branches for feature development, which are merged into the master branch only after detailed comments are provided and any issues are resolved.

There are lots of good resources on the nuts and bolts of implementing code reviews in different settings.
Regardless of the technical details of the review, it's important to remember that
[there is a person on the other side of the review](https://mtlynch.io/human-code-reviews-1/), and to approach the exercise with respect and [awareness of your own biases](https://blog.mozilla.org/blog/2018/03/08/gender-bias-code-reviews/).

Software Design instructors are not seeking to find every last tiny error in the code. Rather, we will focus on providing course corrections and high-level feedback that can help you shape your work over the final weeks of the project. As such, we'd like you to engage with the following steps to frame your code review.


**0) Review the Documentation worksheet**:
 - You do not need to do the exercises in the worksheet (unlike the breadth students).
 - Read the best practices outlined [here in the documentation worksheet](https://github.com/sd2020spring/ReadingJournal/blob/master/documentation_worksheet.ipynb)


**1) Prepare your repository for external readers and code review**:

Work through the exercises above to prepare your project repository for the review. You should:
 - *Post project README file*
 - *Update and post system architecture diagram*
 - *Solid documentation throughout*, (see guidelines above) but especially the sections under review.
 - *Check project organization*, make sure your files and folder names are logical, remove dead code (e.g., files or functions are no longer utilized) and non-project junk (e.g. ```.pyc``` files, generated program outputs)


**2) Point us in the right direction**:

Complete the Code Review Framing Canvas assignment so that we can prepare to give you useful feedback.

Some ideas for choosing code sections:
 - code that you have questions about
 - code that you want to show off
 - code that you suspect may be fragile or buggy
 - code that is particularly complicated

Ensure that each code section has sufficient documentation for a reviewer to figure out when it's called, what it does, and how it does it.

To point us to 2-3 specific sections of code. Check out the instructions on the [Recipes page](/resources/recipes/#link-to-a-section-of-code-in-github) to see how to create links to your work on GitHub.
