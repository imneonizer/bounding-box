### Imbo rescaling argument example

The rescaling feature helps in handling very high resolution image, the problem with high resolution image is label texts and bounding boxes looks very small and thin.

**To overcome this problem a quick and simple hack is to**:

1. resize the input image to a smaller dimension
2. draw the text and boxes
3. resize image back to original dimension
4. return the image

Similarly if very small resolution image is passed, resize them to larger dimension on step 1.

````bash
python rescale_draw.py
````

<table>
    <h3>Original Image</h3>
    <img src="high_resolution.jpg", width="800px">
    <hr>
    <h3>rescale = False</h3>
    <img src="without_rescaling.jpg", width="800px">
    <hr>
    <h3>rescale = True</h3>
    <img src="with_rescaling.jpg", width="800px">
</table>

