# Naive-Bayes-Classifier-with-Text-representation-using-Bag-Of-Words

# Reading Data:

The code reads a CSV file named "spam.csv" into a DataFrame.
It displays the first few rows of the DataFrame to get an initial look at the data.

# Counting Categories:

Counts and displays the number of occurrences of each unique value in the "Category" column.
This helps understand the distribution of spam and non-spam messages in the dataset.

# Label Conversion:

Adds a new column "spam" to the DataFrame, containing binary labels (1 for "spam" and 0 for "ham").
Uses the "apply" function and a lambda function to convert text labels to numerical labels.

# Train-Test Split:
Splits the data into training and testing sets.
x_train and x_test contain message texts, while y_train and y_test contain corresponding labels.

# Count Vectorization (Training):
Uses CountVectorizer to convert text messages in x_train into a document-term matrix.
This matrix represents the frequency of words in the messages.

# Naive Bayes Training:
Initializes a Multinomial Naive Bayes model and trains it using the document-term matrix (x_train_cv) and labels (y_train).

# Count Vectorization (Testing):
Converts the text messages in the test set (x_test) into a format compatible with the trained model using the same CountVectorizer.

# Prediction:
Uses the trained Naive Bayes model to predict labels for the test data (x_test_cv).

# Evaluation (Without Pipeline):
Prints a classification report that shows metrics like precision, recall, and F1-score to evaluate the performance of the model on the test data.

# Creating a Pipeline:
Creates a pipeline that combines CountVectorizer and Multinomial Naive Bayes steps.

# Pipeline Training:
Fits the pipeline on the training data (x_train and y_train).

# Evaluation (With Pipeline):
Prints a classification report for the pipeline's predictions on the test data (x_test).

The code demonstrates the process of reading, preprocessing, training, and evaluating a spam classification model using the Naive Bayes algorithm and CountVectorizer. It shows the results both without and with the use of a pipeline for streamlining the process.





