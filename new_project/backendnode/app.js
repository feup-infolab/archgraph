const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config();
const cors = require('cors');

const app = express();
app.use(cors())


app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({extended: true})); // support encoded bodies
const PORT = process.env.PORT

const userRoutes = require('./routes/user');
const indexRoutes = require('./routes/index');


app.use('/', indexRoutes);
app.use('/user', userRoutes);

app.get('/*', function(req, res) {
    res.send('Not implemented');
});

app.listen(PORT, function () {
    console.log('Server is running at PORT:', PORT);
});


//
//yarn sequelize-cli model:generate --name User --attributes username:string,firstName:string,lastName:string,password:string
//yarn db:g:seed users
//yarn db:g:migration addPassword
