from PIL import Image 
im=Image.open('1.png')
im1=im.load()
w,h=im.size
#im.show()
im2=im.copy()
im2=im.resize((10,10))
im3=im2.load()
w1,h1=im2.size
for i1 in range(im2.size[0]):
    for j1 in range(im2.size[1]):
        im3[i1,j1]=0
im2.show()
#im3[1,2]=0
print(im1[201,157])
print(im3[1,2])
x,y=200,155
k,l=0,0
if((x+w1-1)<=w and  (y+h1-1)<=h):
    for i in range(x,x+w1):
        l=0
        for j in range(y,y+h1):
#            print(str(k)+" "+str(l))
#            print(im3[k,l])
#            PixelAccess.putpixel(self,(x,j),im3[k,l])
            im1[i,j]=im3[k,l]
            l+=1
        k+=1

print(im1[201,157])
im.show()
#im2.show()