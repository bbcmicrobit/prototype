#!/bin/sh

echo "Cleaning targets..."
rm -rf build dist libs microbug.dmg
echo "Packaging with py2app..."
python setup.py py2app
echo "Fixing dependencies..."
dylibbundler -od -b -x ./Dist/MicrobugLoader.app/Contents/MacOS/MicrobugLoader
echo "Making DMG..."
appdmg dmg.json ./microbug.dmg
echo "DONE!"