# Photo-Viewer_Tkinter
A photo viewer app created using Tkinter, in Python

## How to use:
### Prerequisites 
Add images to the `media/images` (600x600 png) and 
`media/smol` (190x190 png) folders, and the 
audio files to the `media/sounds` folder. The 
names of the files in all the folders
must be identical, barring the file extension, in 
order for the program to work correctly. Example files
are present in the repository. A helpful 
summary is given below.
#### File requirements
In the `media/images` folder: \
Filetype: `.png` \
Size: 600x600 \
eg. `piano.png, airplane.png, slap.png`

In the `media/smol` folder: \
Filetype: `.png` \
Size: 190x190 \
eg. `piano.png, airplane.png, slap.png`

In the `media/sounds` folder: \
Filetype: `.mp3` \
eg. `piano.mp3, airplane.mp3, slap.mp3`

#### **Note:  all file names must be identical across folders.**
### Running
Once the prerequisites are met, Run the main.py file. 

## Technical details
### Project Structure
This project is object-oriented. There is only one 
python file containing all the code. A singular class
contains all the code, apart from reading files
from disk, and the actual running code.

### Quirks
The `__delete_everything` and `__create_everything`
came about as I realised that I was using a lot of 
code to clear the screen and repopulate it as I 
navigate through the different sections of the
application. This code ended up helping me, since it
is easier to add functionality now, as everything
can be cleaned up and recreated in just 2 function
calls. Other benefits include the cleanliness of all 
the methods in the code, especially `__init__`. 


The `__update_buttons` method is the longest method
in the class, and while I did consider splitting it
up, I decided not to, since it is not all that difficult
to understand, and keeping it together does not weigh
upon the readability of the code.


One issue I faced was the `__view_gallery` method. As 
it stands, the application works without any bugs as 
long as the window size is not altered, and there are
fewer than 9 images. In fact, the audio files are not
a requirement at all; in their absence, the images 
will simply be displayed without any accompanying 
sounds (read: program does not self-destruct). The 
code contains the issue commented out, I shall repeat
it here: 
``` python
        # It seems that I cannot have a clickable images with a scroll bar.
        # I can make a scroll bar of Tkinter.Text() objects which would be images, but not clickable.
        # Or I can make a scroll bar with Tkinter.ListBox() items which would be clickable, but not images.
        # can't find any other solution
```

### Final notes
If you made it this far, thank you for reading.