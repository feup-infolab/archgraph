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
  public loginForm: FormGroup;
  public loading = false;
  public submitted = false;
  returnUrl: string | undefined;
  error = '';

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private service: UserServiceService,
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
    // if (this.service.getObservableUser()) {
    //   this.router.navigate(['/']);
    // }
  }

  ngOnInit() {
    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  get formControls() {
    return this.loginForm.controls;
  }

  login() {
    this.submitted = true;

    // stop here if form is invalid
    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;
    this.service.login(this.formControls.username.value, this.formControls.password.value)
      .subscribe(result => {
          if (this.service.getObservableUser()) {
            this.router.navigate(['/']);
          }
        }
      );
  }

  register() {
    this.router.navigate(['/register']);
  }
}

