package com.github.feupinfolab.archgraph.db

import com.tinkerpop.blueprints.impls.orient.OrientGraphFactory
import groovy.transform.CompileStatic

@CompileStatic
class DBConnection {
    OrientGraphFactory graphFactory

    public static final String DATABASE_URI = "remote:127.0.0.1/archgraph"
    public static final String SERVER_USERNAME = "root"
    public static final String SERVER_PASSWORD = "rootpwd"

    static OrientGraphFactory databaseFactory() {
        // change to 'remote:host/dbname' if persistent storage needed
        def factory = new OrientGraphFactory(DATABASE_URI,SERVER_USERNAME, SERVER_PASSWORD).setupPool(1, 20)
        factory
    }
}