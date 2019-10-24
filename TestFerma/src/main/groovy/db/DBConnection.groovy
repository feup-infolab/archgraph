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
	public static final String DATABASE_HOST = "dendro-builder.fe.up.pt"
	public static final String DATABASE_URI = "remote:"+DATABASE_HOST+ "/" + DATABASE_NAME
	public static final String SERVER_USERNAME = "root"
	public static final String SERVER_PASSWORD = "rootpwd"
	public static final boolean DESTROY_ON_STARTUP = true;

	static OrientGraphFactory databaseFactory() {
		if(!databaseExists)
		{
			OrientDB orientDB = new OrientDB(DATABASE_URI,SERVER_USERNAME, SERVER_PASSWORD, OrientDBConfig.defaultConfig());
			if(DESTROY_ON_STARTUP)
			{
				if(orientDB.exists(DATABASE_NAME))
				{
					orientDB.drop(DATABASE_NAME);
				}
			}
			// create database if not exists
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