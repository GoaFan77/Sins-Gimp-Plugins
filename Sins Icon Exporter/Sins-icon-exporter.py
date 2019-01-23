#!/usr/bin/python
 
# This plugin automates saving multi-state icon sets for the game Sins of a Solar Empire Rebellion.
# An Export Sins HUDicons option will be added to the Gimp file menu. It takes an image, directory, and name of the file
# and saves 4 variants of the image, one for each icon state (Normal, Disabled, Cursor Over, and Pressed)
# Normal is the original image.
# Disabled is in Greyscale
# Cursor Over is brightened.
# Pressed is moved down and to the right.
 
from gimpfu import *

# Change these constants to customize the script to your specifications.
CURSOR_OVER_BRIGHTNESS_PERCENT = 25
PRESSED_X_ADJUSTMENT = 2
PRESSED_Y_ADJUSTMENT = 2
 
def export_sins_hud_icons(directory, filename, image):
	full_path = directory + '/' + filename
	
	drawable = pdb.gimp_image_get_active_drawable(image)
	pdb.gimp_edit_copy(drawable)
	
	#Normal
	pdb.file_tga_save(image, drawable, full_path + "_Normal.tga", filename, 0, 0)

	#Disabled
	pdb.gimp_drawable_hue_saturation(drawable, 0, 0, 0, -100, 0)
	pdb.file_tga_save(image, drawable, full_path + "_Disabled.tga", filename, 0, 0)
	
	#Cursor Over
	reset_image(drawable)
	pdb.gimp_drawable_hue_saturation(drawable, 0, 0, CURSOR_OVER_BRIGHTNESS_PERCENT, 0, 0)
	pdb.file_tga_save(image, drawable, full_path + "_CursorOver.tga", filename, 0, 0)
	
	#Pressed
	reset_image(drawable)
	pdb.gimp_drawable_offset(drawable, 0, 1, PRESSED_X_ADJUSTMENT, PRESSED_Y_ADJUSTMENT)
	pdb.file_tga_save(image, drawable, full_path + "_Pressed.tga", filename, 0, 0)

# Paste the original image for the next file.
def reset_image(drawable):
	floating_sel = pdb.gimp_edit_paste(drawable, FALSE)
	pdb.gimp_floating_sel_anchor(floating_sel)
	
	
register(
    "export_sins_hud_icons",
    "Saves a set of Sins HUD icons into the 4 needed variants.",
    "Saves a set of Sins HUD icons into the 4 needed variants.",
    "Nathanael Bonney",
    "Nathanael Bonney",
    "2019",
    "Export Sins HUDicons",
    "*",
    [
        (PF_DIRNAME, "directory", "Directory to save files. ", None),
        (PF_STRING, "filename", "Base name of the file. Suffixes for each type (_Normal, _Disabled etc.) will be added. ", ''),
		(PF_IMAGE, "image", "Image to export. ", None),
    ],
    [],
    export_sins_hud_icons,
    menu = "<Image>/File/Save/"
)
 
main()