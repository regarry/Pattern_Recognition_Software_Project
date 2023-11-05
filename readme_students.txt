% pattern recognition software, GEB, summer 2023

% scripts
*test_knn              test built-in knn classifier using testdata.mat
                       includes use of metadata and scatter plots

% functions
*metagen               create meta data associated with a dataset
*performance           evaluate performancev of a classifier
                       (confusion matrix, probability classif. error,
                        conditional prob. class error given true class)
% datasets
*testdata.mat          for testing and debug
*irisf34.mat           iris, features 1&2 (sepal len, width) deleted
*iristestvectors.mat   set of 7 test vectors for milestone2 (meastest,speciestest)

% datasets in csv format (for Python programming and certain MATLAB tools)
*iriscorrected.csv    corrected iris dataset per iris.names file
*irisf34.csv          corrected iris dataset, only features 3 and 4