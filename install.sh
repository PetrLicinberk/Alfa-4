INSTALL_DIR="/usr/local/bin/translator"
SERVICE_FILE="/etc/systemd/system/translator.service"

if [ -d "${INSTALL_DIR}" ]; then
    echo "Translator is already installed"
else
    mkdir "${INSTALL_DIR}"
    cp -r "src/" "${INSTALL_DIR}"
    cp -r "config/" "${INSTALL_DIR}"
    cp "translator.service" "${SERVICE_FILE}"
    mkdir "${INSTALL_DIR}/log"
    touch "${INSTALL_DIR}/log/log.txt"
    chmod ugo+w "${INSTALL_DIR}/log/log.txt"
fi