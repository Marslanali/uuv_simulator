
"use strict";

let SetOriginSphericalCoord = require('./SetOriginSphericalCoord.js')
let SetCurrentVelocity = require('./SetCurrentVelocity.js')
let GetCurrentModel = require('./GetCurrentModel.js')
let TransformToSphericalCoord = require('./TransformToSphericalCoord.js')
let GetOriginSphericalCoord = require('./GetOriginSphericalCoord.js')
let SetCurrentModel = require('./SetCurrentModel.js')
let TransformFromSphericalCoord = require('./TransformFromSphericalCoord.js')
let SetCurrentDirection = require('./SetCurrentDirection.js')

module.exports = {
  SetOriginSphericalCoord: SetOriginSphericalCoord,
  SetCurrentVelocity: SetCurrentVelocity,
  GetCurrentModel: GetCurrentModel,
  TransformToSphericalCoord: TransformToSphericalCoord,
  GetOriginSphericalCoord: GetOriginSphericalCoord,
  SetCurrentModel: SetCurrentModel,
  TransformFromSphericalCoord: TransformFromSphericalCoord,
  SetCurrentDirection: SetCurrentDirection,
};
