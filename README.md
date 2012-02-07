
fbresizer
=========


Install
-------

Requires the python library [PIL](http://www.pythonware.com/products/pil/).

Python easy install.

    $ easy_install PIL

apt-get

    $ sudo apt-get python-imaging

or just download the installer.

Note that I had some problems getting the installer to work on windows with 64 bit python.

---

Once yo have PIL you can simply use the `main.py` or the `fbresizer` shell script.
From here on I'll be referring to `fbresizer` but you could also use `python main.py` if you're on windows.


Usage
-----

For a simple help use

    $ fbresizer -h

an example of resizing some images.

    $ fbresizer -out output image.jpg

this will resize the images so the longest side is 960px (perfect for Facebook),
and save it to the `output` directory

you can also add a watermark

    $ fbresizer -w watermark.png br -p s image.jpg

this command will resize the image, place the watermark in the bottom right(`br`),
and save the image in the original directory with the prefix 's' `-p s`.
