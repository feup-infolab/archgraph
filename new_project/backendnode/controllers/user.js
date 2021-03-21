const User = require('../models').User;

module.exports = {
    create(req, res) {
        console.log(req.body);
        return User
            .create({
                username: req.body.username,
                password: req.body.password,
                firstname: req.body.firstname,
                lastname: req.body.lastname

            })
            .then((user) => res.status(201).send(user))
            .catch((error) => res.status(400).send(error));
    },
}
exports.nao = function (req, res) {
    res.send('NOT IMPLEMENTED: Author list');
};
/*
    list(req, res) {
        return Todo
            .findAll({
                include: [{
                    model: TodoItem,
                    as: 'todoItems',
                }],
                order: [
                    ['createdAt', 'DESC'],
                    [{model: TodoItem, as: 'todoItems'}, 'createdAt', 'ASC'],
                ],
            })
            .then((todos) => res.status(200).send(todos))
            .catch((error) => res.status(400).send(error));
    },

    retrieve(req, res) {
        return Todo
            .findById(req.params.todoId, {
                include: [{
                    model: TodoItem,
                    as: 'todoItems',
                }],
            })
            .then((todo) => {
                if (!todo) {
                    return res.status(404).send({
                        message: 'Todo Not Found',
                    });
                }
                return res.status(200).send(todo);
            })
            .catch((error) => res.status(400).send(error));
    },

    update(req, res) {
        return Todo
            .findById(req.params.todoId, {
                include: [{
                    model: TodoItem,
                    as: 'todoItems',
                }],
            })
            .then(todo => {
                if (!todo) {
                    return res.status(404).send({
                        message: 'Todo Not Found',
                    });
                }
                return todo
                    .update({
                        title: req.body.title || todo.title,
                    })
                    .then(() => res.status(200).send(todo))
                    .catch((error) => res.status(400).send(error));
            })
            .catch((error) => res.status(400).send(error));
    },

    destroy(req, res) {
        return Todo
            .findById(req.params.todoId)
            .then(todo => {
                if (!todo) {
                    return res.status(400).send({
                        message: 'Todo Not Found',
                    });
                }
                return todo
                    .destroy()
                    .then(() => res.status(204).send())
                    .catch((error) => res.status(400).send(error));
            })
            .catch((error) => res.status(400).send(error));
    },*/

