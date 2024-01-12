### Install and import opencv
### Hint: PyPi.org
import cv2



if __name__ == "__main__":
    ### First read the image and assign it to a variable.
    image = cv2.imread(r"C:\Users\Surface\IMG_200714_094055_0043_RGB.JPG")

    ### Now display the image. Therefore don't forget to use the waitKey() function.
    cv2.imshow("Orignales Bild", image)
    cv2.waitKey(0)
    ### What is the integer argument doing at the waitKey() function? 
    ### Hint: An argument is something that you insert into a function's brackets when calling it. 
    """Die Funktion cv2.waitKey() nimmt einen ganzzahligen Wert als Argument entgegen. Dieser Wert gibt die Zeit in Millisekunden an, wie lange das Programm warten soll, bis es fortfährt.
    Bei cv.waitKey(0) wartet er unendlich lang und fährt es fort, wenn man das angezeigte Bild schließt."""

    ### You have probably noticed that the image is too large to be shown completely on your computer screen.
    ### What is the current image shape?
    print(f"Aktuelle Bildgröße: {image.shape}")

    """Aktuelle Bildgröße: 3456*4608 Pixel"""

    ### Resize the image to size (922, 691) and continue with the resized image for the next tasks.
    Neues_Bild = cv2.resize(image, (922, 691))
    cv2.imshow("Neues_Bild", Neues_Bild)
    cv2.waitKey(0)

    ### Blur the image and transform it into grey scale.
    GaussianBlur = cv2.GaussianBlur(Neues_Bild, (5, 5), 0)
    Graues_Blur_Bild_Gaussian = cv2.cvtColor(GaussianBlur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grau Gaussian Blur", Graues_Blur_Bild_Gaussian)
    cv2.waitKey(0)


    ### Use another blurring function from cv2 which is not cv2.GaussianBlur().
    MedianBlur = cv2.medianBlur(Neues_Bild, 5)
    Graues_Blur_Bild_Median = cv2.cvtColor(MedianBlur, cv2.COLOR_BGR2GRAY)

    ### Finally, display the image.
    cv2.imshow("MedianBlur", Graues_Blur_Bild_Median)
    cv2.waitKey(0)

    ### Mention one difference of the method you chose compared to cv2.GaussianBlur().
    """cv2.medianBlur() verwendet einen Medianfilter statt einer gewichteten Summe wie cv2.GaussianBlur()."""
    

    ### Create a binary mask of the blurred grey scale image with the cv2.inRange() function.
    inRange_Filter = cv2.inRange(Graues_Blur_Bild_Median, 128, 255)


    ### Try to tweak the boundaries. Most of the plants should be set to white and the soil to black.
    inRange_Filter_Update = cv2.inRange(Graues_Blur_Bild_Median, 60, 128)
    

    ### What is the minimum and what is the maximum boundary? Hint: Images are usually encoded as 8bit values.
    """Der minimale Grenzwert ist 0 (schwarz) und der maximale Grenzwert 255 (weiß)"""
    

    ### Now apply the mask to the resized RGB image. Therefore use the cv2.bitwise_and() function.
    Maske_Original_Bild = cv2.bitwise_and(Neues_Bild, Neues_Bild, mask=inRange_Filter_Update)
    cv2.imshow("Maske angewendet auf originales Bild", Maske_Original_Bild)
    cv2.waitKey(0)
    ### Congratulations: If everything went right, you now segmented the maize plants from the soil!


    ### Bonus question: Some of the arguments that you give to the cv2.bitwise_and() function are redundant. 
    ### Which arguments are redundant and what is the reason for the redundancy?
    """Die Angabe des Quellbildes ist redundant. Der Grund hierfür ist, dass das Ziel ist, die Maske nur mit einem
    einzigen Bild zu kombinieren, weshalb das Bild sowohl die Quelle als auch das Ziel ist, wodurch die Angabe
    redundant wird"""
    
    
    ### Save the image.
    cv2.imwrite(r"C:\Users\Surface\Assignment_02_Ergebnisbild.jpg", Maske_Original_Bild)
