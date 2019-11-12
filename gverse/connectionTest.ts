//var OrientDB = require('orientjs');
var ODatabase = require('orientjs').ODatabase;

var db = new ODatabase({
  host:     'localhost',
  port:     2424,
  username: 'root',
  password: 'root',
  name:     'DatabaseGraph'
});

//create class
db.class.create('Player', 'V')
.then(
  function(player){
      console.log('Created Vertex Class: ' + player.name);
})
.catch(function(error){
  console.log("Didn't create class:", error.message)
}) 

//getting class
var player = db.class.get('Player')
.then(function(player){
    console.log('Retrieved class: ' + player.name);

    //addProporty
    player.property.create({
      name: 'name',
      type: 'String'
    },
    {
      name: 'idade',
      type: 'Integer'
    })
    .then(function(property){
        console.log("Created Property: " + property.name);
    })
    .catch(function(error){
        console.log(error.message)
    });

    //add player
    player.create({
    name: "Ty Cobb",
    idade: 12
    })
    .then(
      function(player){
        console.log('Created Record: ', player.name);
    })
    .catch(
        function(error){
          console.log("Didn't create Record: ", error.message);
    });
})
.catch(function(error){
  console.log(error.message)
});

//updatting class
db.class.update({
  name: 'Player',
  superClass: 'V'
})
.then(function(player){
  console.log(
    'Updated Class: ' + player.name
    + ' to extend ' + player.superClass
  );
})
.catch(function(error){
  console.log(error.message)
});



//query
var idade = 10;
var hitters = db.query(
  'SELECT * FROM Player WHERE idade >= :idade ',
  {params: {
    idade: idade,
  },limit: 20 }
)
.then(function(players){
  console.log(players);
})
.catch(function(error){
  console.log(error.message)
})



//close database
/*
db.close()
.then(function(){
  console.log('closed');
});
*/
