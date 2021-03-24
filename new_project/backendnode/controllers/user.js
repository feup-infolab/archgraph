const User = require('../models').User;
const bcrypt = require('bcrypt');

module.exports = {
    async create(req, res) {
        console.log(req.body);
        const username = req.body.username;

        if (!username) {
            res.status(400).send('username is required');
        }
        const user = await User.findOne({where: {username: username}})
        if (user === null) {
            try {

                const user = await User.create({
                    username: req.body.username,
                    password: req.body.password,
                    firstName: req.body.firstName,
                    lastName: req.body.lastName,
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
            const user = await User.findByPk(req.params.id);
            if (!user) {
                return res.status(404).send({
                    message: 'User Not Found',
                });
            }
            return res.status(200).send(user);
        } catch (e) {
            return res.status(400).send(e.message)
        }

    },
    async getAll(req, res) {
        try {
            const users = await User.findAll({
                order: [
                    ['id', 'ASC'],
                ],
            });
            if (!users) {
                return res.status(404).send({
                    message: 'User Not Found',
                });
            }
            return res.status(200).send(users);
        } catch (e) {
            res.status(400).send(e.message)

        }
    },
    async delete(req, res) {

        try {
            const user = await User.findByPk(req.params.id);
            if (!user) {
                return res.status(400).send({
                    message: 'User Not Found',
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
        const user = await User.findByPk(req.params.id);
        if (!user) {
            return res.status(404).send({
                message: 'User Not Found',
            });
        }
        try {
            await user
                .update({
                    firstName: req.body.firstName || user.firstName,
                    lastName: req.body.lastName || user.lastName,
                    updatedAt: new Date(),
                    createdAt: user.createdAt,
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
        const user = await User.findOne({where: {username: username}})
        if(!user){
            return res.status(400).send('username not exists');
        }
        const userPassword = user.getDataValue('password')


        bcrypt.compare(password, userPassword, function (err, isMatch) {
            if (err) {
                throw err
            } else if (!isMatch) {
                return res.send(null)
            } else {
                return res.send(user)
            }
        })

    }
}


