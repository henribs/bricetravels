function EmbedMedia(path_folder){
    const fs = require('fs');
    const path = require('path');
    
    
    // Read the directory
    fs.readdir(path_folder, (err, files) => {
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        } 
        // Print the names of each file
        files.forEach(file => {
            console.log(file);
        });
    });
    
}


EmbedMedia('/Users/brice/Documents/Coding/Travel_blog/assets/media/Cebu')