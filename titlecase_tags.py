import sys
import musicfile 
def title_case(folder):
    for file_path, meta in musicfile.musicfiles(folder):
        if not meta:
            print "Skipping %s" % file_path
            continue
        print "Processing %s" % file_path
        for prop in ['title', 'album', 'artist']:
            if prop in meta:
                meta[prop] = meta[prop].title()
        meta.write()
    
if __name__ == "__main__":
    title_case(sys.argv[1])
