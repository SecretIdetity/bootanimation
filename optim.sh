# execute in each partx
pngquant --force --ext .png *.png
for fn in *.png ; do
  zopflipng -m ${fn} ${fn}s.new && mv -f ${fn}s.new ${fn}
done # ~70+% less bytes, but doesnt actually help with faster loading
