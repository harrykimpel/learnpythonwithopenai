### **Summary**

Interested to explore programming and AI? You can explore the sample code and resources I used in my hands-on workshop by following the steps described below.

First, we'll provide an overview of basic programming concepts in Python and discuss how the internet works. Then, we'll dive into more advanced topics such as Large Language Models (LLM) and Prompt Engineering, which will teach you how to ask the right questions to OpenAI. Finally, we'll guide you through the process of building your own AI bot using all the concepts we've covered.

By the end of the workshop, you'll be able to interact with your AI bot, gain a better understanding of how things work, and start leveraging AI services to increase your productivity.

The tech stack used for this project includes HTML, CSS (with the Milligram framework), Python 3, Flask, and OpenAI. The project is used to support initiatives such as Women@NR and New Reluc Student Edition deployed in a virtual lab - Instruqt.

Presentation - [HERE](https://docs.google.com/presentation/d/1w8g8scW_mRSUYNHW6EsSvoS6Rmwk9WSQ_UzrmwDkCU0/edit?usp=sharing)

---

### Prerequisites

Here are some essential packages that need to be installed before you can start building your own AI bot using OpenAI and Python.

Firstly, you will need to download and install Python3 from the [official website](https://www.python.org/downloads/). This is an interpreted, high-level, and general-purpose programming language that is easy to learn and has a vast library of modules that enable you to accomplish a wide range of tasks.

Next, you will need to install Pip3, which is the package installer for Python. Pip3 is used to install, upgrade, and manage Python packages and their dependencies. To install Pip3, please visit the [official website](https://pip.pypa.io/en/stable/installation/) and follow the instructions provided.

It is essential too that you have [Python Flask](https://flask.palletsprojects.com/en/2.3.x/installation/) installed on your computer. Python Flask is a popular web framework used by developers to create web applications. It is a lightweight, flexible, and easy-to-use framework that can help you create web applications quickly and efficiently. Therefore, to get the most out of this workshop, we highly recommend that you take the time to install Python Flask.

Finally, you will need to install OpenAI, which is a powerful and flexible open-source library for building and training large-scale artificial intelligence models. OpenAI provides a simple and easy-to-use API that allows developers to access state-of-the-art AI models and technologies. You can install OpenAI by visiting the [official website](https://pypi.org/project/openai/) and following the installation instructions.

Optional - for better insight into your application's behavior, consider installing the [Python agent](https://docs.newrelic.com/install/python/) provided by New Relic. This agent is part of a powerful observability platform that can give you real-time visibility into your application. By detecting potential issues before they affect your users, you can optimize your application's performance and provide a better experience for your users.

---

### **Instructions**

Each level is designed to run as a standalone application to avoid unnecessary issues.

**Level One** is denoted by a reference code provided by OpenAI, but it cannot be executed successfully. This level is essential, as it serves as a foundation for more advanced concepts later on. For reference, please see [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create).

**Level Two** will dive deeper into the world of programming by learning about variables and data structures. These are crucial concepts that will help you in your future projects.

Variables are like containers that hold values. They allow you to store and manipulate data in your code. In Python, you can assign any value to a variable, such as numbers, strings, or even other variables. Data structures, on the other hand, are ways of organizing and storing data in a program. They allow you to work with collections of values, such as lists, tuples, and dictionaries.

To start learning about variables and data structures in Python, simply type the following commands:

```shell
export OPENAI_API_KEY=YOUR_API_KEY_HERE

python3 leveltwo.py
```

**Level Three** will delve into the concepts of inputs, outputs, and functions, which are the building blocks of any programming language. Through this level, you will learn how to create, modify, and use functions to perform specific tasks in your programs.

To start learning about inputs, outputs, and functions in Python, simply type the following commands:

```shell
export OPENAI_API_KEY=YOUR_API_KEY_HERE

python3 levelthree.py
```

**Level Four** introduces you to the world of APIs using a Python microframework called Flask. Flask is a powerfulfor building web applications, and it's especially useful for building APIs. APIs, or application programming interfaces, enable different software applications to communicate with each other.

To start Flask, simply type the following commands:

```shell
flask --app levelfour.py run --host 0.0.0.0 --port 5000
```

**Level Five** will dive deeper by leveraging our previous experience with implementing OpenAI with functions and Flask. Specifically, we will take the function we previously created and make it available as an endpoint using Flask. By doing so, we will be able to expand the functionality of our application and make it more accessible to users.

To start the application, simply type the following commands:

```shell
export OPENAI_API_KEY=YOUR_API_KEY_HERE

flask --app levelfive.py run --host 0.0.0.0 --port 5002
```

**Level Six** is an optional challenge that focuses on observability. This concept is important to ensure that the application runs smoothly and optimally for users. To achieve this, we will onboard a New Relic Python agent into our app. The agent collects data and provides real-time visibility into application behavior, helping to identify potential issues before they impact users.

To start the application, simply type the following commands:

```shell
export OPENAI_API_KEY=YOUR_API_KEY_HERE

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program flask --app levelsix.py run --host 0.0.0.0 --port 5004
```

**Level Seven** is an optional challenge that focuses on some fun image generation capabilities. This part of the OpenAI capabilities, i.e. leveraging dall-e-3 model, is not yet supported with New Relic AI Monitoring, but will soon be supported as well. The purpose of this exercise is purely to have some fun with image generation capabilities.

To start the application, simply type the following commands:

```shell
export OPENAI_API_KEY=YOUR_API_KEY_HERE

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program flask --app levelseven.py run --host 0.0.0.0 --port 5004
```
