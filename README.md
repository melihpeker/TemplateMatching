# TemplateMatching
This is a simple Python script for Template Matching task. It requires following libraries:

- OpenCV
- Numpy
- Tqdm

## Run Demo
In order to run the script:
`$ python3 templateMatching.py StarMap.png Small_area.png `
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

- Small_area.png

    Top Left: [855,150]
    Top Rigth: [969,150]
    Bottom Left: [855,264]
    Bottom Rigth: [969,264]
    Tilt Angle: 0.0 degree

- Small_are_rotated.png
    Top Left: [420,639]
    Top Rigth: [552,560]
    Bottom Left: [499,771]
    Bottom Rigth: [631,692]
    Tilt Angle: 31.0 degree
    
When we visualize these coordinate, we can see the locations of the small patches.

Image:

![](https://pandao.github.io/editor.md/examples/images/4.jpg)

> Follow your heart.

    
