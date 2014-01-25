[![endorse](http://api.coderwall.com/rags/endorsecount.png)](http://coderwall.com/rags)

Manage Files
---------------
The script copies over music over to a specified directory in artist/album/title.xxx format. A good example of this is coping music library files from apple devices (ipod/iphone). Apple's music library obfuscates the file names. This can also be used in any situation where you need to reorganize/rename your music file based on the ID3 tags.  

Usage: 
Run the script with 2 params ipod's Music dir and the destination dir.
```
python import.py "/media/ipod/iPod_Control/Music" "/your_destination/directory"
```

Manage ID3 Tags
-----------------
ID3 can be titalized (title cased) to make then uniform. This can be useful if "Lamb of God", "Lamb Of God" show up as different artists.
```
Artist: OBITUARY        -->      Artist: Obituary
Album:  slowly we rot   -->      Album:  Slowly We Rot 
Title:  Gates to Hell   -->      Title:  Gates To Hell
```
Usage:
```
 python titlecase_tags.py /your/library/folder
```

The script has dependency on [quodlibet](https://code.google.com/p/quodlibet/).

```
    sudo apt-get install quodlibet
``` 
