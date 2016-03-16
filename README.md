# SF-DAT-20

##Lecture 1 Summary

 - We talked about different roles of Data Scientists 
 - T-Shaped Data Scientists
 - Data Science Workflow
 - Continuous, Discrete and Qualitative Data
 - Supervised vs Unsupervised Learning
 - Set up github accounts
 - set ipython notebook
 - Introduced Numpy
 	
## Lecture 2 Summary
- Classification vs Clustering and Regression vs Dimentionality Reduction
- Flexibility vs Interpretability
- Different types of data (Cross-Sectional, Time-Series, Panel Data) 
- Walkthrough Acquire& Parses with Pandas
- HW 1 assigned - Due date Feb 8th at 6:30PM

## Lecture 3 Summary
- Measures of central tendency (Mean, Median, Mode, Quartiles, Percentiles)- Measures of Variability (IQR, Standard Deviation, Variance)- Skewness Coefficient - Kurtosis Coefficient- Boxplots- Bias vs Variance- Central Limit Theorem – Standard Error of Mean- Class/Dummy Variables
- Walkthrough describing and visualizing data in Pandas

## Lecture 4 Summary
- Linear Regression lines
- Single Variable and Multi-Variable Regression Lines
- Capture non-linearity using Linear Regression lines.
- Interpretting regression coefficients
- Dealing with dummy variables in regression lines
- intro on sklearn and searborn library
- HW 2 assigned - Due date Feb 17th 2016 at 6:30PM

## Lecture 5 Summary
- Hypothesis test - test of significance on regression coefficients
- p-value
- Capture non-linearity using Linear Regression lines.
- Different types of errors and R-squared
- Interaction Effects
	
## Lecture 6 Summary

- Bias-Variance Trade off
- Validation (Test vs Train set)
- Cross-Validation
- Ridge and Lasso Regression
- (Optional) Backward Selection, Forward Selection, All Subset Selection. (If you want to use these methods you need to use R)

## Lecture 7 Summary
- Types of missing data (MCAR, MAR, NMAR)
- Single imputation and their limitations
- Imuptation using regression lines and error
- Hot deck imputation
- multiple imputation


## Lecture 8 Summary
- Classification Problems
- Misclassifciation Error
- KNN algorithm for Classification
- Cross-Validation for KNN Algorithm
- Limitations of KNN Algorithm
- KNN algorithm for Regression

## Lecture 9 Summary
- Intro to Logistic Regression
- Odds vs Probability
- Using Logistic Regression to Make predictions
- How one interprets coefficients of Logistic Regression model
- Strength and weaknesses of Logistic Regression Model

## Lecture 10 Summary
- Unbalanced observations and Logistic Regression
- FP/FN/TP/TN/FPR/TPR
- The effect of chaning Threshold
- ROC Curves
- Area Under Curve
- How to compare classifciation algorithms

## Lecture 11 Summary
- Decision Tree for Regression
- Greedy Approach
- Decision Tree for Classification
- Gini Index and Entropy index
- Limitation of Simple Decision Tree

## Lecture 12 Summary
- Bagging
- Random Forest
- Boosting
- Tuning parameters for boosting and Random Forest

**Additional Resources**

- [Decision Tree - Video - Part 1](https://www.youtube.com/watch?v=U-dYqlvafYA)
- [Decision Tree - Video - Part 2](https://www.youtube.com/watch?v=6fopQt_ENeU)
- [Decision Tree - Video - Part 3](https://www.youtube.com/watch?v=BaPmPEWxKu0)
- [BootStrap - Video](https://www.youtube.com/watch?v=8bLsk1WXgDk)
 

## Lecture 13 Summary
- Definition of Natural Language Processing 
- NLP applications
- Basic NLP practice
- Stop words, bag-of-words, IF-DIF

**Additional Resources**

* If you want to learn a lot more NLP, check out the excellent [video lectures](https://class.coursera.org/nlp/lecture) and [slides](http://web.stanford.edu/~jurafsky/NLPCourseraSlides.html) from this [Coursera course](https://www.coursera.org/course/nlp) (which is no longer being offered).
* [Natural Language Processing with Python](http://www.nltk.org/book/) is the most popular book for going in-depth with the [Natural Language Toolkit](http://www.nltk.org/) (NLTK).
* [A Smattering of NLP in Python](https://github.com/charlieg/A-Smattering-of-NLP-in-Python/blob/master/A%20Smattering%20of%20NLP%20in%20Python.ipynb) provides a nice overview of NLTK, as does this [notebook from DAT5](https://github.com/justmarkham/DAT5/blob/master/notebooks/14_nlp.ipynb).
* [spaCy](http://spacy.io/) is a newer Python library for text processing that is focused on performance (unlike NLTK).
* If you want to get serious about NLP, [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml) is a suite of tools (written in Java) that is highly regarded.
* When working with a large text corpus in scikit-learn, [HashingVectorizer](http://scikit-learn.org/stable/modules/feature_extraction.html#vectorizing-a-large-text-corpus-with-the-hashing-trick) is a useful alternative to CountVectorizer.
* [Automatically Categorizing Yelp Businesses](http://engineeringblog.yelp.com/2015/09/automatically-categorizing-yelp-businesses.html) discusses how Yelp uses NLP and scikit-learn to solve the problem of uncategorized businesses.
* [Modern Methods for Sentiment Analysis](http://districtdatalabs.silvrback.com/modern-methods-for-sentiment-analysis) shows how "word vectors" can be used for more accurate sentiment analysis.
* [Identifying Humorous Cartoon Captions](http://www.cs.huji.ac.il/~dshahaf/pHumor.pdf) is a readable paper about identifying funny captions submitted to the New Yorker Caption Contest.