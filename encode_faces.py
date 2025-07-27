"""
Face Encoding Generation System

This module generates facial encodings from a dataset of face images for use in
face recognition systems. It processes images, detects faces, and creates 128-dimensional
facial feature vectors that can be used for face comparison and identification.

Key Features:
- Face detection using HOG or CNN models
- 128-dimensional facial encoding generation
- Support for multiple face detection methods
- Batch processing of image datasets
- Serialization of encodings for later use

Usage:
    python encode_faces.py --dataset dataset/ --encodings encodings.pickle

Author: UAV Security System Team
License: MIT
"""

# USAGE
# python encode_faces.py --dataset dataset --encodings encodings.pickle

# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

def process_face_dataset(dataset_path, encodings_path, detection_method="cnn"):
    """
    Process a dataset of face images and generate facial encodings.
    
    This function processes all images in the specified dataset directory,
    detects faces in each image, generates facial encodings, and saves
    them to a pickle file for later use in face recognition.
    
    Args:
        dataset_path (str): Path to the directory containing face images
        encodings_path (str): Path where encodings will be saved
        detection_method (str): Face detection method ('hog' or 'cnn')
        
    Note:
        The dataset should be organized with subdirectories named after
        each person, containing their face images.
    """
    # grab the paths to the input images in our dataset
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images(dataset_path))

    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,
            len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]

        # load the input image and convert it from RGB (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
            model=detection_method)

        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)

        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open(encodings_path, "wb")
    f.write(pickle.dumps(data))
    f.close()

def main():
    """
    Main function to parse arguments and process face dataset.
    
    This function handles command line argument parsing and calls the
    face processing function with the specified parameters.
    """
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--dataset", required=True,
        help="path to input directory of faces + images")
    ap.add_argument("-e", "--encodings", required=True,
        help="path to serialized db of facial encodings")
    ap.add_argument("-d", "--detection-method", type=str, default="cnn",
        help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())
    
    # Process the face dataset
    process_face_dataset(args["dataset"], args["encodings"], args["detection_method"])

if __name__ == "__main__":
    main()