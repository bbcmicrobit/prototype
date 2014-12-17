#!/bin/sh

echo "Cleaning targets..."
rm -rf build dist libs BBCBug.dmg
echo "Packaging with py2app..."
python setup.py py2app
echo "Fixing dependencies..."
dylibbundler -od -b -x ./Dist/BBCBugLoader.app/Contents/MacOS/BBCBugLoader
echo "Making DMG..."
appdmg dmg.json ./BBCBug.dmg
echo "DONE!"