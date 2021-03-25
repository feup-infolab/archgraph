'use strict';
const {
    Model
} = require('sequelize');
const bcrypt = require('bcrypt');
module.exports = (sequelize, DataTypes) => {
    class Users extends Model {
        /**
         * Helper method for defining associations.
         * This method is not a part of Sequelize lifecycle.
         * The `models/index` file will call this method automatically.
         */
        static associate(models) {
            // define association here
        }
    }
    Users.init({
        username: {
            type: DataTypes.STRING,
            allowNull: false,
            unique: true,
            validate: {
                notNull: {msg: "username is required"},
            },
        },
        firstName: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {
                notNull: {msg: "firstName is required"},
            },
        },
        lastName: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {
                notNull: {msg: "lastName is required"},
            },
        },
        password: {
            type: DataTypes.STRING,
            get() {
                return () => this.getDataValue('password')
            },
            allowNull: false,
            validate: {
                notNull: {msg: "password is required"},
            },
            set(value) {
                const hash = bcrypt.hashSync(value, 10);
                this.setDataValue('password', hash);
            },
        },
    }, {
        sequelize,
        modelName: 'Users',
    });
    return Users;
};
