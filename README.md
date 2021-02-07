# TemplateMatching
This is a simple Python script for Template Matching task. I take the image and uses **cv2.matchTemplate** function, which uses FFT based correlation between the input image and template. However, this method is rotation variant, meaning that it does not perform matching if the template or input image is rotated. In order to make it rotation invariant, I rotate the template image in different angles and try matching for each angle. Score for each rotational angle is stored and best scored match is given as final result.

Although this method is robust, it works slow. In order to speed up the process, first, I create an image pyramid and downsize both input and template images by 0.5. Afterwards, to have binary features for increasing the matching success, I apply a threshold and convert image to binary. Then do a quick template matching on those binary, downsized images with 180 different rotational angles and record the scores for those angles.

After we get the scores for small and 180 rotational angles, for a finer grained matching, I apply template matching using full frames around the angle that gave maximum score in previous run. The angle that gives the highest score is recorded with the top left coordinates.

Finally, for applying rotation on coordinates, I use a rotational matrix with the tilt angle and rotate the corner points with respect to their center. 

It requires following libraries:

- OpenCV
- Numpy
- Tqdm

## Run Demo
In order to run the script:
`$ python3 templateMatching.py Images/StarMap.png Images/Small_area.png `
where, _StarMap.png_ is the search image and _Small_area.png_ is the template that we wanted to find.

## Output
The script outputs the corner points of the found template and the rotational angle of the template.

    Top Left: [855,150]
    Top Rigth: [969,150]
    Bottom Left: [855,264]
    Bottom Rigth: [969,264]
    Tilt Angle: 0.0 degree
    
## Example Small Area Outputs
The output locations of _Small_area.png_ and _Small_area_rotated.png_ is found by scirpt as follows:

### Small_area.png
    Top Left: [855,150] 
    Top Rigth: [969,150]
    Bottom Left: [855,264]
    Bottom Rigth: [969,264]
    Tilt Angle: 0.0 degree
    
### Small_area_rotated.png
    Top Left: [420,639]
    Top Rigth: [552,560]
    Bottom Left: [499,771]
    Bottom Rigth: [631,692]
    Tilt Angle: 31.0 degree
    
When we visualize these coordinates, we can see the locations of the small patches:
![](https://github.com/melihpeker/TemplateMatching/blob/main/Images/output.png)
> Bounding boxes drawn according to output of the algorithm.

    
