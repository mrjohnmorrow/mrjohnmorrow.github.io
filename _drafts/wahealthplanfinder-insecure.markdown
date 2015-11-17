---
layout: post
title:  "Washington Health Plan Finder Security Issues"
date:   2015-11-15 08:19:33
categories:
---

WARNING: If you  have an account on [Washington Health Plan Finder](https://www.wahealthplanfinder.org/) you need to immediately go and change your security questions to avoid exposing your Social Security Number to attackers:

* Go to [https://www.wahealthplanfinder.org/](https://www.wahealthplanfinder.org/)
* Sign-in via the button in the upper right corner
* Once you are signed-in, click "Change Account Settings" under "Quick Links"
* Click "Update Security Questions"
* Use long, secure passwords for each answer, and save your settings. That's right, don't answer the questions - use long secure passwords as the answer.

I contacted Washington Health Plan Finder via phone and email on November 14th. They said they would get back to me in 3-5 days. I have continued to contact them to no avail. It is at this point I figured that it would be better to let people know how to protect themselves then to continue pursuing a solution with them.

### What is Washington Health Plan Finder?

 Washington Health Plan Finder is the healthcare exchange used by Washington State residents.  With [over 1.7 million people](http://www.medicaid.gov/medicaid-chip-program-information/by-state/washington.html) in the state enrolled in Medicaid alone, this site is used by people all over the state to manage their healthcare and information.

### What is wrong with the website?

The website does two very problematic things:

1. Allows a user to reset their password with only the answer to one security question
2. Displays users' SSNs to them in plain text on the site

**This means that anyone who can guess ONE of your security questions can steal your SSN.**

By allowing you to reset your password in this manner, it is equivalent to having your security question *be* your password. Allowing malicious attackers to access your health care information is bad enough, but by exposing users to identity theft via their SSNs, Washington Health Plan Finder makes the situation much worse.

This security hole is easy to exploit, and obvious. I would be surprised if people's accounts have not been compromised already.

### How does the "exploit" work?

1. An attacker can start by guessing usernames on the website.  Usernames are a serious of letters and numbers, but I was very quickly able to guess a few for common names in the format "FirstnameLastname1", which is what mine was (johnmorrow1).

2. You then are taken to a password reset screen.  Here, you are only prompted to answer ONE security question. If you get it right, you are allowed to reset the password. Let's look at the questions they offer: ![Security Questions](/images/securityques.png) Many of these would be easy to guess with only a few tries for even someone who knew nothing about you at all. My security question was "What was the make of your first car?" With only a few guesses you could access most of the accounts with that question. My answer "ford", could easily be the same as 10% of other users. Again, *this is all an attacker needs to access your account*.

3. Once you have reset the password, you have access to the account. This is bad, but it is made worse by how easily an attacker with access to your account can see your SSN. At this time of the year, the website prompts you to "Complete Your Application" for your 2016 health insurance. When you click on this link, it takes you to a screen to shows you all of your personal data in case any of it is incorrect. This includes your entire SSN, with none of it obfuscated with asterisks. ![SSN is one click away](/images/completeapp.png)

On top of this, there doesn't seem to be anything stopping someone finding a list of usernames from the password reset page (which allows you to check if a username is valid over and over again). Once a attacker has a valid username, there again doesn't seem to be a restriction on how many times you can guess at a security question. I wrote a script using [Selenium WebDriver](http://www.seleniumhq.org/projects/webdriver/) which would try a new answer to the security question (for my own account, of course) every 10s or so, and it was not rate-limited by the website.

### If I update my security questions, am I safe?

I am not a security expert and I was easily able to find this problem the second time I ever used the website. I didn't look further for other issues, but with an issue as obvious as this, it is likely there are other security problems. It is clear that the people who made the site did not follow best practices and that the there hasn't been a real review of the security by a competent auditor. I will continue to try to contact Washington Health Plan Finder technical support  to find someone that will help escalate this issue. If you have an account on Washington Health Plan Finder, I encourage you to do the same:

*  Call them at 1-855-WAFINDER (1-855-923-4633)
*  Email them at customersupport@wahbexchange.org

Changing your security questions is definitely the least you can do to stop attackers from accessing your account. However, without Washington Health Plan Finder fixing the issues with their site, your data is likely still at risk.
