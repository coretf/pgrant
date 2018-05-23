
# pgrant
A GUI wrapper for a TF2 promotional distribution script.

## Installation

For Linux systems, you should already have Python 3 installed. You can check if you have it by typing in the following command in terminal:
`python3`

For Windows, download any Python version that is greater than 3.4 [here](https://www.python.org/downloads/). Please double check that, Python 2.7 will **not** run this.

## Running 

For Linux, download the [latest release](https://github.com/mkrl/pgrant/releases), put it anywhere on your disk. Open up a terminal in the directory you have this program in, and use `python3 grant.py` to run the program.

For Windows, if you have done everything right, you can either follow the Linux way or double-click on the program and it should start.

## Usage

On startup, you'll see 2 windows: console and a window prompting your Steam API key and a promo ID that represents the item you are giving away.

The program works with a file formatted in the following way: 1 steamID64 per line.
SteamID64 is a 17-symbol digit string.

This is an example of how your input file can look like:

`file.txt`:
```
76561198071371521
76561198071371521
76561198071371511
76561198071361421
76561198071371551
76561198071312451
```

Fill in your API key and a Promo ID, press "Load a file" button and select the file you need. The path to the file will appear at the bottom of the window. 
The console window will show how many SteamIDs it detected in the file.

Once the file was loaded, you'll be able to press the "Grant" button. Once pressed, the window may become non-responsive, this is normal. 

Take a look at the console window, it will show you the progress of the distrubution process.
You'll see something that looks like this:

```
Granting [promo id] to:
76561198071371521 [SUCCESS!]
76561198071371511 [SUCCESS!]
76561198071361421 [SUCCESS!]
76561198071371551 [SUCCESS!]
76561198071312451 [SUCCESS!]
76561198071371551 [SUCCESS!]
--------------------------
Finished file processing
```

If the distribution fails, you'll see `[FAIL (reason)]`  instead of the usual success message. Usually it will be either invalid token or internet connection problems.

## Logging

On every program launch, it will generate/overwrite `log.txt` file, at the same directory the program is running.
This file is basically an echo of what you'll see in the console window.

If you had some of your requests failed, be sure to save your log / steamids that failed into another place and try granting again later.
