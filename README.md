This is the code for the "Cranial implant prediction by learning an ensemble of slice-based skull completion networks"
MICCAI AutoImplant Challenge 2021

To run this model, you first need to go this "SourceCode' file.
Then you need to put the your folder that content the nrrd files in this folder.
If you use the dataset of the AutoImplant Challenge 2021 task1's dataset.
You can just put the folder that called "nrrd" in that zip file in this folder, every thing will work fine.
If you uses your own dataset, please make sure you have set all the nrrd file to the 512x512x512.

Then we need to create a dataset for the CNN model.
you can find there is a python file called "CreateCNNdataset.py".
If you uses the Challenge's dataset, you can just run this code. uses:
python CreateCNNdataset.py.
you do not need to change any thing.
If your uses you own dataset,
you need to change every folderPath variable, output variable, skulls variable, imp_data variable and the def_data variable.
For the first part in the python file is used to reorder the nrrd files provided by the competition team.
you maybe do not need it for your own dataset.
The second part is going to create the slice of different axis.
the output1 to output3 are the targets.
The output4 to output6 are the inputs.
The skulls are the primary path that uses to find the list of the name of the targets.
For the slicer part. we found that the result is not good if we have the blank targets.
therefore, we have removed all the blank image and the corresponding inputs images.
The imp_data is the targets,
The def_data is the inputs.

Finally we need to run the model.
The model and the training and evaluate code are in the CodeForPaper.ipynb file.
you can just follow the instructions that I have write in that file to get the result.  
