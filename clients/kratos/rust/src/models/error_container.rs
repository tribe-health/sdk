/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.6.1-alpha.1
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct ErrorContainer {
    /// Errors in the container
    #[serde(rename = "errors")]
    pub errors: Vec<serde_json::Value>,
    #[serde(rename = "id")]
    pub id: String,
}

impl ErrorContainer {
    pub fn new(errors: Vec<serde_json::Value>, id: String) -> ErrorContainer {
        ErrorContainer {
            errors,
            id,
        }
    }
}


