---
layout: post
title:  "Google Foobar Challenge 1: Adding Digits"
date:   2014-11-17 20:01:33
categories:
---

I saw that someone posted a link to [Google Foobar](http://www.google.com/foobar) on [Hacker News](https://news.ycombinator.com/) and my curiosity was immediately piqued. Since I have a lot of time on my hands now that I have quit Microsoft, and want to hone my coding skills, it seemed like the perfect thing to try.

If you don't know what Foobar is, that makes two of us, because even after completing two coding challenges on the site, I still don't know what it's for. What I do know is this:

* If you google a bunch of coding terms, e.g. "python for loop syntax" and have search history turned on, Google will display a banner that invites you to join Foobar.

* When you join, you are provided with a web interface that provides a simple Unix-esque command line and a text editor:
![Google Foobar ](/images/googlefoobar.png)

* You can request coding challenges by typing "request" into the command line.  You have a few days to complete each challenge.

I assume that this is some sort of recruitment tool for Google, but as far as I can tell, they haven't mentioned it formally in any public statements (other than [a cryptic response sent to Business Insider](http://www.businessinsider.com/google-hiring-developers-foobar-challenge-2014-11)).

You can solve the challenges in either Java or Python, and I chose Python because I figured it would be less verbose for simple challenges like these.  I've posted my answers online, in [this Github repo](https://github.com/mrjohnmorrow/googlefoobar).

# The First Challenge

The first challenge I received was called "guard_game".  I am not going to reproduce the text of the challenge here, both because I don't think I have permission to and because it is unecessary.  The challenge was simple - write a function that turns an integer into a single digit by recursively adding the digits comprising it. E.g. `123 -> 1 + 2 + 3 = 6` or `1235 -> 1 + 2 + 3 + 5 = 11 -> 1 + 1 = 2`


I was given two days to complete the challenge, which only took a few minutes. I first started to trying to use integer division and the modulo operator to try to peel of each digit one at a time, but it quickly became evident that the best solution involved simple string manipulation.  

{%highlight python%}
def answer(x):
    sum = 0
    xstr = str(x)
    for c in list(xstr):
        sum += int(c)
    if sum < 10:
        return sum
    else:
        return answer(sum)
{%endhighlight python%}

I submitted my answer, Google accepted my solution, and told me I had completed "Level 1" of Foobar. I typed "request" and received [my next challenge]({% post_url 2014-11-17-google-foobar-2 %}).
