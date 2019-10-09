import ratpack.http.MutableHeaders
import ratpack.jackson.Jackson

import static ratpack.groovy.Groovy.ratpack

//Loader l = new Loader()
//String json = l.getJsonLd()

def helloHandler
ratpack {
    handlers {
        path("cidoc") {
            byMethod {
                MutableHeaders headers = response.headers
                headers.set('Access-Control-Allow-Origin', '*')
                headers.set('Access-Control-Allow-Headers', 'x-requested-with, origin, content-type, accept')
                get {
                    render json
                }
                post {

                    parse(Jackson.jsonNode()).then{
                        string ->
                            println(string.toString())
                            l.loadJsonLd(l.getNeo4jSession(),string.toString())
                            render string.toString()
                    }

                    //l.loadJsonLd(l.getNeo4jSession(),jsonLd)
                    //render jsonLd
                }
            }
        }
        path("cidoc/relations/:reltype") {
            byMethod {
                MutableHeaders headers = response.headers
                headers.set('Access-Control-Allow-Origin', '*')
                headers.set('Access-Control-Allow-Headers', 'x-requested-with, origin, content-type, accept')

                get {
                    render l.getAllRelations(pathTokens.reltype).toString()
                }
            }
        }
        path("cidoc/counterdomain"){
            byMethod {
                MutableHeaders headers = response.headers
                headers.set('Access-Control-Allow-Origin', '*')
                headers.set('Access-Control-Allow-Headers', 'x-requested-with, origin, content-type, accept')

                post {
                    parse(Jackson.jsonNode()).then{
                        string ->
                            render l.packCounterDomain(string.toString())

                    }
                }
            }
        }
    }
}