/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.6.1-alpha.1
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// RecoveryFlow : This request is used when an identity wants to recover their account.  We recommend reading the [Account Recovery Documentation](../self-service/flows/password-reset-account-recovery)



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct RecoveryFlow {
    /// Active, if set, contains the registration method that is being used. It is initially not set.
    #[serde(rename = "active", skip_serializing_if = "Option::is_none")]
    pub active: Option<String>,
    /// ExpiresAt is the time (UTC) when the request expires. If the user still wishes to update the setting, a new request has to be initiated.
    #[serde(rename = "expires_at")]
    pub expires_at: String,
    #[serde(rename = "id")]
    pub id: String,
    /// IssuedAt is the time (UTC) when the request occurred.
    #[serde(rename = "issued_at")]
    pub issued_at: String,
    /// RequestURL is the initial URL that was requested from Ory Kratos. It can be used to forward information contained in the URL's path or query for example.
    #[serde(rename = "request_url")]
    pub request_url: String,
    #[serde(rename = "state")]
    pub state: String,
    /// The flow type can either be `api` or `browser`.
    #[serde(rename = "type", skip_serializing_if = "Option::is_none")]
    pub _type: Option<String>,
    #[serde(rename = "ui")]
    pub ui: Box<crate::models::UiContainer>,
}

impl RecoveryFlow {
    /// This request is used when an identity wants to recover their account.  We recommend reading the [Account Recovery Documentation](../self-service/flows/password-reset-account-recovery)
    pub fn new(expires_at: String, id: String, issued_at: String, request_url: String, state: String, ui: crate::models::UiContainer) -> RecoveryFlow {
        RecoveryFlow {
            active: None,
            expires_at,
            id,
            issued_at,
            request_url,
            state,
            _type: None,
            ui: Box::new(ui),
        }
    }
}


