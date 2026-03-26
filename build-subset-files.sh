#!/bin/bash
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Regular.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Italic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Thin.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ThinItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLight.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLightItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Light.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-LightItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Medium.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-MediumItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-SemiBold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-SemiBoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Bold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-BoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Heavy.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-HeavyItalic.ttf --unicodes-file=unicodes.txt
mv ./dist/CambridgeSans/TTF/CambridgeSans-Thin.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Thin.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-ThinItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-ThinItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLight.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-ExtraLight.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLightItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-ExtraLightItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Light.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Light.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-LightItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-LightItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Regular.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Regular.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Italic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Italic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Medium.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Medium.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-MediumItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-MediumItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-SemiBold.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-SemiBold.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-SemiBoldItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-SemiBoldItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Bold.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Bold.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-BoldItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-BoldItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBold.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-ExtraBold.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBoldItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-ExtraBoldItalic.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-Heavy.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-Heavy.ttf
mv ./dist/CambridgeSans/TTF/CambridgeSans-HeavyItalic.subset.ttf ./dist/CambridgeSans/TTF-Subset/CambridgeSans-HeavyItalic.ttf
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Regular.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Italic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Thin.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-ThinItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-ExtraLight.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-ExtraLightItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Light.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-LightItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Medium.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-MediumItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-SemiBold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-SemiBoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Bold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-BoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-ExtraBold.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-ExtraBoldItalic.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-Heavy.ttf --unicodes-file=unicodes.txt
~/.local/bin/fonttools subset ./dist/CambridgeMono/TTF/CambridgeMono-HeavyItalic.ttf --unicodes-file=unicodes.txt
mv ./dist/CambridgeMono/TTF/CambridgeMono-Thin.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Thin.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-ThinItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-ThinItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-ExtraLight.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-ExtraLight.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-ExtraLightItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-ExtraLightItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Light.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Light.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-LightItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-LightItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Regular.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Regular.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Italic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Italic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Medium.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Medium.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-MediumItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-MediumItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-SemiBold.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-SemiBold.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-SemiBoldItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-SemiBoldItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Bold.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Bold.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-BoldItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-BoldItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-ExtraBold.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-ExtraBold.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-ExtraBoldItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-ExtraBoldItalic.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-Heavy.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-Heavy.ttf
mv ./dist/CambridgeMono/TTF/CambridgeMono-HeavyItalic.subset.ttf ./dist/CambridgeMono/TTF-Subset/CambridgeMono-HeavyItalic.ttf
exit
