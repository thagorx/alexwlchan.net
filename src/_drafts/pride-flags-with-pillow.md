---
layout: post
title: Pride flags with Pillow
tags: pride pillow python
---

One of the bigger things I worked on last year was setting up the image server for the new Wellcome Collection website.
We have entries for 110k images, all served through a IIIF Image server, [Loris][loris].

Briefly quoting from [my blog post about Loris][loris_stacks]:

> IIIF is the [International Image Interoperability Framework][iiif], which is a set of standards for serving large images. It’s an open standard used by many libraries and archives, and it provides a way to combine resources from different collections. When a client asks for an image, they can make a very particular request — such as size, or crop, or rotation—and the server prepares the exact image they want, and sends that along. It’s a practical way to deal with really large images.

[loris_stacks]: https://stacks.wellcomecollection.org/using-loris-for-iiif-at-wellcome-6ed1fefaf801
[loris]: https://github.com/loris-imageserver/loris
[iiif]: http://iiif.io/

The format of our IIIF Image URLs is as follows:

```
https://iiif.wellcomecollection.org/image//{identifier}/{region}/{size}/{rotation}/{quality}.{format}
```

So, for example, requesting the URL:

```
https://iiif.wellcomecollection.org/image/B0009864.jpg/0,0,500,750/300,/90/default.jpeg
```

gets you the image B0009864.jpg from our collection.
More specifically, it's a 500&times;750 region from the top left-hand corner, resized to be 300 pixels wide, rotated through 90&deg; and as a JPEG.

This is what it looks like:

<figure style="max-width: 450px">
  <img src="/images/2018/mouse_kidney.jpg">
  <figcaption>
    Extract from an image of a mouse kidney.
    Image credit: <a href="https://wellcomecollection.org/works/brmfsunp">Kevin Mackenzie, University of Aberdeen</a>.
  </figcaption>
</figure>

On my way home on Monday night, I began poking through the image set, and I was thinking of fun things to do.
I'd been thinking about ways to riff on the [rainbow flag][flag], and I tried to see if I could do something with the images:

[![A rainbow flag, with the six coloured stripes replaced by segments of different images.](/images/2018/rainbow_450.jpg)](/images/2018/rainbow.jpg)

In the rest of this post, I'll explain how I used [Pillow][pillow] to generate this image.
What's particularly fun is that I wrote all the code for this on a train, with just my iPad and [Pythonista][pythonista].

[flag]: https://en.wikipedia.org/wiki/Rainbow_flag
[pillow]: https://pillow.readthedocs.io/en/5.1.x/
[pythonista]: http://omz-software.com/pythonista/

---

https://wellcomecollection.org/works/d6w73y9p?page=5&query=blue
https://wellcomecollection.org/works/ryfuzafq?page=3&query=blue

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
