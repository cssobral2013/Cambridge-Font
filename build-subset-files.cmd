@echo off
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Regular.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Italic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Thin.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ThinItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLight.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraLightItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Light.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-LightItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Medium.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-MediumItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-SemiBold.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-SemiBoldItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-Bold.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-BoldItalic.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBold.ttf --unicodes-file=unicodes.txt
fonttools subset ./dist/CambridgeSans/TTF/CambridgeSans-ExtraBoldItalic.ttf --unicodes-file=unicodes.txt
move .\dist\CambridgeSans\TTF\CambridgeSans-Thin.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Thin.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-ThinItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-ThinItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-ExtraLight.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-ExtraLight.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-ExtraLightItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-ExtraLightItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-Light.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Light.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-LightItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-LightItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-Regular.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Regular.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-Italic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Italic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-Medium.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Medium.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-MediumItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-MediumItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-SemiBold.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-SemiBold.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-SemiBoldItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-SemiBoldItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-Bold.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-Bold.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-BoldItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-BoldItalic.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-ExtraBold.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-ExtraBold.ttf
move .\dist\CambridgeSans\TTF\CambridgeSans-ExtraBoldItalic.subset.ttf .\dist\CambridgeSans\TTF-Subset\CambridgeSans-ExtraBoldItalic.ttf
exit
