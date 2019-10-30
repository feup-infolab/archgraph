Database = require('arangojs').Database;

void async function() {

db = new Database('http://127.0.0.1:8529');

db.useBasicAuth('root', 'openSesame')

db.createDatabase('arangoDB2').then(
  () => console.log('Database created'),
  err => console.error('Failed to create database:', err.response.body.errorMessage)
);

db.useDatabase('arangoDB2');

e1Collection = db.collection('E1_CRM_Entity');
e1Collection.create().then(
  () => console.log('Collection created'),
  err => console.error('Failed to create collection:', err.response.body.errorMessage)
);


e55Collection = db.collection('E55_Type');
e55Collection.create().then(
  () => console.log('Collection created'),
  err => console.error('Failed to create collection:', err.response.body.errorMessage)
);


const p2Collection = db.edgeCollection('P2_has_type');

p2Collection.create({
	waitForSync: true
}).then(
  () => console.log('Edge Collection created'),
  err => console.error('Failed to create edge collection:', err.response.body.errorMessage)
);

const graph = db.graph("graph");

graph.create({
	edgeDefinitions: [{
		collection: 'P2_has_type',
		from: ['E1_CRM_Entity'],
		to: ['E55_Type']
	}]
}).then(
  () => console.log('Graph created'),
  err => console.error('Failed to create Graph:', err.response.body.errorMessage)
);

//graph.addVertexCollection('E1_CRM_Entity');

//graph.addVertexCollection('E55_Type');


const col1 = graph.vertexCollection("E1_CRM_Entity");
const col2 = graph.vertexCollection("E55_Type");
const edge1 = graph.edgeCollection("P2_has_type");

const crmEntity = await col1.save({ name: "E1" });

console.log("Created " + crmEntity.vertex._id);

const crmType = await col2.save({ name: "E55" });

console.log("Created " + crmType.vertex._id);
//console.log("Created E55Types/" + crmType["_id"]);


const edge = edge1.save(
	{name: "P2"},
	crmEntity.vertex._id,
	crmType.vertex._id
).then(
  () => console.log('Edge P2 document created'),
  err => console.error('Failed to create Edge P2 from ' + crmEntity._id + ' '+ crmType._id +  ':', err.response.body.errorMessage)
);
}();






/*

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
  

