import {Component, OnInit} from '@angular/core';
import {Location} from "@angular/common";
import {ActivatedRoute} from "@angular/router";
import {MyServiceService} from "../../../service/service-service";
import {Router} from '@angular/router';


@Component({
  selector: 'app-view-template',
  templateUrl: './view-template.component.html',
  styleUrls: ['./view-template.component.css']
})
export class ViewTemplateComponent implements OnInit {

  constructor(
    private location: Location,
    private router: ActivatedRoute,
    private service: MyServiceService,
    private route: Router
  ) {
  }

  uid = '';
  objectKeys = Object.keys;
  templates = {};
  key: any;
  template: any;
  hasTemplate = false


  ngOnInit() {
    this.router.paramMap.subscribe(params => {
      this.uid = params.get('uid');
      console.log(this.uid);
      this.getTemplatesFromEntity(this.uid);

    });
  }


  private getTemplatesFromEntity(uid: string) {
    this.service.getTemplatesFromEntity(uid)
      .subscribe(templates => {
        console.log(templates);
        let index = 1;
        if (templates["message"]) {
          this.hasTemplate = false
        } else {
          for (let template of templates) {
            let name = "template " + index;
            this.templates[name] = template;
            index++
          }
          if (templates.length > 0) {
            this.key = "template 1"
            this.hasTemplate = true
            this.template = this.templates[this.key]
          }
        }


      });

  }

  selectChangeHandler($event) {
    console.log($event.target.value);
    this.key = $event.target.value
    this.template = this.templates[this.key]

  }

  editEntity() {
    //this.route.navigateByUrl(this.uid);
    this.route.navigate([this.uid],
      {
        queryParams:
          {
            template: JSON.stringify(this.template)
          }
      }
    );
    //this.route.navigate([this.uid], { queryParams: { template: "this.template" }});


  }

  editTemplate() {
    this.route.navigate(['/edit-template/', this.uid],
      {
        queryParams:
          {
            template: JSON.stringify(this.template)
          }
      }
    );
  }
}
