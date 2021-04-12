import {Component, OnInit} from '@angular/core';
import {UserService} from '../../../service';
import {AlertService} from '../../../_alert/alert.service';
import {MatDialog} from '@angular/material/dialog';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };

  constructor(private service: UserService,
              public alertService: AlertService
  ) {
  }

  ngOnInit(): void {
    // this.alertService.success('Success!!', this.options);
    // this.alertService.error('Error :(', this.options);
    // this.alertService.info('Some info....', this.options);
    // this.alertService.warn('Warning: ...', this.options);

  }

  getAll() {
    this.service.getAll()
      .subscribe(result => {
          console.log(result);
        }
      );
  }
}
