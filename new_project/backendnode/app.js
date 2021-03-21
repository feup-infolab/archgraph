const express = require('express')
const bodyParser = require('body-parser')
const app = express()
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({extended: true})); // support encoded bodies
require('dotenv').config();
const PORT = process.env.PORT
const User = require('./models').User

const userRoutes = require('./routes/user');
//const user = require('./controllers').user


app.use('/user', userRoutes);
// app.use('/', function(req, res) {
// });
// app.route('/user/create',).get(function (req, res) {
//     console.log(req.param('id'));
//     User.create({
//         username: req.body.username,
//         password: req.body.password,
//         firstname: req.body.firstname,
//         lastname: req.body.lastname
//
//     })
//         .then((user) => res.status(201).send(user))
//         .catch((error) => res.status(400).send(error));
//     res.status(200).send({'model': 'Your data is saved'});
//
// });
//
// app.route('/user/create',).post(function (req, res) {
//     console.log(req.body);
//     User.create({
//         username: req.body.username,
//         password: req.body.password,
//         firstname: req.body.firstname,
//         lastname: req.body.lastname
//
//     })
//         .then((user) => res.status(201).send(user))
//         .catch((error) => res.status(400).send(error));
// });

app.listen(PORT, function () {
    console.log('Server is running at PORT:', PORT);
});


//
//yarn sequelize-cli model:generate --name User --attributes username:string,firstName:string,lastName:string,password:string
//yarn db:g:seed users
//yarn db:g:migration addPassword
