
//var OrientDB = require('orientjs');


var ODatabase = require('orientjs').ODatabase;

var db = new ODatabase({
  host:     'localhost',
  port:     2424,
  username: 'root',
  password: 'root',
  name:     'DatabaseGraph'
});




/*

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
*/

async function func() {
  var result =[]
  //create class
  result.push(await db.class.create('player', 'V'))
  result.push(await db.class.create('player1', 'V'))
  //get classes
  console.log('getClasses')
  result.push(await db.class.get('player'))
  result.push(await db.class.get('player1'))

  //close database
  await db.close()
  return result;
}
func()
.then(
  function(result){
    result.forEach(element => {
      console.log(element.name)
    });
})
.catch(function(error){
  console.log(error.message)
  db.close()
}) 
