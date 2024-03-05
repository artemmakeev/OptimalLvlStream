Script meant to run in pypy environment since it's very heavy.

Here's example of script running:

.................

...Start of best range...

At streaming distance: 1.490

ratio: 1.778

Max tiles:  16

Min tiles:  9

.................

...Start of best range...

At streaming distance: 1.500

ratio: 1.455

Max tiles:  16

Min tiles:  11

.................

...Start of best range...

At streaming distance: 1.536

ratio: 1.333

Max tiles:  16

Min tiles:  12

.................

...Start of best range...

At streaming distance: 1.542

ratio: 1.231

Max tiles:  16

Min tiles:  13

.................

End of best range: 1.551

.................

.................

...Start of best range...

At streaming distance: 2.008

ratio: 1.200

Max tiles:  24

Min tiles:  20



What it means is it's searching for lowest ratio between max possible streamable tiles to minimum streamable tiles. 
Why lower ratio is important?

Example: 
let's say each streaming level is 1 units in x coordinates and 1 units in y coordinates.
If we set streaming distance to <0.5 then if player is in the middle of a single tile only a single level tile will be loaded.
If player is at the cross section between 4 level tiles - all 4 levels will be streamed. Ratio is 4/1 here.

But if we set streaming distance to between 1.49 - 1.5 we'll get 16/9 ratio or 1.778.
At streaming distance 1.542-1.551 we'll get 16/13 ratio or 1.231
But if streaming distance is anywhere between 1.551 and 2.008 we'll have ratio worse than 1.231


