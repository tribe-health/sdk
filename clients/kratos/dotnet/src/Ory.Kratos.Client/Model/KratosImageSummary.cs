/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.6.1-alpha.1
 * Contact: hi@ory.sh
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Ory.Kratos.Client.Client.OpenAPIDateConverter;

namespace Ory.Kratos.Client.Model
{
    /// <summary>
    /// ImageSummary image summary
    /// </summary>
    [DataContract(Name = "ImageSummary")]
    public partial class KratosImageSummary : IEquatable<KratosImageSummary>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="KratosImageSummary" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected KratosImageSummary()
        {
            this.AdditionalProperties = new Dictionary<string, object>();
        }
        /// <summary>
        /// Initializes a new instance of the <see cref="KratosImageSummary" /> class.
        /// </summary>
        /// <param name="containers">containers (required).</param>
        /// <param name="created">created (required).</param>
        /// <param name="id">Id (required).</param>
        /// <param name="labels">labels (required).</param>
        /// <param name="parentId">parent Id (required).</param>
        /// <param name="repoDigests">repo digests (required).</param>
        /// <param name="repoTags">repo tags (required).</param>
        /// <param name="sharedSize">shared size (required).</param>
        /// <param name="size">size (required).</param>
        /// <param name="virtualSize">virtual size (required).</param>
        public KratosImageSummary(long containers = default(long), long created = default(long), string id = default(string), Dictionary<string, string> labels = default(Dictionary<string, string>), string parentId = default(string), List<string> repoDigests = default(List<string>), List<string> repoTags = default(List<string>), long sharedSize = default(long), long size = default(long), long virtualSize = default(long))
        {
            this.Containers = containers;
            this.Created = created;
            // to ensure "id" is required (not null)
            this.Id = id ?? throw new ArgumentNullException("id is a required property for KratosImageSummary and cannot be null");
            // to ensure "labels" is required (not null)
            this.Labels = labels ?? throw new ArgumentNullException("labels is a required property for KratosImageSummary and cannot be null");
            // to ensure "parentId" is required (not null)
            this.ParentId = parentId ?? throw new ArgumentNullException("parentId is a required property for KratosImageSummary and cannot be null");
            // to ensure "repoDigests" is required (not null)
            this.RepoDigests = repoDigests ?? throw new ArgumentNullException("repoDigests is a required property for KratosImageSummary and cannot be null");
            // to ensure "repoTags" is required (not null)
            this.RepoTags = repoTags ?? throw new ArgumentNullException("repoTags is a required property for KratosImageSummary and cannot be null");
            this.SharedSize = sharedSize;
            this.Size = size;
            this.VirtualSize = virtualSize;
            this.AdditionalProperties = new Dictionary<string, object>();
        }

        /// <summary>
        /// containers
        /// </summary>
        /// <value>containers</value>
        [DataMember(Name = "Containers", IsRequired = true, EmitDefaultValue = false)]
        public long Containers { get; set; }

        /// <summary>
        /// created
        /// </summary>
        /// <value>created</value>
        [DataMember(Name = "Created", IsRequired = true, EmitDefaultValue = false)]
        public long Created { get; set; }

        /// <summary>
        /// Id
        /// </summary>
        /// <value>Id</value>
        [DataMember(Name = "Id", IsRequired = true, EmitDefaultValue = false)]
        public string Id { get; set; }

        /// <summary>
        /// labels
        /// </summary>
        /// <value>labels</value>
        [DataMember(Name = "Labels", IsRequired = true, EmitDefaultValue = false)]
        public Dictionary<string, string> Labels { get; set; }

        /// <summary>
        /// parent Id
        /// </summary>
        /// <value>parent Id</value>
        [DataMember(Name = "ParentId", IsRequired = true, EmitDefaultValue = false)]
        public string ParentId { get; set; }

        /// <summary>
        /// repo digests
        /// </summary>
        /// <value>repo digests</value>
        [DataMember(Name = "RepoDigests", IsRequired = true, EmitDefaultValue = false)]
        public List<string> RepoDigests { get; set; }

        /// <summary>
        /// repo tags
        /// </summary>
        /// <value>repo tags</value>
        [DataMember(Name = "RepoTags", IsRequired = true, EmitDefaultValue = false)]
        public List<string> RepoTags { get; set; }

