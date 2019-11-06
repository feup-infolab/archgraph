
Database = require('arangojs').Database;
db = new Database('http://127.0.0.1:8529');
var Cao = require('./Classes/Cao.js');


db.useBasicAuth('root', 'openSesame')

db.createDatabase('arangoDB').then(
  () => console.log('Database created'),
  err => console.error('Failed to create database:', err.response.body.errorMessage)
);

db.useDatabase('arangoDB');
CollectionAnimal = db.collection('Animal');
CollectionCao = db.collection('Cao');


CollectionAnimal.create().then(
  () => console.log('Collection Animal created'),
  err => console.error('Failed to create collection:', err.response.body.errorMessage)
);

CollectionCao.create().then(
  () => console.log('Collection Cao created'),
  err => console.error('Failed to create collection:', err.response.body.errorMessage)
);

var cao =new Cao("raça","Dude") 
  cao.sayHi()// Hello Dude! 
  //
  console.log(Cao.prototype)

cao1 = {
  _key: 'firstCao',
  name: cao.getName(),
  raca: cao.getRaca()
};

CollectionCao.save(cao1).then(
  meta => console.log('Cao1 saved:', meta._rev),
  err => console.error('Failed to save Cao1:', err.response.body.errorMessage)
);

/*
collection.update('firstDocument', {d: 'qux'}).then(
  meta => console.log('Document updated:', meta._rev),
  err => console.error('Failed to update document:', err.response.body.errorMessage)
);
*/
  

