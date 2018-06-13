---
layout: post
title: Pride flags with Pillow
tags: pride pillow python
---

One of the bigger things I worked on last year was the image server for the new Wellcome Collection website.
We have entries for 110k images, all served through a IIIF Image server, Loris.

IIIF is a series of standards used by museums and libraries for serving images.
A lot of images in those institutions are extremely large – for example, medical photography or high-resolution digitisation – and sending the entire file on every request would get expensive!
The IIIF APIs let a client make a request for specific regions or resolutions of an image, which has a dramatic bandwidth saving.

The format of a IIIF Image URL is as follows:

[example]

So, for example, requesting:

[red stripe]

Gets you the first 100*100 pixels from the top left-hand corner of the image L000001.jpg, rotated by 45 degrees, with a grayscale colour profile and as a JPEG.

# Building a manifest

Found example of multi image canvas

# Combine images with Pillow

The IIIF Image API lets us select the right crop of each of the images.
Next, we need to combine them, one on top of the other.
For this, I turned to Pillow, a Python library for manipulating images.

In Pillow, individual images are represented by the Image class.
For example:

from PIL import Image

im = Image.open('example.jpg')

First, I want a way to combine individual images into a single image.
I wrote a function to stack images, like so:

def combine_images_vertically(images):
if iter(images) is not iter(images): raise ValueError

total_width = max(im.width for im in images)
total_height = sum(im.height for im in images)
new_im = Image.new('RGB', (total_width, total_height))

y_offset = 0
for im in images:
new_im.paste(im, (0, y_offset))
y_offset += im.height

return new_im

Gets a list of Image objects
Not loaded from file at this point – only deal with in-memory Image objects
Much better to test (sans IO)

Iter foo
https://effectivepython.com/2015/01/03/be-defensive-when-iterating-over-arguments/

Get dimensions of new image, create new Image instance

Then paste images in
Track existing height with y_offset

Fun fact: I helped out in the height attribute in images!

Then we need to get Images from the IIIF URLs.
Here's a another wrapper:

from io import BytesIO

from PIL import Image
import requests

def im_from_url(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return Image.open(BytesIO(resp.content))

Plus docstring
BytesIO turns it into a file like object that can be read, without ever having a file on the fs

Putting these pieces together, I can write a script like this:

urls = […]
images = [im_from_url(u) for u in urls]
new_im = combine_images_vertically(images)
new_im.save('flag.jpg')

Then I went one step further, and added a little wrapper, so it gets configured from a file.
Full script:

You can download a copy of the JSON manifest.



# generating manifests and images

Explain script

Height is mine!!
# Examples

Now some examples
View all as a manifest

Or click through to see images
Served through IIIF, naturally ;-)

Rainbow
Asexual
Trans
Bisexual
Genderqueer
Aromantic
Lesbian (?)

# Next steps

Once you've picked out the images, you don't have to render them as a static image – another approach might be creating a IIIF manifest
Let's you draw multiple images on a single canvas, and embed annotations - for example, links to the original descriptions
Image file can travel without metadata!

Our resident data scientist Harrison has been doing work to detect colour palletes in our images
(spoiler: lots of beige!)
MY approach for finding images is typing colours into the search box, which relies on somebody using the colour name in some of e image metadata
Better: use this search

Don't know when time will arise, so figured I'd post – they'll be extra posts if/when I have time
For now, enjoy!
