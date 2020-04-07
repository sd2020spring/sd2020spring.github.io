---
title: Architectural Review
parent: final-project
---

{% include toc %}

## Updates for Spring 2020

This content has been updated as best we could to incorporate needed adjustments for virtual instruction.


## Overview

During the course of the final project, your team will complete an Architectural
Peer Review. This review will focus on high-level design decisions, and will give your team an
opportunity to present ideas of how the architecture of the code will be.

**What it is**

* Two-way conversation between your team and the other people at your review
  * for Spring 2020 this will be instructors and course assistants
    * if you'd like other classmates to attend, feel free to tell us names
* Forward-looking and focused around a design decision that you are in the process of making
* Opportunity to get constructive feedback and outside perspectives on challenges you are currently facing

**What it isn't**

* Highly polished final presentation of your work (that comes later)
* One-way presentation

For more tips and guidelines, check out one version of the [information on SCOPE Technical
Reviews]({% link files/final-project/Technical_Review_Deliverable_and_Rubric.pdf %})
given to SCOPE students in recent years.

## Before the Architectural Review

The core of the architectural review is a constructive discussion between the
presenting team and the audience/reviewers. In order to get the most out of this
conversation, you must prepare a Preparation and Framing document ahead of
time.

You should identify concrete things that you want to get from your audience
and make sure that you structure your review to elicit the information that you are
looking for. Your technical review should **always** start with a discussion
of what you hope to get out of it.

There are many potential structures you can use for a review, and the structure you choose should be appropriate to where we are in our project cycle. Below is a list of examples, some of which are appropriate for an early stage architectural review and some of which are more appropriate for late stage architectural reviews:

* **Risk identification and mitigation** (appropriate for early stage): early in this project we ask you to identify the biggest outstanding questions / risks / unknowns that you have regarding your final project. Doing this early in your project cycle is invaluable for helping you to appropriately scope your project, determine your system architecture, and assign tasks to individual team members. A very efficient use of an early stage architectural review is to pose these questions / risks to your reviewers, to make sure that you have both identified the right ones and to make sure that you collect as many good ideas for how to address these questions as possible. For the first AR, we want everyone to structure their review towards getting input in this area (among others).
* **Software architecture discussion** (appropriate for early stage): discuss some aspect of your software architecture (_e.g._ how you are structuring the various classes that make up your program). Present a particularly difficult aspect of your software architecture, and ask the reviewers if they have any advice/feedback.
* **Technical discussion** (typically appropriate for later stages, unless building upon previous work): if this type of information is available during the AR, you can introduce it. If not, there will be a code review later in the project. Bring some particularly difficult technical problem to either review (_e.g._ choosing the right algorithm to solve some problem). Discuss potential solutions and pros and cons. Ask the reviewers which solution sounds best and whether there are other potential solutions that you should consider.
* **Prototype feedback** (appropriate for later stage): have the reviewers use a prototype of your software (make sure to provide laptops with the software ready to go if needed, or a README that outlines required environments) and give you feedback on your interface and features.
* Alternatively, you can use a combination of the above, or something else entirely.

Your Preparation and Framing document should have (at least) the following
sections:

1. **Background and context** What information about your project does the audience need to participate fully in the  review? You should share enough to make sure that your audience understands the questions you are asking, but without going into unnecessary detail.
2. **Key questions** What do you want to learn from the review? What are the most important decisions your team is currently contemplating? Where might an outside perspective be most helpful? As you select key questions to ask during the review, bear in mind both the time limitations and background of your audience.
3. **Agenda for technical review session** Be specific about how you plan to use your allotted time. What strategies will you use to communicate with your audience?
4. ONLY IF YOU ARE PRESENTING FACE TO FACE WITH REVIEWERS OR WITH A LARGER  **Feedback form** Create a Google form that folks in the review will use to provide you with feedback or answers to various questions you pose to your audience.  The time you have to present is relatively short. You should expect much of the feedback you get to come from this form rather than thoughts expressed orally during your session. Please create a feedback form tailored for your architectural review and share the link no less than 2 hours before class.

The Preparation and Framing document must be submitted before the review takes
place. Instructors will review it prior to joining your session. You should also post any additional materials (e.g. slides, handouts, Google forms) that you use during the review.

## Day of the Architectural Review

The teaching team provides a google sheet that has the times for reviews. Teams sign up for a time that works for them and report to the class Zoom room prior to that start time. Instructors will take reviewing teams into a breakout room to perform the review, which will be recorded with reviewers permission, for later review. The sessions will be 10 minutes. Instructors will follow up with feedback if time does not permit delivering every comment on our minds. Teams can opt to present in the main Zoom space with other students if they'd appreciate a larger audience.

