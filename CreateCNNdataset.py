# -*- coding: utf-8 -*-
import glob
import os
import nrrd
import cv2

# This part is used to reorder the nrrd files provided by the competition team

folderPath = './nrrd/implant/frontoorbital'

fileSequence = 114

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1

folderPath = './nrrd/implant/parietotemporal'

fileSequence = 228

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1

folderPath = './nrrd/implant/random_1'

fileSequence = 342

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1

folderPath = './nrrd/implant/random_2'

fileSequence = 456

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1



folderPath = './nrrd/defective_skull/frontoorbital'

fileSequence = 114

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1


folderPath = './nrrd/defective_skull/parietotemporal'

fileSequence = 228

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1

folderPath = './nrrd/defective_skull/random_1'

fileSequence = 342

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1

folderPath = './nrrd/defective_skull/random_2'

fileSequence = 456

for filename in os.listdir(folderPath):
	os.rename(folderPath + '//' + filename,folderPath + '//' + str(fileSequence) + '.nrrd')
	fileSequence +=1


# This part is used to slice the nrrd file provided by the contestant

output1 = "./CNN_dataset/implant/registrations/z_axis"
output2 = "./CNN_dataset/implant/registrations/y_axis"
output3 = "./CNN_dataset/implant/registrations/x_axis"
output4 = "./CNN_dataset/defective_skull/registrations/z_axis"
output5 = "./CNN_dataset/defective_skull/registrations/y_axis"
output6 = "./CNN_dataset/defective_skull/registrations/x_axis"

if not os.path.exists(output1):
    os.makedirs(output1)
if not os.path.exists(output2):
    os.makedirs(output2)
if not os.path.exists(output3):
    os.makedirs(output3)
if not os.path.exists(output4):
    os.makedirs(output4)
if not os.path.exists(output5):
    os.makedirs(output5)
if not os.path.exists(output6):
    os.makedirs(output6)

skulls = glob.glob("./nrrd/implant/bilateral/*.nrrd")
case = sorted([os.path.basename(s).split(".")[0] for s in skulls])

print(len(case))

for i, case in enumerate(case):
    print("case: ", case)
    imp_data, option = nrrd.read("./nrrd/implant/bilateral/"+case+".nrrd")
    def_data, option = nrrd.read("./nrrd/defective_skull/bilateral/" + case + ".nrrd")
    x, y, z = imp_data.shape
    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, :, i])
        def_image.append(def_data[:, :, i])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output1, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output4, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, i, :])
        def_image.append(def_data[:, i, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output2, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output5, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[i, :, :])
        def_image.append(def_data[i, :, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output3, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output6, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

skulls = glob.glob("./nrrd/implant/frontoorbital/*.nrrd")
case = sorted([os.path.basename(s).split(".")[0] for s in skulls])

print(len(case))

for i, case in enumerate(case):
    print("case: ", case)
    imp_data, option = nrrd.read("./nrrd/implant/frontoorbital/"+case+".nrrd")
    def_data, option = nrrd.read("./nrrd/defective_skull/frontoorbital/" + case + ".nrrd")
    x, y, z = imp_data.shape
    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, :, i])
        def_image.append(def_data[:, :, i])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output1, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output4, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, i, :])
        def_image.append(def_data[:, i, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output2, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output5, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[i, :, :])
        def_image.append(def_data[i, :, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output3, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output6, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

skulls = glob.glob("./nrrd/implant/parietotemporal/*.nrrd")
case = sorted([os.path.basename(s).split(".")[0] for s in skulls])

print(len(case))

for i, case in enumerate(case):
    print("case: ", case)
    imp_data, option = nrrd.read("./nrrd/implant/parietotemporal/"+case+".nrrd")
    def_data, option = nrrd.read("./nrrd/defective_skull/parietotemporal/" + case + ".nrrd")
    x, y, z = imp_data.shape
    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, :, i])
        def_image.append(def_data[:, :, i])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output1, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output4, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, i, :])
        def_image.append(def_data[:, i, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output2, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output5, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[i, :, :])
        def_image.append(def_data[i, :, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output3, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output6, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

skulls = glob.glob("./nrrd/implant/random_1/*.nrrd")
case = sorted([os.path.basename(s).split(".")[0] for s in skulls])

print(len(case))

for i, case in enumerate(case):
    print("case: ", case)
    imp_data, option = nrrd.read("./nrrd/implant/random_1/"+case+".nrrd")
    def_data, option = nrrd.read("./nrrd/defective_skull/random_1/" + case + ".nrrd")
    x, y, z = imp_data.shape
    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, :, i])
        def_image.append(def_data[:, :, i])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output1, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output4, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, i, :])
        def_image.append(def_data[:, i, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output2, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output5, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[i, :, :])
        def_image.append(def_data[i, :, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output3, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output6, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

skulls = glob.glob("./nrrd/implant/random_2/*.nrrd")
case = sorted([os.path.basename(s).split(".")[0] for s in skulls])

print(len(case))

for i, case in enumerate(case):
    print("case: ", case)
    imp_data, option = nrrd.read("./nrrd/implant/random_2/"+case+".nrrd")
    def_data, option = nrrd.read("./nrrd/defective_skull/random_2/" + case + ".nrrd")
    x, y, z = imp_data.shape
    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, :, i])
        def_image.append(def_data[:, :, i])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output1, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output4, "{}-{}".format(case, k) + "-z.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[:, i, :])
        def_image.append(def_data[:, i, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output2, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output5, "{}-{}".format(case, k) + "-y.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

    imp_image = []
    def_image = []
    for i in range(z):
        imp_image.append(imp_data[i, :, :])
        def_image.append(def_data[i, :, :])
    k = 1
    for i in imp_image:
        if i.sum()!=0:
            output_name = os.path.join(output3, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, i)
            output_name = os.path.join(output6, "{}-{}".format(case, k) + "-x.png")
            cv2.imwrite(output_name, def_image[k])
        k += 1

