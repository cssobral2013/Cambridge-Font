@echo off
echo Building Iosevka cache...
npm install
echo Building proportional fonts...
npm run build ttf::cambridge-sans ttf::cambridge-slab
echo Building monospace fonts...
npm run build ttf::cambridge-mono ttf::cambridge-slab-mono
echo Building extra fonts...
npm run build ttf::cambridge-mono-one ttf::cambridge-mono-two
echo Subsetting proportional fonts...
./subset-sans.cmd
./subset-slab.cmd
exit