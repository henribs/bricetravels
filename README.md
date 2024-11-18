Blog: https://bricechivu.github.io/bricetravels/

#### Update procedure
1. Download images on Google photos
2. Paste them in the corresponding folder (name of the city) inside assets/media/
3. Run python3 print_img_src.py  --country={country}
4. Copy-paste the output in index.html
5. Change the order of the pictures only after the whole city is done


For image compression:
- [(previous method - old)](https://github.com/calibreapp/image-actions?tab=readme-ov-file)
- ```find media/ -type f \( -iname '*.jpg' -o -iname '*.png' \) -exec identify -format "%w %h %i\n" {} \; | awk '$1 > 2000 && $2 > 2000 {print $3}' | xargs mogrify -resize '2000x2000>' -interlace plane```
