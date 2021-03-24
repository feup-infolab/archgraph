
const bcrypt = require('bcrypt');
'use strict';
const {
    Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class User extends Model {
        /**
         * Helper method for defining associations.
         * This method is not a part of Sequelize lifecycle.
         * The `models/index` file will call this method automatically.
         */
        static associate(models) {
            // define association here
        }
    }

    User.init({
        username: {
            type: DataTypes.STRING,
            allowNull: false,
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
                return() => this.getDataValue('password')
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
        modelName: 'User',
        freezeTableName: true,

    });


    return User;
};

