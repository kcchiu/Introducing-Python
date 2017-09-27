Course: CIS-581
Content: Project1
Author: Kaun-Cheng Chiu
PennKey: chiuk
Notes:
1. The test images are stored in a single folder "canny_dataset"
2. The api scipy.interpolate.interp2d from the scipy package was used to calculate the 2d interpolation in nonMaxSup.py
3. The result images are at the top level of this folder. They are named by the order they run. 
4. XX-1.png are the result image from utils.visDerivatives. XX-2.png are the rsult image from utils.visCannyEdge.

---------Challange 3---------
The function for challange 3 is challenge_3(I,im, E) in helpers.py. The resulting images are in the Challenge3 folder. 
The images corresponding coordinates are as follow:
1. (0,0) is the original image.
2. (0,1) is the colored edge image.
3. (0,2) is the canny edge image in gray scale.
4. (1,0) is the edge image in red.
5. (1,1) is the edge image in green.
6. (1,2) is the edge image in blue.