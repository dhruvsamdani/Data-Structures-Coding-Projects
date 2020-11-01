import os



def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    pathList = []
    def searchFiles(suffix, path):

      if path == '' or path == None or suffix == None:
       
        return print('Invalid path or suffix')

      if path.endswith(suffix):
        pathList.append(path)
        return
      if not (os.path.isfile(path)):
        if os.path.isdir(path):
          for value in os.listdir(path):

            newpath = path + '/' + value
            
            searchFiles(suffix, newpath)
        
      else:
        return
      
    searchFiles(suffix, path)
    return pathList

print(find_files('.c', 'testdir')) # ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/t1.c']

print(find_files('', 'testdir')) # ['testdir']

print(find_files('.abdf', '')) # []

print(find_files(None, 'testdir')) # []