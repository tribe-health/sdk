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
import { PluginConfigArgs } from './pluginConfigArgs';
import { PluginConfigInterface } from './pluginConfigInterface';
import { PluginConfigLinux } from './pluginConfigLinux';
import { PluginConfigNetwork } from './pluginConfigNetwork';
import { PluginConfigRootfs } from './pluginConfigRootfs';
import { PluginConfigUser } from './pluginConfigUser';
import { PluginEnv } from './pluginEnv';
import { PluginMount } from './pluginMount';

export class PluginConfig {
    'args': PluginConfigArgs;
    /**
    * description
    */
    'description': string;
    /**
    * Docker Version used to create the plugin
    */
    'dockerVersion'?: string;
    /**
    * documentation
    */
    'documentation': string;
    /**
    * entrypoint
    */
    'entrypoint': Array<string>;
    /**
    * env
    */
    'env': Array<PluginEnv>;
    '_interface': PluginConfigInterface;
    /**
    * ipc host
    */
    'ipcHost': boolean;
    'linux': PluginConfigLinux;
    /**
    * mounts
    */
    'mounts': Array<PluginMount>;
    'network': PluginConfigNetwork;
    /**
    * pid host
    */
    'pidHost': boolean;
    /**
    * propagated mount
    */
    'propagatedMount': string;
    'user'?: PluginConfigUser;
    /**
    * work dir
    */
    'workDir': string;
    'rootfs'?: PluginConfigRootfs;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "args",
            "baseName": "Args",
            "type": "PluginConfigArgs"
        },
        {
            "name": "description",
            "baseName": "Description",
            "type": "string"
        },
        {
            "name": "dockerVersion",
            "baseName": "DockerVersion",
            "type": "string"
        },
        {
            "name": "documentation",
            "baseName": "Documentation",
            "type": "string"
        },
        {
            "name": "entrypoint",
            "baseName": "Entrypoint",
            "type": "Array<string>"
        },
        {
            "name": "env",
            "baseName": "Env",
            "type": "Array<PluginEnv>"
        },
        {
            "name": "_interface",
            "baseName": "Interface",
            "type": "PluginConfigInterface"
        },
        {
            "name": "ipcHost",
            "baseName": "IpcHost",
            "type": "boolean"
        },
        {
            "name": "linux",
            "baseName": "Linux",
            "type": "PluginConfigLinux"
        },
        {
            "name": "mounts",
            "baseName": "Mounts",
            "type": "Array<PluginMount>"
        },
        {
            "name": "network",
            "baseName": "Network",
            "type": "PluginConfigNetwork"
        },
        {
            "name": "pidHost",
            "baseName": "PidHost",
            "type": "boolean"
        },
        {
            "name": "propagatedMount",
            "baseName": "PropagatedMount",
            "type": "string"
        },
        {
            "name": "user",
            "baseName": "User",
            "type": "PluginConfigUser"
        },
        {
            "name": "workDir",
            "baseName": "WorkDir",
            "type": "string"
        },
        {
            "name": "rootfs",
            "baseName": "rootfs",
            "type": "PluginConfigRootfs"
        }    ];

    static getAttributeTypeMap() {
        return PluginConfig.attributeTypeMap;
    }
}

