
Database = require('arangojs').Database;
db = new Database('http://127.0.0.1:8529');

db.useBasicAuth('root', 'openSesame')

db.createDatabase('arangoDB').then(
  () => console.log('Database created'),
  err => console.error('Failed to create database:', err.response.body.errorMessage)
);

db.useDatabase('arangoDB');
collection = db.collection('secondCollection');

collection.create().then(
  () => console.log('Collection created'),
  err => console.error('Failed to create collection:', err.response.body.errorMessage)
);
/*

doc = {
  _key: 'firstDocument',
  a: 'foo',
  b: 'bar',
  c: Date()
};

collection.save(doc).then(
  meta => console.log('Document saved:', meta._rev),
  err => console.error('Failed to save document:', err.response.body.errorMessage)
);


collection.update('firstDocument', {d: 'qux'}).then(
  meta => console.log('Document updated:', meta._rev),
  err => console.error('Failed to update document:', err.response.body.errorMessage)
);
*/
	
