# ORPerceptron
Lydia Noureldin
April 7 2017

ORPeceptron implemented in Python v 2.7 

In machine learning, the "perceptron" is an algorithm for supervised learning of binary classifiers (functions that can decide whether an input, represented by a vector of numbers, belongs to some specific class or not). For more on perceptrons see: https://en.wikipedia.org/wiki/Perceptron 

This particular perceptron was trained to classify a four-input OR function, that is  A v B v C v D. The Perceptron uses a few formulas during its learning process. It uses weights, wi … w4, a X input value, and a Y output value (or step value). These are calculated using formulas that are explained in the technical document. 

Please refer to the technical document for an in-depth explanation of the algorithm and code.

Project contains/produces:
1. ORPerceptron_training.py - file used to train ORPerceptron
2. training.txt - file produced after running ORPerceptron_training.py. This contains the trained weight values
3. ORPerceptron.py - file used to test trained ORPerceptron 
4. in.txt - input file containing vectors separated by a new line
5. out.txt - output file produced after running ORPerceptron.py. This will contain ORPerceptron output values separated by a bank line. 
6. TechnicalDocument.pdf

You only need to run ORPerceptron.py. The ORPectron_training.py has already been run and training.txt is already populated with the trained weights. If you want to go through the process of training the perceptron follow the following steps:
1. Delete the training.txt file from the folder
2. Run ORPerceptron_training.py (this will create a new training.txt file)
3. Run ORPerceptron.py
