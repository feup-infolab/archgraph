import Gverse from "gverse"
import {Edge} from "gverse/dist/gverse/gverse";

const graph = new Gverse.Graph(
  new Gverse.Connection({ host: "localhost", port: 9080 , debug: true})
);

class User extends Gverse.Vertex {
  type = "User";
  name: string = ""
}

class Repo {
  type: "Repository";
  name: string;
  owner: User;
  contributors: User[];
  _edges: {
    owner: Edge.toVertex
    contributors: Edge.toVertices
  }
}

async function createUser()
{
  let  user = new User();
  user.name = "Zak";
  await graph.create(user);
}

async function getUser(uid)
{
  const user = (await graph.get(User, uid)) as User;
  console.log(user.name); // = "Zak"
}

createUser()
