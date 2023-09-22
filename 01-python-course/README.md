# 01 Python Course

Welcome to the **01 Python Course** folder!

This folder contains all the code and notes to complete the Python course as part of [Embedded Linux Diploma](https://github.com/darkstar0x714/Embedded-Linux-Course) program from [Moatasem El Sayed.](https://eg.linkedin.com/in/moatasem-el-sayed)

## Course Description

In this course, you will learn:

the fundamentals of Python programming and how to apply Python as powerful scripting tool to help us in automation of tasks in our Embedded linux journey.

## Table of Contents

- [Course Outline :](#course-outline)
  - [01-Introduction to Python.](#1-introduction-to-python)
  - [02-Deep Dive and Python modules.](#2-deep-dive-and-python-modules)
  - [03-Advanced python.](#3-advanced-python)
  - [04-OOP In python.](#4-oop-in-python)

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
  - [subprocess.](#subprocess)
  - [keyboard.](#keyboard)
  - [pyAutoGUI.](#pyautogui)
  - [platform.](#platform)
  - [uuid.](#uuid)
  - [smtplib.](#smtplib)
  - [sys.](#sys)
  - [plyer.](#plyer)
  - [time.](#time)
  - [openpyxl.](#openpyxl)

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
  
  - [02-Deep dive and python modules Tasks :](#02-deep-dive-and-python-modules)
    - [01 find max number](#01-find-max-number)
    - [02 find bitcoin price](#02-find-bitcoin-price)
    - [03 make custom system keyboard shortcut](#03-make-custom-system-keyboard-shortcut)
    - [04 print multi function inputs](#04-print-multi-function-inputs)
    - [05 add multi function inputs](#05-add-multi-function-inputs)
  
  - [03-Advanced python](#03-advanced-python)
    - [01 open web page](#01-firelink-app)
    - [02 activity suggest](#02-i-am-bored)
    - [03 get my public ip](#03-get-my-public-ip)
    - [04 install vsCode extension](#04-setup-vscode-extension)
    - [05 make .cpp file and .h file](#05-cpp-file-creation)
  
  - [04-oop in python](#04-oop-in-python)
    - [01 number of lines](#01-number-of-lines-in-file)
    - [02 number of words in file](#02-number-of-words-in-file)
    - [03 write list to a file](#03-write-list-to-a-file)
    - [04 gpio file generator](#04-gpio-file-generator)
    - [05 email checker](#05-email-checker)
    - [06 battery notifier](#06-battery-notifier)
    - [07 get argument from terminal](#07-get-argument-from-terminal)
    - [08 print an ascii code for an input](#08-print-an-ascii-code-for-an-input)
    - [09 .h parser to excel](#09-h-parser-to-excel)
    - [10 email alert](#10-email-alert)

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

### 2. Deep dive and python modules

- Built in functions vs object functions.
- string methods.
- string substitution.
- using help command.
- functions:
  - normal:
    - void.
    - return.
  - value:
    - assign.
    - default.
  - variadic argument:
    - *list.
    - **dict.
- local and global function.
- lambda expression.
- some examples on modules.

### 3. Advanced python

- make your own module.
- built in variables.
- alias import.
- from import.
- garbage collector.
- list methods.
- shallow clone.
- deep clone.
- tuple methods.
- set methods.
- unpacking concept.
- pyautogui module.
- make global alise.
- dictionary methods.
- del keyword.
- .copy() usage.
- pass by value in functions.
- pass by reference in functions.
- files manipulation.

### 4. oop in python

- OOP
  - oop concept
    - attribute
    - actions
  - constructor
  - destructor
  - built-in actions
    - str
    - doc
    - init
    - del
  - Inheritance
    - depending conflict
    - super calling
    - multi-level inheritance
  - Private member
  - static method
  - Operator overloading
- error handling
  - error types
  - try
  - except
  - else
  - finally
- files
  - **with** keyword
  - csv
  - openpyxl
- multi-threading
  - process vs threads
  - line process
  - .start
  - .join
  - .isAlive  

## Python Modules

### termcolor

The **termcolor** module is a Python library that simplifies the process of adding colored text to terminal output.

It allows you to easily apply colors to text and background, making your command-line applications more visually appealing and user-friendly.

termcolor is particularly useful for highlighting important information or organizing data within terminal-based applications.

### psutil

The **psutil** module is a Python library that provides an interface for retrieving system-related information, such as CPU usage, memory usage, network statistics, and more.

It simplifies system monitoring and management tasks, making it a valuable tool for developers working on system-related applications.

### os

The **os** module is a Python library that provides a wide range of functions for interacting with the operating system.

It allows you to perform tasks such as file and directory manipulation, environment variable management, and process control, making it essential for system-level programming and file handling in Python.

### datetime

The **datetime** module is a Python library that provides classes and functions to represent and manipulate dates, times, and time intervals, making it essential for tasks involving time-related calculations and formatting.

### pyfiglet

The **pyfiglet** module is a Python library that allows you to create stylized text art, also known as ASCII art, using various font styles. It's a fun and creative tool for generating decorative text for banners, headers, and more in your Python projects.

### Requests

The **Requests** module is a Python library used for making HTTP requests to web services and fetching data from URLs.

It simplifies the process of sending GET, POST, and other HTTP requests, making it a popular choice for web scraping, API interactions, and web-based data retrieval in Python.

### pytube

The **pytube** module is a Python library that simplifies the downloading of YouTube videos. It provides an easy-to-use interface for extracting video and audio streams from YouTube URLs, making it a valuable tool for working with YouTube content in Python applications.

### math

The **math** module is a Python library that provides a set of mathematical functions and constants for performing complex mathematical operations, including basic arithmetic, trigonometry, logarithms, and more. It's a fundamental tool for mathematical calculations in Python programs.

### calendar

The **calendar** module is a Python facilitates the creation and manipulation of calendars.

It enables you to generate calendars, work with dates, and perform various date-related calculations, making it valuable for tasks involving scheduling, event planning, and date-based applications.

### python-vlc

The **python-vlc** module is a Python binding for the VLC media player, allowing developers to control and integrate VLC functionality into their Python applications, making it possible to automate media playback and manipulation.

### gtts

The **gtts** module is a Python module enable developers to convert text into speech by leveraging Google's Text-to-Speech API. It provides a convenient way to generate audio files or play speech directly from text, enhancing the accessibility and interactivity of applications.

### subprocess

The **subprocess** module is a Python library for running external processes, commands, and programs from within your Python scripts. It provides a powerful way to interact with the system shell, execute system commands, and capture their output, making it a versatile tool for automation and system integration tasks.

### keyboard

The **keyboard** module is a Python library that enables programmatically simulating and monitoring keyboard input. It allows you to automate and interact with keyboard events, making it useful for tasks like creating keyboard macros, automated testing, and simulating user input in various applications.

### pyautogui

The **pyautogui** module is a Python library for automating GUI interactions by simulating mouse and keyboard input. It enables developers to automate repetitive tasks, create GUI-based scripts, and perform UI testing and interaction with applications on a computer, making it a powerful tool for automation and testing purposes.

### webbrowser

The **webbrowser** module is a Python provides a simple interface for opening web browsers and displaying web pages, making it convenient for automating web-related tasks and opening URLs programmatically in your Python scripts.

### platform

The **platform** module is a Python provides a simple interface to access information about the host operating system, including details like the OS name, version, and hardware architecture, making it useful for cross-platform compatibility and system-specific code.

### uuid

The **uuid** module is a Python is used to generate and work with universally unique identifiers (UUIDs). These UUIDs are 128-bit values that are typically used for unique identification in various applications and systems.

### smtplib

The **smtplib** module is a Python is used for sending email messages using the Simple Mail Transfer Protocol (SMTP). It enables developers to create and send email messages programmatically, making it a valuable tool for automating email-related tasks in Python applications.

### sys

The **sys** module is a Python library that provides access to system-specific parameters and functions. It is often used for command-line arguments, interacting with the Python runtime environment, and other system-related tasks.

### plyer

The **plyer** module is a Python library that simplifies cross-platform access to common hardware features, such as notifications, camera, GPS, and more. It enables developers to create platform-independent applications with ease.

### time

The **time** module is a Python provides functionality for working with time, including functions for measuring time intervals, formatting time, and interacting with system time. It is commonly used for tasks such as benchmarking, scheduling, and date/time manipulation in Python programs.

### openpyxl

The **openpyxl** module is a Python library for working with Excel files (both .xlsx and .xlsm formats). It enables developers to create, modify, and extract data from Excel spreadsheets programmatically.

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

### 02-Deep dive and python modules

#### [01 find max number](02-Deep_Dive_and_Python_modules/01_find_Max_num.py)

simple program to print the max number from given list.

#### [02 find bitcoin price](02-Deep_Dive_and_Python_modules/02_find_bitcoin_price.py)

simple program get bitcoin price from api and print it in USD.

#### [03 make custom system keyboard shortcut](02-Deep_Dive_and_Python_modules/03_keyboard_shortcut.py)

simple program make a shortcut to open python course.

#### [04 print multi function inputs](02-Deep_Dive_and_Python_modules/04_print_multi_argument.py)

simple program to print the function input list and dic content without know len of list or dic.

#### [05 add multi function inputs](02-Deep_Dive_and_Python_modules/05_add_multi_parametes.py)

program to print the sum of input to function using multi argument style

### 03-Advanced python

#### [01 fireLink app](03-advanced-python/01_fireLinkApp)

simple program to make custom lib and use web browser module.

#### [02 i am bored](03-advanced-python/02_iAmBored.py)

simple program to use api to suggest tasks to do when i am bored.

#### [03 get my public ip](03-advanced-python/03_getMyPublicIP.py)

simple program to use api to get my public ip.

#### [04 setup vscode extension](03-advanced-python/04_setupVsCodeExtention.py)

train to use pyautogui module to open vs code then setup an extension.

#### [05 cpp file creation](03-advanced-python/05_cppFileCreation.py)

create .cpp and .h files with given name with a starter code.

### 04-OOP in python

#### [01 number of lines in file](04-OOP_files/01_numberOfLines)

simple program to count number of lines in file .

#### [02 number of words in file](04-OOP_files/02_numberOfWords.py)

simple program to count number of words in file .

#### [03 write list to a file](04-OOP_files/03_writeListToFile)

simple program to write list to txt file .

#### [04 gpio file generator](04-OOP_files/04_GPIOFileGenerator.py)

simple c code generator for avr GPIO driver.

#### [05 email checker](04-OOP_files/05_emailChecker.py)

simple email checker when computer is opening.

#### [06 battery notifier](04-OOP_files/06_batteryNotifier.py)

simple program to send notification when battery is low.

#### [07 get argument from terminal](04-OOP_files/07_getArgumentFromTerminal.py)

simple program get arguments from user in terminal and use it.

#### [08 print an ascii code for an input](04-OOP_files/08_ASCIIValueOfCharacter.py)

simple program to print ascii code of a character.

#### [09 .h parser to excel](04-OOP_files/09_.hParserToExcelFile)

simple program to parse functions into excel sheet.

#### [10 email alert](04-OOP_files/10_emailAlertWhenOpenLap.py)

program to send email when ever the laptop get opened with device name and mac.
