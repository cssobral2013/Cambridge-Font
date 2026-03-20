from fonttools.ttLib import TTFont

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Light.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeSans-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeSans-HeavyItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Light.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeSans-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeSans-HeavyItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Light.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeSans-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeSans-HeavyItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Light.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF/CambridgeMono-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF/CambridgeMono-HeavyItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Light.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF-Subset/CambridgeMono-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Subset/CambridgeMono-HeavyItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Regular.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Regular.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Italic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Italic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Thin.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Thin.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-ThinItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-ThinItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-ExtraLight.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-ExtraLight.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-ExtraLightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-ExtraLightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Light.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Light.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-LightItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-LightItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Medium.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Medium.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-MediumItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-MediumItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-SemiBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-SemiBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-SemiBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-SemiBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Bold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Bold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-BoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-BoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-ExtraBold.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-ExtraBold.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-ExtraBoldItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-ExtraBoldItalic.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-Heavy.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-Heavy.ttf')

# Load the font
font = TTFont('/dist/TTF-Unhinted/CambridgeMono-HeavyItalic.ttf')

# 1. Change Vertical Metrics (OS/2 and hhea tables)
# It is best practice to keep OS/2 and hhea in sync
new_ascender = 1000
new_descender = -300
new_linegap = 0

# Modify hhea table
font['hhea'].ascent = new_ascender
font['hhea'].descent = new_descender
font['hhea'].lineGap = new_linegap

# Modify OS/2 table
font['OS/2'].sTypoAscender = new_ascender
font['OS/2'].sTypoDescender = new_descender
font['OS/2'].sTypoLineGap = new_linegap
font['OS/2'].usWinAscent = new_ascender
font['OS/2'].usWinDescent = abs(new_descender)


# Save the modified font
font.save('/dist/TTF-Unhinted/CambridgeMono-HeavyItalic.ttf')
