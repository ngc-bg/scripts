    #!/usr/bin/env python

    #********************************* README **************************************

    #

    # SNAPSHOT / BACKUP script for Windows/Linux

    # script by Jan-Philip Gehrcke -- jgehrcke@gmail.com -- http://gehrcke.de

    #

    # 0) DESCRIPTION:

    # ===============

    # On invocation, the script creates a snapshot of ORIG_DIR's contents and writes

    # it to BACKUP_DIR into 1) a new subdirectory or 2) a .tar.bz2 archive or 3) a

    # 7zip archive (choose it!). The time of snapshot creation is written into the

    # subdirectorie's name / archive file name. An optional second location can

    # be defined to which the snapshot will be written additionally.

    #

    # This script is useful to manually and quickly create snapshots of a multi-file

    # project you're working on, enabling _rollbacks_ to an older version of your

    # project's files. Furthermore, using the additional backup location on another

    # physical storage, the script prevents _data loss_.

    #

    # Primarily, this script is written for Windows users: simple double-click .py

    # file invocation is considered. Should work on Linux systems, too, but the

    # "press any key to continue" dialogue is quite un-unixoid.

    #

    # 1) USAGE:

    # =========

    #

    # Download and install Python 2.6.x: http://python.org/download/

    # For 7zip method, download http://www.7-zip.org/download.html

    #

    # Put the script file into the directory containing the directory you want to

    # back up, adjust settings (below) and then run the script (doubleclick on Win).

    #

    # The snapshot/backup of

    #  ./ORIG_DIR/*

    # will go to

    #  ./BACKUP_DIR/BACKUP_PREFIX_timestring/*       (SIMPLE method, built-in)

    # OR to the archive

    #  ./BACKUP_DIR/BACKUP_PREFIX_timestring.tar.bz2 (BZ2 method, built-in)

    # OR to the archive

    #  ./BACKUP_DIR/BACKUP_PREFIX_timestring.7z      (7zip method; ultra strong

    #                                                 compression; faster than BZ2;

    #                                                 requires 7zip to be available)

    #

    # Of course, ORIG_DIR and BACKUP_DIR can be absolute paths, too. Then, the

    # location of this script does not matter.

    #

    # 2) SETTINGS:

    # ============

    # always use SLASHES ("/") in paths, even on Windows -> don't use "\"

    ORIG_DIR = "C:/project"          # e.g. "." or "C:/project"

    BACKUP_DIR = "C:/backups"        # e.g. "C:/backups"

    BACKUP_PREFIX = "thesis_bckp"      # e.g. "thesis_bckp"

     

    # choose backup method: 'SIMPLE' OR 'BZ2' OR '7zip':

    METHOD = '7zip'     # quick and really strong compression, 7zip.exe required

    #METHOD = 'SIMPLE'  # copy directory tree; e.g. if you don't have many files..

    #METHOD = 'BZ2'     # builtin method; if you like compression, but no 7zip.

     

    # in case of 7zip, specify 7z executable path:

    SEVENZIPPATH = "c:/Programs/7-Zip/7z.exe" # e.g. "c:/Programs/7-Zip/7z.exe"

     

    # set ADDITIONAL_BACKUP_DIR to double-save backup (e.g. on another hard disk)

    # (outcomment the line if this is undesired behavior)

    ADDITIONAL_BACKUP_DIR = "F:/backups"   # e.g. "F:/backups"

    #*******************************************************************************

     

    import os, time, shutil, sys, tarfile, subprocess, traceback

     

    def backup_directory_simple(srcdir,dstdir):

        if os.path.exists(dstdir):

            exit_stop("backup path %s already exists!" % dstdir)

        try:

            shutil.copytree(srcdir,dstdir)

        except:

            print "Error while copying tree in %s to %s" % (srcdir,dstdir)

            print "Traceback:\n%s"%traceback.format_exc()

            return False

        return dstdir

     

    def backup_directory_bz2(srcdir,tarpath):

        if os.path.exists(tarpath):

            exit_stop("backup path %s already exists!" % tarpath)

        try:

            tar = tarfile.open(tarpath, "w:bz2")

            for filedir in os.listdir(srcdir):

               tar.add(os.path.join(srcdir,filedir),arcname=filedir)

            tar.close()

        except:

            print "Error while creating tar archive: %s" % tarpath

            print "Traceback:\n%s"%traceback.format_exc()

            return False

        return tarpath

     

    def backup_directory_7zip(srcdir,arcpath):

        if os.path.exists(arcpath):

            exit_stop("backup path %s already exists!" % arcpath)

        try:

            # -mx9 means maximum compression

            arglist = [SEVENZIPPATH,"a",arcpath,"*","-r","-mx9"]

            print ("try running cmd:\n %s\nin directory\n %s" %

                (' '.join(arglist),srcdir))

            # run 7zip (in the directory to be backupped!)

            sp = subprocess.Popen(

                args=arglist,

                stdout=subprocess.PIPE,

                stderr=subprocess.PIPE,

                cwd=srcdir)

        except:

            print "Error while running 7zip subprocess. Traceback:"

            print "Traceback:\n%s"%traceback.format_exc()

            return False

        # wait for process to terminate, get stdout and stderr

        stdout, stderr = sp.communicate()

        if stdout:

            print ("\n>>> 7zip subprocess STDOUT START:\n%s"

                    ">>> 7zip subprocess STDOUT END\n" % stdout)

        if stderr:

            print "7zip STDERR:\n%s" % stderr

            return False

        return arcpath

     

    def any_key():

        print "Press any key to continue."

        getch()

     

    def exit_stop(exitstring):

        print exitstring

        any_key()

        sys.exit(exitstring)

     

    def so_flushwr(string):

        sys.stdout.write(string)

        sys.stdout.flush()

     

    # provide getch() method

    # (http://stackoverflow.com/questions/1394956/how-to-do-hit-any-key-in-python

    try:

        # Win32

        from msvcrt import getch

    except ImportError:

        # UNIX

        def getch():

            import sys, tty, termios

            fd = sys.stdin.fileno()

            old = termios.tcgetattr(fd)

            try:

                tty.setraw(fd)

                return sys.stdin.read(1)

            finally:

                termios.tcsetattr(fd, termios.TCSADRAIN, old)

     

    # build timestring, check settings and invoke corresponding backup function

    print "*********************************************************************"

    print "* snapshot backup script by Jan-Philip Gehrcke -- http://gehrcke.de *"

    print "*********************************************************************\n"

     

    timestr = time.strftime("_%y%m%d_%H%M%S",time.localtime())

    if METHOD not in ["SIMPLE", "BZ2", "7zip"]:

        exit_stop("METHOD not 'SIMPLE' OR 'BZ2' OR '7zip'")

    if not os.path.exists(ORIG_DIR):

        exit_stop("ORIG_DIR does not exist: %s" % os.path.abspath(ORIG_DIR))

    if not os.path.exists(BACKUP_DIR):

        exit_stop("BACKUP_DIR does not exist: %s" % os.path.abspath(BACKUP_DIR))

    else:

        print ("write snapshot of\n  %s\nto\n  %s\nusing the %s method...\n" %

                (os.path.abspath(ORIG_DIR),os.path.abspath(BACKUP_DIR),METHOD))

        if METHOD == "SIMPLE":

            rv = backup_directory_simple(srcdir=ORIG_DIR,

                dstdir=os.path.join(BACKUP_DIR, BACKUP_PREFIX + timestr))

        elif METHOD == "BZ2":

            rv = backup_directory_bz2(srcdir=ORIG_DIR,

                tarpath=os.path.join(BACKUP_DIR,

                    BACKUP_PREFIX + timestr + ".tar.bz2"))

        else:

            try:

                if not os.path.exists(SEVENZIPPATH):

                    exit_stop("7zip executable not found: %s" % SEVENZIPPATH)

            except NameError:

                exit_stop("variable SEVENZIPPATH not defined")

            rv = backup_directory_7zip(srcdir=os.path.abspath(ORIG_DIR),

                arcpath=os.path.abspath(os.path.join(BACKUP_DIR,

                    BACKUP_PREFIX + timestr + ".7z")))

     

    if rv:

        print "Snapshot successfully written to\n  %s" % os.path.abspath(rv)

    else:

        print "Failure during backup :-("

     

    if 'ADDITIONAL_BACKUP_DIR' in globals() and rv:

        if not os.path.exists(ADDITIONAL_BACKUP_DIR):

            exit_stop(("ADDITIONAL_BACKUP_DIR does not exist: %s"

                % os.path.abspath(ADDITIONAL_BACKUP_DIR)))

        so_flushwr("\nwrite additional backup to %s.." % ADDITIONAL_BACKUP_DIR)

        try:

            dst = os.path.join(ADDITIONAL_BACKUP_DIR,os.path.basename(rv))

            if os.path.isdir(rv):

                shutil.copytree(rv,dst) # simple method, copy directory tree

            else:

                shutil.copy(rv,dst) # copy 7zip or bz2 archive

            so_flushwr("success\n")

        except:

            print "Traceback:\n%s"%traceback.format_exc()

            print "Additional backup not written. For diagnosis look above."

     

    any_key()