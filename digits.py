# This example shows how scikit-learn can be used to recognize images of hand-written digits, from 0-9.

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause


# Import datasets, classifiers and performance metrics
from utils import preprocess_data, train_model, split_train_dev_test,read_digits,predict_and_eval

gama_ranges = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
C_ranges = [0.1,1,2,5,10]
# The digits dataset consists of 8x8 pixel images of digits. The images attribute of the dataset stores 8x8 arrays of grayscale values for each image. We will use these arrays to visualize the first 4 images. The target attribute of the dataset stores the digit each image represents and this is included in the title of the 4 plots below.
# Note: if we were working from image files (e.g., ‘png’ files), we would load them using matplotlib.pyplot.imread.

# 1. Data Loading


x,y = read_digits()

# 3. Data splitting
X_train, X_test,X_dev, y_train, y_test,y_dev = split_train_dev_test(x, y, test_size=0.3, dev_size=0.2);

# 4. Data Preprocessing
X_train = preprocess_data(X_train)
X_test = preprocess_data(X_test)
X_dev = preprocess_data(X_dev)

best_accuracy_so_far = -1
best_model = None
for cur_gamma in gama_ranges:
    for cur_c in C_ranges:
        cur_model = train_model(X_train, y_train, {'gamma': cur_gamma,'C':cur_c}, model_type='svm')
        cur_accuracy,predicted = predict_and_eval(cur_model, X_dev, y_dev)
        if cur_accuracy > best_accuracy_so_far:
            print(f"New best accuracy {cur_accuracy}")
            best_accuracy_so_far = cur_accuracy
            optimal_gamma = cur_gamma
            optimal_C = cur_c
            best_model = cur_model

print(f"Optimal C is {optimal_C} , Optimal gamma is {optimal_gamma}")


# 5. Train the data
model = train_model(X_train, y_train, {'gamma': optimal_gamma,'C':optimal_C}, model_type='svm')



# Predict the value of the digit on the test subset
# 6.Predict and Evaluate 
accuracy,predicted = predict_and_eval(model, X_test, y_test)
