"""
This may be used with proper edits as per your code.

The goal of this project was to make things simpler for all and
provide everyone an easy way to make a separator.

This only works for the root window (the CTk() function)
For frame separators, use the other file in main.
"""

from customtkinter import *
from typing import Any, Optional

def CTkWindowSeparator(master: Any,
                      size: int = 2, #1 doesn't work becuase CustomTkinter has an inbuilt function that rounds width and height to the nearest even number
                      length: int = 75, #It is 75 percent. 75% * 200 = Length of Separator
                      multiply: int = 200,
                      orientation: str = "Horizontal",
                      colour = Optional[Union[str, Tuple[str, str]]] = None):
  SetColour = colour
  LineLength = length/100 * multiply
  if orientation == "Horizontal":
    Separator = CTkProgressBar(master=master, height=size, width=LineLength)
  else:
    Separator = CTkProgressBar(master=master, width=size, height=LineLength)

  Separator.configure(progress_color=SetColour, fg_color=SetColour)
  return Separator
