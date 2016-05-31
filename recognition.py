from videoai.recognition import Recognition 
import argparse


parser = argparse.ArgumentParser(description='VideoAI command line tool.', epilog='Have fun using VideoAI.')
parser.add_argument('-i', '--image', dest='image', help='specify an image')
parser.add_argument('-v', '--video', dest='video', help='specify a video to use')
parser.add_argument('--host', dest='host', default='', help='The VideoAI host to use')
parser.add_argument('--key-file', dest='key_file', help='use this file for your keys (otherwise defaults ~/.video)')
parser.add_argument('--tags', dest='tags', action='store_true', help='List all the tags')
parser.add_argument('--tagged', dest='tagged', action='store_true', help='List all the tagged object')
parser.add_argument('--tag', dest='tag', help='A tag name.')
parser.add_argument('--create', dest='create', action='store_true', help='Create a tag')
parser.add_argument('--colour', dest='colour', default='#95a5a6', help='Create a tag with this colour')
parser.add_argument('--delete', dest='delete', action='store_true', help='Delete a tag(s).')
parser.add_argument('--object', dest='object', help='Perform delete.')
parser.add_argument('--verbose', dest='verbose', action='store_true', help='Be more verbose')
parser.set_defaults(download=True)
args = parser.parse_args()

recognition = Recognition(host=args.host, key_file=args.key_file, verbose=args.verbose)

# List tags
if args.tags:
    print "Listing all the tags"
    tags = recognition.list_tags()

# List tags
if args.tagged:
    print "Listing all the tags"
    tags = recognition.list_tagged(args.tag, args.object)

# Generic delete tag
elif args.delete:
    try:
        recognition.delete_tag(tag_name=args.tag, object_id=args.object)
    except:
        print 'Unable to delete tag id'

# Generic update tags
elif args.create:
    try:
        recognition.create_tag(args.tag)
    except:
        print 'Failed to create tag {}'.format(args.tag)


