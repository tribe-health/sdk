/**
 * ORY Hydra
 * Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.
 *
 * The version of the OpenAPI document: v1.7.4
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';

/**
* VolumeUsageData Usage details about the volume. This information is used by the `GET /system/df` endpoint, and omitted in other endpoints.
*/
export class VolumeUsageData {
    /**
    * The number of containers referencing this volume. This field is set to `-1` if the reference-count is not available.
    */
    'refCount': number;
    /**
    * Amount of disk space used by the volume (in bytes). This information is only available for volumes created with the `\"local\"` volume driver. For volumes created with other volume drivers, this field is set to `-1` (\"not available\")
    */
    'size': number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "refCount",
            "baseName": "RefCount",
            "type": "number"
        },
        {
            "name": "size",
            "baseName": "Size",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return VolumeUsageData.attributeTypeMap;
    }
}

