
from random import shuffle

# I initially wrote the program using lists and dictionaries, and then I realized it would have been optimized if I used classes instead. 
# For the top preference of each person, I kept the code using the dictionaries and lists.
# For the second and third preferences, I implemented classes and objects. 

# The class for each person's second and third choice debates
class person: 
    def __init__(self, full_name, s_name, second_choice, third_choice):
        self.full_name = full_name;
        self.s_name = s_name;
        self.second_choice = second_choice;
        self.third_choice = third_choice;


# Sort to Groups will sort the students to the group of students from each school. Each student will also have their top debate choice for each block "attached" to them. 
# The function will return two dictionaries: "schools" is a list of students from each school. "first_choice" is a list of the top debate choice the student wants per block
def sort_to_groups():

    attendees = [];
    schools = {"mca" : []};
    first_choice = {"test" : []};

    # The index of the attendees list, specifying each person in the attendees list
    p_num = -1;
    
    while (True):

        p_num += 1;

        # Ask user for their first and last name 
        line = file.readline().strip();
        full_name = "";
        s = 0;
        while (line[s] != ','):
            full_name += line[s];
            s += 1;

          # If name = "done," exit the sort_to_group function
        if (full_name.lower() == "done"):
            break;
        
        # Ask user for their school
        s_name = "";
        s += 2;
        while (line[s] != ','):
            s_name += line[s];
            s += 1;
        s_name = s_name.lower();

        # As of now, this student is the first person from their school
        s_exists = False;
 
        # Check if this person IS the first from their school 
        for i in range(len(schools)):
            if (list(schools.keys())[i] == s_name):
                s_exists = True;

        # If this person is the first from their school, add their school as a new "school" in the list. Each new school is a list, which will contain the students' names in that school
        if (s_exists == False):
            schools[s_name] = [];
    
        i = 0;

        # Each index of the "schools" list is a list of students' names from that school. This will add each student to the list of students for their school
        while (list(schools.keys())[i] != s_name):
             i = i+1;
        
        # Add the student's name to the list of students from that certain school
        schools[s_name].append(full_name);


        
        # Up to this point will sort the current student into the group of students from that school ___________________________________________________________________________________________________________________________________________________

        # Now we match the debate choices which the students ___________________________________________________________________________________________________________________________________________________________________________________________


        # The dictionary, "first_choice," has keys of each student's name, and the values are the top preference debates in order of blocks, that the student wants.
        first_choice[full_name] = [];
        for i in range(8):
            n = "";
            s += 2;
            while (line[s] != ','):
                n += line[s];
                s += 1;
            first_choice[full_name].append(n);

        # Append all of the second_choices in the object of that person in "attendee"
        second_choice = [];
        s += 2;
        for i in range(8):
            n = "";
            s += 2;
            while (line[s] != ','):
                n += line[s];
                s += 1;
                second_choice.append(n);

        # Append all of the third_choice in the object of that person in "attendee"
        third_choice = [];
        s += 2;
        for i in range(8):
            n = "";
            s += 2;
            while (line[s] != ','):
                n += line[s];
                s += 1;
                third_choice.append(n);

    # Add a new person to the list "attendees" and fill in the attributes of that person (Person is an object)
    attendees.append(person(full_name, s_name, second_choice, third_choice));

        # Return the list with all the schools attending and all the students grouped by their school. Delete the "test" item in the first_choice dictionary
    del first_choice["test"];



    return schools, first_choice, attendees;

# Coordinate Debates will allocate studets into each debate so that every debate has the same number of students per school
def coordinate_first_debates(schools, first_choice):

    # Each block is a dictionary. The keys of each block are the debates for that block, and the values are a list of students who will be in that debate for that block
    b1 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b2 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b3 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b4 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b5 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b6 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b7 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};
    b8 = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : []};

    # The count to activate the code for each block 
    block = 1;

    # Coordinate block 1
    if (block == 1):

        for d_num in range(8):
            cont = True;

        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make it continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:

                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[0] == str(d_num)):
                                    b1[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);

    # Coordinate block 2
    if (block == 2):

        for d_num in range(8):
            cont = True;

        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:

                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[1] == str(d_num)):
                                    b2[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 3
    if (block == 3):

        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                             
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[2] == str(d_num)):
                                    b3[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 4
    if (block == 4):
        
        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                             
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[3] == str(d_num)):
                                    b4[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 5
    if (block == 5):
        
        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                             
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[4] == str(d_num)):
                                    b5[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;
        
        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 6
    if (block == 6):
        
        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                              
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[5] == str(d_num)):
                                    b6[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 7
    if (block == 7):
        
        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                             
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[6] == str(d_num)):
                                    b7[str(d_num)].append(name);
                              except IndexError:
                                break;
        block += 1;

        # Rearrange the list of students for each school
    for n in range(len(schools)):
        shuffle(schools[list(schools.keys())[n]]);


    # Coordinate block 8
    if (block == 8):
        
        for d_num in range(8):
            cont = True;
        
        # The count for each debate. There are 8 debates each block, named by numbers here
            d_num += 1;

            # "j" is the count for how many students in each debate, currently set to 5 but we want to make continue until a school has no more students
            for j in range(5):
                if (cont == False):
                    break;

                # This process of assigning students to debates goes 1 student in a school, then the next school
                for i in range(len(schools)):
              
                        # "name" = the name of each student in the list of students for each school in "schools." 
                        try:
                            s_name = list(schools.keys())[i];
                            name = (schools[s_name])[j]
                        except IndexError:
                             cont = False;
                             break;
                        else:
                             
                        # If this student chose this debate as their main for block 1, then add them to the list of students for this debate in block  
                              try:
                                if ((first_choice[name])[7] == str(d_num)):
                                    b8[str(d_num)].append(name);
                              except IndexError:
                                break;
    
    return b1, b2, b3, b4, b5, b6, b7, b8;
def coordinate_second_debates(attendees):
    second_choices = attendees.second_choices;
def coordinate_third_debates(attendees):
    third_choices = attendees.third_choices;


    # Main function
if __name__== "__main__":

    # Open Text File 
    file = open("MAS Convention Attendance Info.txt", "r");

    # Sort the students     by grouping them into their schools
    schools, first_choice, attendees  = sort_to_groups();

    file.close();

    # Coordinate the debates so that each debate of each block has the same number of students from each school
    b1, b2, b3, b4, b5, b6, b7, b8 = coordinate_first_debates(schools, first_choice);

    print(b1, '\n', b2, '\n',  b3, '\n', b4, '\n', b5, '\n', b6, '\n', b7, '\n', b8)


         