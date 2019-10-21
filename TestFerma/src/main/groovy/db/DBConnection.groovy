package db

import com.orientechnologies.orient.core.db.ODatabaseType
import com.orientechnologies.orient.core.db.OrientDB
import com.orientechnologies.orient.core.db.OrientDBConfig
import org.apache.tinkerpop.gremlin.orientdb.OrientGraphFactory
import groovy.transform.CompileStatic

@CompileStatic
class DBConnection {
	OrientGraphFactory graphFactory
	static databaseExists = false;

	public static final String DATABASE_NAME = "archgraph"
	public static final String DATABASE_HOST = "127.0.0.1"
	public static final String DATABASE_URI = "remote:"+DATABASE_HOST+ "/" + DATABASE_NAME
	public static final String SERVER_USERNAME = "root"
	public static final String SERVER_PASSWORD = "rootpwd"

	static OrientGraphFactory databaseFactory() {
		if(!databaseExists)
		{
			// create database if not exists
			OrientDB orientDB = new OrientDB("remote:localhost",SERVER_USERNAME, SERVER_PASSWORD, OrientDBConfig.defaultConfig());
			orientDB.createIfNotExists(DATABASE_NAME, ODatabaseType.PLOCAL);
			orientDB.close();
			databaseExists = true;
		}

		// change to 'remote:host/dbname' if persistent storage needed
		def factory = new OrientGraphFactory(DATABASE_URI,SERVER_USERNAME, SERVER_PASSWORD).setupPool(1, 20)
		factory.getDatabase(true, false)
		factory
	}

	static OrientGraphFactory memoryFactory(){
		OrientGraphFactory factory = new OrientGraphFactory("memory:tinkerpop")
		factory
	}
}