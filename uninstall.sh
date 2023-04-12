INSTALL_DIR="/usr/local/bin/translator"
SERVICE_FILE="/etc/systemd/system/translator.service"

if [ -d "${INSTALL_DIR}" ]
then
    rm -d -r "${INSTALL_DIR}"
    rm "${SERVICE_FILE}"
fi