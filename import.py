import sys, os, glob,  shutil
import quodlibet
from quodlibet.formats import MusicFile

def import_files(ipod_control_music_dir, dest_dir):
    quodlibet.config.init()
    print "Importing music from  '%s'" % ipod_control_music_dir
    
    for fname in glob.glob(os.path.join(ipod_control_music_dir,'*')):
            print "importing %s" % fname
            import_file(fname, dest_dir)
    
def safe_read_tag(tags,key):
    return tags[key].strip().replace('/',' ').encode('utf-8') if tags and key in tags and len(tags[key].strip())>0 else 'Unknown ' + key.title()

def import_file(ipod_file,dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    try:
        tags = MusicFile(ipod_file)
        artist = safe_read_tag(tags,'artist')
        album = safe_read_tag(tags,'album')
        title = safe_read_tag(tags,'title')
        artist_album_dest_dir = os.path.join(dest_dir,artist, album)
        not(os.path.exists(artist_album_dest_dir)) and os.makedirs(artist_album_dest_dir) 
        dest_file = os.path.join(artist_album_dest_dir,title) + os.path.splitext(ipod_file)[1]
        print "{} -> {}".format(ipod_file,dest_file)
        shutil.copyfile(ipod_file,dest_file)
    except Exception as e:
        print "Error processing [{}]\n Error: {}".format(ipod_file,e)

if __name__ == "__main__":
    import_files(sys.argv[1], sys.argv[2])
