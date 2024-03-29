## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)
![Lanes Image](./examples/example_output.jpg)

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./output_images/calibrate.png "Calibration"
[image2]: ./output_images/undistorted.png "Undistort"
[image3]: ./output_images/exampleimg.png "Combined Filter Binary"
[image4]: ./output_images/unwarped.png "Unwarp"
[image8]: ./output_images/threshold.png "threshold"
[image9]: ./output_images/curvefitting.png "curvefitting"
[image10]: ./output_images/Equation.png "Equation"
[image11]: ./output_images/Example.png "Example"

[image5]: ./test_images/test5.jpg "Original Pic"
[image6]: ./test_images/test5_line.png "Detect Lane Lines"
[image7]: ./test_images/prefinal.png "Final Output"
[image7]: ./test_images/Equition.jpg "Curve Radius Calculation"

[video1]: ./videos/project_video_output.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Camera Calibration

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  The calibration logic is in calibration.py. I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]


### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, the following images are original test image and undistorted one accordingly:
![alt text][image2]

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image. Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image (thresholding steps at lines 12 through 42 in `lines.py`). Here's an example of my output for this step. 

![alt text][image8]

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `unwarp()`, which is in the file `unwarp.py` The `unwarp()` function takes as inputs an image (`img`), as well as source (`src`) and destination (`dst`) points.  The `src` and destination `dst` is chosen mannually using the pic straight_line1.png

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 576, 464      | 450, 0        | 
| 262, 682      | 450, 720      |
| 1049, 682     | 830, 720      |
| 707, 464      | 830, 0        |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

I did this in `lines.py`. First, use histgram to find line start point, then use sliding window to locate the most possible line points. Then I curvefit the line points with a 2nd order polynomial. In the real application in video, if previous frame have good detection, next frame only need to find line points around fitting lines of previous frame.

![alt text][image9]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in lines 123 through 141 in my code in `lines.py`,based on the following equation:

![alt text][image10]

I then scaled it from pixel space to real world space in meters. 

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

The fitted 2nd order polynomial line should be transfer back from bird view to normal view. Then they can be plotted on top of the original picture as following.
I implemented this step in `CODE.ipynb` in the function `process_image()`.  Here is an example of my result on a test image:

![alt text][image11]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video_output.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

1. The code would fail when the lane marks are partially or fully covered with snow or other objects. 

2. In order to have more stable results especially the curve radius calcuation, robust fitted lines of previous frame should be stored, then averaged to get more smooth and reasonable result.

3. Combined threshold should be fine tuned to get more useful data. The gradient should be used to improve output in certain condition.



