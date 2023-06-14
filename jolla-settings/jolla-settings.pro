TEMPLATE = aux

settings-entry.path = /usr/share/jolla-settings/entries
settings-entry.files = entries/x10iii-cam-button.json

settings-ui.path = /usr/share/jolla-settings/pages/x10iii-cam-button
settings-ui.files = pages/x10iii-cam-button/EnableSwitch.qml

INSTALLS += settings-ui settings-entry

lupdate_only {
    SOURCES += pages/*.qml
}

TRANSLATIONS += translations/x10iii-cam-button.ts \
                translations/x10iii-cam-button-de.ts \
                translations/x10iii-cam-button-sv.ts

include(translations/translations.pri)
