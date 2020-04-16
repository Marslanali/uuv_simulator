#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/arslanali/uuv_simulator/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/arslanali/uuv_simulator/install/lib/python2.7/dist-packages:/home/arslanali/uuv_simulator/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/arslanali/uuv_simulator/build" \
    "/usr/bin/python2" \
    "/home/arslanali/uuv_simulator/uuv_control/uuv_thruster_manager/setup.py" \
    build --build-base "/home/arslanali/uuv_simulator/build/uuv_control/uuv_thruster_manager" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/arslanali/uuv_simulator/install" --install-scripts="/home/arslanali/uuv_simulator/install/bin"
