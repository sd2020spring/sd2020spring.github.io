---
title: Final Project
date: 2019-03-29 0:00:00 -04:00
description: |
  From now until the end of the semester you will be working with a team
  of students on a group software project. The project will culminate during the Final
  Event period for this class,  with an EXPO style demo / poster session.
Xannounce: 2019-03-29 10:50:00 -04:00
due: 2019-05-07 12:00:00 -04:00
proposal_survey_url: 
spreadsheet_url: 
parts:
- name: Registration Surveys
  due: 2019-03-29 17:00:00 -04:00
  tag: registration-surveys
- name: Project Proposal
  due: 2019-04-03 10:50:00 -04:00
  tag: project-proposal
- name: AR Preparation Document
  due: 2019-04-12 10:50:00 -04:00
  tag: architectural-review
- name: AR Reflection Document
  due: 2019-04-13 10:50:00 -04:00
  tag: architectural-review
- name: Project Website MVP
  due: 2019-04-30 17:00:00 -04:00
  tag: project-website-mvp
- name: Project Website, feedback addressed
  due: 2019-05-03 12:30:00 -04:00
  tag: project-website-final
- name: Demo Video
  due: 2019-05-06 22:00:00 -04:00
  tag: demo-session-video
- name: Code Submission
  due: 2019-05-07 12:00:00 -04:00
  tag: code-submission 
type: index
registration_surveys_part: 0
proposal_part: 1
arch_review_part: 2
website_part: 4
website_revision: 5
video_part: 6
code_part: 7
expo_part: 7
final_deliverables_part: 7
---

{% include toc %}

## Overview

From now until the end of the semester you will be working with a team of
students on a group software project. The project will culminate during the
Final Event period for this class, with an EXPO style demo session.

## Project Topic

### Requirements

* As this class is called "Software Design", your project should have a substantial software design component (interfacing with mechanical or electrical systems is considered on a case by case basis, but the software should be the major component).
* Most of the your final project should be written in Python. It is okay if some amount is written in another language, but the bulk of the project should be implemented in Python. Part of the reason for this requirement is to facilitate peer design reviews.
* You will create a Software Impact Statement that illustrates your reflection on the ethical considerations you made throughout the design process, starting with project ideation and the priorities you set for your team.

### Suggestions for Project Topics

* Because the theme of this course is "computation as applied to interesting problems in science, engineering, and beyond" you may want to use this project as an opportunity to explore how computation can be applied to a discipline / problem you care deeply about. Choosing an interdisciplinary project may also allow your software design project to overlap with work you are doing in other courses (we are fine with this, but we would have to check with the other instructors to make sure this is okay). If you choose to be interdisciplinary, perhaps we can recruit an appropriate faculty angel adviser for your project.
* If you want to have some experience doing a project "for" a client, talk to faculty and staff on campus. Talk to parents and relatives with real jobs. They may have a need that your team can help with.
* Make a positive difference in the world. See broken things and try to fix them.
* A good project is one that meets your learning goals. For instance, if it is really important to you to learn how to create a program with a GUI, you should make sure that your project topic aligns with this learning goal.
* A good project is one that has a realistic and well-defined minimum deliverable as well as many opportunities for going beyond the minimum deliverable (depending on the pace and enthusiasm of the team).

## Teaming

### Requirements

* You will work on a team of 3-4 students. Instructors will help facilitate teaming and form final teams

### Team Formation Advice

* Try to **work with people because you share a common interest** rather than simply working with your friends (we will offer guidance during the final project kick-off).
* **Work with people that want to devote similar amounts of time to the project.** For instance, if you want to devote your life to making the best most awesomest SoftDes project ever, you should probably work with other people who share that desire!
* **Work with people that envision a similar style of work on the project.** For instance, if you really want to pair-program the entire project, but your teammates prefer to divvy up the work and work independently, that may be a less effective collaboration.

Refer back to the answers you provided during the reflection and teaming surveys throughout the semester and share your thoughts with potential teammates.

## Project Activities / Deliverables

### Registration Surveys
_Due {{ page.parts[page.registration_surveys_part].due | date: site.part_due_date_format }}_

In class we will have a guided activity for identifying your personal learning goals and generating project ideas.
As part of this exercise you will fill out two surveys, which the faculty will use to help form final teams.

### Project Proposal

