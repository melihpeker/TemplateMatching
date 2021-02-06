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
`Top Left: [855,150]
 Top Rigth: [969,150]
 Bottom Left: [855,264]
 Bottom Rigth: [969,264]
 Tilt Angle: 0.0 degree `
