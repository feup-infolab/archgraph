import {Injectable} from '@angular/core';
import {User} from '../models';
import {map} from 'rxjs/operators';
import {BehaviorSubject, Observable, Subject} from 'rxjs';
import {Router} from '@angular/router';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  baseUrl = 'http://localhost:8010';
  public userSubject: BehaviorSubject<User>;
  public user: Observable<User>;

  constructor(private router: Router,
              private http: HttpClient
  ) {
    const user: any = localStorage.getItem('user');
    this.userSubject = new BehaviorSubject<User>(JSON.parse(user));
    this.user = this.userSubject.asObservable();
  }

  public get currentUserValue(): User {
    return this.userSubject.value;
  }
  getObservableUser(): Observable<any> {
    return this.userSubject.asObservable();
  }

  login(username: any, password: any) {
    return this.http.post<any>(`${this.baseUrl}/user/login`, {username, password})
      .pipe(map(result => {
        localStorage.setItem('user', JSON.stringify(result.user));
        this.userSubject.next(result.user);
        return result;
      }));
  }

  logout() {
    localStorage.removeItem('user');
    // @ts-ignore
    this.userSubject.next(null);
    this.router.navigate(['/home']);
    return;
  }

  register(user: User) {
    return this.http.post(`${this.baseUrl}/users/register`, user);
  }

  getAll() {
    return this.http.get<User[]>(`${this.baseUrl}/user/getall`);
  }

  getById(id: string) {
    return this.http.get<User>(`${this.baseUrl}/user/${id}`);
  }

  update(id: string, params: any) {
    // return this.http.put(`${this.baseUrl}/users/${id}`, params)
    //   .pipe(map(x => {
    //     // update stored user if the logged in user updated their own record
    //     // tslint:disable-next-line:triple-equals
    //     if (id == this.userValue.id) {
    //       // update local storage
    //       const user = {...this.userValue, ...params};
    //       localStorage.setItem('user', JSON.stringify(user));
    //
    //       // publish updated user to subscribers
    //       this.userSubject.next(user);
    //     }
    //     return x;
    //   }));
  }

}
