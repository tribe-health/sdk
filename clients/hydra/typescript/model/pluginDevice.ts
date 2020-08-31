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
* PluginDevice plugin device
*/
export class PluginDevice {
    /**
    * description
    */
    'description': string;
    /**
    * name
    */
    'name': string;
    /**
    * path
    */
    'path': string;
    /**
    * settable
    */
    'settable': Array<string>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "description",
            "baseName": "Description",
            "type": "string"
        },
        {
            "name": "name",
            "baseName": "Name",
            "type": "string"
        },
        {
            "name": "path",
            "baseName": "Path",
            "type": "string"
        },
        {
            "name": "settable",
            "baseName": "Settable",
            "type": "Array<string>"
        }    ];

    static getAttributeTypeMap() {
        return PluginDevice.attributeTypeMap;
    }
}

