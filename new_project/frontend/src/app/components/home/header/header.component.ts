import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {AlertService, UserService} from '../../../service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']

})
export class HeaderComponent implements OnInit {
  @Output() public sidenavToggle = new EventEmitter();
  public username: any;


  constructor(private userService: UserService,
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
  }

  logout() {
    this.userService.logout();
  }
}
