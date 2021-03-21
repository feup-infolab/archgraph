'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {

      await queryInterface.bulkInsert('Users', [{
        username: 'SuperAdmin',
        firstName: 'firstname',
        lastName: 'lastname',
        password: 'password',
        createdAt : new Date(),
        updatedAt: new Date(),

      }], {});

  },

  down: async (queryInterface, Sequelize) => {

     return await queryInterface.bulkDelete('Users', null, {});
  }
};
