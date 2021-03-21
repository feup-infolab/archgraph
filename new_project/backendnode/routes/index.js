// const user = require('../controllers').user
//
// module.exports = (app) => {
//   app.get('/api', (req, res) => res.status(200).send({
//     message: 'Welcome to the Todos API!',
//   }));
//
//
//   app.post('/user/new', user.create);
//

// app.post('/api/todos/:todoId/items', todoItemsController.create);
// app.put('/api/todos/:todoId/items/:todoItemId', todoItemsController.update);
// app.delete(
//   '/api/todos/:todoId/items/:todoItemId', todoItemsController.destroy
// );
// app.all('/api/todos/:todoId/items', (req, res) => res.status(405).send({
//   message: 'Method Not Allowed',
// }));
//};

// const express = require('express')
// const router = express.Router();
// router.get('/', function(req, res) {
//   res.redirect('/catalog');
// });

//const user = require('../controllers').user
var express = require('express');
var app = express.Router();
app.get('/about', function (req, res) {
    res.send('about');
});
// app.get('/api', (req, res) => res.status(200).send({
//     message: 'Welcome to the Todos API!',
// }));
// app.get('/.*', function(req, res) {
//     res.redirect('/');
// });

//app.post('/user/create', user.create);

module.exports = app;
