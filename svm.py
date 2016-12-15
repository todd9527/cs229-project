from sklearn.svm import SVC
import sys 
import model
import model_util 

X_DIR = 'HOG'

def main():
	if len(sys.argv) != 4:
		return
	batch = sys.argv[1]
	name = sys.argv[2]
	num_pages = int(sys.argv[3])

	# Get descriptors by reading descriptor file (single file for train/test!!!)
	# Get labels by calling model_util.prepare_data(batch, name, num_pages)

	clf = SVC(kernel='rbf')
    clf.fit(X_train, Y_train)
    preds = clf.predict(X_test))
	print preds 
	# Calculate precision and recall here 


	# Do cross validation here 


if __name__ == "__main__":
    main()


#****Example code from SKlearn*********
# class sklearn.svm.SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', 
# 	coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, 
# 	class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None,
# 	 random_state=None)[source]¶
# clf = SVC()
# clf.fit(X, y) 
# ##SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)   ##
# print(clf.predict([[-0.8, -1]]))
#***************************************


###Example random forest code from SKlearn***
# class sklearn.ensemble.RandomForestClassifier(n_estimators=10, 
# 	criterion='gini', max_depth=None, min_samples_split=2,
# 	 min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', 
# 	 max_leaf_nodes=None, min_impurity_split=1e-07, bootstrap=True, oob_score=False,
# 	  n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)[source]¶
# fit(X, y, sample_weight=None)[source]
# predict(X)[source]
#********************************************

