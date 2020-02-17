import ftplib
import os
# ff.upFTP(con)
def upFTP(path):
    session = ftplib.FTP('162.241.60.204', 'servidor@percepcionmexico.com', 'WPloel0BlWmn')
    def placeFiles(ftp, path):
        for name in os.listdir(path):
            localpath = os.path.join(path, name)
            if os.path.isfile(localpath):
                print("STOR", name, localpath)
                ftp.storbinary('STOR ' + name, open(localpath, 'rb'))
            elif os.path.isdir(localpath):
                print("MKD", name)
                try:
                    ftp.mkd(name)
                # ignore "directory already exists"
                except error_perm as e:
                    if not e.args[0].startswith('550'):
                        raise
                print("CWD", name)
                ftp.cwd(name)
                placeFiles(ftp, localpath)
                print("CWD", "..")
                ftp.cwd("..")

    placeFiles(session, path)
    session.quit()

    # recortar
