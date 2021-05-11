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
	"time"
)

// VerifiableAddress struct for VerifiableAddress
type VerifiableAddress struct {
	Id string `json:"id"`
	Status string `json:"status"`
	Value string `json:"value"`
	Verified bool `json:"verified"`
	VerifiedAt *time.Time `json:"verified_at,omitempty"`
	Via string `json:"via"`
}

// NewVerifiableAddress instantiates a new VerifiableAddress object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewVerifiableAddress(id string, status string, value string, verified bool, via string) *VerifiableAddress {
	this := VerifiableAddress{}
	this.Id = id
	this.Status = status
	this.Value = value
	this.Verified = verified
	this.Via = via
	return &this
}

// NewVerifiableAddressWithDefaults instantiates a new VerifiableAddress object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewVerifiableAddressWithDefaults() *VerifiableAddress {
	this := VerifiableAddress{}
	return &this
}

// GetId returns the Id field value
func (o *VerifiableAddress) GetId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Id
}

// GetIdOk returns a tuple with the Id field value
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetIdOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Id, true
}

// SetId sets field value
func (o *VerifiableAddress) SetId(v string) {
	o.Id = v
}

// GetStatus returns the Status field value
func (o *VerifiableAddress) GetStatus() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Status
}

// GetStatusOk returns a tuple with the Status field value
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetStatusOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Status, true
}

// SetStatus sets field value
func (o *VerifiableAddress) SetStatus(v string) {
	o.Status = v
}

// GetValue returns the Value field value
func (o *VerifiableAddress) GetValue() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Value
}

// GetValueOk returns a tuple with the Value field value
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetValueOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Value, true
}

// SetValue sets field value
func (o *VerifiableAddress) SetValue(v string) {
	o.Value = v
}

// GetVerified returns the Verified field value
func (o *VerifiableAddress) GetVerified() bool {
	if o == nil {
		var ret bool
		return ret
	}

	return o.Verified
}

// GetVerifiedOk returns a tuple with the Verified field value
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetVerifiedOk() (*bool, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Verified, true
}

// SetVerified sets field value
func (o *VerifiableAddress) SetVerified(v bool) {
	o.Verified = v
}

// GetVerifiedAt returns the VerifiedAt field value if set, zero value otherwise.
func (o *VerifiableAddress) GetVerifiedAt() time.Time {
	if o == nil || o.VerifiedAt == nil {
		var ret time.Time
		return ret
	}
	return *o.VerifiedAt
}

// GetVerifiedAtOk returns a tuple with the VerifiedAt field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetVerifiedAtOk() (*time.Time, bool) {
	if o == nil || o.VerifiedAt == nil {
		return nil, false
	}
	return o.VerifiedAt, true
}

// HasVerifiedAt returns a boolean if a field has been set.
func (o *VerifiableAddress) HasVerifiedAt() bool {
	if o != nil && o.VerifiedAt != nil {
		return true
	}

	return false
}

// SetVerifiedAt gets a reference to the given time.Time and assigns it to the VerifiedAt field.
func (o *VerifiableAddress) SetVerifiedAt(v time.Time) {
	o.VerifiedAt = &v
}

// GetVia returns the Via field value
func (o *VerifiableAddress) GetVia() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Via
}

// GetViaOk returns a tuple with the Via field value
// and a boolean to check if the value has been set.
func (o *VerifiableAddress) GetViaOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Via, true
}

// SetVia sets field value
func (o *VerifiableAddress) SetVia(v string) {
	o.Via = v
}

func (o VerifiableAddress) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["id"] = o.Id
	}
	if true {
		toSerialize["status"] = o.Status
	}
	if true {
		toSerialize["value"] = o.Value
	}
	if true {
		toSerialize["verified"] = o.Verified
	}
	if o.VerifiedAt != nil {
		toSerialize["verified_at"] = o.VerifiedAt
	}
	if true {
		toSerialize["via"] = o.Via
	}
	return json.Marshal(toSerialize)
}

type NullableVerifiableAddress struct {
	value *VerifiableAddress
	isSet bool
}

func (v NullableVerifiableAddress) Get() *VerifiableAddress {
	return v.value
}

func (v *NullableVerifiableAddress) Set(val *VerifiableAddress) {
	v.value = val
	v.isSet = true
}

func (v NullableVerifiableAddress) IsSet() bool {
	return v.isSet
}

func (v *NullableVerifiableAddress) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableVerifiableAddress(val *VerifiableAddress) *NullableVerifiableAddress {
	return &NullableVerifiableAddress{value: val, isSet: true}
}

func (v NullableVerifiableAddress) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableVerifiableAddress) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


