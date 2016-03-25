---
layout: post
title:  "The Game Theory of Disagreement"
date:   2015-08-25 08:19:33
categories:
---

The Meek Mill and Drake feud is not the only high-profile dispute to echo through the Twitterverse this past summer.  Economist Paul Romer published [a paper](http://paulromer.net/mathiness/) in the American Economic Review that accused a few leading economists of using Math in misleading an unscientific ways.  Romer fired shots at a some big names, including Nobel Prize Winner Robert Lucas and everyone's favorite econometrician, Thomas Piketty. On top of this, he published a series of posts on his [blog](http://paulromer.net/category/blog/) that answered some of the feedback and criticisms the paper had received. In [one of these posts](http://paulromer.net/freshwater-feedback-part-1-everybody-does-it/), he makes an offhand remark that is presents of the most elucidating applications of game theory I have ever encountered.

> One way to characterize the underlying disagreement about what is wrong is to say that we are both commenting on strategic interaction between economists that takes the form of a repeated, multi-player prisoner’s dilemma.

 Romer's application of game theory here shows how people's rational protection of their reputation could result in persisting disagreement.  Romer's posts do a great job of explaining how this applies to economics, but I think it applies in other situations as well. I will present an overview repeated prisoner's dilemma. I will then detail two examples of other situations this applies; climate change and customer data analysis.

## The Repeated Prisoners Dilemma

Before I get into the repeated variant of the prisoners dilemma, I will quickly address the standard version.  Even if you are already familiar, it will be useful to skim it to get on the same page in regards to payout values / prison sentence lengths.

### The Standard Version

The standard Prisoners Dilemma is a "game" that involves two "players", Calvin and Klein (using the names from [1]). Calvin and Klein are two criminals who are accused of being co-conspirators in a crime. They are separately given the option to confess or stay silent. If they both stay silent, they each get one year in jail. If one confesses and the other doesn't, the one who confesses goes free, while the other gets fifteen years. If they both confess (in an effort to receive the reduced sentence) then they both get five years in jail. They are unable to know what the other will do before they have to act themselves.


| -----------------|-|----------------:|-|----------------:|
| Calvin / *Klein* | |*Confess*        | |*Not Confess*    |
| Confess          | |5, *5*           | |  0, *15*        |
| Not Confess      | |15, *0*          | |   1, *1*        |
|                  | |                 | |                 |


Imagine, you are Calvin, and you think Klein is going to confess. Then it is in your best interest to confess too, because your sentence would be reduced from 15 to 5 years. Also, even if you think Klein will not confess, you still should confess, since it will reduce your sentence from 1 to 0 years. You can see that when the players act rationally, they will always end up both confessing. Though [Homo economicus](https://en.wikipedia.org/wiki/Homo_economicus) would clearly always confess, it's hard to say how Homo sapiens would act, though it should be easy to see that both Calvin and Klein are incentivized in a deleterious fashion.

### ... Repeated

If you are to consider a situation where Calvin and Klein were going to play this game (commit this crime) over and over again, you would see that cooperation would be a bit easier. Imagine Calvin says to Klein "I will keep my mouth shut if you do. However, if you confess once, I will confess every time after that and we will both be stuck getting 5 year sentences over and over again." This is called a [grim trigger strategy](https://en.wikipedia.org/wiki/Grim_trigger). The payoff of Klein confessing now also has the long term cost of Calvin confessing in every subsequent game. This means that Klein will serve one less year in the first iteration of the game, but then will serve four more in every subsequent iteration. So if Calvin sticks with the plan, his total jail time could be expressed as:


$$
\begin{align*}
  & jail \, time = 1 + \delta + \delta^2 \ldots = 1 + \frac{1}{1 - \delta} \\
\end{align*}
$$

Here $$ \delta $$ is the discount rate of future payoffs (in this case, years in / not in jail). If it is not intuitive why the risk of future jail time might be less costly than current jail time, there are a lot of ways to think about this. Humans discount future payoffs/costs on a merely psychological level, as well as for a much more logical reason - you might die.  It doesn't make sense to act now to avoid a jail sentence you would serve when you were dead. So, if Calvin deviates from the plan, he will get one less year of jail in the first iteration, but four times as much jail time in subsequent iterations.  

$$
\begin{align*}
  & jail \, time = 0 + 5\delta + 5\delta^2 \ldots = \frac{5}{1 - \delta} \\
\end{align*}
$$

So as long as Calvin doesn't very aggressively discount future jail time, then:

$$
\begin{align*}
  & 1 + \frac{1}{1 - \delta} < \frac{5}{1 - \delta} \\
\end{align*}
$$

e.g. for  $$ \delta = .9 $$ , 11 < 50. So if Calvin is rational, he would still cooperate, no matter how ruthless he might be. You can also see that Calvin and Klein do not necessarily need to employ a grim trigger strategy, where punishment continues forever.  They could also incentivize cooperation with a much shorter punishment period, as far future rounds have little impact on current behavior due to the discount factor. This repeated game sheds some light on the real world behavior of organized criminals, who often fail to confess to police despite the fact it is not rational in the short term. In criminal organizations, criminals are not faced with identical situations over and over again into perpetuity, as discussed here. However, they do face similar situations where trust is tested over and over again. Coupled with other ways to provide punishment or reward, like physical violence or compensation paid to family members, organizations are able to get members to cooperate over long periods of time, regardless of possible short term benefits of helping police.

 Let's leave our $$ \delta $$  at .9, assume Calvin and Klein play the same strategy we just investigated, and look at our payout table again.


| -----------------|-|----------------:|-|----------------:|
| Calvin / *Klein* | |*Confess*        | |*Not Confess*    |
| Confess          | |55, *55*         | |  50, *65*       |
| Not Confess      | |65, *50*         | |  11, *11*       |
|                  | |                 | |                 |

You can see that Calvin and Klein no longer are subject to the perversion of incentives that encouraged them to confess before. Whereas earlier in the single-game variant, no matter what Klein did, Calvin was better off confessing. Here it is better to confess only if Calvin thinks Klein will fail to cooperate with him.  So sure, if one confesses and the other has to employ the trigger strategy, it will be hard to start cooperating again as it was in the single-game version.  However there is the profound difference that when co-operating, both players are incentivized to continue to do so.  This results in it two states emerging:

* the **cooperative** state, where both players work together to create a better outcome and are incentivized to continue to do so
* the **non-cooperative** state, where the players both keep confessing and are incentivized to continue to do so

# The Global Warming Debate

The current debate around global warming 

# Customer Data Analysis

TODO: stop calling it a game everywhere and use criminal/crime terminology not player

TODO: fix confusing language which uses cooperate in oppposite contexts (police cooperation and criminal cooperation)

# Parallels in Mathiness

So how does this apply to the Mathiness Romer is criticizing? Let's first start with a summary of the Repeated Prisoners Dilemma.

1. If the prisoners cooperate (neither confesses), they can achieve the best outcome over time, where they spend the least time in prison.
2. If one prisoner confesses in an effort to reap a short-term gain, then the other can punish them by confessing in future rounds of the game
3. This threat of punishment can incentivize participants to act co-operatively
4. This creates an equilibrium where rational players will continue to co-operate because of the perceived threat
5. There is also an equilibrium in the case that neither are cooperating, in that once cooperation ceases, players are not incentivized to cooperate again

1. When both freshwater and saltwater economists adhere to the scientific method, they benefit in that their reputations are both better in the academic community, as the perception of economics in general is higher as a result of the progress the discipline makes when in the co-operative equilibrium
2. When freshwater economists engage in Mathiness, or other forms of merely adversarial posturing that do not follow the scientific method, they can gain a short term reputational boost, and deliver a reputational blow to saltwater economists.  This is a result of the fact that even though a paper that does not follow the scientific method may not have real value, it's ostensible validity provides the reputational boost to it's author, and calls into question the valid claims of saltwater economists, providing the reputational hit.
3. When both freshwater and saltwater economists deviate from the scientific method, there is an non-cooperative equilibrium where individual actors are disincentivized from using the scientific method. If they try to, they will fall into the situation described above in number two where non-scientific criticisms call their claims into question
4. Romer thinks that
Romer compares the situation in Economics to the repeated prisoner's dilemmna.






[1] *Strategies and Games*. Prajit K. Dutta. MIT Press 1999
