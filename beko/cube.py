
volume = 0 
side_length = 0 

print("Enter the side lenght of the cube that you want to calculate the volume: ")
side_length = int(input())

def cube_volume(side_length):
    if side_length <= 0:
        return 0
    else:
        volume = side_length * side_length * side_length
        return volume

print("The volume of your cube is: ", cube_volume(side_length))