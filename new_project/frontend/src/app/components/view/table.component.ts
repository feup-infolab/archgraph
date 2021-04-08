import {AfterViewInit, Component, Input, ViewChild} from '@angular/core';
import {MatSort} from '@angular/material/sort';
import {MatPaginator} from '@angular/material/paginator';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css'],
})
export class TableComponent implements AfterViewInit {
  public dataSource: any;
  public columnsHeader: any[] | undefined;
  public columnHref: any;
  public otherColumns: any[] | undefined;
  public concluded: boolean | undefined;
  public myHrefTo: any;

  @ViewChild(MatPaginator, {static: false})
  set paginator(value: MatPaginator) {

    if (this.dataSource) {
      this.dataSource.paginator = value;
    }
  }

  @ViewChild(MatSort, {static: false})
  set sort(value: MatSort) {
    if (this.dataSource) {
      this.dataSource.sort = value;
    }
  }

  @Input()
  set columns(value: any[]) {
    if (value) {
      this.otherColumns = [];
      this.columnHref = [];
      this.columnsHeader = [];
      for (let i = 1; i < value.length; i++) {
        if (i === 1) {
          this.columnHref = {
            id: value[i],
            href: value[i - 1],
            value: value[i],
          };
        } else {
          const object = {
            id: value[i],
            value: value[i]
          };
          this.otherColumns.push(object);
        }
        this.columnsHeader.push(value[i]);
      }

    }
  }

  @Input()
  set data(value: any[]) {
    this.dataSource = value;

  }

  @Input()
  set hrefTo(value: any) {
    this.myHrefTo = value;
  }

  ngAfterViewInit() {
    if (this.myHrefTo === undefined || this.dataSource === undefined || this.columnsHeader === undefined) {
      throw new Error('Attributes "hrefTo", "data" and "columns"  are required');

    }
    setTimeout(() => {
      this.concluded = true;
    });
  }


}
