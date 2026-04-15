import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt


"""
# Define the matrix A and the vector y
A = np.array([[0.1, -0.2, 0.3],
              [0.2, -0.1, 0.4],
              [-0.1, -0.4, 0.1],
              [0.2, 0.8, -0.2]])

y = np.array([0.4, 0.3, 0.7, 0.5])


# # Calculate the determinant of A
# det_A = np.linalg.det(A)

# # Print the determinant
# print("Determinant of A:", det_A)

# Calculate the determinant of ATA
det_ATA = np.linalg.det(np.dot(A.T, A))

# Print the determinant
print("Determinant of A^TA:", det_ATA)


# Perform Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Calculate the rank of A (number of non-zero singular values)
rank_A = np.linalg.matrix_rank(A)

# Determine if the system is over-, under-, or mixed determined
num_unknowns = A.shape[1]  # Number of columns in A
if rank_A == num_unknowns:
    print("The system is determined.")
elif rank_A < num_unknowns:
    print("The system is underdetermined (infinite solutions).")
else:
    print("The system is overdetermined (no exact solution).")

# Check if A is rank deficient
if rank_A < min(A.shape):
    print("Matrix A is rank deficient.")
else:
    print("Matrix A is not rank deficient.")

# You can also print the rank and the singular values
print("Rank of A:", rank_A)
print("Singular values of A:", S)

# Use least squares to find the solution
a, residuals, rank, singular_values = np.linalg.lstsq(A, y, rcond=None)

# Print the solution
print("Solution for a:", a)
print(a, residuals, rank, singular_values)

#singular_values[2] = 0
a2 =  np.dot(VT.T, np.dot(S, np.dot(U.T, y)))


# # Compute and print the residual error
# # Sums of squared residuals: 
# # Squared Euclidean 2-norm for each column in b - a @ x. 
# # If the rank of a is < N or M <= N, this is an empty array.
print(residuals)
# # If b is 1-dimensional, this is a (1,) shape array. 
# # Otherwise the shape is (K,).
# residual_error = residuals[0]
# print("Residual error:", residual_error)


res = []
res.append(np.abs(y[0] - (0.1*a[0] - 0.2*a[1] + 0.3*a[2]))**2)
res.append(np.abs(y[1] - (0.2*a[0] - 0.1*a[1] + 0.4*a[2]))**2)
res.append(np.abs(y[2] - (-0.1*a[0] - 0.4*a[1] + 0.1*a[2]))**2)
res.append(np.abs(y[3] - (0.2*a[0] + 0.8*a[1] - 0.2*a[2]))**2)
print("Residual error:", res)

# Compute the covariance matrix
C = np.dot(VT.T, np.dot(np.diag(S**2), VT))

# Print the covariance matrix
print("Covariance Matrix:")
print(C)

# Compute the normal equations
ATA = np.dot(A.T, A)
ATy = np.dot(A.T, y)

# Solve the system using NumPy's linear algebra solver
a1 = np.linalg.solve(ATA, ATy)

# Print the solution
print("Solution for a:", a1)

# Calculate solution manually
#s2 = [[9.99465763e-01, 0, 0], [0, 5.01067049e-01, 0], [0, 0, 6.04080328e-17]]
s2 = np.diag(1/S)
s2[2][2] = 0
a2 = np.dot(VT.T, np.dot(s2, np.dot(U.T, y)))
print("Solution for a:", a2)
"""
########################################################################################
"""
A = np.array([[0.1, -0.2, 0.3],
              [0.2, -0.1, 0.4],
              [-0.1, -0.4, 0.1],
              [0.2, 0.8, -0.2001]])

y = np.array([0.4, 0.3, 0.7, 0.5])

# Perform Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Calculate the rank of A (number of non-zero singular values)
rank_A = np.linalg.matrix_rank(A)
print(rank_A)

# Determine if the system is over-, under-, or mixed determined
num_unknowns = A.shape[1]  # Number of columns in A
if rank_A == num_unknowns:
    print("The system is determined.")
elif rank_A < num_unknowns:
    print("The system is underdetermined (infinite solutions).")
else:
    print("The system is overdetermined (no exact solution).")

# Check if A is rank deficient
if rank_A < min(A.shape):
    print("Matrix A is rank deficient.")
else:
    print("Matrix A is not rank deficient.")

# Print the rank and the singular values
print("Rank of A:", rank_A)
print("Singular values of A:", S)

# Use least squares to find the solution
a, residuals, rank, singular_values = np.linalg.lstsq(A, y, rcond=None)

# Print the solution
print("Solution for a:", a)
print(a, residuals, rank, singular_values)

print(VT.T)


"""
"""
# Compute and print the residual error
# Sums of squared residuals: 
# Squared Euclidean 2-norm for each column in b - a @ x. 
# If the rank of a is < N or M <= N, this is an empty array.
print(residuals)
# If b is 1-dimensional, this is a (1,) shape array. 
# Otherwise the shape is (K,).
residual_error = residuals[0]
print("Residual error:", residual_error)
"""
"""

res = []
res.append(np.abs(y[0] - (0.1*a[0] - 0.2*a[1] + 0.3*a[2]))**2)
res.append(np.abs(y[1] - (0.2*a[0] - 0.1*a[1] + 0.4*a[2]))**2)
res.append(np.abs(y[2] - (-0.1*a[0] - 0.4*a[1] + 0.1*a[2]))**2)
res.append(np.abs(y[3] - (0.2*a[0] + 0.8*a[1] - 0.2*a[2]))**2)
print("Residual error:", res)

# Compute the covariance matrix
C = np.dot(VT.T, np.dot(np.diag(S**2), VT))

# Print the covariance matrix
print("Covariance Matrix:")
print(C)

# Compute the normal equations
ATA = np.dot(A.T, A)
ATy = np.dot(A.T, y)

# Solve the system using NumPy's linear algebra solver
a1 = np.linalg.solve(ATA, ATy)

# Print the solution
print("Solution for a:", a1)

print(np.dot(A,a))
print(np.dot(A,a1))

# Calculate solution manually
#s2 = [[9.99465763e-01, 0, 0], [0, 5.01067049e-01, 0], [0, 0, 6.04080328e-17]]
s2 = np.diag(1/S)
#s2[2][2] = 0
a2 = np.dot(VT.T, np.dot(s2, np.dot(U.T, y)))
print("Solution for a:", a2)
"""

