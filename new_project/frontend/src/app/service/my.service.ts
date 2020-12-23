import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';


@Injectable({
    providedIn: 'root'
})
export class MyService {
    baseUrl = 'http://localhost:3030/ds';
    prefixLigacao = 'prefix ligacao: <http://www.episa.inesctec.pt/ligacao#>';
    prefixDataObject = 'prefix data_object:<http://www.episa.inesctec.pt/data_object#>';

    constructor(private http: HttpClient) {
    }

    fuseki(): Observable<any> {
        return this.http.get<any>(`${this.baseUrl}/?query=SELECT ?s ?p ?o WHERE {?s ?p ?o}`);
    }

    getSuppliedTitle(id: any): Observable<any> {
        let query;
        query = ' SELECT ?title ' +
            'WHERE { ' +
            '<http://erlangen-crm.org/200717/E31_Document335> <http://erlangen-crm.org/200717/P102_has_title> ?ARE3SuppliedTitle. ' +
            '?ARE3SuppliedTitle ligacao:hasValue ?data_object. ' +
            '?data_object data_object:stringValue ?title. ' +
            '}';
        let completeQuery;
        completeQuery = this.prefixLigacao + this.prefixDataObject + query;
        return this.http.get<any>(`${this.baseUrl}/?query=${encodeURIComponent(completeQuery)}`);
    }

    getNote(id: any): Observable<any> {
        let query;
        query = 'SELECT ?has_note ' +
            'WHERE { ' +
            '<http://erlangen-crm.org/200717/E31_Document335> <http://erlangen-crm.org/200717/P3_has_note> ?has_note.' +
            '}';
        return this.http.get<any>(`${this.baseUrl}/?query=${encodeURIComponent(query)}`);
    }
}

