'use strict';
const bcrypt = require('bcrypt');
module.exports = {
    up: async (queryInterface, Sequelize) => {

        await queryInterface.bulkInsert('User', [{
            username: 'SuperAdmin',
            firstName: 'firstname',
            lastName: 'lastname',
            password: bcrypt.hashSync('password', 10),
            createdAt: new Date(),
            updatedAt: new Date(),


        }], {});

    },

    down: async (queryInterface, Sequelize) => {

        return await queryInterface.bulkDelete('User', null, {});
    }
};
