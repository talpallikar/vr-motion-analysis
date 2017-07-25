import csv

#read the bones that I want to read by frame
def mixed_read(file_name, has_header=True, keep_header=False):
    
    good_bones = [
    "HMD",
    "Hips",
    "LeftUpperLeg",
    "RightUpperLeg",
    "LeftLowerLeg",
    "RightLowerLeg",
    "LeftFoot",
    "RightFoot",
    "Spine",
    "Chest",
    "Neck",
    "Head",
    "LeftShoulder",
    "RightShoulder",
    "LeftUpperArm",
    "RightUpperArm",
    "LastBone"]

    header = ["ID", "Condition", "Trial Number", "Starting Location", "Ending Location", "Distance", "State", "Time", "Frame"]
    bone_components = [item for sublist in list(map(lambda x: [x+"X", x+"Y", x+"Z"], good_bones)) for item in sublist]
    header.extend(bone_components)
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        csv_list = list(readCSV)
        data = []
        
        
        if has_header:
            i = 1
            if keep_header:
                data.append(header)            
        else:
            i = 0

        frame_counter = csv_list[i][8]
        current_row = 0 
        
        while i <  len(csv_list):
            row = list(map(lambda x: x.strip(), csv_list[i]))

            #check if the row is of a useful bone
            
            if row[9] in good_bones:
                
                #If the frame of the transform does not match the last frame, we need to create a new frame
            
                if frame_counter != row[8]:

                    data.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[10],row[11],row[12],row[13],row[14],row[15]])

                    #update the frame counter now that we are on a  new frame
                    frame_counter = row[8]
                    current_row += 1 
                #otherwise, we need to add to the old frame
                else:
                    data[current_row].extend([row[10],row[11],row[12],row[13],row[14],row[15]])
            i+=1
    return(data)

#Read only the continuous variables - not the categorical variables
def cont_read(file_name, has_header=True, keep_header=False):
    
    good_bones = [
    "HMD",
    "Hips",
    "LeftUpperLeg",
    "RightUpperLeg",
    "LeftLowerLeg",
    "RightLowerLeg",
    "LeftFoot",
    "RightFoot",
    "Spine",
    "Chest",
    "Neck",
    "Head",
    "LeftShoulder",
    "RightShoulder",
    "LeftUpperArm",
    "RightUpperArm",
    "LastBone"]

    header = ["Trial Number", "Distance", "Time", "Frame"]
    bone_components = [item for sublist in list(map(lambda x: [x+"X", x+"Y", x+"Z"], good_bones)) for item in sublist]
    header.extend(bone_components)
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        csv_list = list(readCSV)
        data = []
        
        
        if has_header:
            i = 1
            if keep_header:
                data.append(header)            
        else:
            i = 0

        frame_counter = csv_list[i][8]
        current_row = 0
        
        while i <  len(csv_list):
            row = list(map(lambda x: x.strip(), csv_list[i]))

            #check if the row is of a useful bone
            
            if (row[9] in good_bones) and (row[6]=="Walking"):
                
                #If the frame of the transform does not match the last frame, we need to create a new frame
            
                if frame_counter != row[8]:
                    #Keep the frame number and the rotations of each bone
                    data.append([row[8],row[13],row[14],row[15]])
                    
                    #Keeps the trial number, the frame number, and the positions + rotations
                    #data.append([row[2],row[8],row[10],row[11],row[12],row[13],row[14],row[15]])

     #update the frame counter now that we are on a  new frame
                    frame_counter = row[8]
                    current_row += 1 
                #otherwise, we need to add to the old frame
                else:
                    #append the positions and rotations of the new  bone to the current frame
                    data[current_row-1].extend([row[10],row[11],row[12],row[13],row[14],row[15]])
            i+=1
    return(data)

def test():
    print(cont_read('log_gait_1_RW.csv')[0])

def main():
    test()
    


if __name__ == "__main__":
    main()
    
