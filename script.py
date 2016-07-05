import sys
import requests
import time
import shutil
import urllib
import os
import argparse


def getUrls(file):
    """
    Read the Content of the file and split it by line into a List : Every line is an Element in the returned list
    Args:
        file: A Path to a textplain file

    Returns:
        A List of strings : URLs
    Raises:
        IOError
    """
    try:
        return [line.rstrip('\n') for line in open(file)] # get Urls fron a Text File return a list of string : URLs
    except Exception as e:
        print 'Something went wrong when getting URLs from file : ' + file
        raise e

def ensureDirectoryExists(directory):
    """Check if the directory Exists and if not create the directory

    Args:
        directory: A Path to a directory

    Returns:

    Raises:
        IOError : Permission denied
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        print 'Something went wrong.'
        raise e


def downloadImages(imagesURLs,localFolder):
    """
    Downloads Images to a local Folder
    Args:
        imagesURLs: a List of string : URLs of Images
        localFolder : A  string Path to a directory
    Returns:

    Raises:
        IOError: No such file or directory
    It only print the error and continue in order to download other images. In a bigger system it must be logged.
    """
    ensureDirectoryExists(localFolder) # Ensuring that the Folder exists if not  creating it.
    for imageURL in imagesURLs: # Looping through the List of URLs
        try:
            filename = imageURL.strip().split('/')[-1].strip() # getting the filename consdediring that the URL is in this format : http://somewebsrv.com/img/filename
            print 'Getting: ' + filename
            urllib.urlretrieve(imageURL, os.path.join(localFolder,filename)) # Saving the Image to the Local Folder
        except Exception as e:
            print '  An error occured with file :  '+ filename +' . Continuing.'
        print 'Done.'

def getArgs():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Script Downloads Images and save them to a local Folder.')
    # Add arguments
    parser.add_argument(
        '-f', '--file', type=str, help='File that contains  URLs.', required=True)
    parser.add_argument(
        '-d', '--directory', type=str, help='The Directory where to save images.', required=False, default='images')
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    file = args.file
    directory = args.directory
    # Return all variable values
    return file, directory

if __name__ == '__main__':
    file , localFolder = getArgs() # Get Arguments
    URLs = getUrls(file) # Get Urls fron the file
    downloadImages(URLs,localFolder) # Download Images
