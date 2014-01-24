[![endorse](http://api.coderwall.com/rags/endorsecount.png)](http://coderwall.com/rags)

The script copies over music over to a specified directory in artist/album/title.xxx format. A good example of this is coping music library files from apple devices (ipod/iphone). Apple's music library obfuscates the file names. This can also be used in any situation where you need to reorganize/rename your music file based on the ID3 tags.  

Usage: 
Run the script with 2 params ipod's Music dir and the destination dir.
```
python import.py "/media/ipod/iPod_Control/Music" "/your_destination/dirrectory"
```

The script has dependency on [quodlibet](https://code.google.com/p/quodlibet/).

```
    sudo apt-get install quodlibet
``` 
