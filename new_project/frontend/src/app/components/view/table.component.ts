import {AfterViewInit, Component, Input, ViewChild} from '@angular/core';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';

@Component({
    selector: 'app-table',
    templateUrl: './table.component.html',
    styleUrls: ['./table.component.css'],
})
export class TableComponent implements AfterViewInit {
    public displayedColumns: any[] | undefined;
    public concluded: boolean | undefined;
    public dataSource: any;
    public myColumns: any[] | undefined;

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

    @Input() set columns(value: any[]) {
        if (value) {
            this.myColumns = value;
            this.displayedColumns = [];
            this.myColumns.forEach(element => {
                const object = {
                    id: element,
                    value: element
                };
                // @ts-ignore
                this.displayedColumns.push(object);
            });
        }
    }

    @Input() set data(value: any[]) {
        if (value) {
            this.dataSource = value;
        }
    }

    ngAfterViewInit() {
        setTimeout(() => {
            this.concluded = true;
        });


    }

}
