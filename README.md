# Clock

This is a clock that refreshes the screen every minute and generates the time and date in 
random locations every time that the screen refreshes. Honestly, I'm pretty happy with what I came
up with, while I'm positive there's improvements that could be made to the actual code, the clock
itself actually came out just how I imagined it. 

# Notes
- There used to be a bug where sometime a minute would pass, but the screen wouldn't refresh 
  for some reason. I'm not sure if I fixed this at some point, but it doesn't seem to happen anymore.
  It did happen pretty rarely though, and it would correct itself when the next minute passed. But 
  for the time being, I do not plan on looking any further into that issue.
- Adjustments may have to be made to accommodate different screens. It should still work,
  but it may not look as nice (for example, if you have a vertical screen or something).

# Possible future improvements to look into
- Making this into a screen saver.
- Making the day of the week generate above the date. This was the original plan, but I thought having
  them separate would look cooler. This should be an easy adjustment, but I think I like it more as
  it is.
- Replacing the use of textboxes with labels. Everything works with textboxes, but users can edit them,
  so I might need to look into making the switch or disabling the editing if possible. In theory, 
  this shouldn't be too hard to do, but idk...

# Some stuff that I learned about
- Tags are used to edit aspects of a widget (colors, text alignment, etc.). To create/edit a tag 
  you use `.tag_configure(...)`, but this doesn't actually activate the tag. To activate a tag you 
  have to use `.tag_add(...)`. Widgets can have multiple tags attached to them. And you can delete
  a tag using `.tag_delete(...)`.
- Apparently tkinter isn't "thread safe", so you can't use python's threading functions. However,
  tkinter has it's own version of "threads" to make up for this and allow for concurrency. It's
  `root.after(time, function, args*)`, time is in milliseconds and will call the given function
  with the args (if provided) after the specified number of milliseconds has passed. 
  - Make sure to omit the `()` after the function. For example, the following will call the 
    SayHi function after 1 second has passed:
      ```python
    import tkinter as tk
    
    root = tk.Tk()
        
    def SayHi():
        print("Hi")
        
    root.after(1000, SayHi)
      ```

# Resources
- [tkinter docs](https://tkdocs.com/tutorial/index.html)
- [geeksforgeeks tkinter tutorial](https://www.geeksforgeeks.org/python-tkinter-tutorial/)
- Idk if I actually needed this, but [tkinter gridlines](https://kyletk.com/index.php/2017/03/11/tkinter-grid-set-default-grid-size/)
- [timedate stuff](https://www.w3schools.com/python/python_datetime.asp)
- [textbox border (relief) settings](https://www.tutorialspoint.com/python/tk_relief.htm)

