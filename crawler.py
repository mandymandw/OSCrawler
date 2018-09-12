import os, subprocess

def getPerms(path, isFile=True):
    if isFile:
        rwx = subprocess.Popen(['ls', '-l', path], stdout=subprocess.PIPE).communicate()
        return rwx[0][:10]
    else:
        rwx = subprocess.Popen(['ls', '-l', str(os.path.dirname(path))], stdout=subprocess.PIPE).communicate()
        for x in rwx[0].split('\n'):
            if os.path.basename(path) in x:
                return x.split()[0][:10]

def showFolderTree(path,show_files=False,indentation=2,file_output=False):
    """
    Shows the content of a folder in a tree structure.
    path -(string)- path of the root folder we want to show.
    show_files -(boolean)-  Whether or not we want to see files listed.
                            Defaults to False.
    indentation -(int)- Indentation we want to use, defaults to 2.   
    file_output -(string)-  Path (including the name) of the file where we want
                            to save the tree.
    """
    tree = []
    if not show_files:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' '*indentation*(level)
            tree.append('{}{}/'.format(indent,os.path.basename(root)))

    if show_files:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' '*indentation*(level)
            p = getPerms(root, False)
            tree.append('{}{}/\t{}'.format(indent, os.path.basename(root), p))    
            for f in files:
                subindent=' ' * indentation * (level+1)
                print root+'/'+f
                p = getPerms(root+'/'+f)
                tree.append('{}{}\t{}'.format(subindent,f, p))

    if file_output:
        output_file = open(file_output,'w')
        for line in tree:
            output_file.write(line)
            output_file.write('\n')
    else:
        # Default behaviour: print on screen.
        for line in tree:
            print line

if __name__=="__main__":
    showFolderTree('~/Downloads',show_files=True,indentation=4,file_output='~/Desktop/os_crawl.txt')