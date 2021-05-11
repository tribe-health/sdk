/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * API version: v0.6.1-alpha.1
 * Contact: hi@ory.sh
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package client

import (
	"encoding/json"
)

// ContainerUpdateOKBody ContainerUpdateOKBody OK response to ContainerUpdate operation
type ContainerUpdateOKBody struct {
	// warnings
	Warnings []string `json:"Warnings"`
}

// NewContainerUpdateOKBody instantiates a new ContainerUpdateOKBody object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewContainerUpdateOKBody(warnings []string) *ContainerUpdateOKBody {
	this := ContainerUpdateOKBody{}
	this.Warnings = warnings
	return &this
}

// NewContainerUpdateOKBodyWithDefaults instantiates a new ContainerUpdateOKBody object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewContainerUpdateOKBodyWithDefaults() *ContainerUpdateOKBody {
	this := ContainerUpdateOKBody{}
	return &this
}

// GetWarnings returns the Warnings field value
func (o *ContainerUpdateOKBody) GetWarnings() []string {
	if o == nil {
		var ret []string
		return ret
	}

	return o.Warnings
}

// GetWarningsOk returns a tuple with the Warnings field value
// and a boolean to check if the value has been set.
func (o *ContainerUpdateOKBody) GetWarningsOk() ([]string, bool) {
	if o == nil  {
		return nil, false
	}
	return o.Warnings, true
}

// SetWarnings sets field value
func (o *ContainerUpdateOKBody) SetWarnings(v []string) {
	o.Warnings = v
}

func (o ContainerUpdateOKBody) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["Warnings"] = o.Warnings
	}
	return json.Marshal(toSerialize)
}

type NullableContainerUpdateOKBody struct {
	value *ContainerUpdateOKBody
	isSet bool
}

func (v NullableContainerUpdateOKBody) Get() *ContainerUpdateOKBody {
	return v.value
}

func (v *NullableContainerUpdateOKBody) Set(val *ContainerUpdateOKBody) {
	v.value = val
	v.isSet = true
}

func (v NullableContainerUpdateOKBody) IsSet() bool {
	return v.isSet
}

func (v *NullableContainerUpdateOKBody) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableContainerUpdateOKBody(val *ContainerUpdateOKBody) *NullableContainerUpdateOKBody {
	return &NullableContainerUpdateOKBody{value: val, isSet: true}
}

func (v NullableContainerUpdateOKBody) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableContainerUpdateOKBody) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


