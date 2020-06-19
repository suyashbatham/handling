# try:
#     with open("sample","r") as fp:
#         for line in fp:
#             print(line,end=" ")
#
# except FileExistsError:
#     print("File not found exception")


# try:
#     with open("sample","r") as fp:
#         while True:
#             curr_line = fp.readline()   # read as a string
#             if(curr_line==" "):
#                 break
#             print(curr_line)
# except FileExistsError:
#     print("File not found exception")


# try:
#     with open("sample","r") as fp:
#         while True:
#             curr_line = fp.readlines()   # return as list
# except FileExistsError:
#     print("File not found exception")
#
# for i in range(len(curr_line)):
#     print("Line : "+i+": "+curr_line[i])


#iterate all files
# import os
# root_dir = os.getcwd()
# for root,folder,files in os.walk(root_dir):
#     for filename in files:
#         print(root,filename)


#writing mode
with open("sample1","a") as f:
    f.write("Th")
