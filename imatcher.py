import os
import cv2
import pprint

class Imatcher():
    def __init__(self, image_path: str):
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        
    def compare(self, path: str) -> dict:
        dct = dict()

        if os.path.isdir(path):
            exts = ['jpg', 'jpeg', 'bmp', 'png']
            for fname in (f for f in os.listdir(path) if any(f.endswith(e) for e in exts)):
                image = cv2.imread(os.path.join(path, fname), cv2.IMREAD_COLOR)
                dct[fname] = self.get_match(image)

        else:
            image = cv2.imread(path, cv2.IMREAD_COLOR)
            dct[path] = self.get_match(image)

        return dct

    def get_match(self, image) -> float:
        '''
        returns percentage of match dd.dd%
        '''
        image_match = cv2.matchTemplate(self.image, image, cv2.TM_CCOEFF_NORMED)[0][0]
        return round(image_match * 100, 2)


if __name__ == "__main__":
    imatcher = Imatcher('1.jpg')
    pprint.pprint(imatcher.compare('2.jpg'))
