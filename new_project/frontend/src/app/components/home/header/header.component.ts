import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {Document} from '../../document/searchPage/doc-search-page.component';
import {MyService, UserServiceService} from '../../../service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @Output() public sidenavToggle = new EventEmitter();
  public username: any;

  constructor(
    private service: UserServiceService) {
  }

  ngOnInit() {
    const user = this.service.userValue;
    if (user != null) {
      this.username = user.username;
    }
    console.log(this.username);
  }

  public onToggleSidenav = () => {
    this.sidenavToggle.emit();
  }
}
