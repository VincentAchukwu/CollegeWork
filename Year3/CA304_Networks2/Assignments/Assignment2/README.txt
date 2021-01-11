(Note: when running the program, it may sometimes take a few seconds before any 
output is displayed. I think this caused by the pandas module.)

I used the pandas library in order to display the routing table for a router. 
The output from get_path() is a string, and I split that string to get the necessary 
information from that output in order to have it in the table. 
Every second item in the list is the info we place to the table. (If you print(info) 
below line 80 of router.py, you can see this more clearly). The necessary parts are 
appended to the associated list in order to have a list of items to place into the 
pandas table. I then return it using from_dict().

The extra feature I decided to include for this assignment was NetworkX. The one issue 
I had with this was how the first graph was shown ok in "beforeDeletion.png", but in 
the second version of the graph ("afterDeletion.png"), the 2 graphs seem to merge in 
the diagram and I couldn't quite find the fix for that.
The reason I decided to include 2 versions is to show what the graphs would look like 
before and after deletion of a router.

I also tried to have the edge weights displayed on the graph, but the values seemed 
to scatter in random places rather than on their associated edges. This can be seen 
within lines 170 to 172 in router.py (commented out). Feel free to uncomment that 
code to see the result.
