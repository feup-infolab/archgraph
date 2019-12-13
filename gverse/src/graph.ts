import Gverse from "gverse"

class DBConnection
{
	private static graph: Gverse.Graph;
	
	static getDatabase(): Gverse.Graph
	{
		if(!DBConnection.graph)
		{
			DBConnection.graph = new Gverse.Graph(
				  new Gverse.Connection({ host: "localhost", port: 9080 })
				)
		}
		
		return DBConnection.graph;
	}
}

module.exports.DBConnection = DBConnection;