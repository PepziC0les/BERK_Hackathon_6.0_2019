# coding:utf-8
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.pts= []
        
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        
        ret, img= self.capture.read()
        
        if ret:
            gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            gray = cv2.GaussianBlur(gray, (15, 15), 0)

            (minVal, maxVal, minLoc, maxLoc)= cv2.minMaxLoc(gray)
            
            print(maxLoc)
            print(maxVal)
            self.pts.append(maxLoc)
            for i in self.pts:
                cv2.circle(img, i ,15 ,[0,0,0], -1)
            
            buf1 = cv2.flip(img, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(img.shape[1], img.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture
        
        

class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=1000)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    CamApp().run()