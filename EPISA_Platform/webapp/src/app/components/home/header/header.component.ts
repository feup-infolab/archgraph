import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {AlertService, UserService} from '../../../service';
import {Router, ActivatedRoute} from '@angular/router';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']

})
export class HeaderComponent implements OnInit {
  @Output() public sidenavToggle = new EventEmitter();
  public username: any;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };

  constructor(private userService: UserService,
              public alertService: AlertService,
              public router: Router,
  ) {
    this.userService.getObservableUser().subscribe(user => {
      if (user) {
        this.username = user.username;
      } else {
        this.username = null;
      }
    });
  }

  ngOnInit() {
  }

  public onToggleSidenav = () => {
    this.sidenavToggle.emit();
  };

  logout() {
    this.userService.logout();
    this.alertService.success('Successful logout', this.options);
  }

  goToHome() {
    this.router.navigate(['/']);
  }
}
