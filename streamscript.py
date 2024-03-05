#import sys
import math
#import random
#import threading
#import time

offset_x = 0.0
offset_y = 0.0
best_ratio = 4.0
best_range = False
#stream_distance = 2.721
stream_distance = 1.49
scan_range = math.trunc(stream_distance) + 3
active_tiles = 0
max_tiles = 0
min_tiles = 50000
x = 0
y = 0

# checking distance between streaming center and corner edges of tiles. 
#Works correctly for non zero coordinates only

# iterating streaming distance:
for i in range(50000):
	max_tiles = 0
	min_tiles = 50000
	scan_range = math.trunc(stream_distance) + 3
	# loop with iterating x/y offsets
	for offset_xi in range(-50, 5050):
		offset_x = offset_xi/10000
		for offset_yi in range(-50, 5050):
			offset_y = offset_yi/10000
			active_tiles = 0

			#looping though tiles with non zero coordinates
			for x in range(-scan_range,-1):
				x += 1

				
				# handling tiles with y at zero
				#and handling tiles with x at zero, x as counter for y
				if (((x + offset_x)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((x + offset_x)**2 + (offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((x + offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((offset_x)**2 + (x + offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1

				for y in range(-scan_range,-1):
					y += 1
					if (((x + offset_x)**2 + (y + offset_y)**2) <= (stream_distance**2)):
						active_tiles += 1
				for y in range(2,scan_range-1):
					y -= 1
					if (((x + offset_x)**2 + (y + offset_y)**2) <= (stream_distance**2)):
						active_tiles += 1

			for x in range(2,scan_range-1):
				x -= 1

				# handling tiles with y at zero
				#and handling tiles with x at zero, x as counter for y
				if (((x + offset_x)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((x + offset_x)**2 + (offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((x + offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1
				if (((offset_x)**2 + (x + offset_y)**2) <= (stream_distance**2)):
					active_tiles += 1

				for y in range(-scan_range,-1):
					y += 1
					if (((x + offset_x)**2 + (y + offset_y)**2) <= (stream_distance**2)):
						active_tiles += 1
				for y in range(2,scan_range-1):
					y -= 1
					if (((x + offset_x)**2 + (y + offset_y)**2) <= (stream_distance**2)):
						active_tiles += 1

			# Handling 4 squares in the center:
			active_tiles += 4
			if ((offset_x**2 + offset_y**2) > stream_distance**2):
				active_tiles -= 1
			if (abs(offset_y) > stream_distance):
				active_tiles -= 1
			if (abs(offset_x) > stream_distance):
				active_tiles -= 1

			


			# setting min/max tiles
			if active_tiles > max_tiles:
				max_tiles = active_tiles
			if active_tiles < min_tiles:
				min_tiles = active_tiles

	stream_distance += 0.0001
	ratio = max_tiles / min_tiles
	if (best_ratio < ratio) and (best_range == True):
		best_range = False
		print (".................")
		print ("End of best range: {:.3f}".format(stream_distance))
		print (".................")
	if ratio < best_ratio:
		best_range = True
		best_ratio = ratio
		print (".................")
		print ("...Start of best range...")
		print ("At streaming distance: {:.3f}".format(stream_distance))
		print ("ratio: {:.3f}".format(ratio))
		print ("Max tiles: ", max_tiles)
		print ("Min tiles: ", min_tiles)
	



				

