## Decision Trees

Decision tree learning or induction of decision trees is one of the predictive modelling approaches used in statistics, data mining and machine learning. It uses a decision tree (as a predictive model) to go from observations about an item (represented in the branches) to conclusions about the item's target value (represented in the leaves). Tree models where the target variable can take a discrete set of values are called classification trees; in these tree structures, leaves represent class labels and branches represent conjunctions of features that lead to those class labels. Decision trees where the target variable can take continuous values (typically real numbers) are called regression trees. Decision trees are among the most popular machine learning algorithms given their intelligibility and simplicity.

The model splits the input space into (hyper) rectangles, and predictions are made according to the area observations fall into.
![image](https://user-images.githubusercontent.com/12089275/120892513-0378f580-c60f-11eb-826f-72e1c163d82c.png)


### Learning:


Learning of a CART is done by a greedy approach called recursive binary splitting of the input space:
At each step, the best predictor $X_j$ and the best cutpoint s
are selected such that $\{X|X_j < s\}$  and $\{X|X_j ≥ s\}$ 
minimizes the cost.
- For regression the cost is the Sum of Squared Error.
- For classification the cost function is the Gini index.
    
The Gini index is an indication of how pure are the leaves, if all observations are the same type G=0 (perfect purity),
while a 50-50 split for binary would be G=0.5 (worst purity).
    
The most common **Stopping Criterion** for splitting is a minimum of training observations per node.
The simplest form of pruning is Reduced Error Pruning:
Starting at the leaves, each node is replaced with its most popular class. If the prediction accuracy is not affected, then
the change is kept.
    
    
### Advantages:
+ Easy to interpret and no overfitting with pruning
+ Works for both regression and classification problems
+ Can take any type of variables without modifications, and do not require any data preparation

### Usecase examples:
- Fraudulent transaction classification
- Predict human resource allocation in companies
