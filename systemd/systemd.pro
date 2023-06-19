TEMPLATE = aux

unit.files = $$PWD/org.nephros.sailfish.x10iiicamera.service
unit.path = $$INSTALL_ROOT/usr/lib/systemd/system

polkit.files = 10-x10iii-cam-button-allow-manage-service.rules
polkit.path = $$INSTALL_ROOT/etc/polkit-1/rules.d

INSTALLS += unit polkit