### Being a good presenter

* Make sure you have a clear agenda. Anything you present should be focused around getting valuable feedback, or else informing some discussion that you hope to have. Do present appropriate context. Don't present unnecessary detail.
* Make sure it is realistic for your audience to give you the type of feedback you are looking for. For instance, if you ask your audience to help you pick the right machine learning algorithm for your project, you should be relatively confident that your audience has the relevant background knowledge to help you with this issue. Avoid asking about things that require intimate knowledge of your codebase (unless you can give appropriate context).
* Make sure to allow adequate time to receive feedback from your audience. Be explicit about when you would like to receive feedback (either at the end or during your presentation).
* Have one member of your team take notes during the technical review.
* Be open-minded to feedback from your audience.
* If you are presenting online, be clear about speaking handoffs, as cues for changing speakers can be are harder to transmit digitally than in person.
* Thank your audience.

### Being a good audience member

* If you are a student invited to hear a peer's review...
* Focus your feedback on what the presenters ask for (_i.e._ if they want feedback on their software architecture, don't tell them you don't like the feature set they are implementing).
* Be respectful and constructive in your feedback.
* Don't be playing on your laptop or phone during the technical review. Focus all attention on the presenters.

## After the Architectural Review

The best advice in the world is useless if you don't do anything with it!
After the review, you must prepare a Reflection and Synthesis
document summarizing what you learned. This document must be submitted before the next class after the
review.

Your Reflection and Synthesis document should have (at least) the following
sections:

1. **Feedback and decisions**
Based upon your notes from the technical review, synthesize the feedback you
received addressing your key questions. How do you plan to incorporate it
going forward? What new questions did you generate?

2. **Review process reflection**
How did the review go? Did you get answers to your key questions? Did you
provide too much/too little context for your audience? Did you stick closely
to your planned agenda, or did you discover new things during the discussion
that made you change your plans? What could you do next time to have an even
more effective technical review?

## Grading rubric

The architectural review is worth 15% of your total project grade. Unless otherwise specified.

### Before: Preparation and Framing

Your team must submit a Preparation and Framing document before the review takes place.

**100%** |

* Document is well organized including all required sections
* Provided background gives sufficient context for audience to engage with questions effectively
* Key questions are selected appropriately for the audience and time limitations
* Clear agenda and plan for the review session are included

---|---

**75%** |

* As above, but perhaps 1-2 of the prompts are not adequately addressed
* Key questions may be either obvious or too vague
* Writing may be less clear, and some key concepts or terms may not be adequately explained

**50%** |  A significant component of the document is missing
**25%** | The document is very unclear and missing multiple key elements
**0%** | You didn't turn in anything, or you clearly didn't put any effort into creating the document

### During: At the review session

You must attend your scheduled technical review session and contribute both as
part of the presenting team and as an audience member. If you will be absent
on the day of the technical review, you must contact the teaching team
beforehand.

**Presenting team**

**100%** |

* Set a clear agenda for the review and share it with the audience
* Provide an appropriate level of context without going into unnecessary detail
* Effectively guide the conversation and solicit contributions from the audience
* Take notes on the discussion

---|---

**50%** |

* Ineffective conversation, due to failure to provide adequate context or poor engagement with audience
* One-way presentation rather than dialog
* Failure to take notes and record audience contributions

**0%** |

* Minimal effort or unexcused absence

**Audience member**

(values below reflect karma points, not SoftDes points)
**100%** |

* Practice active, engaged listening
* Contribute thoughtful questions and comments directed at the presenting group's identified key questions
* Come prepared with background reading (if applicable)

---|---

**50%** |

* Divided attention (laptop use other than research or note-taking)
* Derailing or severely off-topic questions or comments

**0%** |

* Minimal effort or unexcused absence

### After: Reflection and Synthesis

Your team must submit a Reflection and Synthesis document before the next class after the review.

**100%** |

* Document is well organized including all required sections
* Audience feedback is synthesized into a coherent story centered around your key questions
* Includes concrete plan for moving forward incorporating lessons learned from the technical review
* Reflection on review process is thoughtful and contains actionable lessons for next time

---|---

**75%** |

* As above, but perhaps one of the prompts is not adequately addressed
* Audience feedback may be listed, but not processed or synthesized
* Writing may be less clear, and some key concepts or terms may not be adequately explained

**50%** |  A significant component of the document is missing
**25%** | The document is very unclear and missing multiple key elements
**0%** | You didn't turn in anything, or you clearly didn't put any effort into creating the document
