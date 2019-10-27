# coding:utf-8
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import pyautogui
from kivy.core.window import Window
import numpy as np
import stuff
import androidApp_images

class MyGif(Image):
    pass

class Camera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self.pts= []
        self.fileNum= 0
        self.numOfSpellsCasted= 0
        self.boundaries = [([255,255,255], [255,255,255])]
        Window.fullscreen = True
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        
        ret, img= self.capture.read()
        
        if ret:
            gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (15, 15), 0)
            
            lower = np.array(self.boundaries[0][0], dtype = "uint8")
            upper = np.array(self.boundaries[0][1], dtype = "uint8")
 
            mask = cv2.inRange(img, lower, upper)
            self.black = cv2.bitwise_and(img, img, mask = mask)
             
            (minVal, maxVal, minLoc, maxLoc)= cv2.minMaxLoc(gray)
            
            #print(maxVal)
            if maxVal >= float(252):
                self.pts.append(maxLoc)
            else:
                image = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                name= './androidApp_images/frame%d.png' % (self.fileNum)
                #print("[%d] Creating files | name: %s" % (self.fileNum, name))
                cv2.imwrite(name, image)
                x=  stuff.read_file(name)
                if x == "fire":
                    print("Eat fire")
                elif x == "water":
                    print("Eat water wesley")
                elif x == "wind":
                    print("Eat wind kram")
                elif x == "earth":
                    print("Momma earth")
                else: print("Nothing matched")
                self.numOfSpellsCasted+= 1
                self.fileNum+= 1
                self.pts= []
            
            for (x,y) in self.pts:
                #cv2.circle(img, i ,15 ,[0,0,0], -1)
                print(x, " | ",y)
                cv2.circle(self.black, (x, y) ,15 ,[255,255,255], -1)
                 
                
            buf1 = cv2.flip(self.black, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(self.black.shape[1], self.black.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture
        
        

class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = Camera(capture=self.capture, fps=5000)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    CamApp().run()