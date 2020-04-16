// Generated by gencpp from file uuv_world_ros_plugins_msgs/SetOriginSphericalCoord.msg
// DO NOT EDIT!


#ifndef UUV_WORLD_ROS_PLUGINS_MSGS_MESSAGE_SETORIGINSPHERICALCOORD_H
#define UUV_WORLD_ROS_PLUGINS_MSGS_MESSAGE_SETORIGINSPHERICALCOORD_H

#include <ros/service_traits.h>


#include <uuv_world_ros_plugins_msgs/SetOriginSphericalCoordRequest.h>
#include <uuv_world_ros_plugins_msgs/SetOriginSphericalCoordResponse.h>


namespace uuv_world_ros_plugins_msgs
{

struct SetOriginSphericalCoord
{

typedef SetOriginSphericalCoordRequest Request;
typedef SetOriginSphericalCoordResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetOriginSphericalCoord
} // namespace uuv_world_ros_plugins_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > {
  static const char* value()
  {
    return "be1cd7093c79a14933c2ac116d54917a";
  }

  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord&) { return value(); }
};

template<>
struct DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > {
  static const char* value()
  {
    return "uuv_world_ros_plugins_msgs/SetOriginSphericalCoord";
  }

  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord&) { return value(); }
};


// service_traits::MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest> should match 
// service_traits::MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > 
template<>
struct MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord >::value();
  }
  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest> should match 
// service_traits::DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > 
template<>
struct DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest>
{
  static const char* value()
  {
    return DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord >::value();
  }
  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse> should match 
// service_traits::MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > 
template<>
struct MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord >::value();
  }
  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse> should match 
// service_traits::DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord > 
template<>
struct DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse>
{
  static const char* value()
  {
    return DataType< ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoord >::value();
  }
  static const char* value(const ::uuv_world_ros_plugins_msgs::SetOriginSphericalCoordResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UUV_WORLD_ROS_PLUGINS_MSGS_MESSAGE_SETORIGINSPHERICALCOORD_H
