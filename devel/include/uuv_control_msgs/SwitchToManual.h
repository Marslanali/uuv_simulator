// Generated by gencpp from file uuv_control_msgs/SwitchToManual.msg
// DO NOT EDIT!


#ifndef UUV_CONTROL_MSGS_MESSAGE_SWITCHTOMANUAL_H
#define UUV_CONTROL_MSGS_MESSAGE_SWITCHTOMANUAL_H

#include <ros/service_traits.h>


#include <uuv_control_msgs/SwitchToManualRequest.h>
#include <uuv_control_msgs/SwitchToManualResponse.h>


namespace uuv_control_msgs
{

struct SwitchToManual
{

typedef SwitchToManualRequest Request;
typedef SwitchToManualResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SwitchToManual
} // namespace uuv_control_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::uuv_control_msgs::SwitchToManual > {
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::uuv_control_msgs::SwitchToManual&) { return value(); }
};

template<>
struct DataType< ::uuv_control_msgs::SwitchToManual > {
  static const char* value()
  {
    return "uuv_control_msgs/SwitchToManual";
  }

  static const char* value(const ::uuv_control_msgs::SwitchToManual&) { return value(); }
};


// service_traits::MD5Sum< ::uuv_control_msgs::SwitchToManualRequest> should match 
// service_traits::MD5Sum< ::uuv_control_msgs::SwitchToManual > 
template<>
struct MD5Sum< ::uuv_control_msgs::SwitchToManualRequest>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_control_msgs::SwitchToManual >::value();
  }
  static const char* value(const ::uuv_control_msgs::SwitchToManualRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_control_msgs::SwitchToManualRequest> should match 
// service_traits::DataType< ::uuv_control_msgs::SwitchToManual > 
template<>
struct DataType< ::uuv_control_msgs::SwitchToManualRequest>
{
  static const char* value()
  {
    return DataType< ::uuv_control_msgs::SwitchToManual >::value();
  }
  static const char* value(const ::uuv_control_msgs::SwitchToManualRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::uuv_control_msgs::SwitchToManualResponse> should match 
// service_traits::MD5Sum< ::uuv_control_msgs::SwitchToManual > 
template<>
struct MD5Sum< ::uuv_control_msgs::SwitchToManualResponse>
{
  static const char* value()
  {
    return MD5Sum< ::uuv_control_msgs::SwitchToManual >::value();
  }
  static const char* value(const ::uuv_control_msgs::SwitchToManualResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::uuv_control_msgs::SwitchToManualResponse> should match 
// service_traits::DataType< ::uuv_control_msgs::SwitchToManual > 
template<>
struct DataType< ::uuv_control_msgs::SwitchToManualResponse>
{
  static const char* value()
  {
    return DataType< ::uuv_control_msgs::SwitchToManual >::value();
  }
  static const char* value(const ::uuv_control_msgs::SwitchToManualResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UUV_CONTROL_MSGS_MESSAGE_SWITCHTOMANUAL_H
