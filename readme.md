[![endorse](http://api.coderwall.com/rags/endorsecount.png)](http://coderwall.com/rags)

The script copies over music from your ipod/iphone to a specified directory in artist/album/title.xxx format.

Usage: 
Run the script with 2 params ipod's Music dir and the destination dir.
```
python import.py "/media/ipod/iPod_Control/Music" "/your_destination/dirrectory"
```

The script has dependency on [quodlibet](https://code.google.com/p/quodlibet/) and [quodlibet-cli](https://github.com/jmcantrell/quodlibet-cli).

```
    sudo apt-get install quodlibet
    pip install quodlibet-cli
``` 
