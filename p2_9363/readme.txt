Nikolai Ruhe
04/13/2018
Dr. Chan
AI Class

This program is not written with any API for the bayesian classifier
or the weka file arff input. All code work is original.

However, some test cases may break this program, so please start testing with
the sample data I provide, and maybe your data will work. String comparison was also
creating difficult situations for me when going back and forth between linux using
python 2.7.6 and my windows machine running pycharm with 2.7.13.
This is why the .__contains__ method was used in the testing section....
an act of god kind of bug....

Anyway, sorry for the long readme, Cameron. Please let me know if you have any questions:
Niko Ruhe
nmr33@zips.uakron.edu

Start by using the training file:
	weather.nominal.arff

Then use the testing file:
	weather.nominal.testdata.arff
	
Modify these files to have the same format to test different types of cases.
Uploading your own files may or may not work depending on format. Sorry about that.

To run this program, follow these steps:
1) open a linux terminal
2) run the command:
	python p2_9363.py
	
3) enter the training file:
	weather.nominal.arff
	
4) notice the bayesian classifier is outputted as weather.nominal.arff.bin

5) enter the testing file:
	weather.nominal.testdata.arff
	
6) notice the confusion matrix is outputted as weather.nominal.testdata.arff.CONFUSION

Thank you
