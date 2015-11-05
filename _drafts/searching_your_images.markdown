---
layout: post
title:  "Searching your pictures"
date:   2015-11-04 22:01:33
categories:
---

I have a Kryptonite bike lock, which I have used extensively for the past 4 years. I even took it to Europe and back when I biked across northern Italy and southern France. One great thing about this type of lock is that if you lose your key, you can order a new one (often for free). All you need is the key number. When I lost the first of my two keys sometime last year, I took a picture of the key so I wouldn't forget the number. However, that picture is buried somewhere in the thousands of photos on my computer. After a few searches through my photos, I was unable to find it. Maybe it's in a folder I didn't look in, or maybe I am just human and skipped over it too quickly. As I was flipping through the photos, the repetitive nature of the task screamed to be automated. So naturally, that is what I tried to do.

But how do you use a computer to recognize a key? I try two simple methods.

## OCR Search

Since what I need is not a key, but the 6 digit number written on the key, I decided to give OCR a shot. There are a few OCR solutions out there, but I decided to go with [tesseract-ocr](https://github.com/tesseract-ocr), since it is [easy to use with Python](https://pypi.python.org/pypi/pytesseract) and worked well in a quick test I did.

# Getting set up

To get started, you will need to install a few packages:

* [leptonica](http://www.leptonica.org/)
* [pytesseract](https://pypi.python.org/pypi/pytesseract)
* [tesseract-ocr](https://github.com/tesseract-ocr)
* [pillow](https://python-pillow.github.io/)

More info on this can be found in [this helpful post](https://realpython.com/blog/python/setting-up-a-simple-ocr-server/). If you have already installed (and have no issues with) [brew](http://brew.sh/) and [pip](https://pypi.python.org/pypi/pip), you should be able to install everything with just the following few commands.

{%highlight bash%}

brew install leptonica
brew install tesseract
sudo pip install pytesseract
sudo pip install tesseract-ocr
sudo pip install pillow

{%endhighlight bash%}

If you are like me, and recently installed OS X Capitan, you will need to fix up your Brew install via `brew update` and `brew prune` (and maybe not just that :/ ).

# Running the Search

It is a bit too long too include inline but the code I used can be found [here](https://github.com/mrjohnmorrow/mrjohnmorrow.github.io/blob/master/code/OCRsearch.py). What I do is:

* Walk the file directory
* Run the OCR on anything that looks like an image (in my case JPG, since iPhone photos are JPGs)
* Stick the file name and OCR output in a CSV
* Scan the CSV manually to see if any of the output text looks to be a 6-digit number. You would think it would be obvious to use a regex here, but that's only if you have seen any raw OCR output before.

It does take a while to run on most computers, about 2-3 seconds a picture on my 2013 Macbook Pro. I just ran it overnight on my Pictures directory and looked at the results in the morning.

# Results

So I was hoping to see something like "634895" or ",234:76" in the output files, and there were actually a few ostensible hits. However, when I looked up the original file, none of them turned out to be the photo I was looking for. A few things that limit this approach:

* OCR is finicky. For instance, if the text is not rotated correctly, you will get wildly different results.  The only solution is to run the search 4 times, for each orientation of the photo. Thankfully, I am confident that the photo in question was rotated correctly.
* OCR likes high contrast text. Actually, I think everyone likes high-contrast text but OCR is lost without sharp features around the letters to help with recognition.
* There is a lot of garbage. I actually considered appending the OCR output as metadata to the files it scans, but once I saw a few samples, I realized how often it detects text when there is none to be found. Here's a sample from a few photos ([Google Sheets](https://docs.google.com/spreadsheets/d/1lJL2Z6UraO_lTDUr01qUozdHhvnLtUhrYu5lqJXot8M/edit?usp=sharing) and [Github](/Users/john/OneDrive/Pictures/2014/12/08/20141208-224117/IMG_2268.JPG)), only one of which had any text in it.  You can see a hopeful "510111" as well as "Sungay November 23", pretty close to the only actual text, from the lock screen of a computer. The "510111" is from a photo of my ex-girlfirend, who is already in a lot of my photos, but was in a disproportionately high number of the possible matches, as if my computer was trying to make me feel bad about keeping it up all night.

## Picture Matching

If I had to solve a simple classification problem such as "is a particular photo of a key?", there are a host of machine learning techniques that could help me do so. A neural net comes to mind first. However, I don't have a large data set with which to train my model, and I could create one with a camera and a similar key, but it would be time consuming. However, taking one photo would be simple.

What I decided to do was to try to recreate the photo, and then compare it to every photo on my computer to see which ones it most resembled. Then, I could search through a manageable subset of my photos - the ones that resembled the recreation - and not the whole lot of them.

## Conclusions

* I have taken an embarassing number of selfies. And not just the "I'd be embarassed if anyone knew how many I took" way, it's embarssing even if no one were to find out, embarassed for myelf at myself. (TODO: fix this up)

sources:
https://docs.python.org/2/library/csv.html
