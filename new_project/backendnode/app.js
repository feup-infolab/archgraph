const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config();
const cors = require('cors');

const app = express();
app.use(cors())

var env;
var myArgs = process.argv.slice(2);
if(myArgs.length>0){
    env = myArgs[0]
}
const config = require(__dirname + '/config/config.js')[env];
console.log('host: ' + config.host)
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({extended: true})); // support encoded bodies
const PORT = config.my_port

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
//yarn sequelize-cli model:generate --name User --attributes username:string,firstname:string,lastname:string,password:string
//yarn db:g:seed users
//yarn db:g:migration addPassword
//psql -h localhost -U admin -d db -p 5432 -a -f config/populate.sql
//yarn sequelize-cli model:generate --name usera --attributes username:string,firstname:string,lastname:string,password:string
