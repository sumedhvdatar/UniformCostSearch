Name : Sumedh Vilas Datar

-----------------------------------------------------------------------------------------------------------------------------------------------------

UTA ID : XXXXXXXXX

------------------------------------------------------------------------------------------------------------------------------------------------------

Language Used : Python

-------------------------------------------------------------------------------------------------------------------------------------------------------

Structure of the Code:

Uniform Cost Search Algorithm is implemented using python.
It has the main function which has all the declarations of various of all lists,hashmap and other variables.
It has other methods which perform various functions and operation of each function is mentioned below :-

1. def backtrack_to_get_optimized_path : This method will take the last pair and then backtrack till 
the source and then printout the final optimized path

2. def select_cheapest_pair_with_least_distance - This method will return the final destination and its parent with the shortest distance.

3. def input_file - This method has the implementation details
of Uniform Cost Search. BFS is applied and each 
source and destination is stored into a sorted hashmap
Format queue[parent|child|distance from origin|distance from parent] = distance
The shortest distance is picked next and expanded to get its child and it is removed 
from the hash map.

A list called visited list is used to store the visited cities so that it is not repeated while
storing the child details in the hashmap to avoid overlap.

4. def check_if_source_and_destination_is_in_the_text_file - This method will check if the source and destination is in the text file.
Following are the outputs:
return:
      1. True : The source and destination is valid
      2. 0 : The source and destination is same
      3. False : The source or destination or both is not valid

---------------------------------------------------------------------------------------------------------------------------------------------------------      

Running the Code: 

The python file name is called find_route.py. While running on omega using shell command, the following command must be typed.

$python find_route.py $input_file.txt $source $destination

Note : The source and destination is case sensitive. The name of the place must start with a captial letter or the place name input
must match with the name given in the input text file.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
