const Users = require('../models').users;
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
let env;
const myArgs = process.argv.slice(2);
if (myArgs.length > 0) {
    env = myArgs[0]
}
const config = require(__dirname + '/../config/config.js')[env];


module.exports = {


    async create(req, res) {
        console.log(req.body);
        const username = req.body.username;

        if (!username) {
            res.status(400).send('username is required');
        }
        const user = await Users.findOne({where: {username: username}})
        if (user === null) {
            try {

                const user = await Users.create({
                    username: req.body.username,
                    password: req.body.password,
                    firstname: req.body.firstname,
                    lastname: req.body.lastname,
                });
                res.status(201).send(user)
            } catch (e) {
                res.status(400).send(e.message)
            }
        } else {
            res.status(400).send(`There is already user with username = ${username}`)
        }
    },
    async getById(req, res) {
        console.log(req.params)
        try {
            const user = await Users.findByPk(req.params.id);
            if (!user) {
                return res.status(404).send({
                    message: 'Users Not Found',
                });
            }
            return res.status(200).send(user);
        } catch (e) {
            return res.status(400).send(e.message)
        }

    },
    async getAll(req, res, next) {
        try {
            const users = await Users.findAll({
                order: [
                    ['id', 'ASC'],
                ],
            });
            if (!users) {
                return res.status(404).send({
                    message: 'Users Not Found',
                });
            }
            return res.status(200).send(users);
        } catch (e) {
            res.status(400).send(e.message)

        }
    },
    async delete(req, res) {

        try {
            const user = await Users.findByPk(req.params.id);
            if (!user) {
                return res.status(400).send({
                    message: 'Users Not Found',
                });
            }

            await user.destroy();
            return res.status(200).send({
                message: 'Deleted',
            })
        } catch (e) {
            return res.status(400).send(e.message)
        }
    },
    async update(req, res) {
        const user = await Users.findByPk(req.params.id);
        if (!user) {
            return res.status(404).send({
                message: 'Users Not Found',
            });
        }
        try {
            await user
                .update({
                    firstname: req.body.firstname || user.firstname,
                    lastname: req.body.lastname || user.lastname,
                    updatedAt: new Date(),
                    createdat: user.createdat,
                    password: req.body.password || user.password
                })
            return res.status(200).send(user)
        } catch (e) {
            return res.status(400).send(e.message)
        }
    },
    async login(req, res) {
        console.log(req.body);
        const username = req.body.username;
        const password = req.body.password;

        if (!username || !password) {
            return res.status(400).send('username and password are required');
        }
        const user = await Users.findOne({where: {username: username}})
        if (!user) {
            return res.status(400).send('username not exists');
        }
        const userPassword = user.getDataValue('password')

        bcrypt.compare(password, userPassword, function (err, isMatch) {
            if (err) {
                throw err
            } else if (!isMatch) {
                return res.send(null)
            } else {

                const token = jwt.sign({id: user.id}, config.secret, {
                    expiresIn: 86400 // expires in 24 hours
                });
                const newUser = Object.assign(user.toJSON(), {token: token});

                return res.status(200).send(newUser);
            }
        })

    },
}
