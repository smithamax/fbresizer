
fbresizer
=========


Install
-------

Requires the python library [PIL](http://www.pythonware.com/products/pil/).

Python easy install.

    $ easy_install PIL

or apt-get

    $ sudo apt-get python-imaging

or just download the installer.

Note that I had some problems getting the installer to work on windows with 64 bit python.

---

Once you have PIL you can simply use the `main.py` or the `fbresizer` shell script.
From here on I'll be referring to `fbresizer` but you could also use `python main.py` if you're on windows.


Usage
-----

For a simple help use

    $ fbresizer -h

The flags avalible are:

- __-l__ ___length___ resize image so the longest side is _length_.
- __-w__ ___imgfile pos___ place a watermark image at _pos_. Watermarks can be positioned absolutely using an _x,y_ pair (no spaces) or using `tl` top left, `br` bottom right, `bl` bottom left or `tr` top right.
- __-o__ ___output___ put the resized copies in _output_ directory.
- __-p__ ___prefix___ save the resized images with _prefix_.
- __-v__ verbose mode, print the progress.
- __--width__ ___width___ resize images to _width_.
- __--height__ ___height___ resize images to _height_.


Examples
--------

an example of resizing some images.

    $ fbresizer -o output image.jpg

this will resize the images so the longest side is 960px (perfect for Facebook),
and save it to the `output` directory

you can also add a watermark

    $ fbresizer -w watermark.png br -p s image.jpg

this command will resize the image, place the watermark in the bottom right(`br`),
and save the image in the original directory with the prefix 's' `-p s`.
