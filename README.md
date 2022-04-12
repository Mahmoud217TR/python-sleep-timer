# Python Sleep Timer

This is a timer written in Python to put your PC to sleep, **Windows Only**.

<p>
   <img align='right' src='src/artwork/Logo.png' width='256'>
</p>

**Features:**
* 2 options to run the program (Console, GUI).
* Sleep timer goes from 0:0:0 to 24:59:59.
* Easy to use.
* The Console option uses regex to detect time.

**Table of Contents**
* [Requirements](#requirements)
* [How To Use](#how-to-use)
    * [Console](#console)
    * [GUI](#gui)
* [Notes](#notes)

***

<p align='center'>
   <img src='gallery/Photo 1.jpg' width='30%'>
   <img src='gallery/Photo 2.jpg' width='30%'>
   <img src='gallery/Photo 3.jpg' width='30%'>
</p>

***

## Requirements
* Only Python


## How To Use

You have 2 options:
* [Console](#console)
* [GUI](#gui)


### Console

To use the console option you have 2 ways:
* Run the executable file `console.exe`.
* Open Command Prompt in the `src` directory, then run this command `python console.py`.


### GUI

This is a **lot larger** in size because of pyqt5 package.

Here we have 3 methods:
* Run the executable file `setup.exe` and install the program, you will find a shortcut on the desktop named `Sleep Timer` you can run it.
* Unzip `gui.rar` then run the executable file inside the unziped folder called `gui.exe`.
* Open the command Prompt in `src` directory, then run this command `python gui.py` **(requires [PyQt5](https://pypi.org/project/PyQt5) package)**.


## Notes

* I used [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) to make an excutable file.
* The large size of GUI id because of the [PyQt5](https://pypi.org/project/PyQt5) package.
* If you have any problem please make an issue.
* If you have any modification feel free to make a pull request.
