package archgraph

import cidoc.Loader

class Entity {

    String type
    String name



    static constraints = {
        name maxSize: 255

    }
}
