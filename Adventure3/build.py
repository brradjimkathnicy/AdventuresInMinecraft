# Adventure 3: build.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program builds a block at an absolute coordinate

# Import necessary modules
import mcpi.minecraft as minecraft

# Create constant for block
GLOWING_OBSIDIAN = 246

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Build a block
mc.setBlock(1, 2, 3, GLOWING_OBSIDIAN)

# END
