// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	strfmt "github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// JSONWebKeySet json web key set
// swagger:model jsonWebKeySet
type JSONWebKeySet struct {

	// The value of the "keys" parameter is an array of JWK values.  By
	// default, the order of the JWK values within the array does not imply
	// an order of preference among them, although applications of JWK Sets
	// can choose to assign a meaning to the order for their purposes, if
	// desired.
	Keys []*JSONWebKey `json:"keys"`
}

// Validate validates this json web key set
func (m *JSONWebKeySet) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateKeys(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *JSONWebKeySet) validateKeys(formats strfmt.Registry) error {

	if swag.IsZero(m.Keys) { // not required
		return nil
	}

	for i := 0; i < len(m.Keys); i++ {
		if swag.IsZero(m.Keys[i]) { // not required
			continue
		}

		if m.Keys[i] != nil {
			if err := m.Keys[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("keys" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *JSONWebKeySet) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *JSONWebKeySet) UnmarshalBinary(b []byte) error {
	var res JSONWebKeySet
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
