import Image
import os
import sys
import argparse
from glob import glob

rots = {
    1: 0,
    3: 180,
    6: 270,
    8: 90
}


def scale_size(size, width=None, height=None):
    w, h = size
    if width:
        return (width, int((float(h) / w) * width))
    if height:
        return (int((float(w) / h) * height), height)
    return size


def resize_image(img, longside=960, width=None, height=None):
    w, h = img.size
    if height:
        newsize = scale_size(img.size, height=height)
    elif width:
        newsize = scale_size(img.size, width=width)
    elif longside:
        if w < h:
            newsize = scale_size(img.size, height=longside)
        else:
            newsize = scale_size(img.size, width=longside)
    else:
        return img

    return img.resize(newsize, Image.ANTIALIAS)


def parse_position(posStr, img, mark):
    if posStr.find(',') != -1:
        x, y = posStr.split(',')
        pos = (int(x), int(y))

    else:
        bottom = img.size[1] - mark.size[1]
        right = img.size[0] - mark.size[0]

        if posStr == 'br':
            pos = (right, bottom)
        if posStr == 'bl':
            pos = (0, bottom)
        if posStr == 'tr':
            pos = (right, 0)
        if posStr == 'tl':
            pos = (0, 0)

    return pos


def watermark_image(img, mark, pos):
    if type(pos) == str:
        pos = parse_position(pos, img, mark)
    img.paste(mark, pos, mark)


def save_image(img, imgpath, prefix=None, outdir=None):
    name = os.path.basename(imgpath)
    if outdir == None:
        outdir = os.path.dirname(imgpath)

    if prefix:
        name = prefix + name

    img.save(os.path.join(outdir, name))


def process_images(args):
    watermarks = []

    if args.watermarks:
        for markpath, pos in args.watermarks:
            watermarks.append((Image.open(markpath), pos))

    for imagepath in args.images:
        img = Image.open(imagepath)
        img = fix_rotation(img)

        if args.width:
            img = resize_image(img, width=args.width)
        elif args.longside:
            img = resize_image(img, longside=args.longside)
        elif args.height:
            img = resize_image(img, height=args.height)
        else:
            img = resize_image(img)

        for mark, pos in watermarks:
            watermark_image(img, mark, pos)

        if args.show:
            show_image(img)

        if args.verbose:
            print imagepath

        save_image(img, imagepath, args.prefix, args.outdir)


def get_orientation(img):
    # rotation refrence http://sylvana.net/jpegcrop/exif_orientation.html
    # EXIF usage http://stackoverflow.com/a/765403/730767
    info = None

    if img._getexif:
        info = img._getexif()

    if info:
        for tag, value in info.items():
            if tag == 274:
                return value

    return None


def fix_rotation(img):
    o = get_orientation(img)
    if o:
        return img.rotate(rots[o])
    else:
        return img


def show_image(img):
    img.show()


def main():
    parser = argparse.ArgumentParser(description='')

    resizers = parser.add_mutually_exclusive_group()

    resizers.add_argument('--width',
            metavar='pixels', type=int,
            help=''
            )

    resizers.add_argument('--height',
            metavar='pixels', type=int,
            help=''
            )

    resizers.add_argument('-l', '--longside',
            metavar='pixels', type=int,
            dest='longside',
            help=''
            )

    parser.add_argument('-w', '--watermark',
            metavar=('img', 'pos'),
            nargs=2, action='append',
            dest='watermarks',
            help=''
            )

    parser.add_argument('-o', '--output-dir',
            metavar=('dir'),
            dest='outdir',
            help=''
            )

    parser.add_argument('-s', '--show',
            action='store_true',
            help=''
            )

    parser.add_argument('-v', '--verbose',
            action='store_true',
            help=''
            )

    parser.add_argument('-p', '--prefix',
            metavar=('str'),
            help=''
            )

    parser.add_argument('images',
            nargs='*',
            help='images to resize'
            )

    args = parser.parse_args()

    if sys.platform == 'win32' and len(args.images) > 0:
        args.images = glob(args.images[0])
    print args
    process_images(args)

if __name__ == '__main__':
    main()
