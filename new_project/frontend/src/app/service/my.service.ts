import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient, HttpParams} from '@angular/common/http';


@Injectable({
    providedIn: 'root'
})
export class MyService {
    baseUrl = 'http://localhost:8080';
    prefixLigacao = 'prefix ligacao: <http://www.episa.inesctec.pt/ligacao#>';
    prefixDataObject = 'prefix data_object:<http://www.episa.inesctec.pt/data_object#>';

    constructor(private http: HttpClient) {
    }

    fuseki(): Observable<any> {
        return this.http.get<any>(`http://localhost:3030/?query=SELECT ?s ?p ?o WHERE {?s ?p ?o}`);
    }

    getSuppliedTitle(id: any): Observable<any> {
        let doc = 335;
        if (id === '1') {
            doc = 127;
        }
        let query;
        query = ' SELECT ?title ' +
            'WHERE { ' +
            // tslint:disable-next-line:max-line-length
            '<http://erlangen-crm.org/200717/E31_Document' + doc + '> <http://erlangen-crm.org/200717/P102_has_title> ?ARE3SuppliedTitle. ' +
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

    getDocById(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getDocSummary(referenceCode: any): Observable<any> {
        const params = new HttpParams()
            .set('refcode', referenceCode);

        return this.http.get(`${this.baseUrl}/searchdoc`, {params});

        // const params = new HttpParams()
        //     .set('query', 'SELECT ?s ?p ?o WHERE {?s ?p ?o}');
        //
        // return this.http.get(`${this.baseUrl}/`, {params});
    }

    getActorById(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getActorSummary(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getEventById(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getEventSummary(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getOrgById(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getOrgSummary(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getPlaceById(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }

    getPlaceSummary(id: any): Observable<any> {
        // @ts-ignore
        return true;
    }
}

