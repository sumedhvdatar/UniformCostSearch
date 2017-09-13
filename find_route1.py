"""
Author: Sumedh Vilas Datar
Implementation of Uniform Cost Search
CSE 5360 Fall 2017
Assignment 1
"""

import sys
"""
This method will take the last pair and then backtrack till 
the source and then printout the final optimized path
"""
def backtrack_to_get_optimized_path(last_pair):
    connected_pair = None
    get_parent_from_child = last_pair.split("|")[0]
    for visited_pair in visited_list:
        if(get_parent_from_child == visited_pair.split("|")[1]):
            break
    if(visited_pair.split("|")[0] == source_location):
        optimized_path.append(visited_pair)
        for v in reversed(optimized_path):
            start = v.split("|")[0]
            end = v.split("|")[1]
            distance_between_them = v.split("|")[3]
            print start+" to "+end+","+distance_between_them
    else:
        #print visited_pair
        optimized_path.append(visited_pair)
        backtrack_to_get_optimized_path(visited_pair)


# class MyPriorityQueue(PriorityQueue):
#     def __init__(self):
#         PriorityQueue.__init__(self)
#         self.counter = 0
#
#     def put(self, item, priority):
#         PriorityQueue.put(self, (priority, self.counter, item))
#         self.counter += 1
#
#     def get(self, *args, **kwargs):
#         _, _, item = PriorityQueue.get(self, *args, **kwargs)
#         return item

"""
This method will return the final destination 
and its parent with the shortest distance
"""
def select_cheapest_pair_with_least_distance(get_multiple_paths):
    distance_list = []
    for pair in get_multiple_paths:
        distance_list.append(int(pair.split("|")[2]))
    distance_list.sort()
    least_distance = distance_list[0]
    print least_distance

    for p in get_multiple_paths:
        if(p.split("|")[2] == str(least_distance)):
            return p




"""
This method has the implementation details
of Uniform Cost Search. BFS is applied and each 
source and destination is stored into a sorted hashmap
Format queue[parent|child|distance from origin|distance from parent] = distance
The shortest distance is picked next and expanded to get its child and it is removed 
from the hash map.

A list called visited list is used to store the visited cities so that it is not repeated while
storing the child details in the hashmap to avoid overlap.

"""

def input_file(filename,source,destination,distance_to_add):
    file = open(filename,"r")
    parent = 0
    for line in file:

        if(line != "END OF INPUT"):
            convert_line_to_array = line.split(" ")
            location_1 = convert_line_to_array[0]
            location_2 = convert_line_to_array[1]
            #print convert_line_to_array[2]
            distance = int(convert_line_to_array[2]) + int(distance_to_add)
            if (location_1 == source):
                delete = False
                for visited_node in visited_list:
                    visited_node = visited_node.split("|")[0]
                    #print visited_node
                    if(visited_node == location_2):
                        delete = True
                        parent = 1
                if delete == False:
                    key = source+"|"+location_2+"|"+str(distance)+"|"+convert_line_to_array[2]
                    queue[key] = distance
                    #queue.put(source+"|"+location_2+"|"+str(distance),distance)
            elif (location_2 == source):
                delete = False
                for visited_node in visited_list:
                    visited_node = visited_node.split("|")[0]
                    if (visited_node == location_1):
                        delete = True
                        parent = 1
                if(delete == False):
                    value = source+"|"+location_1+"|"+str(distance)+"|"+convert_line_to_array[2]
                    queue[source + "|" + location_1 + "|" + str(distance)+"|"+convert_line_to_array[2]] = distance
                    #queue.put(source+"|"+location_1+"|"+str(distance), distance)
    #location_list_to_backtrack.append(connected_location_list[0])
    #print connected_location_list
    #print sorted(queue, key=queue.get)
    contents = None
    for key in sorted(queue, key=queue.get):
        contents = key
        break
    if contents == None:
        print "Distance:infinity"
        print "Route : None"
    else:
        #print contents
        del queue[contents]
        parent = contents.split("|")[0]
        location_to_be_sent = contents.split("|")[1]
        distance_to_be_sent = contents.split("|")[2]
        actual_distance = contents.split("|")[3]
        if(parent != 1):
            visited_list.append(parent+"|"+location_to_be_sent+"|"+distance_to_be_sent+"|"+actual_distance)
        #print "This is poped first "+location_to_be_sent+" and its parent is "+source+" and distance is "+distance_to_be_sent

        if (location_to_be_sent == destination):
            get_multiple_paths.append(contents)
            #print queue.queue
            for key in queue:
                get_details = key
                check_destination = get_details.split("|")[1]
                if(check_destination == destination):
                    #print get_details
                    get_multiple_paths.append(get_details)
            #location_list_to_backtrack.append(destination)
            #print "Printing all possible location from source and destination, not necessary to be connnected"
            choose_cheapest_pair = select_cheapest_pair_with_least_distance(get_multiple_paths)
            #print choose_cheapest_pair
            optimized_path.append(choose_cheapest_pair)
            backtrack_to_get_optimized_path(choose_cheapest_pair)
            # location_list_from_destination_to_source = reversed(location_list_to_backtrack)
            # back_tracking = True
            #get_full_path_from_destination_to_source(location_list_to_backtrack, destination_location)
            # get_full_path_from_destination_to_source(reversed(location_list_to_backtrack), "Hamburg")
        else:
        #     #contents = connected_location_list[0].split(",")
             input_file(input_file_name, location_to_be_sent,destination_location, distance_to_be_sent)

