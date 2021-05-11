/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.6.1-alpha.1
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// SettingsViaApiResponse : The Response for Settings Flows via API



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct SettingsViaApiResponse {
    #[serde(rename = "flow")]
    pub flow: Box<crate::models::SettingsFlow>,
    #[serde(rename = "identity")]
    pub identity: Box<crate::models::Identity>,
}

impl SettingsViaApiResponse {
    /// The Response for Settings Flows via API
    pub fn new(flow: crate::models::SettingsFlow, identity: crate::models::Identity) -> SettingsViaApiResponse {
        SettingsViaApiResponse {
            flow: Box::new(flow),
            identity: Box::new(identity),
        }
    }
}


