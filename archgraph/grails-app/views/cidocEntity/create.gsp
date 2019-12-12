<!DOCTYPE html>
<html>
    <head>
        <meta name="layout" content="main" />
        <g:set var="entityName" value="${message(code: 'cidocEntity.label', default: 'CidocEntity')}" />
        <title><g:message code="default.create.label" args="[entityName]" /></title>
    </head>
    <body>
        <a href="#create-cidocEntity" class="skip" tabindex="-1"><g:message code="default.link.skip.label" default="Skip to content&hellip;"/></a>
        <div class="nav" role="navigation">
            <ul>
                <li><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></li>
                <li><g:link class="list" action="index"><g:message code="default.list.label" args="[entityName]" /></g:link></li>
            </ul>
        </div>
        <div id="create-cidocEntity" class="content scaffold-create" role="main">
            <h1><g:message code="default.create.label" args="[entityName]" /></h1>
            <g:if test="${flash.message}">
            <div class="message" role="status">${flash.message}</div>
            </g:if>
            <g:hasErrors bean="${this.cidocEntity}">
            <ul class="errors" role="alert">
                <g:eachError bean="${this.cidocEntity}" var="error">
                <li <g:if test="${error in org.springframework.validation.FieldError}">data-field-id="${error.field}"</g:if>><g:message error="${error}"/></li>
                </g:eachError>
            </ul>
            </g:hasErrors>
            <g:form resource="${this.cidocEntity}" method="POST">
                <fieldset class="form">
                    <label for="cidocEntity.label">
                        <g:message code="cidocEntity.label.label" default="Cidoc Entity"/>
                    </label>
                    <g:select name="cidocEntity.label" from="${['E01_CRM_Entity', 'E52_Time_Span', 'E41_Appelation']}" value="${label}" noSelection="['':'-Choose your label-']"/>
                    <label for="cidocEntity.name">
                        <g:message code="cidocEntity.name.label" default="Name"/>
                        <span class="required-indicator">*</span>
                    </label>
                    <g:textField name="cidocEntity.name" value="${myValue}" />
                </fieldset>
                <fieldset class="buttons">
                    <g:submitButton name="create" class="save" value="${message(code: 'default.button.create.label', default: 'Create')}" />
                </fieldset>
            </g:form>
        </div>
    </body>
</html>
