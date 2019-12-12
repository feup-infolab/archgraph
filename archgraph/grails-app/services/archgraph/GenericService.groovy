package archgraph

import cidoc.Loader
import org.neo4j.ogm.session.Session

abstract class GenericService<T> implements Service<T> {

    private static final int DEPTH_LIST = 0
    private static final int DEPTH_ENTITY = 1
    protected Loader loader = Loader.getInstance()
    protected Session session = loader.getNeo4jSession()

    @Override
    Iterable<T> findAll() {
        return session.loadAll(getEntityType(), DEPTH_LIST)
    }

    @Override
    T find(Long id) {
        return session.load(getEntityType(), id, DEPTH_ENTITY)
    }

    @Override
    void delete(Long id) {
        session.delete(session.load(getEntityType(), id))
    }

    @Override
    T createOrUpdate(T entity) {
        session.save(entity, DEPTH_ENTITY)
        return (T) find(entity.id)
    }

    int getCount(){
        return loader.countEntities()
    }

    abstract Class<T> getEntityType()
}
