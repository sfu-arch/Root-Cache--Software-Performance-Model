# generate 1024 random entries between 1-1M
from random import randrange
def extract_bits(num, start_pos, num_bits):
    mask = (1 << num_bits) - 1  # Create a mask with 'num_bits' set to 1
    masked_value = num& mask  # Apply the mask to the desired range
    return masked_value


list_1024_Entries=[]

for i in range(1024):
    list_1024_Entries.append(randrange(1,1000000,1))

print(list_1024_Entries)

#3 lists : 1 - 4096, list 2 - 1024, list 3 - 1024
size1 = 4096
list_1 = [0 for _ in range(size1)]

size2 = 1024
list_2 = [0 for _ in range(size2)]

size3 = 1024
list_3 = [0 for _ in range(size3)]

#for i in list 1024, extract first 12 bits
# Example usage:
print()
for i in range(1024):
    num = list_1024_Entries[i]  # Binary: 111010110111100110100010101
    start_pos = 0
    num_bits = 12
    extracted_value = extract_bits(num, start_pos, num_bits)
    list_1[extracted_value]+=1  # Output: 1649
    num=num>>12
    start_pos = 0
    num_bits = 10
    extracted_value = extract_bits(num, start_pos, num_bits)
    list_2[extracted_value]+=1
    num=num>>10
    start_pos = 0
    num_bits = 10
    extracted_value = extract_bits(num, start_pos, num_bits)
    list_3[extracted_value]+=1 

# print("New Lists")

# print(list_1)

# print("New Lists")

# print(list_2)
# print("New Lists")

# print(list_3)

list_1_counter=0
list_2_counter=0
list_3_counter=0


#increment counter for each list to show how many pages to allocate
for i in range(4096):
    if(list_1[i]!=0):
        list_1_counter+=1
for i in range(1024):
    if(list_2[i]!=0):
        list_2_counter+=1
for i in range(1024):
    if(list_3[i]!=0):
        list_3_counter+=1

print(list_1_counter*4,"kB for 4096")
print(list_2_counter*4,"kB for 1024")
print(list_3_counter*4,"kB for 1024")


