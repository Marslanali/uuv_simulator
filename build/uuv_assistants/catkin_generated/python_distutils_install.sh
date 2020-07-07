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

echo_and_run cd "/home/arslan/uuv_simulator/uuv_assistants"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/arslan/uuv_simulator/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/arslan/uuv_simulator/install/lib/python2.7/dist-packages:/home/arslan/uuv_simulator/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/arslan/uuv_simulator/build" \
    "/usr/bin/python2" \
    "/home/arslan/uuv_simulator/uuv_assistants/setup.py" \
    build --build-base "/home/arslan/uuv_simulator/build/uuv_assistants" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/arslan/uuv_simulator/install" --install-scripts="/home/arslan/uuv_simulator/install/bin"
