// Generated by gencpp from file uuv_control_msgs/InitCircularTrajectoryRequest.msg
// DO NOT EDIT!


#ifndef UUV_CONTROL_MSGS_MESSAGE_INITCIRCULARTRAJECTORYREQUEST_H
#define UUV_CONTROL_MSGS_MESSAGE_INITCIRCULARTRAJECTORYREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Time.h>
#include <geometry_msgs/Point.h>

namespace uuv_control_msgs
{
template <class ContainerAllocator>
struct InitCircularTrajectoryRequest_
{
  typedef InitCircularTrajectoryRequest_<ContainerAllocator> Type;

  InitCircularTrajectoryRequest_()
    : start_time()
    , start_now(false)
    , radius(0.0)
    , center()
    , is_clockwise(false)
    , angle_offset(0.0)
    , n_points(0)
    , heading_offset(0.0)
    , max_forward_speed(0.0)
    , duration(0.0)  {
    }
  InitCircularTrajectoryRequest_(const ContainerAllocator& _alloc)
    : start_time(_alloc)
    , start_now(false)
    , radius(0.0)
    , center(_alloc)
    , is_clockwise(false)
    , angle_offset(0.0)
    , n_points(0)
    , heading_offset(0.0)
    , max_forward_speed(0.0)
    , duration(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Time_<ContainerAllocator>  _start_time_type;
  _start_time_type start_time;

   typedef uint8_t _start_now_type;
  _start_now_type start_now;

   typedef double _radius_type;
  _radius_type radius;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _center_type;
  _center_type center;

   typedef uint8_t _is_clockwise_type;
  _is_clockwise_type is_clockwise;

   typedef double _angle_offset_type;
  _angle_offset_type angle_offset;

   typedef int32_t _n_points_type;
  _n_points_type n_points;

   typedef double _heading_offset_type;
  _heading_offset_type heading_offset;

   typedef double _max_forward_speed_type;
  _max_forward_speed_type max_forward_speed;

   typedef double _duration_type;
  _duration_type duration;





  typedef boost::shared_ptr< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> const> ConstPtr;

}; // struct InitCircularTrajectoryRequest_

typedef ::uuv_control_msgs::InitCircularTrajectoryRequest_<std::allocator<void> > InitCircularTrajectoryRequest;

typedef boost::shared_ptr< ::uuv_control_msgs::InitCircularTrajectoryRequest > InitCircularTrajectoryRequestPtr;
typedef boost::shared_ptr< ::uuv_control_msgs::InitCircularTrajectoryRequest const> InitCircularTrajectoryRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace uuv_control_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'uuv_control_msgs': ['/home/arslan/uuv_simulator/uuv_control/uuv_control_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "33f617e6e74b9a5a4089105d4a0a3b2f";
  }

  static const char* value(const ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x33f617e6e74b9a5aULL;
  static const uint64_t static_value2 = 0x4089105d4a0a3b2fULL;
};

template<class ContainerAllocator>
struct DataType< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uuv_control_msgs/InitCircularTrajectoryRequest";
  }

  static const char* value(const ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
std_msgs/Time start_time\n\
bool start_now\n\
float64 radius\n\
geometry_msgs/Point center\n\
bool is_clockwise\n\
float64 angle_offset\n\
int32 n_points\n\
float64 heading_offset\n\
float64 max_forward_speed\n\
float64 duration\n\
\n\
================================================================================\n\
MSG: std_msgs/Time\n\
time data\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.start_time);
      stream.next(m.start_now);
      stream.next(m.radius);
      stream.next(m.center);
      stream.next(m.is_clockwise);
      stream.next(m.angle_offset);
      stream.next(m.n_points);
      stream.next(m.heading_offset);
      stream.next(m.max_forward_speed);
      stream.next(m.duration);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct InitCircularTrajectoryRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::uuv_control_msgs::InitCircularTrajectoryRequest_<ContainerAllocator>& v)
  {
    s << indent << "start_time: ";
    s << std::endl;
    Printer< ::std_msgs::Time_<ContainerAllocator> >::stream(s, indent + "  ", v.start_time);
    s << indent << "start_now: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.start_now);
    s << indent << "radius: ";
    Printer<double>::stream(s, indent + "  ", v.radius);
    s << indent << "center: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.center);
    s << indent << "is_clockwise: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.is_clockwise);
    s << indent << "angle_offset: ";
    Printer<double>::stream(s, indent + "  ", v.angle_offset);
    s << indent << "n_points: ";
    Printer<int32_t>::stream(s, indent + "  ", v.n_points);
    s << indent << "heading_offset: ";
    Printer<double>::stream(s, indent + "  ", v.heading_offset);
    s << indent << "max_forward_speed: ";
    Printer<double>::stream(s, indent + "  ", v.max_forward_speed);
    s << indent << "duration: ";
    Printer<double>::stream(s, indent + "  ", v.duration);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UUV_CONTROL_MSGS_MESSAGE_INITCIRCULARTRAJECTORYREQUEST_H
