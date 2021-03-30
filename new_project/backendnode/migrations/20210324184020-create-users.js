'use strict';
module.exports = {
    up: async (queryInterface, Sequelize) => {
        await queryInterface.createTable('users', {
            id: {
                allowNull: false,
                autoIncrement: true,
                primaryKey: true,
                type: Sequelize.INTEGER,
                defaultValue: 'nextval("users_id_seq"::regclass)',
            },
            username: {
                type: Sequelize.STRING,
                allowNull: false,
                unique: true
            },
            firstname: {
                type: Sequelize.STRING
            },
            lastname: {
                type: Sequelize.STRING
            },
            password: {
                type: Sequelize.STRING
            },

        });
    },
    down: async (queryInterface, Sequelize) => {
        await queryInterface.dropTable('users');
    }
};