_Due {{ page.parts[page.proposal_part].due | date: site.part_due_date_format }}_

**The project proposal is worth 10% of the project grade ([rubric]({% link _assignments/final-project/project-proposal-rubric.md %})).**

<!--
Create your GitHub repository by accepting the [GitHub classroom assignment]({{ site.data.github.finalproject_invite }}) and adding all team members to the repository.
You will be using this repository to turn in all of the project deliverables listed below.
-->

Create a document that answers the following questions. More detailed answers give us an ability to give you better feedback to start the project (or revise your proposal).

1. **The Big Idea:** What is the main idea of your project? What topics will you explore and what will you generate? What is your **minimum viable product**? What is a **stretch goal**?
2. **Learning Goals:** What are your individual learning goals for this project?
3. **Implementation Plan:** This will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don't have any idea how you will implement your project, provide a rough plan for how you will determine this information.
4. **Project schedule:** You have 6 weeks (roughly) to finish the project. Sketch out a rough schedule for completing the project. Depending on your project, you may be able to do this in great specificity or you may only be able to give a broad outline. Additionally, longer projects come with increased uncertainty, and this schedule will likely need to be refined along the way.
5. **Collaboration plan:** How do you plan to collaborate with your teammates on this project? Will you split tasks up, complete them independently, and then integrate? Will you pair program the entire thing? Make sure to articulate your plan for successfully working together as a team. This might also include information about any software development methodologies you plan to use (e.g. [agile development](http://en.wikipedia.org/wiki/Agile_software_development)). Make sure to make clear why you are choosing this particular organizational structure.
6. **Risks:** What do you view as the biggest risks to the success of this project? Since you've identified them, how will you mitigate them? How would you describe the ethical risks of a fully realized version of your project?
7. **Additional Course Content:** What are some topics that we might cover in class that you think would be especially helpful for your project?

Please do not just paste in these questions and answer them (you’re better than that). Instead, use them as guidelines to check for completeness as you draft a cohesive proposal document.

The teaching team will either approve your proposal, or provide suggestions and request revisions.

### Architectural Review

_First Review Date: {{ page.parts[page.arch_review_part].due | date: '%A, %B %-d' }}_

**The Architectural reviews are worth 15% of the project grade ([rubric]({% link _assignments/final-project/architectural-review.md %})).**

Each team will complete two architectural reviews, which will entail teams presenting plans for their project to other teams, NINJAs, and instructors.
These reviews are intended to be interactive, and will focus on soliciting useful/actionable feedback rather than being a one-way brain dump.
In addition to the in-person component of this activity, there will be a
framing/agenda setting document due before the review and a
reflection/synthesis document due after.

See the [Architectural Review]({% link _assignments/final-project/architectural-review.md %}) page for full details about the assignment.


### Project Website

{% assign part = page.parts[page.website_part] %}
_Due: {{ part.due | date: '%-I:%M %p %A, %B %-d' }}._

_Final revision, that incorporates instructor feedback, due {{ page.parts[page.website_revision].due | date: '%-I:%M %p %A, %B %-d' }}._

**The final website is worth 25% of the project grade**

Your project website is the lasting record of what you have accomplished over
the course of this project, and hopefully a valuable contribution to your
professional portfolio. You should draw upon all the deliverables and
activities above to create the final site, combining, reformatting, and adding
to them to effectively tell the story of your project.

The project website can serve many audiences, including:

* Current and future SoftDes students and faculty
* Potential users of your software and those with a domain-specific interest in your topic
* Future employers
* Final event audience, broader Olin community, family

There are many successful formats for a project website, but you should
consider including:

* **Big Idea/Goal/What is this?/** **Why did we do this?**
Quick and easily understandable explanation of what your project is all about.
Consider including a narrative or example use case, e.g. via screenshots,
video, or story boarding.

* **User instructions/README**
Information to help users download, install, and get started running your
software ([README rubric]({% link _assignments/final-project/readme-rubric.md %}))

* **Implementation information**
Code doesn't tell a story by itself. Use more effective methods such as
flowcharts and architectural, class, or sequence diagrams to explain how your
code works. You could consider including or linking to snippets of code to
highlight a particularly crucial segment.

* **Results**
Though the details will be different for each project, show off what your
software can do! Screenshots and video are likely helpful. Include graphs or
other data if appropriate.

* **Software Impact Statement**
Reflect on the ethical considerations you made throughout the design process, starting with project ideation and the priorities you set for your team. You should think of all of the stakeholders that might be impacted by your project and unintended consequences of the deployment of your software in real world scenarios. Discuss strategies for mitigating these issues.

* **Project evolution/narrative**
Tell an illustrative story about the process of creating your software,
showing how it improved over time. This may draw upon what you learned from
the two peer technical reviews and from the code review. Consider the use of
screenshots or other tools to demonstrate how your project evolved.

* **Attribution**
Give proper credit for external resources used.

**_Note_**: These content prompts exist to inspire your thinking, and you should use whatever organization and sections make sense for your project and the story you're telling. Simply answering the given prompts sequentially is not the strongest way to communicate your work to an external audience. Think about what you've accomplished and frame it nicely - finish strong!

Your final project website will be implemented using 
[GitHub pages](https://pages.github.com/),
possibly along with [Jekyll](http://jekyllrb.com/docs/github-pages/) (as we do for the course website).
If you have a compelling reason you need to use a different platform, please discuss with course staff.

<!-- If you'd like to make a GitHub site with multiple pages using Markdown,
former SoftDes NINJAs Patrick and Franton have written a [helpful
guide](http://phuston.github.io/patrickandfrantonarethebestninjas/howto). -->

You **must** include a link to your
project website from your GitHub repository.

**Submission mechanics**: Your project's GitHub repo page should link to your web site. This means either the README, or the Website that is optionally displayed in the upper right corner of your GitHub repo page, should contain this link.

### Demo Session Video and Poster

{% assign part = page.parts[page.video_part] %}
_Completed and shared before {{ part.due | date: '%-H:%M %p' }} on {{ part.due | date: '%A, %B %-d' }}_

**The project video and poster are worth 10% of the project grade.**

Each team will create a short (1-2 minute) video giving a pitch for your project and demonstrating its functionality.
Consider including the project's goal, what the software does, how to use it, why your team made it, and what you would do if you had more time.

The teaching team will offer suggestions and give feedback on draft videos related to production quality and content.

Each team will also generate an informational poster about your project following the template provided by course staff.

**Submission mechanics**: 
Submit a link to your demo video on Canvas.
Your demo video must be completed and shared in time to present at the final event.
Your project README or project web site should also link to your video. Please **do not** host large binary files like your video in your GitHub repo; ask the teaching team if you need help with alternatives.

### Code submission

{% assign part = page.parts[page.code_part] %}
_Due: {{ part.due | date: '%A, %B %-d' }}_

**Project code is worth 40% of the project grade (see code rubric on the [course policy page]({% link pages/policies.md %}))**

Project code must be submitted via GitHub by {{ part.due | date: '%B %-d' }}. You must include a
README describing how to run your code, including any required dependencies
(e.g. libraries to install) and any input files ([README rubric]({% link _assignments/final-project/readme-rubric.md %})).

Proper documentation is important to your final submission, and one way to
ensure you have adequate docstrings is to generate documentation from them.
You can do this using [pydoc](https://docs.python.org/3/library/pydoc.html):

`$ pydoc path/to/my_project.py`

This will open a help file based on your docstrings (use q to quit). Make sure
the help file would be useful to someone using your code, and feel free to
attach it to your code submission as an appendix. If you want to generate
truly beautiful documentation, check out [Sphinx](http://sphinx-doc.org/) (the
tool used to generate the [Python documentation](https://docs.python.org/3/)).

Make sure that your code gives appropriate attribution to external resources
used, as per the [course policy page]({% link pages/policies.md %}). If you have any questions
about this, just ask.

**Submission mechanics**: Push your work to GitHub, and verify that all your final changes are reflected on github.com. Submit a link to your work on Canvas.

### Final Demo / Presentation Session

{% assign part = page.parts[page.expo_part] %}
_Date: {% if part.due %}{{ part.due | date: '%A, %b %-d, %-H:%M %p' }}{% else %}TBD{% endif %}_

During the Final Event, {% if site.sections > 1 %} all studios of {% endif %}
SoftDes will meet {{ site.final_room_number }}
for an EXPO style poster/demo session of your final projects. This session is
for everyone to share what they've created, and will not be evaluated. We will
be inviting other members of the Olin community to check out your fantastic
work.
