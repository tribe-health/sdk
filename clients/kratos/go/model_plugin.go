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

// Plugin Plugin A plugin for the Engine API
type Plugin struct {
	Config PluginConfig `json:"Config"`
	// True if the plugin is running. False if the plugin is not running, only installed.
	Enabled bool `json:"Enabled"`
	// Id
	Id *string `json:"Id,omitempty"`
	// name
	Name string `json:"Name"`
	// plugin remote reference used to push/pull the plugin
	PluginReference *string `json:"PluginReference,omitempty"`
	Settings PluginSettings `json:"Settings"`
}

// NewPlugin instantiates a new Plugin object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPlugin(config PluginConfig, enabled bool, name string, settings PluginSettings) *Plugin {
	this := Plugin{}
	this.Config = config
	this.Enabled = enabled
	this.Name = name
	this.Settings = settings
	return &this
}

// NewPluginWithDefaults instantiates a new Plugin object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPluginWithDefaults() *Plugin {
	this := Plugin{}
	return &this
}

// GetConfig returns the Config field value
func (o *Plugin) GetConfig() PluginConfig {
	if o == nil {
		var ret PluginConfig
		return ret
	}

	return o.Config
}

// GetConfigOk returns a tuple with the Config field value
// and a boolean to check if the value has been set.
func (o *Plugin) GetConfigOk() (*PluginConfig, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Config, true
}

// SetConfig sets field value
func (o *Plugin) SetConfig(v PluginConfig) {
	o.Config = v
}

// GetEnabled returns the Enabled field value
func (o *Plugin) GetEnabled() bool {
	if o == nil {
		var ret bool
		return ret
	}

	return o.Enabled
}

// GetEnabledOk returns a tuple with the Enabled field value
// and a boolean to check if the value has been set.
func (o *Plugin) GetEnabledOk() (*bool, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Enabled, true
}

// SetEnabled sets field value
func (o *Plugin) SetEnabled(v bool) {
	o.Enabled = v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Plugin) GetId() string {
	if o == nil || o.Id == nil {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Plugin) GetIdOk() (*string, bool) {
	if o == nil || o.Id == nil {
		return nil, false
	}
	return o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Plugin) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *Plugin) SetId(v string) {
	o.Id = &v
}

// GetName returns the Name field value
func (o *Plugin) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// GetNameOk returns a tuple with the Name field value
// and a boolean to check if the value has been set.
func (o *Plugin) GetNameOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Name, true
}

// SetName sets field value
func (o *Plugin) SetName(v string) {
	o.Name = v
}

// GetPluginReference returns the PluginReference field value if set, zero value otherwise.
func (o *Plugin) GetPluginReference() string {
	if o == nil || o.PluginReference == nil {
		var ret string
		return ret
	}
	return *o.PluginReference
}

// GetPluginReferenceOk returns a tuple with the PluginReference field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *Plugin) GetPluginReferenceOk() (*string, bool) {
	if o == nil || o.PluginReference == nil {
		return nil, false
	}
	return o.PluginReference, true
}

// HasPluginReference returns a boolean if a field has been set.
func (o *Plugin) HasPluginReference() bool {
	if o != nil && o.PluginReference != nil {
		return true
	}

	return false
}

// SetPluginReference gets a reference to the given string and assigns it to the PluginReference field.
func (o *Plugin) SetPluginReference(v string) {
	o.PluginReference = &v
}

// GetSettings returns the Settings field value
func (o *Plugin) GetSettings() PluginSettings {
	if o == nil {
		var ret PluginSettings
		return ret
	}

	return o.Settings
}

// GetSettingsOk returns a tuple with the Settings field value
// and a boolean to check if the value has been set.
func (o *Plugin) GetSettingsOk() (*PluginSettings, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Settings, true
}

// SetSettings sets field value
func (o *Plugin) SetSettings(v PluginSettings) {
	o.Settings = v
}

func (o Plugin) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["Config"] = o.Config
	}
	if true {
		toSerialize["Enabled"] = o.Enabled
	}
	if o.Id != nil {
		toSerialize["Id"] = o.Id
	}
	if true {
		toSerialize["Name"] = o.Name
	}
	if o.PluginReference != nil {
		toSerialize["PluginReference"] = o.PluginReference
	}
	if true {
		toSerialize["Settings"] = o.Settings
	}
	return json.Marshal(toSerialize)
}

type NullablePlugin struct {
	value *Plugin
	isSet bool
}

func (v NullablePlugin) Get() *Plugin {
	return v.value
}

func (v *NullablePlugin) Set(val *Plugin) {
	v.value = val
	v.isSet = true
}

func (v NullablePlugin) IsSet() bool {
	return v.isSet
}

func (v *NullablePlugin) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePlugin(val *Plugin) *NullablePlugin {
	return &NullablePlugin{value: val, isSet: true}
}

func (v NullablePlugin) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePlugin) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


