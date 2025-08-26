import sys
import os
from ftplib import FTP
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def upload_to_ftp(local_file_path, remote_filename):
    """
    Subir archivo al servidor FTP usando ftplib
    """
    # Configuración FTP
    FTP_HOST = "localhost"   
    FTP_PORT = 21
    FTP_USER = "ftpuser"     
    FTP_PASS = "1234"       
    FTP_REMOTE_DIR = "contactos"  

    ftp = None
    try:
        # Conectar al servidor FTP
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        logger.info(f"Conectado exitosamente a {FTP_HOST}")

        # Ir a la carpeta o crearla
        try:
            ftp.cwd(FTP_REMOTE_DIR)
        except Exception:
            ftp.mkd(FTP_REMOTE_DIR)
            ftp.cwd(FTP_REMOTE_DIR)

        # Verificar que el archivo local existe
        if not os.path.exists(local_file_path):
            raise FileNotFoundError(f"Archivo local no encontrado: {local_file_path}")

        # Subir archivo
        with open(local_file_path, "rb") as file:
            ftp.storbinary(f"STOR {remote_filename}", file)

        # Cerrar conexión
        ftp.quit()
        logger.info(f"Archivo {remote_filename} subido exitosamente")
        print(f"SUCCESS: Archivo {remote_filename} subido exitosamente")
        return True

    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        print(error_msg)
        logger.error(error_msg)
        if ftp:
            try:
                ftp.quit()
            except:
                pass
        return False


if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python ftp.py <archivo_local> <nombre_remoto>")
        sys.exit(1)

    local_file = sys.argv[1]
    remote_name = sys.argv[2]

   
    success = upload_to_ftp(local_file, remote_name)

    sys.exit(0 if success else 1)
