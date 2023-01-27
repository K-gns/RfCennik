'use strict';

/**
 * favourited-item service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::favourited-item.favourited-item');
