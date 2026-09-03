#Activity-3

#Importing Numpy ---> for easy Matrix Multiplication
import numpy

#Specific function for printing the matrix in the order...
def printing_mat(mat):
    for i in mat:
        print(i)



def main():
    print("\n\n-----Avtivity-3-----\n")

    #Matrix Given data
    mat_A = [[1,2,3],[4,5,6]]
    mat_B = [[10,11],[20,21],[30,31]]

    #Printing the Expression
    printing_mat(mat_A)
    print("\nx\n")
    printing_mat(mat_B)
    print("\n=\n")

    #using in-built numpy module's matrix multiplication method
    result = numpy.matmul(mat_A,mat_B)
    print(result)

    print("\n--------------------\n")

if __name__ == "__main__":
    main()