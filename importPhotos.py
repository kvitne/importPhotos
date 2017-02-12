#!/usr/bin/env python3

from datetime import datetime
import os
import time

fromDir = ""


def get_filepaths_ctime(directory):
    """Returns full filepath and file with associated creation-time in a
    datetime-format.
    """
    file_list = []
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        fileInfo = os.stat(filepath)
        cdate = time.ctime(fileInfo.st_ctime)
        creationTime = datetime.strptime(cdate, "%c")
        file_list.append((filepath, creationTime))
    return file_list




print(get_filepaths_ctime(fromDir))


listFilesCtime = get_filepaths_ctime(fromDir)


def convert_dates_toordinal(listFilesCtime):
    filesIntCtime = []
    for fileCtime in listFilesCtime:
        ctime = fileCtime[1]
        print(fileCtime[1])
        date_int = ctime.toordinal()
        print(date_int)
        filesIntCtime.append((fileCtime[0], fileCtime[1], date_int))
    return filesIntCtime


print(convert_dates_toordinal(listFilesCtime))


def is_date_neighbor(listFilesCtime):
    foldernames = []
    for index, x in enumerate(listFilesCtime):
        if index == 0:
            foldernames


# def find_neighbor_dates(listOfTuples):
