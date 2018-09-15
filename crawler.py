import os, subprocess

# def findnth(haystack, needle, n):
#     parts= haystack.split(needle, n+1)
#     if len(parts)<=n+1:
#         return -1
#     return len(haystack)-len(parts[-1])-len(needle)

def getPerms(path, isFile=True):
    if isFile:
        rwx = subprocess.Popen(['ls', '-l', path], stdout=subprocess.PIPE).communicate()
        res = rwx[0].split()
        return res[0][:10], res[2], res[3]
    else:
        rwx = subprocess.Popen(['ls', '-l', str(os.path.dirname(path))], stdout=subprocess.PIPE).communicate()
        for x in rwx[0].split('\n'):
            res = x.split(None, 8)
            if os.path.basename(path) == res[len(res)-1]:
                return res[0][:10], res[2], res[3]

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
            if os.path.basename(root)[0] =='.': continue
            level = root.replace(path, '').count(os.sep)
            indent = ' '*indentation*(level)
            p,u,g = getPerms(root, False)
            # tree.append('{}{}/\t{}'.format(indent, os.path.basename(root), p))  
            # show the entire absolute path without indentation
            tree.append('{}\t{}\t{}\t{}'.format(root, p,u,g))
            for f in files:
                if os.path.basename(f)[0] =='.': continue
                subindent=' ' * indentation * (level+1)
                p,u,g = getPerms(root+'/'+f)
                # tree.append('{}{}\t{}'.format(subindent,f, p))
                tree.append('{}\t{}\t{}\t{}'.format(root+'/'+f, p,u,g))

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
    showFolderTree('/Users/manw/Downloads',show_files=True,indentation=4,file_output='/Users/manw/Documents/Projects/OSCrawler/DownloadsCrawl.txt')