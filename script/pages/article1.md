title: How to Understand Risk in Investing
published: True
date_posted: 15 Jun 21
category: general
author: Charles
index: 1
duration: 7 min read
tags: [ Markovitz, Asset Allocation, Risk Management, Investing, Decision Theory, Uncertainty]
description: The concept of risk is often brought up during discussions about financial markets and instruments accessible to institutions and retail investors. So, what exactly is a useful definition of risk? Is it the standard deviation of financial assets and correlation across asset classes? Is it the uncertainty of outcome? Or should it be a subjective measure depending on an individual's beliefs and access to information? Let's discuss.


Recently, I was asked by a few of my friends to give an opinion on cryptocurrencies and money market funds as investments. A common theme of concern they have revolves the concept of investment risks. Are these assets 'risky investments'? Do they serve as adequete hedge against inflation? It took me awhile to concoct a reasonable response, but here are my thoughts: 


<!-- ![image 1]({{ url_for('static', filename='Images/article1/risk1.jpg') }}) -->


Defining risk in the context of investing is a nuanced undertaking. To establish a baseline, we can claim that investment risk should at least encapsulate the quantifiable and unquantifiable likelihood of unfavorable outcomes that might jeopardize our investment goals. This means that uncertainty of future events and severity of losses from the realization of such events lie at the core of its definition. 

However, since none of us are prophets, we unfortunately cannot divine the specific details of future events that govern the realm of investment risk (*informally known as the Knightian uncertainty*). The best we can do, is perhaps study past events rigorously, and hope to find patterns and predictors that persist through time. 

There are a few ways of approaching this endeavor, and I will try to comment on the major ones in this article. 

##### Too good to be true
To avoid the complications of forecasting future valuations, most people prefer to focus their attention solely on the downside. That is, an investment with a likelihood of yielding negative returns is risky, and should rightfully be treated with caution. 

Some implications of this line of thinking is reflected in the popularity of insurance policies, savings accounts and fixed deposits amongst common households. The idea is that since we cannot predict the future, we should instead focus our efforts on safeguarding our existing wealth. 

While this viewpoint is not exactly wrong, it does become problematic when we blindly default to simplistic heuristics like "playing it safe" in our decision making process. Given the multitude of exogenous factors that affect our personal lives, it seems neither prudent nor realistic to avoid negative outcomes altogether. In the context of financial decisions, the phrase 'out of sight, out of mind' rarely applies, as seemingly invisible forces like inflation affect everyone all the same. 

> "Given a ten percent chance of a 100 times payoff, you should take that bet every time. But you’re still going to be wrong nine times out of ten." — **Jeff Bezos, 2015 Amazon Annual Shareholder Letter**

##### Are we all the same? 
Some academics tries to formalize this innate behavior with the concept of loss aversion, and attempts to use probability and statistics concepts to map individual behavior to mathematically defined risk preferences (with a caveat of rationality thrown in for good measures). 

