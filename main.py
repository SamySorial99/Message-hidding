import sys
from PIL import Image
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


def Encode(pictureNameDotFormat,Image_new_name):
    Image1 = Image.open(pictureNameDotFormat)
    bitmap = np.array(Image1)
    asciiofmessage = np.array([])
    message = input("Enter message to Hide in picture")
    for character in message:
        asciiofmessage =np.append(asciiofmessage, ord(character))

    messageCoulmn = 2#random.randint(1, int(bitmap.shape[0]))
    messageRow = 2#random.randint(1, int(bitmap.shape[1]) - int(asciiofmessage.shape[0]))

    numberOfRows = (bitmap[1].size - messageRow) / asciiofmessage[0].size
    numberOfRowsInt = int(numberOfRows)
    if numberOfRows > numberOfRowsInt:
        numberOfRowsInt = numberOfRowsInt + 1

    print(asciiofmessage.size, messageCoulmn, messageRow)
    bitmap[-1,-1,0] = int(asciiofmessage.size)
    bitmap[-1,-1,1] = messageCoulmn
    bitmap[-1,-1,2] = messageRow
    ascciCodeIndex = 0
    for j in range(numberOfRowsInt):
        print(bitmap.shape[1])
        for i in range(messageRow,  bitmap.shape[1]):
            if ascciCodeIndex == asciiofmessage.size-1:
                break
            bitmap[messageCoulmn + j][i][0] = asciiofmessage[ascciCodeIndex]
            print("bitmap["+str(messageCoulmn + j)+"]["+str(i)+"][0]")
            ascciCodeIndex = ascciCodeIndex + 1
        if ascciCodeIndex == asciiofmessage.size-1:
            break
    Image1 = Image.fromarray(bitmap, 'RGB')
    Image1.save(Image_new_name)


def Decode (ImageNameDotFormat):
    asciiCode = np.array([])
    Image1 = Image.open(ImageNameDotFormat)
    bitmap = np.array(Image1)
    sizeOfMessage = bitmap[-1,-1,0]
    coulmn = bitmap[-1,-1,1]
    startingRow = bitmap[-1,-1,2]
    numberOfRows = (bitmap[1].size - startingRow) / sizeOfMessage
    numberOfRowsInt = int(numberOfRows)
    if numberOfRows > numberOfRowsInt:
        numberOfRowsInt = numberOfRowsInt + 1
    shit = 0
    for j in range(numberOfRowsInt):
        for i in range(startingRow, bitmap.shape[1]):
            if shit == sizeOfMessage:
                break
            asciiCode = np.append(asciiCode, bitmap[coulmn + j, i, 0])
            shit = shit +1
        if shit == sizeOfMessage:
            break
    asciiCode = asciiCode.astype(np.uint8).squeeze()
    ASCII_string = "".join([chr(value) for value in asciiCode])
    print(ASCII_string)


print("Notice that all pictures should be in png format to prevent a lossy conversion which leads to bad encoding\n")
choice = input("Choose :\nEncode a picture enter[1]\nDecode a Picture enter[2]\n")
if int(choice) == 1:
    Name = input("Enter name of the file dot it's format like picture.png : ")
    Edited = input("Enter name of the picture to be saved as Dot it's Format like picture.jpg")
    Encode(Name, Edited)
elif int(choice) == 2:
    Name = input("Enter name of the file dot it's format like picture.png : ")
    Decode(Name)
else: print("Enter a valid choice")

