import {Component, OnInit} from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {first} from 'rxjs/operators';

import {UserServiceService, AlertService} from '../../../service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public username: any;
  public password: any;

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private service: UserServiceService,
  ) {
    // redirect to home if already logged in
    // if (this.service.userValue) {
    //   this.router.navigate(['/']);
    // }
  }


  loading = false;
  submitted = false;
  returnUrl: string | undefined;

  // convenience getter for easy access to form fields


  ngOnInit() {

    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  onSubmit() {
    this.submitted = true;

    // reset alerts on submit
    // this.alertService.clear();

    // stop here if form is invalid
    // @ts-ignore
    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;

  }

  login() {
    console.log(this.username + this.password);
    this.service.login(this.username, this.password)
      .subscribe(result => {
          if (this.service.userValue) {
            this.router.navigate(['/']);
          }else {
            this.router.navigate(['/']);
          }
        }
      );
  }

}