Through the lens of [decision theory](https://en.wikipedia.org/wiki/Decision_theory), we can model risk attitude amongst individuals using frameworks such as the expected utility hypothesis. Some illuminating work done in this field include <a class="ui-tooltip" title="Bernoulli showed that people tend to maximize their overall utility rather than monetary outcomes when faced with decision under uncertainty."><i style="cursor: help;">Bernoulli (1738)</i></a><sup>1</sup>, <a class="ui-tooltip" title="Wald showed that hypothesis testing and parameter estimation, the two pillars of frequentist statistics, are special cases of the general decision problem."><i style="cursor: help;">Wald (1939)</i></a><sup>2</sup>, and <a class="ui-tooltip" title="Neumann & Morganstern formalized the expected utility theory with general axioms like completeness, transivity, continuity & independence."><i style="cursor: help;">Neumann & Morganstern (1947)</i></a><sup>3</sup>. The work done by these academics proved to be pivotal to the field of economics, as they laid down a preliminary blueprint for understanding human behavior in a generalized setting, inching one step closer towards physical sciences like physics and chemistry. 

Subsequent work done by other economists intending to disprove these theories (mostly through the departure from rationality assumptions) include <a class="ui-tooltip" title="The Allais paradox questions the independence axiom of expected utility theory through lottery experiments."><i style="cursor: help;">Allais (1953)</i></a><sup>4</sup>, <a class="ui-tooltip" title="Ellsberg showed that people tend to prefer certainty at the expense of utility."><i style="cursor: help;">Ellsberg (1961)</i></a><sup>5</sup>, <a class="ui-tooltip" title="Kahneman & Tversky introduced the prospect theory to show empirically how preferences of individuals are inconsistent among the same choices, depending on how those choices are presented."><i style="cursor: help;">Kahneman & Tversky (1979)</i></a><sup>6</sup>. Their work suggested that in real life settings, individuals are not exactly the cold-blooded calculators described in theoretical literatures (*surprising!*). Instead, they are more susceptible to emotions and perceptions, leading to decisions that are not 'strategically sound' on paper (i.e. bounded rationality).

Interestingly, many of these economists cited above were eventually awarded nobel prizes in economics for their contributions to decision theory, highlighting the importance of this field and our ever evolving understanding of decision making under uncertainty. However, such developments also inevitably raise the question of whether dynamical systems like the financial markets can ever be solved. That is, can we really use mathematics to quantify risk in a general manner? 

<!-- ![image 2]({{ url_for('static', filename='Images/article1/risk2.png') }}) -->


##### High risk high return
In an adjacent field, academics attempt to formalize investment risk by measuring the standard deviation of financial asset returns and the correlation of returns across asset classes (commonly represented as \\(\Sigma_{nxn}\\), the variance-covariance matrix of a portfolio with \\(n\\) assets). 

Selecting efficient portfolios of financial assets using the expectation and variability of returns was first introduced by <a class="ui-tooltip" title="Markovitz showed that investors can reduce risk by constructing a portfolio along the efficient frontier, shedding light on the effects of asset diversification on portfolio risk."><i style="cursor: help;">Markovitz (1952)</i></a><sup>7</sup> in his seminal paper "Portfolio Selection", an outstanding piece of work that eventually won him the nobel prize in economics. Coincidentally, <a class="ui-tooltip" title="Roy showed that ..."><i style="cursor: help;">Roy (1952)</i></a><sup>8</sup> was published in the same year, introducing the eye-opening use of semivariance as a measure of downside risk, though the response was relatively muted as compared to Markovitz's. 

> "On the basis of Markowitz (1952), I am often called the father of modern portfolio theory (MPT), but Roy can claim an equal share of this honor." - **Harry Markowitz, The Early History of Portfolio Theory: 1600-1960**

Nonetheless, their ideas proved to be sticky, as they influenced the way practitioners view risk in asset management ever since. The use of volatility of asset returns as a predominant risk measure became a standard procedure in portfolio analysis. For instance, the widely taught <a class="ui-tooltip" title="The CAPM was introduced by Jack Treynor (1961), William F. Sharpe (1964), John Lintner (1965) and Jan Mossin (1966) independently, building on the earlier work of Harry Markowitz on diversification and modern portfolio theory."><i style="cursor: help;">CAPM model</i></a> assumes a linear relationship between risk and rate of return, and argues for the role of diversification in eliminating unsystematic risks in a multi-asset portfolio.  

However, it must be said that the idea of viewing volatility as risk, and therefore as a variable to be minimized in the objective function, seems incomplete. Strictly speaking, the volatility of asset prices is merely a reflection of market activity, and while an excessive degree does does admittedly rattle our emotions considerably, it nonetheless falls short in offering any predictive insights regarding an asset's future value. Furthermore, as other practitioners and academics pointed out, using historical variance as a risk measure assumes time-invariance of risk and the normality of the error term, both of which are violated more often than not. That being said, the variance-covariance matrix is one of the more convenient data points to calculate, and it possesses many useful mathematical properties for portfolio analysis. Hence, it does make sense to look at asset price volatility, at least as a starting point. 


##### To each his own
In the modern era of portfolio management, risk models that attempts to include subjective views of the future (i.e. a Bayesian approach) or to allocate assets based on their volatility contributions have gained traction. Namely, the <a class="ui-tooltip" title="The Black-Litterman model was introduced by Fisher Black and Robert Litterman in 1992 when they were working at Goldman Sachs. The model offers a way to incorporate investor beliefs into the asset allocation model of the Modern Portfolio Theory, bridging the gap between MPT and equity research."><i style="cursor: help;">Black-Litterman model</i></a> and the <a class="ui-tooltip" title="The Hierarchical Risk Parity model is a variant of risk parity models introduced by De Prado in 2016. The model seeks to utilize graph theory and machine learning techniques to extract information contained in the covariance matrix."><i style="cursor: help;">Hierarchical Risk Parity model</i></a>. 

In laymen's term, the Bayesian approach seeks to quantify the perceived risk level of an asset by factoring in the investor's personal experiences, knowledge, intuition, and beliefs, and should be updated accordingly as he/she gains new information. For example, if you are a chef, and you engaged with the practice of cooking your entire life, then it is fair to say that you have more (potentially predictive) information than most of the others. And assuming that your level of conviction directly correlates with your information advantage (i.e. you trust in your cooking abilities), you should have your risk preferences steered towards identifying and investing in F&B establishments with superior quality food. Your perception of risk of F&B investments should be the lowest, perhaps even lower than the so called risk-free assets. 

This is not to say that you will definitely perform better by investing in low risk assets, as after all, returns are determined by market forces of supply and demand. However, what the framework is able to offer, is the peace of mind that you won't feel the sting of asset depreciation as much, by buying what you know better than others. That being said, perhaps this way of viewing risk would not be as appealing to individual looking for professional advice, as it essentially transfers the ownership of decision making back to the retail investors. 

In the asset management world, the most prominent example of this approach is perhaps Ark Invest. Led by Cathie Wood, the investment management firm markets itself by hiring sector experts from the STEM field to research on disruptive innovations. They operate on the hypothesis that with the in-depth experience of their analysts, they can see the future with greater clarity and profit from the information advantage. This strategy seems to be working thus far, as their flagship fund averaged an annual 39% in ROI since inception.  

Circling back, it feels almost poetic that a concept as abstract as risk should incorporate some predetermined elements like knowledge and experiences, while being stochastic in nature (fluctuates according to our beliefs and intuition). After all, if risk profiles can be perfectly replicated, then the benchmark/equilibrium asset market would exhibit entirely different characteristics. To put it crudely, if all of us can think like Warren Buffet, then he would no longer be known as the Sage of Omaha. 

##### Upshot

It might come at a slight disappointment that there isn't really an all-encompassing framework or equation that captures the essense of risk, not yet at least. However, the positive takeaway is that we have come a long way in understanding and capturing the concept of uncertainty, as well as creating the tools and techniques required to guard against the unknown. Nobody can claim to be a prophet, but at the very least we can aspire to take the right step forward. 

<i>May the odds be in your favor. </i>

---

**Footnote:**

[[1]](https://www.jstor.org/stable/1909829) *Specimen theoriae novae de mensura sortis (Exposition of a New Theory on the Measurement of Risk)* - D. Bernoulli (Jan, 1738)

[[2]](https://www.jstor.org/stable/2235609) *Contributions to the Theory of Statistical Estimation and Testing Hypotheses* - A. Wald (Dec, 1939)

[[3]](https://psycnet.apa.org/record/1945-00500-000) *Theory of Games and Economic Behavior* - J. Von Neumann & O. Morgenstern (1944)

[[4]](https://psycnet.apa.org/record/1954-08664-001) *Le comportement de l'homme rationnel devant le risque: Critique des postulats et axiomes de l'ecole Americaine ( The behavior of rational man in the face of risk: Critique of the postulates and axioms of the American school)* - M. Allais (Oct, 1953)

[[5]](https://www.jstor.org/stable/1884324) *Risk, Ambiguity, and the Savage Axioms* - D. Ellsberg (Nov, 1961)

[[6]](https://www.jstor.org/stable/1914185) *Prospect Theory: An Analysis of Decision under Risk* - D. Kahneman & A. Tversky (Mar, 1979)

[[7]](https://www.jstor.org/stable/2975974) *Portfolio Selection* - H. Markovitz (Mar, 1952)

[[8]](https://www.jstor.org/stable/1907413?origin=crossref) *Safety First and the Holding of Assets* - A. D. Roy (Jul, 1952)