        /// <summary>
        /// shared size
        /// </summary>
        /// <value>shared size</value>
        [DataMember(Name = "SharedSize", IsRequired = true, EmitDefaultValue = false)]
        public long SharedSize { get; set; }

        /// <summary>
        /// size
        /// </summary>
        /// <value>size</value>
        [DataMember(Name = "Size", IsRequired = true, EmitDefaultValue = false)]
        public long Size { get; set; }

        /// <summary>
        /// virtual size
        /// </summary>
        /// <value>virtual size</value>
        [DataMember(Name = "VirtualSize", IsRequired = true, EmitDefaultValue = false)]
        public long VirtualSize { get; set; }

        /// <summary>
        /// Gets or Sets additional properties
        /// </summary>
        [JsonExtensionData]
        public IDictionary<string, object> AdditionalProperties { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class KratosImageSummary {\n");
            sb.Append("  Containers: ").Append(Containers).Append("\n");
            sb.Append("  Created: ").Append(Created).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Labels: ").Append(Labels).Append("\n");
            sb.Append("  ParentId: ").Append(ParentId).Append("\n");
            sb.Append("  RepoDigests: ").Append(RepoDigests).Append("\n");
            sb.Append("  RepoTags: ").Append(RepoTags).Append("\n");
            sb.Append("  SharedSize: ").Append(SharedSize).Append("\n");
            sb.Append("  Size: ").Append(Size).Append("\n");
            sb.Append("  VirtualSize: ").Append(VirtualSize).Append("\n");
            sb.Append("  AdditionalProperties: ").Append(AdditionalProperties).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as KratosImageSummary);
        }

        /// <summary>
        /// Returns true if KratosImageSummary instances are equal
        /// </summary>
        /// <param name="input">Instance of KratosImageSummary to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(KratosImageSummary input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Containers == input.Containers ||
                    this.Containers.Equals(input.Containers)
                ) && 
                (
                    this.Created == input.Created ||
                    this.Created.Equals(input.Created)
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Labels == input.Labels ||
                    this.Labels != null &&
                    input.Labels != null &&
                    this.Labels.SequenceEqual(input.Labels)
                ) && 
                (
                    this.ParentId == input.ParentId ||
                    (this.ParentId != null &&
                    this.ParentId.Equals(input.ParentId))
                ) && 
                (
                    this.RepoDigests == input.RepoDigests ||
                    this.RepoDigests != null &&
                    input.RepoDigests != null &&
                    this.RepoDigests.SequenceEqual(input.RepoDigests)
                ) && 
                (
                    this.RepoTags == input.RepoTags ||
                    this.RepoTags != null &&
                    input.RepoTags != null &&
                    this.RepoTags.SequenceEqual(input.RepoTags)
                ) && 
                (
                    this.SharedSize == input.SharedSize ||
                    this.SharedSize.Equals(input.SharedSize)
                ) && 
                (
                    this.Size == input.Size ||
                    this.Size.Equals(input.Size)
                ) && 
                (
                    this.VirtualSize == input.VirtualSize ||
                    this.VirtualSize.Equals(input.VirtualSize)
                )
                && (this.AdditionalProperties.Count == input.AdditionalProperties.Count && !this.AdditionalProperties.Except(input.AdditionalProperties).Any());
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                hashCode = hashCode * 59 + this.Containers.GetHashCode();
                hashCode = hashCode * 59 + this.Created.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Labels != null)
                    hashCode = hashCode * 59 + this.Labels.GetHashCode();
                if (this.ParentId != null)
                    hashCode = hashCode * 59 + this.ParentId.GetHashCode();
                if (this.RepoDigests != null)
                    hashCode = hashCode * 59 + this.RepoDigests.GetHashCode();
                if (this.RepoTags != null)
                    hashCode = hashCode * 59 + this.RepoTags.GetHashCode();
                hashCode = hashCode * 59 + this.SharedSize.GetHashCode();
                hashCode = hashCode * 59 + this.Size.GetHashCode();
                hashCode = hashCode * 59 + this.VirtualSize.GetHashCode();
                if (this.AdditionalProperties != null)
                    hashCode = hashCode * 59 + this.AdditionalProperties.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
