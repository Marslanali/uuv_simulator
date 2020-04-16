
"use strict";

let ResetController = require('./ResetController.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')
let StartTrajectory = require('./StartTrajectory.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let GoTo = require('./GoTo.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let Hold = require('./Hold.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let GetPIDParams = require('./GetPIDParams.js')
let GoToIncremental = require('./GoToIncremental.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let SwitchToManual = require('./SwitchToManual.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let AddWaypoint = require('./AddWaypoint.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let GetWaypoints = require('./GetWaypoints.js')
let SetPIDParams = require('./SetPIDParams.js')

module.exports = {
  ResetController: ResetController,
  InitWaypointsFromFile: InitWaypointsFromFile,
  StartTrajectory: StartTrajectory,
  SetMBSMControllerParams: SetMBSMControllerParams,
  GoTo: GoTo,
  GetSMControllerParams: GetSMControllerParams,
  Hold: Hold,
  InitWaypointSet: InitWaypointSet,
  InitRectTrajectory: InitRectTrajectory,
  GetPIDParams: GetPIDParams,
  GoToIncremental: GoToIncremental,
  SetSMControllerParams: SetSMControllerParams,
  InitCircularTrajectory: InitCircularTrajectory,
  SwitchToManual: SwitchToManual,
  IsRunningTrajectory: IsRunningTrajectory,
  InitHelicalTrajectory: InitHelicalTrajectory,
  AddWaypoint: AddWaypoint,
  ClearWaypoints: ClearWaypoints,
  SwitchToAutomatic: SwitchToAutomatic,
  GetMBSMControllerParams: GetMBSMControllerParams,
  GetWaypoints: GetWaypoints,
  SetPIDParams: SetPIDParams,
};
