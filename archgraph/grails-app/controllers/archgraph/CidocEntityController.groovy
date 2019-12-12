package archgraph

import grails.validation.ValidationException
import static org.springframework.http.HttpStatus.*

class CidocEntityController {

    CidocEntityService cidocEntityService

    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index(Integer max) {
        params.max = Math.min(max ?: 10, 100)
        respond cidocEntityService.list(params), model:[cidocEntityCount: cidocEntityService.count()]
    }

    def show(Long id) {
        respond cidocEntityService.get(id)
    }

    def create() {
        respond new CidocEntity(params)
    }

    def save(CidocEntity cidocEntity) {
        if (cidocEntity == null) {
            notFound()
            return
        }

        try {
            cidocEntityService.save(cidocEntity)
        } catch (ValidationException e) {
            respond cidocEntity.errors, view:'create'
            return
        }

        request.withFormat {
            form multipartForm {
                flash.message = message(code: 'default.created.message', args: [message(code: 'cidocEntity.label', default: 'CidocEntity'), cidocEntity.id])
                redirect cidocEntity
            }
            '*' { respond cidocEntity, [status: CREATED] }
        }
    }

    def edit(Long id) {
        respond cidocEntityService.get(id)
    }

    def update(CidocEntity cidocEntity) {
        if (cidocEntity == null) {
            notFound()
            return
        }

        try {
            cidocEntityService.save(cidocEntity)
        } catch (ValidationException e) {
            respond cidocEntity.errors, view:'edit'
            return
        }

        request.withFormat {
            form multipartForm {
                flash.message = message(code: 'default.updated.message', args: [message(code: 'cidocEntity.label', default: 'CidocEntity'), cidocEntity.id])
                redirect cidocEntity
            }
            '*'{ respond cidocEntity, [status: OK] }
        }
    }

    def delete(Long id) {
        if (id == null) {
            notFound()
            return
        }

        cidocEntityService.delete(id)

        request.withFormat {
            form multipartForm {
                flash.message = message(code: 'default.deleted.message', args: [message(code: 'cidocEntity.label', default: 'CidocEntity'), id])
                redirect action:"index", method:"GET"
            }
            '*'{ render status: NO_CONTENT }
        }
    }

    protected void notFound() {
        request.withFormat {
            form multipartForm {
                flash.message = message(code: 'default.not.found.message', args: [message(code: 'cidocEntity.label', default: 'CidocEntity'), params.id])
                redirect action: "index", method: "GET"
            }
            '*'{ render status: NOT_FOUND }
        }
    }
}
