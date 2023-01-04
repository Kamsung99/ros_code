// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_interfaces:msg/Intfloat.idl
// generated code does not contain a copyright notice

#ifndef TEST_INTERFACES__MSG__DETAIL__INTFLOAT__BUILDER_HPP_
#define TEST_INTERFACES__MSG__DETAIL__INTFLOAT__BUILDER_HPP_

#include "test_interfaces/msg/detail/intfloat__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace test_interfaces
{

namespace msg
{

namespace builder
{

class Init_Intfloat_floatnum
{
public:
  explicit Init_Intfloat_floatnum(::test_interfaces::msg::Intfloat & msg)
  : msg_(msg)
  {}
  ::test_interfaces::msg::Intfloat floatnum(::test_interfaces::msg::Intfloat::_floatnum_type arg)
  {
    msg_.floatnum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_interfaces::msg::Intfloat msg_;
};

class Init_Intfloat_intnum
{
public:
  Init_Intfloat_intnum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Intfloat_floatnum intnum(::test_interfaces::msg::Intfloat::_intnum_type arg)
  {
    msg_.intnum = std::move(arg);
    return Init_Intfloat_floatnum(msg_);
  }

private:
  ::test_interfaces::msg::Intfloat msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_interfaces::msg::Intfloat>()
{
  return test_interfaces::msg::builder::Init_Intfloat_intnum();
}

}  // namespace test_interfaces

#endif  // TEST_INTERFACES__MSG__DETAIL__INTFLOAT__BUILDER_HPP_
