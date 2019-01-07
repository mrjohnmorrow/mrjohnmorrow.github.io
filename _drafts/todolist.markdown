---
layout: post
title:  "Automatically printing your to-do list every day"
date:   2019-01-06 08:19:33
categories:
---

For a long time I have used hand written to-do lists as a form of daily task tracking. As task management software has gotten better, the inconvenience of the paper list (copying it, losing it, etc.) has made even a luddite like myself ditch it.  I have been using Trello for a few years now and it's been great. However every time I have to futz with my phone to update the list, I long for the good ol' days when I could mark my progress with the swift and satisfying swipe of a sharpie. After hearing about the [Memobird printer](https://amzn.to/2RxkUt5), I figured I could maybe use it to automatically print out my To-do list everyday, so I'd have the best of both worlds.

It turns out the Memobird's API is [still in a private beta](/images/memobirdapi.png) for now, but they do have an [IFTTT service](https://ifttt.com/memobird). This, plus a few other automation tools, is all we need to make this happen. Here's what I did:

* Set up an IFTTT applet with a webhook that printed the payload on the memobird
* Wrote an AWS Lambda endpoint to pull my to-do  list from Trello, format it, and send it to this webhook
* Set up a Zapier "zap" to spin up the Lambda endpoint every day at  8am

# IFTTT configuration

* Create a [new applet](https://ifttt.com/create) and add "Webhooks" as the "this" step
* There should only be one option for trigger, "Receive a web request"
* You then just set the event name to whatever you like, I chose todo_print (anything in snake case is fine)
* Set the "that" step to "Print a message to a memobird service", using the 16-digit hex code ID for your device as the argument for the "Which memobird device?" parameter
* Set the "What message to print?" parameter to ` {{OccurredAt}} {{Value1}}`
* Look up your key [URL here](https://ifttt.com/services/maker_webhooks/settings), where your key is in your URL after use/

![](/images/iftttconfig.png)

You can then test this on your printer with a simple curl command,:

```
curl -X POST "https://maker.ifttt.com/trigger/todo_ready/with/key/{your key}?value1=<html><body><br>test+test2</body></html>"
```

# AWS Lambda

I'm gunna assume you haven't set up Lambda before

* Create a new AWS Lambda function [here](https://us-west-2.console.aws.amazon.com/lambda/home)
* After you click create, you'll choose "Author from scratch"
* Select a name ("getTodoListAndPost"), set the runtime to Python 2, and create a new role with the template "Simple microservice permissions"
![](/images/lambdasetup.png)
* set up the api gateway
* look up the list ID on trello (go to board, menu, more, print and export, export as json)
* in the json, search for "Today" or whatever your "Doing" list is called and copy the adjacent ID
* add your list ID, your key-token pair for trello, and your key for the maker API

![](/images/trellojson.png)

![](/images/trellojsonid.png)

* add the code [here](tbd) in your `lambda_handler`
* Test, using any input ( I used the "Hello World!" sample event)
* publish
* once you've published, add an API Gateway trigger

![](/images/gatewaytrigger.png)

I've shown my settings here configured, but you might need to create the API endpoint, which should be straightforward enough.

* test your API gateway trigger with a curl command e.g.

```
curl -X GET "https://ijmtjfn8f0.execute-api.us-west-2.amazonaws.com/default/getTodolistAndSendToIFTTT?key=f****************************"
```

You can get the URL from the Lambda interface:

![](/images/gatewaytrigger.png)

# Adding the chron job

Once Lambda is set up, you can just create a simple Zap in Zapier to hit it everyday. You might be wondering, couldn't I also do this in IFTTT? The answer is, of course, but I've found Zapier to be a bit more reliable than IFTTT and has better error messages.

* Create a new Zap whose trigger is "Schedule", and select "Every Day" and the time you wake up
* Add the action "POST" from "Webhooks by Zapier"
* Add the URL you tested in the last step, with your API key from your API Gateway configuration


![](/images/zapiersetup.png)
