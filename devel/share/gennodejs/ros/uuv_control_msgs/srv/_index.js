
"use strict";

let AddWaypoint = require('./AddWaypoint.js')
let GoToIncremental = require('./GoToIncremental.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let GoTo = require('./GoTo.js')
let SetPIDParams = require('./SetPIDParams.js')
let SwitchToManual = require('./SwitchToManual.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let ResetController = require('./ResetController.js')
let GetWaypoints = require('./GetWaypoints.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let GetPIDParams = require('./GetPIDParams.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let StartTrajectory = require('./StartTrajectory.js')
let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let Hold = require('./Hold.js')

module.exports = {
  AddWaypoint: AddWaypoint,
  GoToIncremental: GoToIncremental,
  GetSMControllerParams: GetSMControllerParams,
  InitHelicalTrajectory: InitHelicalTrajectory,
  GoTo: GoTo,
  SetPIDParams: SetPIDParams,
  SwitchToManual: SwitchToManual,
  InitWaypointsFromFile: InitWaypointsFromFile,
  ResetController: ResetController,
  GetWaypoints: GetWaypoints,
  SwitchToAutomatic: SwitchToAutomatic,
  InitWaypointSet: InitWaypointSet,
  GetMBSMControllerParams: GetMBSMControllerParams,
  GetPIDParams: GetPIDParams,
  IsRunningTrajectory: IsRunningTrajectory,
  SetMBSMControllerParams: SetMBSMControllerParams,
  InitRectTrajectory: InitRectTrajectory,
  SetSMControllerParams: SetSMControllerParams,
  ClearWaypoints: ClearWaypoints,
  StartTrajectory: StartTrajectory,
  InitCircularTrajectory: InitCircularTrajectory,
  Hold: Hold,
};
