# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uuv_thruster_manager/GetThrusterManagerConfigRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetThrusterManagerConfigRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "uuv_thruster_manager/GetThrusterManagerConfigRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """














"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetThrusterManagerConfigRequest, self).__init__(*args, **kwds)

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
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
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
      pass
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
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uuv_thruster_manager/GetThrusterManagerConfigResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetThrusterManagerConfigResponse(genpy.Message):
  _md5sum = "b5a2d9d3bb510dd91fdb03f95e95b8de"
  _type = "uuv_thruster_manager/GetThrusterManagerConfigResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string tf_prefix
string base_link
string thruster_frame_base
string thruster_topic_prefix
string thruster_topic_suffix
float64 timeout
float64 max_thrust
int32 n_thrusters
float64[] allocation_matrix

"""
  __slots__ = ['tf_prefix','base_link','thruster_frame_base','thruster_topic_prefix','thruster_topic_suffix','timeout','max_thrust','n_thrusters','allocation_matrix']
  _slot_types = ['string','string','string','string','string','float64','float64','int32','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tf_prefix,base_link,thruster_frame_base,thruster_topic_prefix,thruster_topic_suffix,timeout,max_thrust,n_thrusters,allocation_matrix

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetThrusterManagerConfigResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tf_prefix is None:
        self.tf_prefix = ''
      if self.base_link is None:
        self.base_link = ''
      if self.thruster_frame_base is None:
        self.thruster_frame_base = ''
      if self.thruster_topic_prefix is None:
        self.thruster_topic_prefix = ''
      if self.thruster_topic_suffix is None:
        self.thruster_topic_suffix = ''
      if self.timeout is None:
        self.timeout = 0.
      if self.max_thrust is None:
        self.max_thrust = 0.
      if self.n_thrusters is None:
        self.n_thrusters = 0
      if self.allocation_matrix is None:
        self.allocation_matrix = []
    else:
      self.tf_prefix = ''
      self.base_link = ''
      self.thruster_frame_base = ''
      self.thruster_topic_prefix = ''
      self.thruster_topic_suffix = ''
      self.timeout = 0.
      self.max_thrust = 0.
      self.n_thrusters = 0
      self.allocation_matrix = []

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
      _x = self.tf_prefix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.base_link
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_frame_base
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_topic_prefix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_topic_suffix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2di().pack(_x.timeout, _x.max_thrust, _x.n_thrusters))
      length = len(self.allocation_matrix)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.allocation_matrix))
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tf_prefix = str[start:end].decode('utf-8')
      else:
        self.tf_prefix = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_link = str[start:end].decode('utf-8')
      else:
        self.base_link = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_frame_base = str[start:end].decode('utf-8')
      else:
        self.thruster_frame_base = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_topic_prefix = str[start:end].decode('utf-8')
      else:
        self.thruster_topic_prefix = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_topic_suffix = str[start:end].decode('utf-8')
      else:
        self.thruster_topic_suffix = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.timeout, _x.max_thrust, _x.n_thrusters,) = _get_struct_2di().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.allocation_matrix = struct.unpack(pattern, str[start:end])
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
      _x = self.tf_prefix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.base_link
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_frame_base
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_topic_prefix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.thruster_topic_suffix
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2di().pack(_x.timeout, _x.max_thrust, _x.n_thrusters))
      length = len(self.allocation_matrix)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.allocation_matrix.tostring())
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tf_prefix = str[start:end].decode('utf-8')
      else:
        self.tf_prefix = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.base_link = str[start:end].decode('utf-8')
      else:
        self.base_link = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_frame_base = str[start:end].decode('utf-8')
      else:
        self.thruster_frame_base = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_topic_prefix = str[start:end].decode('utf-8')
      else:
        self.thruster_topic_prefix = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.thruster_topic_suffix = str[start:end].decode('utf-8')
      else:
        self.thruster_topic_suffix = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.timeout, _x.max_thrust, _x.n_thrusters,) = _get_struct_2di().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.allocation_matrix = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2di = None
def _get_struct_2di():
    global _struct_2di
    if _struct_2di is None:
        _struct_2di = struct.Struct("<2di")
    return _struct_2di
class GetThrusterManagerConfig(object):
  _type          = 'uuv_thruster_manager/GetThrusterManagerConfig'
  _md5sum = 'b5a2d9d3bb510dd91fdb03f95e95b8de'
  _request_class  = GetThrusterManagerConfigRequest
  _response_class = GetThrusterManagerConfigResponse
