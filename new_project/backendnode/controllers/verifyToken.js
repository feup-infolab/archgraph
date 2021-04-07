var jwt = require('jsonwebtoken');


function verifyToken(req, res, next) {
    var env;
    var myArgs = process.argv.slice(2);
    if(myArgs.length>0){
        env = myArgs[0]
    }
    const config = require(__dirname + '/../config/config.js')[env];
    const token = req.headers['authorization'];
    if (!token)
        return res.status(401).send({message: 'No token provided.' });

    jwt.verify(token, config.secret, function(err, decoded) {
        if (err)
            return res.status(401).send({message: 'Failed to authenticate token.' });

        // if everything good, save to request for use in other routes
        req.userId = decoded.id;
        next();
    });
}

module.exports = verifyToken;
