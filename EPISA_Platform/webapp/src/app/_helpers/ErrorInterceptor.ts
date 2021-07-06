import {Injectable} from '@angular/core';
import {HttpRequest, HttpHandler, HttpEvent, HttpInterceptor} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {catchError} from 'rxjs/operators';
import {AlertService, UserService} from '../service';


@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  constructor(public alertService: AlertService,
              public userService: UserService
  ) {
  }

  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(request).pipe(catchError(err => {
      if (err.status === 400 || err.status === 401) {
        this.alertService.error(err.error.message, this.options);

        // TODO descomentar isto
        this.userService.logout();
      }
      const error = err.error.message || err.statusText;
      return throwError(error);
    }));
  }
}
