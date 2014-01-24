import sys, os,  shutil
import musicfile

def import_files(ipod_control_music_dir, dest_dir):
    print "Importing music from  '%s'" % ipod_control_music_dir
    for metadata in musicfile.musicfiles(ipod_control_music_dir):
            import_file(metadata, dest_dir)
    
def safe_read_tag(tags,key):
    return tags[key].strip().replace('/',' ').encode('utf-8') if tags and key in tags and len(tags[key].strip())>0 else 'Unknown ' + key.title()

def import_file((file_path, tags),dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    try:
        artist = safe_read_tag(tags,'artist')
        album = safe_read_tag(tags,'album')
        title = safe_read_tag(tags,'title')
        artist_album_dest_dir = os.path.join(dest_dir,artist, album)
        not(os.path.exists(artist_album_dest_dir)) and os.makedirs(artist_album_dest_dir) 
        dest_file = os.path.join(artist_album_dest_dir,title) + os.path.splitext(file_path)[1]
        print "{} -> {}".format(file_path,dest_file)
        shutil.copyfile(file_path,dest_file)
    except Exception as e:
        print "Error processing [{}]\n Error: {}".format(file_path,e)

if __name__ == "__main__":
    import_files(sys.argv[1], sys.argv[2])
