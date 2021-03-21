const user = require('../controllers/user');
const express = require('express');
const app = express.Router();



app.post('/create', user.create);

module.exports = app;

