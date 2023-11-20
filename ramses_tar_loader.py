def ramses_tar_loader(path, output, extension=".tar.gz"):
    """
    Function to extract RAMSES data from a 
    tar file to store as a YT data product
    
    Requires
    --------
    import tarfile
    import os
    
    Inputs
    ------
    path:      string representing path to tar file
    output:    integer of the filenumber to extract
    extension: string of the tar extension, defaults to .tar.gz
    
    Returns
    -------
    ds: a yt dataframe for the selected output
    """
    
    filenum = "output_" + f'{output:05d}'
    loadName = filenum + "/info_" + f'{output:05d}' + ".txt"
    with tarfile.open(path + filenum + extension, "r") as tf:
        tf.extractall(path="./tmp_dir")    
    ds = yt.load("./tmp_dir/" + loadName)   # load in the file to yt
    os.rmdir("./tmp_dir")                   # delete temporary extraction
    return ds
