# Instalace
- Pro spuštění programu musíte mít nainstalovaný python!

## Linux
1. Program lze naistalovat pomocí scriptu install.sh (jsou potřeba práva root)
2. Nastavte IP adresu a port v konfiguračním souboru, na které bude server spušťen
- IP adresu počítače lze zjistit např. příkazem 'ip addr'
- Konfigurační soubor se nachází ve složce '/usr/local/bin/translator/config' a nazývá se 'config.ini'
- Můžete nastavit i rozsah ip adres a portů, které bude příkaz TRANSLATESCAN"" skenovat
3. Příkazem 'service translator start' program spustíme (jsou potřeba práva root)

## Windows
1. Nastavte IP adresu a port v konfiguračním souboru, na které bude server spušťen
- IP adresu počítače lze zjistit např. příkazem 'ipconfig'
- Konfigurační soubor se nachází ve složce 'config' a nazývá se 'config.ini'
- Můžete nastavit i rozsah ip adres a portů, které bude příkaz TRANSLATESCAN"" skenovat
2. V Powershellu nebo cmd (Příkazovém řádku) se přepneme do složky se soubory programu
3. Program spustíme příkazem 'python src/main.py'