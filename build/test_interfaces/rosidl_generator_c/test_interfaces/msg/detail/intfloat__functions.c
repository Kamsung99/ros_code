// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_interfaces:msg/Intfloat.idl
// generated code does not contain a copyright notice
#include "test_interfaces/msg/detail/intfloat__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
test_interfaces__msg__Intfloat__init(test_interfaces__msg__Intfloat * msg)
{
  if (!msg) {
    return false;
  }
  // intnum
  // floatnum
  return true;
}

void
test_interfaces__msg__Intfloat__fini(test_interfaces__msg__Intfloat * msg)
{
  if (!msg) {
    return;
  }
  // intnum
  // floatnum
}

bool
test_interfaces__msg__Intfloat__are_equal(const test_interfaces__msg__Intfloat * lhs, const test_interfaces__msg__Intfloat * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // intnum
  if (lhs->intnum != rhs->intnum) {
    return false;
  }
  // floatnum
  if (lhs->floatnum != rhs->floatnum) {
    return false;
  }
  return true;
}

bool
test_interfaces__msg__Intfloat__copy(
  const test_interfaces__msg__Intfloat * input,
  test_interfaces__msg__Intfloat * output)
{
  if (!input || !output) {
    return false;
  }
  // intnum
  output->intnum = input->intnum;
  // floatnum
  output->floatnum = input->floatnum;
  return true;
}

test_interfaces__msg__Intfloat *
test_interfaces__msg__Intfloat__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interfaces__msg__Intfloat * msg = (test_interfaces__msg__Intfloat *)allocator.allocate(sizeof(test_interfaces__msg__Intfloat), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_interfaces__msg__Intfloat));
  bool success = test_interfaces__msg__Intfloat__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
test_interfaces__msg__Intfloat__destroy(test_interfaces__msg__Intfloat * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    test_interfaces__msg__Intfloat__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
test_interfaces__msg__Intfloat__Sequence__init(test_interfaces__msg__Intfloat__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interfaces__msg__Intfloat * data = NULL;

  if (size) {
    data = (test_interfaces__msg__Intfloat *)allocator.zero_allocate(size, sizeof(test_interfaces__msg__Intfloat), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_interfaces__msg__Intfloat__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_interfaces__msg__Intfloat__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_interfaces__msg__Intfloat__Sequence__fini(test_interfaces__msg__Intfloat__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_interfaces__msg__Intfloat__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_interfaces__msg__Intfloat__Sequence *
test_interfaces__msg__Intfloat__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  test_interfaces__msg__Intfloat__Sequence * array = (test_interfaces__msg__Intfloat__Sequence *)allocator.allocate(sizeof(test_interfaces__msg__Intfloat__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = test_interfaces__msg__Intfloat__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
test_interfaces__msg__Intfloat__Sequence__destroy(test_interfaces__msg__Intfloat__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    test_interfaces__msg__Intfloat__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
test_interfaces__msg__Intfloat__Sequence__are_equal(const test_interfaces__msg__Intfloat__Sequence * lhs, const test_interfaces__msg__Intfloat__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!test_interfaces__msg__Intfloat__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
test_interfaces__msg__Intfloat__Sequence__copy(
  const test_interfaces__msg__Intfloat__Sequence * input,
  test_interfaces__msg__Intfloat__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(test_interfaces__msg__Intfloat);
    test_interfaces__msg__Intfloat * data =
      (test_interfaces__msg__Intfloat *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!test_interfaces__msg__Intfloat__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          test_interfaces__msg__Intfloat__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!test_interfaces__msg__Intfloat__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
