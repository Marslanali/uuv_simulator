# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uuv_control_msgs/InitWaypointSetRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuv_control_msgs.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class InitWaypointSetRequest(genpy.Message):
  _md5sum = "a1ff84a20694a6c851879f791bb28d61"
  _type = "uuv_control_msgs/InitWaypointSetRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """














std_msgs/Time start_time
bool start_now
uuv_control_msgs/Waypoint[] waypoints
float64 max_forward_speed
float64 heading_offset
std_msgs/String interpolator

================================================================================
MSG: std_msgs/Time
time data

================================================================================
MSG: uuv_control_msgs/Waypoint
# Copyright (c) 2016 The UUV Simulator Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

std_msgs/Header header
geometry_msgs/Point point
float64 max_forward_speed
float64 heading_offset
bool use_fixed_heading
float64 radius_of_acceptance

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: std_msgs/String
string data
"""
  __slots__ = ['start_time','start_now','waypoints','max_forward_speed','heading_offset','interpolator']
  _slot_types = ['std_msgs/Time','bool','uuv_control_msgs/Waypoint[]','float64','float64','std_msgs/String']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       start_time,start_now,waypoints,max_forward_speed,heading_offset,interpolator

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitWaypointSetRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.start_time is None:
        self.start_time = std_msgs.msg.Time()
      if self.start_now is None:
        self.start_now = False
      if self.waypoints is None:
        self.waypoints = []
      if self.max_forward_speed is None:
        self.max_forward_speed = 0.
      if self.heading_offset is None:
        self.heading_offset = 0.
      if self.interpolator is None:
        self.interpolator = std_msgs.msg.String()
    else:
      self.start_time = std_msgs.msg.Time()
      self.start_now = False
      self.waypoints = []
      self.max_forward_speed = 0.
      self.heading_offset = 0.
      self.interpolator = std_msgs.msg.String()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2IB().pack(_x.start_time.data.secs, _x.start_time.data.nsecs, _x.start_now))
      length = len(self.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints:
        _v1 = val1.header
        buff.write(_get_struct_I().pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v3 = val1.point
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_get_struct_2dBd().pack(_x.max_forward_speed, _x.heading_offset, _x.use_fixed_heading, _x.radius_of_acceptance))
      _x = self
      buff.write(_get_struct_2d().pack(_x.max_forward_speed, _x.heading_offset))
      _x = self.interpolator.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.start_time is None:
        self.start_time = std_msgs.msg.Time()
      if self.waypoints is None:
        self.waypoints = None
      if self.interpolator is None:
        self.interpolator = std_msgs.msg.String()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.start_time.data.secs, _x.start_time.data.nsecs, _x.start_now,) = _get_struct_2IB().unpack(str[start:end])
      self.start_now = bool(self.start_now)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints = []
      for i in range(0, length):
        val1 = uuv_control_msgs.msg.Waypoint()
        _v4 = val1.header
        start = end
        end += 4
        (_v4.seq,) = _get_struct_I().unpack(str[start:end])
        _v5 = _v4.stamp
        _x = _v5
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.frame_id = str[start:end].decode('utf-8')
        else:
          _v4.frame_id = str[start:end]
        _v6 = val1.point
        _x = _v6
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _x = val1
        start = end
        end += 25
        (_x.max_forward_speed, _x.heading_offset, _x.use_fixed_heading, _x.radius_of_acceptance,) = _get_struct_2dBd().unpack(str[start:end])
        val1.use_fixed_heading = bool(val1.use_fixed_heading)
        self.waypoints.append(val1)
      _x = self
      start = end
      end += 16
      (_x.max_forward_speed, _x.heading_offset,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.interpolator.data = str[start:end].decode('utf-8')
      else:
        self.interpolator.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2IB().pack(_x.start_time.data.secs, _x.start_time.data.nsecs, _x.start_now))
      length = len(self.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints:
        _v7 = val1.header
        buff.write(_get_struct_I().pack(_v7.seq))
        _v8 = _v7.stamp
        _x = _v8
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v7.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v9 = val1.point
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_get_struct_2dBd().pack(_x.max_forward_speed, _x.heading_offset, _x.use_fixed_heading, _x.radius_of_acceptance))
      _x = self
      buff.write(_get_struct_2d().pack(_x.max_forward_speed, _x.heading_offset))
      _x = self.interpolator.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.start_time is None:
        self.start_time = std_msgs.msg.Time()
      if self.waypoints is None:
        self.waypoints = None
      if self.interpolator is None:
        self.interpolator = std_msgs.msg.String()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.start_time.data.secs, _x.start_time.data.nsecs, _x.start_now,) = _get_struct_2IB().unpack(str[start:end])
      self.start_now = bool(self.start_now)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints = []
      for i in range(0, length):
        val1 = uuv_control_msgs.msg.Waypoint()
        _v10 = val1.header
        start = end
        end += 4
        (_v10.seq,) = _get_struct_I().unpack(str[start:end])
        _v11 = _v10.stamp
        _x = _v11
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v10.frame_id = str[start:end].decode('utf-8')
        else:
          _v10.frame_id = str[start:end]
        _v12 = val1.point
        _x = _v12
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _x = val1
        start = end
        end += 25
        (_x.max_forward_speed, _x.heading_offset, _x.use_fixed_heading, _x.radius_of_acceptance,) = _get_struct_2dBd().unpack(str[start:end])
        val1.use_fixed_heading = bool(val1.use_fixed_heading)
        self.waypoints.append(val1)
      _x = self
      start = end
      end += 16
      (_x.max_forward_speed, _x.heading_offset,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.interpolator.data = str[start:end].decode('utf-8')
      else:
        self.interpolator.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2IB = None
def _get_struct_2IB():
    global _struct_2IB
    if _struct_2IB is None:
        _struct_2IB = struct.Struct("<2IB")
    return _struct_2IB
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_2dBd = None
def _get_struct_2dBd():
    global _struct_2dBd
    if _struct_2dBd is None:
        _struct_2dBd = struct.Struct("<2dBd")
    return _struct_2dBd
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uuv_control_msgs/InitWaypointSetResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class InitWaypointSetResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "uuv_control_msgs/InitWaypointSetResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success

"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitWaypointSetResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class InitWaypointSet(object):
  _type          = 'uuv_control_msgs/InitWaypointSet'
  _md5sum = 'bca88558d7a8f354f006171461f5d0b2'
  _request_class  = InitWaypointSetRequest
  _response_class = InitWaypointSetResponse
