import pandas as pd
import numpy as np



# =====================================================
# Load CSV
# =====================================================

df = pd.read_csv("StudentsPerformance.csv")

arr = df[[
   "math score",
   "reading score",
   "writing score"
]].to_numpy()

# print(arr[:5])


# =====================================================
# Shape and indexing
# =====================================================

# print(arr.shape)

# print(arr[0])      # first student
# print(arr[:, 0])   # math scores
# print(arr[:, 1])   # reading scores
# print(arr[:, 2])   # writing scores

# =====================================================
# Mean / max / min
# =====================================================

subject_avg = np.mean(arr, axis=0)
# print(np.mean(arr, axis=0))
# print(np.max(arr, axis=0))
# print(np.min(arr, axis=0))

# =====================================================
# Boolean masking
# =====================================================

# Students scoring above 90:
high_math = arr[arr[:, 0] > 90] # in Math
high_reading = arr[arr[:, 1] > 90] # in Reading
high_writing = arr[arr[:, 2] > 90] # in Writing

# print(high_math)
# print(high_reading)
# print(high_writing)


# =====================================================
# Multiple conditions
# =====================================================

top_students = arr[
   (arr[:, 0] > 85) &
   (arr[:, 1] > 85) &
   (arr[:, 2] > 85)
]

# print(top_students)

# =====================================================
# Average score per student
# =====================================================

avg_scores = np.mean(arr, axis=1)

# print(avg_scores[:10].reshape(10,1))


# =====================================================
# Add grades using vectorization
# =====================================================

grades = np.where(avg_scores >= 90, "A",
        np.where(avg_scores >= 75, "B",
        np.where(avg_scores >= 60, "C", "F")))

# print(grades[:10])

# =====================================================
# Sorting
# =====================================================

# Top 5 students:

top_indices = np.argsort(avg_scores)[-5:]

# print(arr[top_indices])

# =====================================================
# Standard deviation
# =====================================================

# print(np.std(arr, axis=0))

# =====================================================
# Normalization
# =====================================================

normalized = (arr - np.mean(arr, axis=0)) / np.std(arr, axis=0)

# print(normalized[:5])


# =====================================================
# Average of each subject
# =====================================================

math_avg = np.mean(arr[:,0],axis=0)
reading_avg = np.mean(arr[:,1],axis=0)
writing_avg = np.mean(arr[:,2],axis=0)

print("\nAverage Scores:\n")
print(f"Math: {math_avg}")
print(f"Reading: {reading_avg}")
print(f"Writing: {writing_avg}")

top_student = np.argmax(avg_scores)

print("\nTop student index:", top_student)
print("Top student average:", avg_scores[top_student])

failed_count = np.sum(grades == "F")

print("\nFailed students count:", failed_count)

# Best subject
subjects = np.array(["Math", "Reading", "Writing"])

best_subject = subjects[np.argmax(subject_avg)]

print("\nBest subject:", best_subject)