"""
This method will check if the source and destination is in the text file.
Following are the outputs:
return:
      1. True : The source and destination is valid
      2. 0 : The source and destination is same
      3. False : The source or destination or both is not valid
"""
def check_if_source_and_destination_is_in_the_text_file(input_file_name,source_location,destination_location):
    if (source_location == destination_location):
        source_is_correct_and_destination_is_correct = "0"
        return source_is_correct_and_destination_is_correct

    else:

        source_is_correct = False
        destination_is_correct = False
        file = open(input_file_name, "r")
        #with open(input_file_name) as f:

        for line in file:
            convert_line_to_array =  line.split(" ")
            location_1 = convert_line_to_array[0]
            location_2 = convert_line_to_array[1]
            if location_1 not in unique_list_of_location_names and location_1 != "END":
                unique_list_of_location_names.append(location_1)

            if location_2 not in unique_list_of_location_names and location_2 != "OF":
                unique_list_of_location_names.append(location_2)

        for unique_location in unique_list_of_location_names:
            if(unique_location == source_location):
                source_is_correct = True

        for unique_location in unique_list_of_location_names:
            if(unique_location == destination_location):
                destination_is_correct = True


        if(source_is_correct == True and destination_is_correct == True):
            return True
        else:
            return False


#queue = MyPriorityQueue()
print "................CODE COMPILING SUCCESSFUL, RUNNING THE CODE.................."
print "PRINTING THE SHORTEST DISTANCE"
queue = {}
#hashmap = list(queue)
optimized_path = []

unique_list_of_location_names = []
from_list = []
visited_list = []
location_list_to_backtrack = []
location_list_from_destination_to_source = []
#input_file_name = "find_route_input1.txt"
input_file_name = sys.argv[1]
source_location = sys.argv[2]
#source_location = "Bremen"
#format = "location|from|distance
#queue.put(source_location,0)
destination_location = sys.argv[3]
#destination_location = "Frankfurt"
get_multiple_paths = []
#visited_list.append(source_location+"|"+source_location)
#final_list_to_print_path = []
#final_list_to_print_path.append(destination_location)

source_is_correct_and_destination_is_correct = check_if_source_and_destination_is_in_the_text_file(input_file_name,source_location,destination_location)

if(source_is_correct_and_destination_is_correct == True):
    input_file(input_file_name,source_location,destination_location,"0")
    #calculate_distance(final_list_to_print_path)

elif(source_is_correct_and_destination_is_correct == "0"):
    print source_location + " to " + destination_location + ",0"

else:
    print "Distance from "+source_location+" to "+destination_location+" is Infinity"
    print "Route = None"