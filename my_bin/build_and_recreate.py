import os
import errno
import subprocess

WEEX_PATH="/home/weewx"
PACKED_FILE="belchertwown-current.tar.gz"
DST_SRC="/home/openhabian/weex_temp"
DO_EXEC=True

def pack_belchertown():
    cmd="".join(["tar -czvf ", DST_SRC, "/", PACKED_FILE ," ../../weewx-belchertown"])
    return execute_command(cmd)

def make_directory(dirName):
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except OSError as e:
        if e.errno == errno.EEXIST:
            print('Directory exists')
        elif e.errno == errno.EACCES:
            print('Access violation')
            return False
        else:
            print('Some other problems in make_directory')
            return False
    return True

def install_extension():
    cmd="".join(["sudo ",WEEX_PATH,"/bin/wee_extension --install ", DST_SRC, "/", PACKED_FILE])
    return execute_command(cmd)

def redo_report():
    cmd="".join(["sudo ",WEEX_PATH,"/bin/wee_reports ", WEEX_PATH, "/weewx.conf"])
    return execute_command(cmd)

def execute_command(cmd):
    print(cmd)
    if DO_EXEC:
        rc = os.system(cmd)
        if rc != 0:
            return False
    return True

def main():
    #from pudb import set_trace; set_trace() # BREAKPOINT
    if (make_directory(DST_SRC) == False):
        print("Error in make_directory")
        return -1
    if (pack_belchertown() == False):
        print("Error in pack_belchertown")
        return -1
    if (install_extension() == False):
        print("Error in install_extension")
        return -1
    if (redo_report() == False):
        print("Error in redo_report")
        return -1


if __name__ == "__main__":
    main()


