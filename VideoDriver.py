import os 
import platform 

def setup_video():
    position = 100, 50 #positions screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
    print(platform.system())
    #picks the platform for the SDL driver
    #TODO Needs to fix for other platforms that aren't mac
    if platform.system() == 'Windows':
        os.environ['SDL_VIDEODRIVER'] = 'windib'
    if platform.system() == "Linux":
        os.environ['SDL_VIDEODRIVER'] = 'x11'


