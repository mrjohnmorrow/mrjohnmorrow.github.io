---
layout: post
title:  "Git for PMs"
date:   2016-09-22 01:01:33
categories:
---

A cute little site ["Oh shit, git!"](http://ohshitgit.com/) came to my attention recently and I found it super useful. However, I haven't been doing a lot of development at work (focusing on uh, my actual job) but I still found myself dusting off the old keyboard from time to time to help make a small change, normally a copy change, etc.  Since I am in and out of Git less frequently, I tend to forget a lot of common commands that are helpful when working with dev to either test changes locally or make small fixes. The Github desktop UI is helpful, but it doesn't cover everything. I figured I put together a list of a few commands I always forget.

# I tried to sync a branch and I got a bunch of weird errors. I just want the latest from the repo and I don't care about my local commits

1. `git checkout master` or select master as your current branch in the UI
2. `git branch -D <branch name>`
3. `git reset --hard HEAD`
4. `git checkout <branch name>` or select <branch name> as your current branch in the UI
5. `git pull` or select "Sync" in the Desktop UI

This is usually something you see after someone else rebases / merges. Normally as a PM, you just want the latest version of a change and don't need to merge old commits you have lying around.

Just one for now but will add more as I think of them. If you have any suggestions, there's a link below to make a PR to this post. 
