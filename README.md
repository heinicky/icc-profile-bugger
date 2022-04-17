# Icc Profile Bugger
this converts an image into a 300x300 square that will not view on most iOS and PC Devices but will view on Android Devices.

# How does it work?
this changes the iCC profile on the image to a specially crafted one which shows on most Default Android Color Profiles but does not on most iOS and PC Color Profiles

# Screenshots
![image-on-pc](https://files.catbox.moe/ymmd5m.png)
![image-on-android](https://files.catbox.moe/z6s0ul.png)

# Notice
for people who still have no idea how this works but still want to use it, it will only work in places that don't post process images like discord.
also don't skid

# Arguments
There is 1 Required Argument and 2 Optional Arguments
- Path               | (path) (required argument)
- Image Name         | (name) (optional, defaults to bug.png)
- Compatibility Mode | (compatibility) (defaults to True)

# Compatibility Mode On
Compatibility Mode Pastes the Image onto the 300x300 Model Image, so you will need to have your images formatted that way or just have it be a square.

# Compatibility Mode Off
This attempts to copy the iCC profile from the Model image onto your image. this easily breaks it, but it does work sometimes and does not require any Rescaling. use PNG.

# Credits
Thank you to iLHacks#0001 for giving me the Model PNG 
