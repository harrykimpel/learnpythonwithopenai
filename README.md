### **Summary**

Interested in learning programming and AI? You can explore the sample code and resources I used in my hands-on workshop by following the steps described below.

First, we'll provide an overview of basic programming concepts in Python and discuss how the internet works. Then, we'll dive into more advanced topics such as Large Language Models (LLM) and Prompt Engineering, which will teach you how to ask the right questions. Finally, we'll guide you through the process of building your own AI bot using all the concepts we've covered.

By the end of the workshop, you'll be able to interact with your AI bot, gain a better understanding of how things work, and start leveraging AI services to increase your productivity.

The tech stack used for this project includes HTML, CSS (with the Milligram framework), Python 3, Flask, and OpenAI.

Presentation - Coming Soon

---

### Prerequisites

Here are some essential packages that need to be installed before you can start building your own AI bot using OpenAI and Python.

Firstly, you will need to download and install Python3 from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/). This is an interpreted, high-level, and general-purpose programming language that is easy to learn and has a vast library of modules that enable you to accomplish a wide range of tasks.

Next, you will need to install Pip3, which is the package installer for Python. Pip3 is used to install, upgrade, and manage Python packages and their dependencies. To install Pip3, please visit [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/) and follow the instructions provided.

Finally, you will need to install OpenAI, which is a powerful and flexible open-source library for building and training large-scale artificial intelligence models. OpenAI provides a simple and easy-to-use API that allows developers to access state-of-the-art AI models and technologies. You can install OpenAI by visiting [https://pypi.org/project/openai/](https://pypi.org/project/openai/) and following the installation instructions.

Optionally, you can also install NewRelic, which is a monitoring tool that provides real-time visibility into application behavior. This tool helps you identify potential issues before they impact users and allows you to optimize your application's performance.

---

### **Instructions**

**Level One** is denoted by a reference code provided by OpenAI, but it cannot be executed successfully. This level is essential, as it serves as a foundation for more advanced concepts later on. For reference, please see [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create).

**Level Two** will dive deeper into the world of programming by learning about variables and data structures. These are crucial concepts that will help you in your future projects.

Variables are like containers that hold values. They allow you to store and manipulate data in your code. In Python, you can assign any value to a variable, such as numbers, strings, or even other variables. Data structures, on the other hand, are ways of organizing and storing data in a program. They allow you to work with collections of values, such as lists, tuples, and dictionaries. These structures can be used in a variety of situations, from keeping track of user input to managing large sets of data.

To start learning about variables and data structures in Python, simply type `python3 leveltwo.py` and run the code. 


**Level Three** will delve into the concepts of inputs, outputs, and functions, which are the building blocks of any programming language. Through this level, you will learn how to create, modify, and use functions to perform specific tasks in your programs. You will also gain an in-depth understanding of how inputs and outputs work, and how they are used to receive and produce data in Python.

To start learning about inputs, outputs, and functions in Python, simply type `python3 levelthree.py` and run the code. 


**Level Four** introduces you to the world of APIs using a Python microframework called Flask. Flask is a powerful tool for building web applications, and it is especially useful for building APIs. APIs, or application programming interfaces, enable different software applications to communicate with each other.

To start learning about APIs in Python, simply type `flask --app levelfour.py run` and run the code. 


**Level Five** will dive deeper by leveraging our previous experience with implementing OpenAI with functions and Flask. Specifically, we will take the function we previously created and make it available as an endpoint using Flask. By doing so, we will be able to expand the functionality of our application and make it more accessible to users. This will require us to carefully consider the design of our code and make strategic decisions about how we structure our application.

To start the application in Python, simply type `flask --app levelfive.py run` and run the code. 


**Level Six** is an optional challenge that focuses on observability. This concept is important to ensure that the application runs smoothly and optimally for users. To achieve this, we will onboard a New Relic Python agent into our app. The agent collects data and provides real-time visibility into application behavior, helping to identify potential issues before they impact users.


To start the application in Python, simply type `NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program flask --app levelsix.py run` and run the code.