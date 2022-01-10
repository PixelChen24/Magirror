from skimage import io
from skimage.filters import gaussian


def get_Container(pic,lt:tuple,rb:tuple,sigma):
    img=io.imread(pic)
    ROI=img[lt[1]:rb[1],lt[0]:rb[0],:]
    dst=gaussian(ROI,sigma)
    filename="Background/Maoboli/"+str(lt)+str(rb)+'.png'
    io.imsave(filename,dst)
    return filename


if __name__ =="__main__":
    get_Container("Background/1080.jpg",(0,0),(540,960),20)