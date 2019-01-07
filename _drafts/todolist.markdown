---
layout: post
title:  "Automatically printing your to-do list every day"
date:   2019-01-06 08:19:33
categories:
---

For a long time I have used hand written to-do lists as a form of daily task tracking. As task management software has gotten better, the inconvenience of the paper list (copying it, losing it, etc.) has made even a luddite like myself ditch it.  I have been using Trello for a few years now and it's been great. However every time I have to futz with my phone to update the list, I long for the good ol' days when I could mark my progress with the swift and satisfying swipe of a sharpie. After hearing about the [Memobird printer](https://amzn.to/2RxkUt5), I figured I could maybe use it to automatically print out my To-do list everyday, so I'd have the best of both worlds.

It turns out the Memobird's API is [still in a private beta](/images/memobirdapi.png) for now, but they do have an [IFTTT service](https://ifttt.com/memobird). This, plus a few other automation tools, is all we need to make this happen. I've included instructions below in case other Memobird owners want to give something like this a shot. Here's what I did:

* Set up an IFTTT applet with a webhook that printed the payload on the Memobird
* Wrote an AWS Lambda endpoint to pull my to-do  list from Trello, format it, and send it to this webhook
* Set up a Zapier "zap" to spin up the Lambda endpoint every day at  8am

# IFTTT configuration

* Create a [new applet](https://ifttt.com/create) and add "Webhooks" as the "this" step
* There should only be one option for trigger, "Receive a web request"
* You then just set the event name to whatever you like, I chose todo_print (anything in snake case is fine)
* Set the "that" step to "Print a message to a memobird service", using the 16-digit hex code ID for your device as the argument for the "Which memobird device?" parameter. You can press the button on the printer twice to print out this ID if you don't have it handy
* Set the "What message to print?" parameter to ` {{OccurredAt}} {{Value1}}`
* Look up your key and URL [here](https://ifttt.com/services/maker_webhooks/settings), where your key is in your URL after `use/`

![](/images/iftttconfig.png)

You can then test this on your printer with a simple curl command,:

```
curl -X POST "https://maker.ifttt.com/trigger/todo_print/with/key/{your key}?value1=<html><body><br>test+test2</body></html>"
```

# AWS Lambda

So it's entirely possible to set this up using just Zapier and IFTTT, if you use a multistep zap on Zapier and their Trello integration. However, you need to buy the paid tier and it starts at $250 a year, hence Lambda. I was looking at the limits on the AWS free tier and unless you had a *very* long to-do list, it's nigh impossible to exceed them with this simple function.

* Create a new AWS Lambda function [here](https://us-west-2.console.aws.amazon.com/lambda/home)
* After you click create, you'll choose "Author from scratch"
* Select a name ("getTodoListAndPost"), set the runtime to Python 2, and create a new role with the template "Simple microservice permissions"
![](/images/lambdasetup.png)

You'll also need to grab some info from Trello so you can point your Lambda function to the right list:
* Look up the list ID on Trello (go to board, menu, more, print and export, export as json)
![](/images/trellojson.png)
* In the json, search for "Today" or whatever your "Doing" list is called and copy the adjacent ID
![](/images/trellojsonid.png)
* Add your list ID, your key-token pair for trello, and your key for the maker API to the environment variables on Lambda
* Add the code [here](/code/lambda_handler.py) in your `lambda_handler`
* Test, using any input ( I used the "Hello World!" sample event). This should print your to-do list on the printer successfully at this point
* Publish your Lambda function

So now that you have your Lambda function all set up, you need to set up a way to tell it when to execute. We'll use an API Gateway to do this.
* On the page where you added the code to your Lambda function, click on "API Gateway" under "Triggers" to begin API Gateway setup
![](/images/gatewaytrigger.png)

I've shown my settings here configured, but you might need to create the API endpoint, which should be straightforward enough.

* Test your API gateway trigger with a curl command e.g.

```
curl -X GET "https://ijmtjfn8f0.execute-api.us-west-2.amazonaws.com/default/getTodolistAndSendToIFTTT?key=f****************************"
```
You can get the URL from the Lambda interface:

![](/images/apigatewaysetup.png)

# Adding the chron job to Zapier

Once Lambda is set up, you can just create a simple Zap in Zapier to hit it everyday. You might be wondering, couldn't I also do this in IFTTT? The answer is, of course, but I've found Zapier to be a bit more reliable than IFTTT and has better error messages.

* Create a new Zap whose trigger is "Schedule", and select "Every Day" and the time you wake up
* Add the action "POST" from "Webhooks by Zapier"
* Add the URL you tested in the last step, with your API key from your API Gateway configuration


![](/images/zapiersetup.png)
