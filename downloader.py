import argparse as ap
import imgur_download as imd

parser = ap.ArgumentParser()
parser.add_argument('keyword', type = str, help = "Type the keyword to search on imgur.")
parser.add_argument('-q', type = int, dest = 'q', help = 'Number of images.', default = 0)
parser.add_argument('--hr', action = "store_true", help = "Type this to download high resoultion pics.")

args = parser.parse_args()

if not args.q and not args.hr:
    imd.scrape_images(args.keyword)

elif args.q and not args.hr:
    imd.scrape_images(args.keyword, args.q)

elif args.q and args.hr:
    imd.scrape_images(args.keyword, args.q, args.hr)

elif not args.q and args.hr:
    imd.scrape_images(args.keyword, high_resolution = args.hr)
