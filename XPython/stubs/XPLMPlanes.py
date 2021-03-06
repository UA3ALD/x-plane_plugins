"""
The XPLMPlanes APIs allow you to control the various aircraft in X-Plane,
both the user's and the sim's.

Constants and enumerations
**************************
"""
XPLM_USER_AIRCRAFT = 0


def XPLMSetUsersAircraft(inAircraftPath):
    """
    This routine changes the user's aircraft.  Note that this will reinitialize
    the user to be on the nearest airport's first runway.  Pass in a full path
    (hard drive and everything including the .acf extension) to the .acf file.
    """


def XPLMPlaceUserAtAirport(inAirportCode):
    """
    This routine places the user at a given airport.  Specify the airport by
    its ICAO code (e.g. 'KBOS').
    """


def XPLMPlaceUserAtLocation(latitudeDegrees,
                            longitudeDegrees,
                            elevationMetersMSL,
                            headingDegreesTrue,
                            speedMetersPerSecond):
    """
    Places the user at a specific location after performing any necessary
    scenery loads.

    As with in-air starts initiated from the X-Plane user interface, the
    aircraft will always start with its engines running, regardless of the
    user's preferences (i.e., regardless of what the dataref
    sim/operation/prefs/startup_running says).
    """


def XPLMCountAircraft():
    """
    This function returns the number of aircraft X-Plane is capable of having,
    as well as the number of aircraft that are currently active.  These numbers
    count the user's aircraft.  It can also return the plugin that is currently
    controlling aircraft.  In X-Plane 7, this routine reflects the number of
    aircraft the user has enabled in the rendering options window.

    outTotalAircraft : list, will contain number of planes X-Plane can have
    outActiveAircraft : list, will contain number of active planes
    outController : list, will return Id of plugin controlling the aircraft
    """
    return (int, int, int)  #: (total, active, controlling Plugin)


def XPLMGetNthAircraftModel(inIndex):
    """
    This function returns the aircraft model for the Nth aircraft.  Indices are
    zero based, with zero being the user's aircraft.  The file name should be
    at least 256 chars in length; the path should be at least 512 chars in
    length.

    inIndex     : model index (integer)
    outFileName : list, will contain model filename
    outPath     : list, will contain path to the model
    """
    return (str, str)  # (model filename, path to model)


def XPLMPlanesAvailable_f(inRefcon):
    """
    Your airplanes available callback is called when another plugin gives up
    access to the multiplayer planes.  Use this to wait for access to
    multiplayer.
    """


def XPLMAcquirePlanes(inAircraft, inCallback, inRefcon):
    """
    XPLMAcquirePlanes grants your plugin exclusive access to the aircraft.  It
    returns 1 if you gain access, 0 if you do not. inAircraft - pass in a list
    of strings specifying the planes you want loaded.  For any plane index you
    do not want loaded, pass an empty string.  Other strings should be full
    paths with the .acf extension.  Pass None if there are no planes you want
    loaded. If you pass in a callback and do not receive access to the planes
    your callback will be called when the airplanes are available. If you do
    receive airplane access, your callback will not be called.

    inAircraft : none or list planes to load (list of strings)
    inCallback : XPLMPlanesAvailable_f
    inRefcon   : object passed to the callback (any object)
    """
    return int  # 1=you gained access; 0=otherwise


def XPLMReleasePlanes():
    """
    Call this function to release access to the planes.  Note that if you are
    disabled, access to planes is released for you and you must reacquire it.
    """


def XPLMSetActiveAircraftCount(inCount):
    """
    This routine sets the number of active planes.  If you pass in a number
    higher than the total number of planes availables, only the total number of
    planes available is actually used.
    """


def XPLMSetAircraftModel(inIndex, inAircraftPath):
    """
    This routine loads an aircraft model.  It may only be called if you  have
    exclusive access to the airplane APIs.  Pass in the path of the  model with
    the .acf extension.  The index is zero based, but you  may not pass in 0
    (use XPLMSetUsersAircraft to load the user's aircracft).
    """


def XPLMDisableAIForPlane(inPlaneIndex):
    """
    This routine turns off X-Plane's AI for a given plane.  The plane will
    continue to draw and be a real plane in X-Plane, but will not  move itself.
    """
