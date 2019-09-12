import os
import shutil
import nibabel as nib
from nibabel.processing import smooth_image
from scipy.ndimage import gaussian_filter

directory = ""		# enter directory here

if os.path.isdir("PIPE/GROUP") == False:
    print("No 'GROUP' folder exists...")
    os.mkdir("PIPE")
    os.mkdir("PIPE/GROUP")
    os.mkdir("PIPE/GROUP/SPECT")
    os.mkdir("PIPE/GROUP/CT")
    print("So a folder 'GROUP' has been created." + "\n")

files = []
for r, d, f in os.walk(directory):
    if r.endswith("results"):
        for file in f:
            if '.nii' in file:
                if file.startswith("s"):
                    files.append(os.path.join(r, file))
                    shutil.copyfile(r + "/" + file, "PIPE/GROUP/SPECT/" + file)
                    print(file)
                if file.startswith("CT_s"):
                    files.append(os.path.join(r, file))
                    shutil.copyfile(r + "/" + file, "PIPE/GROUP/CT/" + file)
                    print(file)

if os.path.isdir("PIPE/SMOOTH") == False:
    print("No 'SMOOTH' folder exists...")
    os.mkdir("PIPE/SMOOTH")
    print("So a folder 'SMOOTH' has been created." + "\n")

for filename in os.listdir("PIPE/GROUP/SPECT/"):
    img_nii = nib.load("PIPE/GROUP/SPECT/" + filename)  # load in the image
    img_nii_smooth = smooth_image(img_nii, [2, 2, 2])  # smooth the image with a Gaussian filter set at 2 mm
    nib.save(img_nii_smooth, "PIPE/SMOOTH/" + filename[:-4] + "_smooth" + ".nii")  # save the new image
    print(filename + " has been smoothed with a Gaussian filter set at 2 mm.")
