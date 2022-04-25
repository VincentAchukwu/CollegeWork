# School of Computing &mdash; Year 4 Project Proposal Form

> Edit (then commit and push) this document to complete your proposal form.
> Make use of figures / diagrams where appropriate.
>
> Do not rename this file.

## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | xxxxxx            |
|Student 1 Name:      | Joseph Lyons      |
|Student 1 ID:        | 16485216          |
|Student 2 Name:      | Vincent Achukwu   |
|Student 2 ID:        | 17393546          |
|Project Supervisor:  | Martin Crane      |

> Ensure that the Supervisor formally agrees to supervise your project; this is only recognised once the
> Supervisor assigns herself/himself via the project Dashboard.
>
> Project proposals without an assigned
> Supervisor will not be accepted for presentation to the Approval Panel.

## SECTION B

> Guidance: This document is expected to be approximately 3 pages in length, but it can exceed this page limit.
> It is also permissible to carry forward content from this proposal to your later documents (e.g. functional
> specification) as appropriate.
>
> Your proposal must include *at least* the following sections.


### Introduction

> Describe the general area covered by the project.

With the rise of Decentralised Finance and cryptocurrencies starting to reshape the way people borrow and save, it is apparent that cryptocurrencies are an important and thriving element in the current digital economy. People all around the world look to invest in various cryptocurrencies in the market and aim to make profits following their own investment plans. We will be developing a web app based on cryptocurrencies. The app will be targeted at people that have an interest in analyzing the price movements of cryptocurrencies and predicting where the price will go in the future. The main objective of the web app is to take in previous price movements of the coins and predict the direction they will go in the future. This project will be based mostly on machine learning and taking in past data to predict the price movements in the future.

We will not be using this app for financial advice for anyone but just to show our skills of training data to predict a future outcome.

### Outline

> Outline the proposed project.

Streamlit is an open-source Python app framework that provides users with an interactable and easy-to-use user web interface. The web application will be designed for all to use with the aim of guiding users to having an idea of the future price movements of various cryptocurrencies. As stated, this is not an application intended for financial advice, as users should know that they must do their own research prior to investing in cryptocurrencies. This application is rather a demonstration of how we can use machine learning to predict the price movements of various tokens in the market.

### Background

> Where did the ideas come from?

Cryptocurrencies are the talk of the future. Since the blow-up of Bitcoin over the past few years, cryptocurrencies have become extremely popular with banks and the general public. The idea of making a price prediction web app appealed to the two of us because it may be beneficial in the future. Being able to train data to predict an outcome is a great skill to learn and we both have an interest in machine learning so the project just made sense. Our goal is to create a useful and accessible application that one could utilise along with their other investment applications to have an idea of the future prices of cryptocurrencies.

We chose to go with a web app because it would be much easier to view and interact with the graphs and other data on a larger screen with a monitor. Also, people interested in the cryptocurrency market typically use web apps such as Binance, Coinmarketcap, Coinbase, and TradingView, which can be accessed easily by switching tabs rather than switching between different applications on a mobile device.

### Achievements

> What functions will the project provide? Who will the users be?

We are going to develop the application to get one coin working properly and have a good prediction outcome for the coin. Then we would like to expand and get multiple coins working on the app. We are considering to also implement the same for stock price predictions, but the main aim is to get the application working for cryptocurrencies. One of the main goals of this project is to make the web application easy to use for all users and of all ages. This web app will appeal to a wide range of people from people curious about where the price of a certain coin is, to people wondering where the price will be in the near future.

In terms of the functionality of the web application itself, we aim to have the majority of these features implemented:
* Menu tab with a dropdown/selection box to select a cryptocurrency to predict the price for.
* An interactable graph to display the historic and predicted price movement of the selected cryptocurrency.
* A slider tool to change the number of days, months and years into the future for which the prices are shown for the selected cryptocurrency.
* News on the current market that could affect the price of each coin.
* Buy/sell signals to inform the user that if the future price of a cryptocurrency is higher than the current price, it may be a good sign to buy in.
* Percentage change between the current price and the predicted price of the selected cryptocurrency.
* Switch between cryptocurrency or stock price predictions.

### Justification

> Why/when/where/how will it be useful?

We decided to develop this web app because there are not many other good web applications like this idea out there at the minute. This will be useful as we will have multiple functions for people to use around cryptocurrencies on the one web app. Being able to see real-time prices and real-time predictions and trending graphs all in one place will be handy for all of our users. As it will be a web app, it will be accessible to anyone with the internet from a mobile device to a desktop and it would provide users with the ease of use of the application when using the interactable features.

### Programming language(s)

> List the proposed language(s) to be used.

* Python

### Programming tools / Tech stack

> Describe the compiler, database, web server, etc., and any other software tools you plan to use.

* Visual Studio Code
* Git
* Streamlit (open-source Python app framework)
* fbprophet (forecasting tool implemented in R and Python)
* Tensorflow
* Pandas data frame
* Sklearn
* Plotly (for plotting data on graphs)
* yfinance (Python library for accessing data from Yahoo Finance)
* Kaggle for data set.

### Hardware

> Describe any non-standard hardware components which will be required.

* Laptop
* PC

### Learning Challenges

> List the main new things (technologies, languages, tools, etc) that you will have to learn.

Given that cryptocurrencies are volatile and that we will be implementing machine learning based on historical data of cryptocurrencies, it is important to ensure that we get the model working well for one cryptocurrency after which we include various other cryptocurrencies. Ensuring ease of use and accessibility is one of our aims in this project as we want users to easily navigate through the web app and easily understand how to interact with the features. Using a good machine learning algorithm is key to make sure we can get the best predictions that we can get from the data. Machine learning will be the main goal of this project.

### Breakdown of work

> Clearly identify who will undertake which parts of the project.
>
> It must be clear from the explanation of this breakdown of work both that each student is responsible for
> separate, clearly-defined tasks, and that those responsibilities substantially cover all of the work required
> for the project.

In order for us to manage the workflow of this project, we will have regular meetings each week to catch up on our progress in order to reach our goals. As our main messaging platform, we will be using Discord to communicate online as we could share our screens if necessary when communicating online or to resolve any issues. As for the documentation of the project, we plan to have equal responsibility for working with it. We will both be working on the machine learning implementation as well as researching more about machine learning throughout the development of the application.

#### Student 1 - Joseph Lyons

> *Student 1 should complete this section.*

* Front end of the web application app. Designing the look and feel of the page.
* Finding the data for machine learning.
* Cleaning the data.
* Pick an algorithm to make the predictions. Such as LSTM which is great for finding paterns in the data set.

#### Student 2 - Vincent Achukwu

> *Student 2 should complete this section.*

* Back end for the web app.
* Studying the trends of the price.
* Unit testing for the web app.
* Classifying the data.