############################################################################################
#"""
# Load the image of cute cat 
Ac = im.imread("cute_cat.jpg")

# SVD on the image
U, S, Vt = np.linalg.svd(Ac, full_matrices=False)

# Number of singular values to keep
num_singular_values2 = 2

# Reconstruct the image using a subset of singular values
reconstructed_image2 = np.dot(U[:, :num_singular_values2], np.dot(np.diag(S[:num_singular_values2]), Vt[:num_singular_values2, :]))

# Display the original and reconstructed images
plt.title('Original Image')
plt.imshow(Ac, cmap='gray')

plt.show()

plt.title('Reconstructed Image ({} singular values)'.format(num_singular_values2))
plt.imshow(reconstructed_image2, cmap='gray')

plt.show()

# Number of singular values to keep
num_singular_values5 = 5

# Reconstruct the image using a subset of singular values
reconstructed_image5 = np.dot(U[:, :num_singular_values5], np.dot(np.diag(S[:num_singular_values5]), Vt[:num_singular_values5, :]))
plt.title('Reconstructed Image ({} singular values)'.format(num_singular_values5))
plt.imshow(reconstructed_image5, cmap='gray')

plt.show()

# Number of singular values to keep
num_singular_values20 = 20

# Reconstruct the image using a subset of singular values
reconstructed_image20 = np.dot(U[:, :num_singular_values20], np.dot(np.diag(S[:num_singular_values20]), Vt[:num_singular_values20, :]))
plt.title('Reconstructed Image ({} singular values)'.format(num_singular_values20))
plt.imshow(reconstructed_image20, cmap='gray')

plt.show()

# Number of singular values to keep
num_singular_values100 = 100

# Reconstruct the image using a subset of singular values
reconstructed_image100 = np.dot(U[:, :num_singular_values100], np.dot(np.diag(S[:num_singular_values100]), Vt[:num_singular_values100, :]))
plt.title('Reconstructed Image ({} singular values)'.format(num_singular_values100))
plt.imshow(reconstructed_image100, cmap='gray')

plt.show()

# Number of singular values to keep
num_singular_values200 = 200

# Reconstruct the image using a subset of singular values
reconstructed_image200 = np.dot(U[:, :num_singular_values200], np.dot(np.diag(S[:num_singular_values200]), Vt[:num_singular_values200, :]))
plt.title('Reconstructed Image ({} singular values)'.format(num_singular_values200))
plt.imshow(reconstructed_image200, cmap='gray')

plt.show()
#"""