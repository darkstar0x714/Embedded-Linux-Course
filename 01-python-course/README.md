# 01 Python Course

Welcome to the **01 Python Course** folder!

This folder contains all the code and notes to complete the Python course as part of [Embedded Linux Diploma](https://github.com/darkstar0x714/Embedded-Linux-Course) program from [Moatasem El Sayed.](https://eg.linkedin.com/in/moatasem-el-sayed)

## Course Description

In this course, you will learn:

the fundamentals of Python programming and how to apply Python as powerful scripting tool to help us in automation of tasks in our Embedded linux journey.

## Table of Contents

- [Course Outline :](#course-outline)
  - [Introduction to Python.](#1-introduction-to-python)

- [Python Modules.](#python-modules)
  - [termcolor.](#termcolor)
  - [psutil.](#psutil)
  - [os.](#os)
  - [datetime.](#datetime)
  - [Requests.](#requests)
  - [pyfiglet.](#pyfiglet)
  - [pytube.](#pytube)
  - [math.](#math)
  - [calendar.](#calendar)
  - [python-vlc.](#python-vlc)
  - [gtts.](#gtts)

- [Tasks](#tasks)
  - [01-Introduction to Python Tasks :](#01-introduction-to-python-tasks)
    - [01 print your info](#01-print-your-info)
    - [02 simple Calculator](#02-simple-calculator)
    - [03 login System](#03-login-system)
    - [04 circle Area Calculator](#04-circle-area-calculator)
    - [05 simple calender](#05-simple-calender)
    - [06 vowel detector](#06-vowel-detector)
    - [07 environment variable](#07-get-environment-variable)
    - [08 count repeated 4 in user list](#08-count-repeated-4-in-list)

## Course Outline

The course is divided into 5 modules, each covering different aspects of Python programming.

Here is an overview of the modules:

### 1. Introduction to Python

- Interpreter Vs Compiler.
- Byte code disclosure.
- Shebang notation.
- Comments.
- Variables.
- Variable naming rules.
- Statically like c++ vs Dynamically types like python.
- Comma Operator .
- Data types:
  - Numeric:
    - integer.
    - float.
    - complex number.
  - Dictionary.
  - Boolean.
  - Set.
  - Sequence type:
    - List
    - Strings
    - Tuple
- Input.
- Operators:
  - Arithmetic operators.
  - Comparison operators.
  - Assignment operators.
  - Logical operators.
  - Identity operators.
  - Membership operators.
  - Bitwise operators.
- if condition:
  - normal.
  - shorthand.
  - Ternary.
  - nested if.
- pass Statement.
- loops:
  - for.
  - while.
- Break.
- continue.
- nested loops.

## Python Modules

### termcolor

The **termcolor** module is a Python library that simplifies the process of adding colored text to terminal output.

It allows you to easily apply colors to text and background, making your command-line applications more visually appealing and user-friendly.

termcolor is particularly useful for highlighting important information or organizing data within terminal-based applications.

**used in [02 simpleCalculator](01-Introduction_to_Python/02_simpleCalculator.py)**
**used in [03 login System](01-Introduction_to_Python/03_loginSystem.py)**

### psutil

The **psutil** module is a Python library that provides an interface for retrieving system-related information, such as CPU usage, memory usage, network statistics, and more.

It simplifies system monitoring and management tasks, making it a valuable tool for developers working on system-related applications.

**used in [print Pc HW State](01-Introduction_to_Python/scriptsForAdvancedModules/printPcHWState.py)**

### os

The **os** module is a Python library that provides a wide range of functions for interacting with the operating system.

It allows you to perform tasks such as file and directory manipulation, environment variable management, and process control, making it essential for system-level programming and file handling in Python.

**used in [07 environment variable](01-Introduction_to_Python/07_getEnvironmentVariable.py)**

### datetime

The **datetime** module is a Python library that provides classes and functions to represent and manipulate dates, times, and time intervals, making it essential for tasks involving time-related calculations and formatting.

### pyfiglet

The **pyfiglet** module is a Python library that allows you to create stylized text art, also known as ASCII art, using various font styles. It's a fun and creative tool for generating decorative text for banners, headers, and more in your Python projects.

**used in [print fancy name](01-Introduction_to_Python/scriptsForAdvancedModules/printFancyName.py)**

### Requests

The **Requests** module is a Python library used for making HTTP requests to web services and fetching data from URLs.

It simplifies the process of sending GET, POST, and other HTTP requests, making it a popular choice for web scraping, API interactions, and web-based data retrieval in Python.

**used in [requesting](01-Introduction_to_Python/scriptsForAdvancedModules/requesting.py)**

### pytube

The **pytube** module is a Python library that simplifies the downloading of YouTube videos. It provides an easy-to-use interface for extracting video and audio streams from YouTube URLs, making it a valuable tool for working with YouTube content in Python applications.

**used in [youtube downloader](01-Introduction_to_Python/scriptsForAdvancedModules/youtubeDownloader.py)**

### math

The **math** module is a Python library that provides a set of mathematical functions and constants for performing complex mathematical operations, including basic arithmetic, trigonometry, logarithms, and more. It's a fundamental tool for mathematical calculations in Python programs.

**used in [04 circle Area Calculator](01-Introduction_to_Python/04_circleAreaCalculator.py)**

### calendar

The **calendar** module is a Python facilitates the creation and manipulation of calendars.

It enables you to generate calendars, work with dates, and perform various date-related calculations, making it valuable for tasks involving scheduling, event planning, and date-based applications.

**used in [05 simple calender](01-Introduction_to_Python/05_calendar.py)**

### python-vlc

The **python-vlc** module is a Python binding for the VLC media player, allowing developers to control and integrate VLC functionality into their Python applications, making it possible to automate media playback and manipulation.

**used in [convert text to speak](01-Introduction_to_Python/scriptsForAdvancedModules/convertTextToSpeak.py)**

### gtts

The **gtts** module is a Python module enable developers to convert text into speech by leveraging Google's Text-to-Speech API. It provides a convenient way to generate audio files or play speech directly from text, enhancing the accessibility and interactivity of applications.

**used in [convert text to speak](01-Introduction_to_Python/scriptsForAdvancedModules/convertTextToSpeak.py)**

## Tasks

### 01-Introduction to Python Tasks

#### [01 print your info](01-Introduction_to_Python/01_print_your_info.py)

Write a Python script that prints your information.
Full Name, Birth Year, Address and faculty.

#### [02 simple Calculator](01-Introduction_to_Python/02_simpleCalculator.py)

simple calculator to perform simple operations (+,-,*,/).

#### [03 login System](01-Introduction_to_Python/03_loginSystem.py)

simple login system to show case dic usage and perform some flow control.

#### [04 circle Area Calculator](01-Introduction_to_Python/04_circleAreaCalculator.py)

simple program to calculate circle area

#### [05 simple calender](01-Introduction_to_Python/05_calendar.py)

simple program to print month calender and perform some basic operation on it like
(next month - next year - previous month - previous year)
with some error handling to verify user input.  

#### [06 vowel detector](01-Introduction_to_Python/06_vowelDetector.py)

simple program to check is input is a vowel char or not.

#### [07 get environment variable](01-Introduction_to_Python/07_getEnvironmentVariable.py)

simple program print path environment variable using OS module

#### [08 count repeated 4 in list](01-Introduction_to_Python/08_countRepeated4InList.py)

simple program print how many 4 in list entered by user
