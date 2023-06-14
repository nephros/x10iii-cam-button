// SPDX-FileCopyrightText: 2023 Peter G. (nephros)
// SPDX-License-Identifier: Apache-2.0

import QtQuick 2.1
import Sailfish.Silica 1.0
import Nemo.DBus 2.0
import com.jolla.settings 1.0
import org.nemomobile.systemsettings 1.0

SettingsToggle {
    id: toggleSwitch

    active: checked
    checked: serviceRunning
    icon.source: checked ? "image://theme/icon-m-triplecam" : "image://theme/icon-m-frontcam" 

    //% "Cams: front"
    //: top menu button status text
    name: qsTrId("settings-x10iii-camera-status-off")
    //% "Cams: triple"
    //: top menu button status text
    activeText: qsTrId("settings-x10iii-camera-status-on")
    //this is just here to have IDs for translations used in entries.json
    //% "X10III Cam Toggle"
    //: button name in the top menu
    property string buttonname: qsTrId("settings-x10iii-cam-button")

    onToggled: {
        if (!checked) {
            console.info("X10iii Triple Camera Toggle: engaged.")
            dbus.start()
        } else {
            console.info("X10iii Triple Camera Toggle: dis-engaged.")
            dbus.stop()
        }
    }

    Component.onCompleted: {
        console.info("X10iii Tripe Camera Toggle v@@UNRELEASED@@ loaded.")
    }

    /*
     * Dbus interface to systemd unit
    */
    property bool serviceRunning: dbus.activeState === "active"
    DBusInterface {
        id: dbus
        bus: DBus.SystemBus
        service: "org.freedesktop.systemd1"
        path: "/org/freedesktop/systemd1/unit/org_2enephros_2esailfish_2ex10iiicamera_2eservice"
        iface: "org.freedesktop.systemd1.Unit"

        propertiesEnabled: true

        property string activeState
        property string subState
        property string unitFileState

        function start() {
            call('Start',
                ["replace",],
                function(result) { console.debug("Job:", JSON.stringify(result)); },
                function(result) { console.warn("Start %1".arg(u), result) }
            );
        }
        function stop() {
            call('Stop',
                [ "replace",],
                function(result) { console.debug("Job:", JSON.stringify(result)); },
                function(result) { console.warn("Stop %1".arg(u), result) }
            );
        }
    }

}

// vim: ft=javascript expandtab ts=4 sw=4 st=4
